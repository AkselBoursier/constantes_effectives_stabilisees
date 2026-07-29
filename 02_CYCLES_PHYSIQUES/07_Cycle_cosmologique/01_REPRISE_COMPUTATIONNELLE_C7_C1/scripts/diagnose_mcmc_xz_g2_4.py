"""Diagnostics techniques de convergence — porte G2.4b (issue #63).

Implémente et QUALIFIE uniquement les diagnostics techniques prescrits
(G2.4a §11, D4-E) :

    reconstruction chronologique des tirages depuis la colonne weight
    (finie, positive, entière à la tolérance numérique) ;
    concaténation ordonnée des segments de reprise ;
    burn-in 30 % ; aucun amincissement ;
    R-hat scindé et normalisé par rang (bulk et replié, Vehtari et al. 2021) ;
    ESS bulk ; ESS tail (indicatrices des quantiles 5 % et 95 %) ;
    présence et contribution des huit chaînes.

Critères gelés : R-hat rang <= 1.01 ; ESS bulk >= 1000 ; ESS tail >= 1000 ;
8 chaînes contributrices.

Qualification sur cas SYNTHÉTIQUES exclusivement : AUCUNE chaîne physique
G2 n'est lue, aucune moyenne de paramètre n'est produite. La comparaison
de référence utilise la bibliothèque reconnue présente localement
(GetDist, version consignée) pour le Gelman-Rubin classique, et des
ancrages analytiques fermés (chaînes iid : ESS ~ N ; AR(1) de coefficient
rho : ESS ~ N (1-rho)/(1+rho)).

Modes :
    --self-test                          : qualification complète, exit 0/1 ;
    --certifier-synthetique converge     : cas convergé, exit 0 attendu ;
    --certifier-synthetique nonconverge  : cas non convergé, exit non nul ;
    --faute poids_non_entier|poids_negatif|poids_non_fini|
            segments_desordonnes         : la faute doit être rejetée
                                           (exit non nul).
"""

from __future__ import annotations

import json
import sys

import numpy as np
from scipy.stats import norm, rankdata

RHAT_SEUIL = 1.01
ESS_SEUIL = 1000.0
BURN_IN = 0.30
TOLERANCE_ENTIER = 1e-9


class DiagnosticErreur(RuntimeError):
    """Entrée diagnostique invalide (poids, segments, chaînes)."""


# ----------------------------------------------- reconstruction temporelle

def reconstruire_chronologie(segments: list[dict]) -> np.ndarray:
    """Reconstruit les tirages chronologiques d'UNE chaîne.

    ``segments`` : liste de dicts {"ordre": int, "poids": array,
    "valeurs": array}. Les segments de reprise doivent être fournis dans
    l'ordre strictement croissant de leur champ ``ordre`` ; chaque état
    est répété selon son poids entier (>0, fini).
    """

    ordres = [int(seg["ordre"]) for seg in segments]
    if ordres != sorted(ordres) or len(set(ordres)) != len(ordres):
        raise DiagnosticErreur(
            f"segments de reprise désordonnés ou dupliqués : {ordres}"
        )
    morceaux = []
    for seg in segments:
        poids = np.asarray(seg["poids"], dtype=float)
        valeurs = np.asarray(seg["valeurs"], dtype=float)
        if poids.shape != valeurs.shape[:1]:
            raise DiagnosticErreur("poids et valeurs de longueurs différentes")
        if not np.all(np.isfinite(poids)):
            raise DiagnosticErreur("poids non fini détecté")
        if np.any(poids <= 0.0):
            raise DiagnosticErreur("poids négatif ou nul détecté")
        entiers = np.rint(poids)
        if np.max(np.abs(poids - entiers)) > TOLERANCE_ENTIER:
            raise DiagnosticErreur("poids non entier à la tolérance numérique")
        morceaux.append(np.repeat(valeurs, entiers.astype(int), axis=0))
    return np.concatenate(morceaux, axis=0)


def appliquer_burn_in(tirages: np.ndarray) -> np.ndarray:
    debut = int(BURN_IN * len(tirages))
    return tirages[debut:]


# ------------------------------------------- R-hat rang / ESS (Vehtari 2021)

def _rangs_normalises(x: np.ndarray) -> np.ndarray:
    """Rangs moyens (ex aequo moyennés) -> scores z (normalisation par rang)."""
    plat = x.reshape(-1)
    rangs = rankdata(plat, method="average")
    z = norm.ppf((rangs - 0.375) / (len(plat) + 0.25))
    return z.reshape(x.shape)


def _rhat_classique(chaines: np.ndarray) -> float:
    """R-hat scindé classique sur un tableau (m chaînes, n tirages)."""
    m, n = chaines.shape
    demi = n // 2
    scinde = np.concatenate(
        [chaines[:, :demi], chaines[:, demi: 2 * demi]], axis=0
    )
    moyennes = scinde.mean(axis=1)
    variances = scinde.var(axis=1, ddof=1)
    b = demi * moyennes.var(ddof=1)
    w = variances.mean()
    var_plus = (demi - 1) / demi * w + b / demi
    return float(np.sqrt(var_plus / w))


def rhat_rang(chaines: np.ndarray) -> float:
    """R-hat scindé normalisé par rang : max(bulk, replié)."""
    bulk = _rhat_classique(_rangs_normalises(chaines))
    replie = _rhat_classique(
        _rangs_normalises(np.abs(chaines - np.median(chaines)))
    )
    return max(bulk, replie)


def _ess_autocorr(chaines: np.ndarray) -> float:
    """ESS par autocorrélations combinées (Geyer, sommes par paires)."""
    m, n = chaines.shape
    variances = chaines.var(axis=1, ddof=1)
    w = variances.mean()
    b_sur_n = chaines.mean(axis=1).var(ddof=1) if m > 1 else 0.0
    var_plus = (n - 1) / n * w + b_sur_n
    if var_plus <= 0:
        return float(m * n)
    rho_moy = []
    centre = chaines - chaines.mean(axis=1, keepdims=True)
    fft_len = 1 << (2 * n - 1).bit_length()
    for k in range(m):
        f = np.fft.rfft(centre[k], fft_len)
        acov = np.fft.irfft(f * np.conjugate(f))[:n] / n
        rho_moy.append(acov)
    acov_moy = np.mean(rho_moy, axis=0)
    rho = 1.0 - (w - acov_moy) / var_plus
    # sommes par paires (Geyer) : tronquer à la première paire négative,
    # imposer la monotonie décroissante.
    somme = 0.0
    precedent = None
    for t in range(1, n // 2):
        paire = rho[2 * t - 1] + rho[2 * t]
        if paire < 0.0:
            break
        if precedent is not None:
            paire = min(paire, precedent)
        precedent = paire
        somme += paire
    # tau = 1 + 2*somme des paires (rho_1+rho_2), (rho_3+rho_4), ...
    tau = max(1.0 + 2.0 * somme, 1.0 / (m * n))
    return float(m * n / tau)


def ess_bulk(chaines: np.ndarray) -> float:
    return _ess_autocorr(_rangs_normalises(chaines))


def ess_tail(chaines: np.ndarray) -> float:
    """min(ESS des indicatrices des quantiles 5 % et 95 %), calculée
    directement sur les indicatrices (sans normalisation par rang),
    conformément à la définition de Vehtari et al. (2021)."""
    valeurs = []
    for q in (0.05, 0.95):
        seuil = np.quantile(chaines, q)
        indicatrice = (chaines <= seuil).astype(float)
        valeurs.append(_ess_autocorr(indicatrice))
    return float(min(valeurs))


def diagnostic_variante(chaines: list[np.ndarray]) -> dict:
    """Diagnostic complet d'une variante : 8 chaînes exigées."""
    if len(chaines) != 8:
        raise DiagnosticErreur(f"8 chaînes exigées, {len(chaines)} fournies")
    longueurs = [len(c) for c in chaines]
    if min(longueurs) == 0:
        raise DiagnosticErreur("chaîne vide : non contributrice")
    n = min(longueurs)
    bloc = np.stack([c[-n:] for c in chaines])
    return {
        "rhat_rang": rhat_rang(bloc),
        "ess_bulk": ess_bulk(bloc),
        "ess_tail": ess_tail(bloc),
        "chaines_contributrices": len(chaines),
        "converge": bool(
            rhat_rang(bloc) <= RHAT_SEUIL
            and ess_bulk(bloc) >= ESS_SEUIL
            and ess_tail(bloc) >= ESS_SEUIL
        ),
    }


# ------------------------------------------------------- cas synthétiques

def _chaines_synthetiques(cas: str) -> list[np.ndarray]:
    rng = np.random.default_rng(6300)
    if cas == "converge":
        brutes = [rng.standard_normal(4000) for _ in range(8)]
    elif cas == "nonconverge":
        brutes = [rng.standard_normal(4000) + 2.0 * k for k in range(8)]
    elif cas == "ar1":
        brutes = []
        rho = 0.9
        for _ in range(8):
            eps = rng.standard_normal(8000)
            x = np.empty_like(eps)
            x[0] = eps[0]
            for i in range(1, len(eps)):
                x[i] = rho * x[i - 1] + np.sqrt(1 - rho**2) * eps[i]
            brutes.append(x)
    else:
        raise ValueError(f"cas inconnu : {cas}")
    chaines = []
    for brute in brutes:
        segments = [
            {"ordre": 0, "poids": np.ones(len(brute) // 2),
             "valeurs": brute[: len(brute) // 2]},
            {"ordre": 1, "poids": np.ones(len(brute) - len(brute) // 2),
             "valeurs": brute[len(brute) // 2:]},
        ]
        chaines.append(appliquer_burn_in(reconstruire_chronologie(segments)))
    return chaines


def self_test() -> int:
    """Qualification des diagnostics sur cas synthétiques + référence."""
    import getdist
    from getdist.mcsamples import MCSamples

    resultat: dict = {
        "bibliotheque_reference": {"nom": "getdist", "version": getdist.__version__},
        "ancrages_analytiques": "iid : ESS ~ N ; AR(1) rho=0.9 : "
        "ESS ~ N(1-rho)/(1+rho) = N/19",
    }
    echecs: list[str] = []

    # Cas convergé : R-hat ~ 1, ESS >> seuils.
    conv = diagnostic_variante(_chaines_synthetiques("converge"))
    resultat["synthetique_converge"] = {
        k: (round(v, 4) if isinstance(v, float) else v) for k, v in conv.items()
    }
    if not conv["converge"]:
        echecs.append("cas convergé non reconnu")
    n_total = sum(len(c) for c in _chaines_synthetiques("converge"))
    if not (0.5 * n_total <= conv["ess_bulk"] <= 1.5 * n_total):
        echecs.append("ESS bulk iid hors de l'ancrage analytique ±50 %")

    # Cas non convergé : doit être rejeté.
    nonconv = diagnostic_variante(_chaines_synthetiques("nonconverge"))
    resultat["synthetique_nonconverge"] = {
        k: (round(v, 4) if isinstance(v, float) else v)
        for k, v in nonconv.items()
    }
    if nonconv["converge"] or nonconv["rhat_rang"] <= RHAT_SEUIL:
        echecs.append("cas non convergé non détecté")

    # AR(1) : ESS proche de l'ancrage analytique N/19.
    ar1 = _chaines_synthetiques("ar1")
    n_ar1 = sum(len(c) for c in ar1)
    attendu = n_ar1 * (1 - 0.9) / (1 + 0.9)
    d_ar1 = diagnostic_variante(ar1)
    resultat["synthetique_ar1"] = {
        "ess_bulk": round(d_ar1["ess_bulk"], 1),
        "ancrage_analytique": round(attendu, 1),
        "rapport": round(d_ar1["ess_bulk"] / attendu, 3),
    }
    if not (0.5 <= d_ar1["ess_bulk"] / attendu <= 2.0):
        echecs.append("ESS AR(1) hors du facteur 2 de l'ancrage analytique")

    # Référence GetDist : Gelman-Rubin classique sur les mêmes blocs.
    for nom_cas, chaines_cas, attendu_conv in (
        ("converge", _chaines_synthetiques("converge"), True),
        ("nonconverge", _chaines_synthetiques("nonconverge"), False),
    ):
        n = min(len(c) for c in chaines_cas)
        rstat = float(
            MCSamples(
                samples=[c[-n:].reshape(-1, 1) for c in chaines_cas],
                loglikes=[np.zeros(n) for _ in chaines_cas],
                names=["x"], sampler="mcmc",
            ).getGelmanRubin()
        )
        resultat[f"getdist_R_moins_1_{nom_cas}"] = round(rstat, 4)
        concorde = (rstat < 0.01) if attendu_conv else (rstat > 0.01)
        if not concorde:
            echecs.append(f"désaccord getdist sur le cas {nom_cas}")

    resultat["porte"] = {"passe": not echecs, "echecs": sorted(echecs)}
    print(json.dumps(resultat, indent=2, sort_keys=True, ensure_ascii=False))
    return 1 if echecs else 0


def executer_faute(nom: str) -> int:
    """Chaque faute injectée doit être rejetée (exit non nul via exception)."""
    base = {"ordre": 0, "poids": np.ones(10), "valeurs": np.arange(10.0)}
    if nom == "poids_non_entier":
        segments = [{**base, "poids": np.full(10, 0.5)}]
    elif nom == "poids_negatif":
        poids = np.ones(10)
        poids[3] = -1.0
        segments = [{**base, "poids": poids}]
    elif nom == "poids_non_fini":
        poids = np.ones(10)
        poids[3] = np.inf
        segments = [{**base, "poids": poids}]
    elif nom == "segments_desordonnes":
        segments = [{**base, "ordre": 1}, {**base, "ordre": 0}]
    else:
        raise ValueError(f"faute inconnue : {nom}")
    reconstruire_chronologie(segments)  # doit lever DiagnosticErreur
    print("FAUTE NON DÉTECTÉE")
    return 0  # atteint seulement si la garde a échoué


def main() -> None:
    args = sys.argv[1:]
    if args[:1] == ["--self-test"]:
        raise SystemExit(self_test())
    if args[:1] == ["--certifier-synthetique"]:
        diag = diagnostic_variante(_chaines_synthetiques(args[1]))
        print(json.dumps({k: (round(v, 4) if isinstance(v, float) else v)
                          for k, v in diag.items()}, sort_keys=True))
        raise SystemExit(0 if diag["converge"] else 1)
    if args[:1] == ["--faute"]:
        raise SystemExit(executer_faute(args[1]))
    print(__doc__)
    raise SystemExit(2)


if __name__ == "__main__":
    main()
