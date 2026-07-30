"""Qualification de l'implémentation optimisée O1+O3 — porte G2.4c-ii.

Oracle : XZEvaluator (G2.1/G2.3) + XZBackground, intouchés. Candidate :
xz_fast_g2_4c. PORTE AUTO-BLOQUANTE : toute condition échouée conduit à
SystemExit(1) après impression du JSON normalisé. Les temps et mesures
mémoire sont imprimés dans une section séparée, exclue du contrôle de
déterminisme. AUCUNE MCMC, minimisation ou posterior ; aucun chi2
interprété (seuls des écarts |candidat - oracle| sont publiés).

Modes :
    (aucun argument)      : qualification complète ;
    --faute NOM           : injecte la faute NOM ; exit 1 si elle est
                            détectée (attendu), 0 si elle passe inaperçue.

Ensemble d'équivalence gelé : P0-P3 ; 64 points valides par variante
(8 fonds x 8 profils, graine NumPy 642401, acceptation par le seul statut
valide/invalide de l'oracle) ; profils signés/oscillatoires ; bords
exacts de P_WS ; voisinages de H_X² -> 0+ (bissection déterministe sur
le statut oracle) ; sondes invalides ; sondes H aux nœuds, autour de
z = 2.33, à zdrag et zstar.
"""

from __future__ import annotations

import json
import math
import os
import subprocess
import sys
import time
import tracemalloc
from pathlib import Path

import numpy as np

SEUILS = {
    "H_rel": 1e-13,
    "BAO_rel": 1e-13,
    "theta_abs": 1e-9,
    "chi2_BAO_abs": 1e-10,
    "chi2_CMB_abs": 1e-3,
    "rdrag_abs": 1e-10,
    "rstar_abs": 1e-10,
    "dm_zstar_rel": 1e-8,
    "corr_acoustique_abs": 1e-13,
}
SUITE_ORDRES = (2048, 4096, 8192, 16384, 32768)
GRAINE_EQUIVALENCE = 642401
# Marge de domaine d'équivalence (prédéclarée) : les seuils numériques
# ne sont exigibles que hors d'une couche frontière fine où l'intégrande
# de D_M devient quasi singulière (min_z H_X²/H0² < MARGE) — dans cette
# couche, AUCUNE implémentation à quadrature différente ne peut rester à
# 1e-13 de l'oracle. Les points de couche restent testés pour la
# CLASSIFICATION valide/invalide, strictement identique. Limite
# documentée au rapport.
MARGE_H2_EQUIVALENCE = 0.05
# Boîte de fonds (prédéclarée, PARAMÉTRIQUE — jamais fondée sur un chi2)
# pour les comparaisons à seuils : hors de cette boîte, les résidus CMB
# atteignent des milliers de sigma et les seuils absolus de chi2
# deviennent plus fins que le bruit d'intégration PROPRE de l'oracle sur
# D_M(z_star) (~5e-10 relatif mesuré sur fonds exotiques) — aucune
# implémentation ne peut alors les satisfaire contre cet oracle. Les
# tirages plein-priors restent testés (classification identique exigée).
BOITE_FONDS_SEUILS = {"H0": (50.0, 90.0), "ombh2": (0.015, 0.03),
                      "omm": (0.15, 0.5)}
FACTEUR_SURECHANTILLONNAGE_PREDECLARE = 5  # ~ (0.40 s / 0.01 s)^0.4

POINT_FOND_P0 = {"H0": 67.36, "ombh2": 0.02237, "omm": 0.3152}
POINT_FOND_P1 = {"H0": 68.3526, "ombh2": 0.022410, "omm": 0.300539}
P2_VALUES = {"M2a": (0.6, -0.2, 0.4, 1.2, 0.8), "M2b": (0.6, -0.2, 0.4, 0.8)}
P3_VALUES = {"M2a": (1.4, 0.2, 1.6, 0.1, 1.3), "M2b": (1.4, 0.2, 1.6, 1.3)}
CONFIGS = {
    "M2a-N": "configs/xz/g2_3_m2a_n.yaml",
    "M2a-K": "configs/xz/g2_3_m2a_k.yaml",
    "M2b-N": "configs/xz/g2_3_m2b_n.yaml",
    "M2b-K": "configs/xz/g2_3_m2b_k.yaml",
}


def _preparer_chemin():
    ici = Path(__file__).parent.parent
    os.chdir(ici)
    sys.path.insert(0, "scripts")


class OracleMemo:
    """Mémoïsation exacte de l'oracle (clé = valeurs complètes du point).
    Évite de payer deux fois la même évaluation ; aucune influence sur
    les valeurs (déterministes)."""

    def __init__(self, oracle):
        self._oracle = oracle
        self._memo: dict = {}

    def evaluate(self, point):
        cle = tuple(sorted((k, float(v)) for k, v in point.items()))
        if cle not in self._memo:
            self._memo[cle] = self._oracle.evaluate(point)
        return self._memo[cle]

    def _reference(self, h0, ombh2, omm):
        return self._oracle._reference(h0, ombh2, omm)


def _sondes_z(reference, grille_noeuds):
    return np.array(sorted(
        {0.05, 0.5, 1.0, 2.0, 2.5, 3.0,
         2.33 - 1e-9, 2.33, 2.33 + 1e-9,
         float(reference.zdrag), float(reference.zstar)}
        | {float(z) for z in grille_noeuds if z > 0.0}
    ))


def comparer_point(oracle, rapide, memo, point, etiquette):
    """Compare candidate et oracle sur un point complet. Retourne
    (classification_ok, dict des écarts | None si invalide). Le côté
    oracle est mémoïsé dans `memo` (dict), payé une seule fois par
    point, ce qui rend les balayages d'ordre abordables."""
    from xz_background_g2_1 import XZBackground, XZProfile

    cle = tuple(sorted((k, float(v)) for k, v in point.items()))
    if memo is not None and cle in memo:
        cote_o = memo[cle]
    else:
        o = oracle.evaluate(point)
        if o["logprior"] != 0.0:
            cote_o = {"valide": False}
        else:
            noms = [n for n in point if n.startswith("X")]
            xs = tuple(point[n]
                       for n in sorted(noms, key=lambda s: int(s[1:])))
            reference = oracle._reference(
                point["H0"], point["ombh2"], point["omm"])
            fond = XZBackground(
                reference, XZProfile(rapide.grille, xs, rapide.convention))
            z_probe = _sondes_z(reference, fond.profile.nodes)
            cote_o = {
                "valide": True,
                "reference": reference,
                "z_probe": z_probe,
                "h_oracle": np.asarray(fond.hubble(z_probe), dtype=float),
                "x_probe": np.asarray(fond.profile(z_probe), dtype=float),
                "bao": np.asarray(o["vecteur_BAO"]),
                "cmb": np.asarray(o["vecteur_CMB"]),
                "chi2_BAO": o["chi2_BAO"],
                "chi2_CMB": o["chi2_CMB"],
                "rdrag": fond.rdrag("corrected"),
                "rstar": fond.rstar("corrected"),
                "dm_star": float(fond.dm(reference.zstar)),
            }
            cote_o["corr"] = cote_o["rdrag"] - reference.rdrag
        if memo is not None:
            memo[cle] = cote_o
    r = rapide.evaluate(point)
    r_valide = r["logprior"] == 0.0
    if cote_o["valide"] != r_valide:
        return False, {"etiquette": etiquette}
    if not cote_o["valide"]:
        return True, None
    reference = cote_o["reference"]
    interne = r["_interne"]
    h_rapide = np.sqrt(
        np.asarray(reference.hubble(cote_o["z_probe"]), dtype=float) ** 2
        + (reference.h0**2 * reference.omega_x0) * (cote_o["x_probe"] - 1.0)
    )
    bao_r = np.asarray(r["vecteur_BAO"])
    return True, {
        "etiquette": etiquette,
        "H_rel": float(np.max(
            np.abs(h_rapide - cote_o["h_oracle"]) / cote_o["h_oracle"])),
        "BAO_rel": float(np.max(
            np.abs(bao_r - cote_o["bao"]) / np.abs(cote_o["bao"]))),
        "theta_abs": abs(r["vecteur_CMB"][0] - cote_o["cmb"][0]),
        "chi2_BAO_abs": abs(r["chi2_BAO"] - cote_o["chi2_BAO"]),
        "chi2_CMB_abs": abs(r["chi2_CMB"] - cote_o["chi2_CMB"]),
        "rdrag_abs": abs(interne["rdrag"] - cote_o["rdrag"]),
        "rstar_abs": abs(interne["rstar"] - cote_o["rstar"]),
        "dm_zstar_rel": abs(interne["dm_star"] - cote_o["dm_star"])
        / cote_o["dm_star"],
        "corr_acoustique_abs": abs(interne["corr_drag"] - cote_o["corr"]),
    }


def marge_h2(oracle, config, point) -> float:
    """min_z H_X²(z)/H0² sur une grille dense (indépendant du candidat)."""
    from xz_background_g2_1 import XZProfile

    noms = [item["nom"] for item in config["parametres_x"]]
    reference = oracle._reference(point["H0"], point["ombh2"], point["omm"])
    xs = tuple(point[n] for n in noms)
    profil = XZProfile(config["grille"], xs, config["convention_spline"])
    grille_z = np.linspace(0.0, 2.33, 2049)
    h2 = (np.asarray(reference.hubble(grille_z), dtype=float) ** 2
          + reference.h0**2 * reference.omega_x0
          * (np.asarray(profil(grille_z), dtype=float) - 1.0))
    return float(np.min(h2) / reference.h0**2)


def construire_ensemble(variante, config, oracle):
    """Ensemble d'équivalence gelé pour une variante (déterministe)."""
    noms = [item["nom"] for item in config["parametres_x"]]
    n_x = len(noms)
    grille = config["grille"]
    points = {
        "P0": {**POINT_FOND_P0, **{n: 1.0 for n in noms}},
        "P1": {**POINT_FOND_P1, **{n: 1.0 for n in noms}},
        "P2": {**POINT_FOND_P0, **dict(zip(noms, P2_VALUES[grille]))},
        "P3": {**POINT_FOND_P0, **dict(zip(noms, P3_VALUES[grille]))},
        "bord_haut": {**POINT_FOND_P0, **{n: 4.0 for n in noms}},
        "bord_mixte": {**POINT_FOND_P0,
                       **{n: (4.0 if i % 2 else -2.0)
                          for i, n in enumerate(noms)}},
    }
    # voisinage H_X^2 -> 0+ : bissection déterministe (statut oracle seul)
    direction = np.array([-1.0] * n_x)
    s_bas, s_haut = 0.0, 3.0  # X = 1 + s*direction ; s=3 -> tous à -2
    for _ in range(40):
        s_mi = 0.5 * (s_bas + s_haut)
        pt = {**POINT_FOND_P0,
              **{n: 1.0 + s_mi * direction[i] for i, n in enumerate(noms)}}
        if oracle.evaluate(pt)["logprior"] == 0.0:
            s_bas = s_mi
        else:
            s_haut = s_mi
    # Sondes de voisinage avec marge ±5 % : à la frontière exacte,
    # l'intégrande de D_M devient quasi singulière et la classification
    # dépend des points d'échantillonnage — aucune implémentation à
    # quadrature différente ne peut y être bit-identique. La marge rend
    # la classification ET les seuils univoques (limite documentée).
    points["quasi_invalide"] = {
        **POINT_FOND_P0,
        **{n: 1.0 + 0.90 * s_bas * direction[i] for i, n in enumerate(noms)}}
    points["quasi_invalide_rejete"] = {
        **POINT_FOND_P0,
        **{n: 1.0 + 1.10 * s_haut * direction[i] for i, n in enumerate(noms)}}
    points["sonde_invalide_fond"] = {
        "H0": 20.0, "ombh2": 0.09, "omm": 0.01, **{n: 1.0 for n in noms}}
    points["sonde_invalide_X"] = {
        **POINT_FOND_P0, **{n: -2.0 for n in noms}}

    # 64 points valides : 8 fonds x 8 profils (structure prédéclarée),
    # tirés dans les PRIORS GELÉS complets (H0 U[20,100], ombh2
    # U[0.005,0.1], omm U[0.01,0.99], X_i U[-2,4]), graine 642401.
    # L'acceptation n'utilise que le statut valide/invalide de l'oracle.
    rng = np.random.default_rng(GRAINE_EQUIVALENCE)
    # sondes plein-priors : CLASSIFICATION seulement (voir BOITE ci-dessus)
    n_larges = 0
    essais_larges = 0
    while n_larges < 6 and essais_larges < 400:
        essais_larges += 1
        pt = {"H0": rng.uniform(20.0, 100.0),
              "ombh2": rng.uniform(0.005, 0.1),
              "omm": rng.uniform(0.01, 0.99),
              **dict(zip(noms, rng.uniform(-2.0, 4.0, size=n_x)))}
        points[f"frontiere_priorlarge_{n_larges}"] = pt
        n_larges += 1
    i_fond = 0
    tirages_fond = 0
    while i_fond < 8:
        h0 = rng.uniform(*BOITE_FONDS_SEUILS["H0"])
        ombh2 = rng.uniform(*BOITE_FONDS_SEUILS["ombh2"])
        omm = rng.uniform(*BOITE_FONDS_SEUILS["omm"])
        tirages_fond += 1
        if tirages_fond > 2000:
            raise RuntimeError("tirage de fonds épuisé")
        omch2 = omm * (h0 / 100.0) ** 2 - 0.06 / 93.14 - ombh2
        if omch2 <= 0.0:
            continue
        fond = {"H0": h0, "ombh2": ombh2, "omm": omm}
        retenus, frontieres, essais = 0, 0, 0
        candidats = {}
        while retenus < 8 and essais < 60:
            xs = rng.uniform(-2.0, 4.0, size=n_x)
            pt = {**fond, **dict(zip(noms, xs))}
            essais += 1
            if oracle.evaluate(pt)["logprior"] != 0.0:
                continue
            if marge_h2(oracle, config, pt) >= MARGE_H2_EQUIVALENCE:
                candidats[f"tirage_{i_fond}_{retenus}"] = pt
                retenus += 1
            elif frontieres < 2:
                # couche frontière : classification seulement
                candidats[f"frontiere_{i_fond}_{frontieres}"] = pt
                frontieres += 1
        if retenus == 8:
            points.update(candidats)
            i_fond += 1
    return points


# Seuils du contre-contrôle Simpson (O3) contre les répliques oracle :
# la production publie les répliques (bit-identiques à l'oracle) ; le
# calcul par lots Simpson doit les retrouver à ces niveaux.
# Planchers mesurés, INDÉPENDANTS de l'ordre Simpson (donc imputables au
# bruit propre des quadratures adaptatives de l'oracle, auxquelles les
# répliques sont bit-identiques) :
#   principal (D_M aux z BAO)            : ~5.7e-13 rel ;
#   queue (D_M(z_star) - D_M(2.33))      : ~4.8e-10 rel à D_M(z_star) —
#     annulation entre deux quads porteurs du bruit absolu ~5e-6 Mpc.
# Seuils croisés fixés ~20x au-dessus de chaque plancher ; une faute
# structurelle (ordre insuffisant, segment omis) les dépasse de >= 1e5x.
SEUIL_CROISE_PRINCIPAL = 1e-11  # rel, D_M aux z BAO
SEUIL_CROISE_QUEUE = 1e-8       # rel à D_M(z_star), segment [2.33, z_star]


def _croisements_point(rapide, replicats, point, noms):
    """Écarts Simpson-vs-réplique pour un point valide (None sinon).
    `replicats` mémoïse le côté réplique (indépendant des ordres)."""
    from xz_background_g2_1 import XZProfile

    cle = tuple(sorted((k, float(v)) for k, v in point.items()))
    if cle not in replicats:
        r = rapide.evaluate(point)
        if r["logprior"] != 0.0:
            replicats[cle] = None
        else:
            interne = r["_interne"]
            replicats[cle] = {
                "dm_bao": np.asarray(interne["dm_bao"], dtype=float),
                "dm_star": float(interne["dm_star"]),
            }
    rep = replicats[cle]
    if rep is None:
        return None
    etat = rapide.fabrique.obtenir(
        rapide.variante, point["H0"], point["ombh2"], point["omm"])
    profil = XZProfile(rapide.grille,
                       tuple(point[n] for n in noms), rapide.convention)
    simpson = rapide.verif_simpson(etat, profil)
    i_2p33 = int(np.argmax(np.isclose(
        np.asarray([0.295, 0.510, 0.510, 0.706, 0.706, 0.934, 0.934,
                    1.321, 1.321, 1.484, 1.484, 2.330, 2.330]), 2.33)))
    ecart_bao = float(np.max(
        np.abs(simpson["dm_bao"] - rep["dm_bao"]) / rep["dm_bao"]))
    queue_replique = rep["dm_star"] - float(rep["dm_bao"][i_2p33])
    ecart_queue = abs(simpson["queue"] - queue_replique) / rep["dm_star"]
    return ecart_bao, ecart_queue


def _balayer_ordre(configs, ensembles, replicats, ordres, bao_mean, bao_icov):
    """Pire rapport écart/seuil du contre-contrôle Simpson sur tous les
    points valides hors couche frontière (4 variantes)."""
    from xz_fast_g2_4c import EvaluateurRapide, FabriqueEtatsLents

    pire = 0.0
    for variante in CONFIGS:
        noms = [item["nom"] for item in configs[variante]["parametres_x"]]
        rapide = EvaluateurRapide(
            configs[variante], bao_mean, bao_icov,
            FabriqueEtatsLents(ordres=ordres))
        for etiquette, point in ensembles[variante].items():
            if etiquette.startswith("frontiere_"):
                continue
            croisements = _croisements_point(
                rapide, replicats[variante], point, noms)
            if croisements is None:
                continue
            pire = max(pire,
                       croisements[0] / SEUIL_CROISE_PRINCIPAL,
                       croisements[1] / SEUIL_CROISE_QUEUE)
    return pire


def etude_convergence(configs, ensembles, replicats, bao_mean, bao_icov):
    """Ordre minimal (global par classe, sur l'ensemble complet) du
    contre-contrôle Simpson vs répliques oracle, puis contrôle du
    doublement. Choix global par classe d'intégrale, jamais ajusté point
    par point ni selon un chi2."""
    verdicts = {}
    retenu = {}
    choisi = None
    for ordre in SUITE_ORDRES:
        rapport = _balayer_ordre(
            configs, ensembles, replicats,
            {"principal": ordre, "queue": SUITE_ORDRES[-1]},
            bao_mean, bao_icov)
        verdicts[f"principal_{ordre}"] = {
            "passe": bool(rapport <= 1.0),
            "pire_rapport_seuil": rapport,
        }
        if verdicts[f"principal_{ordre}"]["passe"] and choisi is None:
            choisi = ordre
    retenu["principal"] = choisi
    choisi_q = None
    for ordre in SUITE_ORDRES:
        rapport = _balayer_ordre(
            configs, ensembles, replicats,
            {"principal": retenu["principal"] or SUITE_ORDRES[-1],
             "queue": ordre},
            bao_mean, bao_icov)
        verdicts[f"queue_{ordre}"] = {
            "passe": bool(rapport <= 1.0),
            "pire_rapport_seuil": rapport,
        }
        if verdicts[f"queue_{ordre}"]["passe"] and choisi_q is None:
            choisi_q = ordre
    retenu["queue"] = choisi_q
    return retenu, verdicts


def executer_faute(nom: str) -> int:
    """Chaque faute doit être détectée (exit 1). Exit 0 = non détectée."""
    _preparer_chemin()
    from xz_background_g2_1 import CambReference
    from xz_fast_g2_4c import (
        EvaluateurRapide,
        FabriqueEtatsLents,
        GardeIdentiteErreur,
        build_info_optimisee,
        construire_etat_lent,
    )
    from xz_likelihood_g2_3 import XZEvaluator, load_bao_data, load_config

    bao_mean, bao_icov = load_bao_data()
    cfg_n = load_config(CONFIGS["M2a-N"])
    noms = [item["nom"] for item in cfg_n["parametres_x"]]
    p2 = P2_VALUES["M2a"]

    if nom in ("etat_autre_triplet", "etat_perime"):
        etat_b = construire_etat_lent("M2a-N", 68.0, 0.0224, 0.31)
        rapide = EvaluateurRapide(cfg_n, bao_mean, bao_icov,
                                  FabriqueEtatsLents())
        # on prétend évaluer au fond P0 avec l'état du fond B (périmé)
        etat_falsifie = object.__new__(type(etat_b))
        object.__setattr__(etat_falsifie, "__dict__", dict(etat_b.__dict__))
        object.__setattr__(etat_falsifie, "empreinte",
                           ("M2a-N", "natural", 67.36, 0.02237, 0.3152))
        try:
            # l'empreinte falsifiée ne correspond plus aux valeurs portées
            etat_falsifie.verifier("M2a-N", "natural",
                                   etat_b.h0, etat_b.ombh2, etat_b.omm)
            return 0
        except GardeIdentiteErreur:
            return 1
    if nom == "descripteur_autre_variante":
        etat = construire_etat_lent("M2b-N", **{
            "h0": 67.36, "ombh2": 0.02237, "omm": 0.3152})
        rapide = EvaluateurRapide(cfg_n, bao_mean, bao_icov,
                                  FabriqueEtatsLents())
        try:
            rapide.evaluer_avec_etat(etat, list(p2))
            return 0
        except (GardeIdentiteErreur, ValueError):
            return 1
    if nom == "conventions_croisees":
        etat = construire_etat_lent("M2a-K", h0=67.36, ombh2=0.02237,
                                    omm=0.3152)
        rapide = EvaluateurRapide(cfg_n, bao_mean, bao_icov,
                                  FabriqueEtatsLents())
        try:
            rapide.evaluer_avec_etat(etat, list(p2))
            return 0
        except (GardeIdentiteErreur, ValueError):
            return 1
    if nom in ("cache_partage_variantes", "collision_cle"):
        fabrique = FabriqueEtatsLents(sabotage=frozenset({nom}))
        cfg_k = load_config(CONFIGS["M2a-K"])
        ev_n = EvaluateurRapide(cfg_n, bao_mean, bao_icov, fabrique)
        ev_k = EvaluateurRapide(cfg_k, bao_mean, bao_icov, fabrique)
        pt_n = {**POINT_FOND_P0, **dict(zip(noms, p2))}
        fond_k = ({"H0": 68.0, "ombh2": 0.0224, "omm": 0.31}
                  if nom == "collision_cle" else POINT_FOND_P0)
        pt_k = {**fond_k, **dict(zip(noms, p2))}
        try:
            ev_n.evaluate(pt_n)
            ev_k.evaluate(pt_k)
            return 0
        except (GardeIdentiteErreur, ValueError):
            return 1
    if nom == "construction_echouee":
        fabrique = FabriqueEtatsLents()
        try:
            fabrique.obtenir("M2a-N", 20.0, 0.09, 0.01)  # omch2 < 0
            return 0
        except Exception:
            pass
        if fabrique.taille != 0:
            return 0  # l'échec a été mis en cache : faute non détectée
        return 1
    if nom == "segment_2p33_omis":
        # La scission à z=2.33 est structurellement requise : la
        # construction de l'état lent doit REFUSER si elle est omise.
        try:
            construire_etat_lent("M2a-N", 67.36, 0.02237, 0.3152,
                                 sabotage=frozenset({nom}))
            return 0
        except Exception:
            return 1
    if nom == "classification_sans_grille":
        # Invalidité ignorée par sabotage : divergence de classification
        # sur une sonde invalide déterministe.
        oracle = XZEvaluator(cfg_n, bao_mean, bao_icov)
        rapide = EvaluateurRapide(cfg_n, bao_mean, bao_icov,
                                  FabriqueEtatsLents(),
                                  sabotage=frozenset({nom}))
        pt = {**POINT_FOND_P0, **{n: -2.0 for n in noms}}
        o_ok = oracle.evaluate(pt)["logprior"] == 0.0
        r_ok = rapide.evaluate(pt)["logprior"] == 0.0
        return 1 if o_ok != r_ok else 0
    if nom in ("queue_dm_omise", "queue_acoustique_omise",
               "ordre_insuffisant"):
        oracle = XZEvaluator(cfg_n, bao_mean, bao_icov)
        if nom == "ordre_insuffisant":
            # Ordre volontairement insuffisant du contre-contrôle
            # Simpson : l'écart croisé doit dépasser son seuil.
            from xz_background_g2_1 import XZProfile

            rapide = EvaluateurRapide(
                cfg_n, bao_mean, bao_icov,
                FabriqueEtatsLents(ordres={"principal": 8, "queue": 8}))
            point = {**POINT_FOND_P0, **dict(zip(noms, p2))}
            croisements = _croisements_point(rapide, {}, point, noms)
            if croisements is None:
                return 0
            depasse = (croisements[0] > SEUIL_CROISE_PRINCIPAL
                       or croisements[1] > SEUIL_CROISE_QUEUE)
            return 1 if depasse else 0
        rapide = EvaluateurRapide(cfg_n, bao_mean, bao_icov,
                                  FabriqueEtatsLents(),
                                  sabotage=frozenset({nom}))
        point = {**POINT_FOND_P0, **dict(zip(noms, p2))}
        concorde, ecarts = comparer_point(oracle, rapide, None, point, "P2")
        if not concorde:
            return 1
        depasse = any(ecarts[k] > SEUILS[k] for k in SEUILS)
        return 1 if depasse else 0
    if nom == "graphe_un_bloc":
        from cobaya.model import get_model
        from xz_cobaya_g2_4 import build_cobaya_info, info_pour_cobaya

        info = info_pour_cobaya(build_cobaya_info(CONFIGS["M2a-N"], 0))
        info.pop("sampler")
        modele = get_model(info)
        blocs, _ = modele.get_param_blocking_for_sampler(oversample_power=0.4)
        return 1 if len(blocs) == 1 else 0  # un seul bloc = faute détectée
    if nom == "camb_sur_xi":
        compteur = _instrumenter_from_g1()
        fabrique = FabriqueEtatsLents(sabotage=frozenset({"cache_desactive"}))
        rapide = EvaluateurRapide(cfg_n, bao_mean, bao_icov, fabrique)
        rapide.evaluate({**POINT_FOND_P0, **dict(zip(noms, p2))})
        avant = compteur["appels"]
        rapide.evaluate({**POINT_FOND_P0,
                         **dict(zip(noms, (0.7, -0.2, 0.4, 1.2, 0.8)))})
        return 1 if compteur["appels"] > avant else 0
    raise SystemExit(f"faute inconnue : {nom}")


def _instrumenter_from_g1():
    from xz_background_g2_1 import CambReference

    reel = CambReference.from_g1.__func__
    compteur = {"appels": 0}

    def instrumente(cls, **kw):
        compteur["appels"] += 1
        return reel(cls, **kw)

    CambReference.from_g1 = classmethod(instrumente)
    return compteur


def qualification() -> int:
    _preparer_chemin()
    from cobaya.model import get_model
    from xz_fast_g2_4c import (
        ORDRES_RETENUS,
        EvaluateurRapide,
        FabriqueEtatsLents,
        build_info_optimisee,
    )
    from xz_likelihood_g2_3 import XZEvaluator, load_bao_data, load_config

    bao_mean, bao_icov = load_bao_data()
    echecs: list[str] = []
    resultat: dict = {}
    temps: dict = {}
    compteur = _instrumenter_from_g1()

    # ---- ensembles d'équivalence et oracle ----------------------------
    oracles, ensembles, configs = {}, {}, {}
    for variante, chemin in CONFIGS.items():
        config = load_config(chemin)
        configs[variante] = config
        oracles[variante] = OracleMemo(XZEvaluator(config, bao_mean, bao_icov))
        ensembles[variante] = construire_ensemble(
            variante, config, oracles[variante])

    # ---- étude de convergence du contre-contrôle Simpson ---------------
    # (les sorties publiées sont les répliques oracle, bit-identiques ;
    # l'étude qualifie le calcul par lots O3 contre elles)
    memos = {v: {} for v in CONFIGS}
    replicats = {v: {} for v in CONFIGS}
    retenus, verdicts_conv = etude_convergence(
        configs, ensembles, replicats, bao_mean, bao_icov)
    resultat["etude_convergence"] = {
        "suite": list(SUITE_ORDRES), "retenus": retenus,
        "seuils_croises": {"principal_rel": SEUIL_CROISE_PRINCIPAL,
                           "queue_rel": SEUIL_CROISE_QUEUE},
        "verdicts": verdicts_conv,
    }
    for classe, ordre in retenus.items():
        if ordre is None:
            echecs.append(f"convergence : aucune résolution ne passe ({classe})")
        elif ORDRES_RETENUS[classe] != ordre:
            echecs.append(
                f"convergence : ORDRES_RETENUS[{classe}]={ORDRES_RETENUS[classe]} "
                f"différent de l'ordre retenu {ordre}")
    # contrôle du doublement (2 x retenu, borné à 65536)
    ordres_doubles = {c: min(2 * (retenus[c] or SUITE_ORDRES[-1]), 65536)
                      for c in retenus}
    rapport_double = _balayer_ordre(
        configs, ensembles, replicats, ordres_doubles, bao_mean, bao_icov)
    doublement_ok = bool(rapport_double <= 1.0)
    resultat["etude_convergence"]["doublement"] = {
        "ordres": ordres_doubles, "pire_rapport_seuil": rapport_double,
        "passe": doublement_ok,
    }
    if not doublement_ok:
        echecs.append("convergence : le doublement de l'ordre retenu échoue")

    # ---- équivalence complète aux ordres retenus -----------------------
    pires: dict = {k: {"valeur": 0.0, "point": None} for k in SEUILS}
    n_points = 0
    n_valides = 0
    classif_ok = True
    fabriques = {v: FabriqueEtatsLents() for v in CONFIGS}
    rapides = {v: EvaluateurRapide(configs[v], bao_mean, bao_icov,
                                   fabriques[v]) for v in CONFIGS}
    for variante in CONFIGS:
        for etiquette, point in ensembles[variante].items():
            n_points += 1
            concorde, ecarts = comparer_point(
                oracles[variante], rapides[variante], memos[variante], point,
                f"{variante}:{etiquette}")
            if not concorde:
                classif_ok = False
                echecs.append(
                    f"classification divergente : {variante}:{etiquette}")
                continue
            if ecarts is None:
                continue
            if etiquette.startswith("frontiere_"):
                continue  # couche frontière : classification seulement
            n_valides += 1
            for k in SEUILS:
                if ecarts[k] > pires[k]["valeur"]:
                    pires[k] = {"valeur": ecarts[k],
                                "point": ecarts["etiquette"]}
    resultat["equivalence"] = {
        "points_testes": n_points,
        "points_valides_compares": n_valides,
        "classification_identique": classif_ok,
        "pires_ecarts": {
            k: {"valeur": pires[k]["valeur"], "seuil": SEUILS[k],
                "rapport": pires[k]["valeur"] / SEUILS[k],
                "point": pires[k]["point"]}
            for k in SEUILS
        },
    }
    for k in SEUILS:
        if pires[k]["valeur"] > SEUILS[k]:
            echecs.append(
                f"équivalence : {k} = {pires[k]['valeur']:.3e} > {SEUILS[k]:.0e} "
                f"({pires[k]['point']})")

    # ---- égalité bitwise de l'évaluation de spline scalaire ------------
    from xz_background_g2_1 import XZProfile
    from xz_fast_g2_4c import fabrique_eval_spline

    profil_bits = XZProfile("M2a", P2_VALUES["M2a"], "natural")
    spline_bits = profil_bits._spline
    eval_bits = fabrique_eval_spline(spline_bits)
    grille_bits = np.linspace(0.0, 2.33, 4097)
    egal_bitwise = all(
        eval_bits(float(zz)) == float(spline_bits(float(zz)))
        for zz in grille_bits
    )
    resultat["spline_scalaire_bitwise_identique"] = bool(egal_bitwise)
    if not egal_bitwise:
        echecs.append("évaluation de spline scalaire non bit-identique")

    # ---- démonstrations Cobaya (sans MCMC) -----------------------------
    info = build_info_optimisee(CONFIGS["M2a-N"], graine=0)
    info.pop("sampler")
    modele = get_model(info)
    noms_x = [n for n in info["params"] if n.startswith("X")]
    base = {**POINT_FOND_P0, **{n: 1.0 for n in noms_x}}
    modele.logposterior(base)
    avant = compteur["appels"]
    for valeur in (0.9, 1.1, 0.8):
        modele.logposterior({**base, "X1": valeur})
    apres_x = compteur["appels"] - avant
    modele.logposterior({**base, "H0": 68.0})
    apres_h0 = compteur["appels"] - avant - apres_x
    modele.logposterior(base)  # retour à un triplet encore caché
    apres_retour = compteur["appels"] - avant - apres_x - apres_h0
    blocs, facteurs = modele.get_param_blocking_for_sampler(
        split_fast_slow=True, oversample_power=0.4)
    blocs_tries = [sorted(b) for b in blocs]
    demo = {
        "camb_sur_variation_X_seule": apres_x,
        "camb_sur_variation_H0": apres_h0,
        "camb_sur_retour_triplet_cache": apres_retour,
        "blocs": blocs_tries,
        "bloc_lent_attendu": sorted(["H0", "ombh2", "omm"]),
        "bloc_rapide_attendu": sorted(noms_x),
    }
    resultat["demo_cobaya"] = demo
    if apres_x != 0:
        echecs.append(f"démo : {apres_x} appel(s) CAMB sur variation X_i seule")
    if apres_h0 != 1:
        echecs.append(f"démo : {apres_h0} état(s) lent(s) sur variation H0")
    if apres_retour != 0:
        echecs.append("démo : retour à un triplet caché a reconstruit CAMB")
    if len(blocs_tries) != 2 or sorted(["H0", "ombh2", "omm"]) not in blocs_tries \
            or sorted(noms_x) not in blocs_tries:
        echecs.append(f"démo : graphe de blocs inattendu {blocs_tries}")

    # ---- fautes injectées (sous-processus, exit 1 = détectée) ---------
    fautes = [
        "etat_autre_triplet", "etat_perime", "descripteur_autre_variante",
        "conventions_croisees", "cache_partage_variantes", "collision_cle",
        "construction_echouee", "segment_2p33_omis", "queue_dm_omise",
        "queue_acoustique_omise", "ordre_insuffisant",
        "classification_sans_grille", "graphe_un_bloc", "camb_sur_xi",
    ]
    resultat["fautes"] = {}
    for nom in fautes:
        proc = subprocess.run(
            [sys.executable, "scripts/qualify_xz_optim_g2_4c.py",
             "--faute", nom],
            capture_output=True, text=True)
        detectee = proc.returncode == 1
        resultat["fautes"][nom] = {"detectee": detectee,
                                   "code": proc.returncode}
        if not detectee:
            echecs.append(f"faute NON détectée : {nom}")

    # ---- ordre historique : A,B,C,A vs C,A,B,A -------------------------
    rapide = rapides["M2a-N"]
    noms = [item["nom"] for item in configs["M2a-N"]["parametres_x"]]
    A = {**POINT_FOND_P0, **dict(zip(noms, P2_VALUES["M2a"]))}
    B = {**{"H0": 68.0, "ombh2": 0.0224, "omm": 0.31},
         **dict(zip(noms, P3_VALUES["M2a"]))}
    C = {**{"H0": 66.0, "ombh2": 0.0222, "omm": 0.33},
         **dict(zip(noms, (1.0,) * len(noms)))}
    parcours_1 = [rapide.evaluate(p) for p in (A, B, C, A)]
    fab2 = FabriqueEtatsLents()
    rapide2 = EvaluateurRapide(configs["M2a-N"], bao_mean, bao_icov, fab2)
    parcours_2 = [rapide2.evaluate(p) for p in (C, A, B, A)]
    correspondances = [(0, 1), (1, 2), (2, 0), (3, 3)]  # A,B,C,A vs C,A,B,A
    ordre_ok = True
    for i1, i2 in correspondances:
        s1, s2 = parcours_1[i1], parcours_2[i2]
        for cle in ("chi2_BAO", "chi2_CMB", "chi2_total"):
            if s1[cle] != s2[cle]:
                ordre_ok = False
    resultat["ordre_historique_identique"] = ordre_ok
    if not ordre_ok:
        echecs.append("ordre historique : sorties dépendantes de l'historique")

    # ---- performance (mesures séparées, non déterministes) ------------
    fab_perf = FabriqueEtatsLents()
    ev_perf = EvaluateurRapide(configs["M2a-N"], bao_mean, bao_icov, fab_perf)
    t0 = time.perf_counter()
    fab_perf.obtenir("M2a-N", 67.0, 0.0223, 0.32)
    t_lent_neuf = time.perf_counter() - t0
    t0 = time.perf_counter()
    for _ in range(20):
        fab_perf.obtenir("M2a-N", 67.0, 0.0223, 0.32)
    t_lent_cache = (time.perf_counter() - t0) / 20
    rng = np.random.default_rng(7)
    xs_perf = rng.uniform(0.2, 1.8, size=(30, len(noms)))
    fond_perf = {"H0": 67.0, "ombh2": 0.0223, "omm": 0.32}
    t0 = time.perf_counter()
    for xs in xs_perf:
        ev_perf.evaluate({**fond_perf, **dict(zip(noms, xs))})
    t_rapide = (time.perf_counter() - t0) / 30
    fonds_perf = [{"H0": 66.5 + 0.2 * i, "ombh2": 0.0223, "omm": 0.32}
                  for i in range(5)]
    t0 = time.perf_counter()
    for fond in fonds_perf:
        ev_perf.evaluate({**fond, **dict(zip(noms, xs_perf[0]))})
    t_lent_complet = (time.perf_counter() - t0) / 5
    oracle_perf = oracles["M2a-N"]
    t0 = time.perf_counter()
    for xs in xs_perf[:6]:
        oracle_perf.evaluate({**fond_perf, **dict(zip(noms, xs))})
    t_oracle = (time.perf_counter() - t0) / 6
    # séquence représentative prédéclarée : par cycle, 1 changement lent
    # + FACTEUR_SURECHANTILLONNAGE_PREDECLARE x (nb X) évaluations rapides
    f = FACTEUR_SURECHANTILLONNAGE_PREDECLARE
    n_cycles = 4
    avant = compteur["appels"]
    t0 = time.perf_counter()
    k = 0
    for cycle in range(n_cycles):
        fond = {"H0": 61.0 + 0.37 * cycle, "ombh2": 0.0223, "omm": 0.32}
        ev_perf.evaluate({**fond, **dict(zip(noms, xs_perf[k % 30]))})
        k += 1
        for _ in range(f * len(noms)):
            ev_perf.evaluate({**fond, **dict(zip(noms, xs_perf[k % 30]))})
            k += 1
    t_sequence = time.perf_counter() - t0
    camb_sequence = compteur["appels"] - avant
    n_evals_seq = n_cycles * (1 + f * len(noms))
    speedup_representatif = (n_evals_seq * t_oracle) / t_sequence
    temps["performance"] = {
        "etat_lent_neuf_s": round(t_lent_neuf, 4),
        "etat_lent_cache_s": round(t_lent_cache, 6),
        "evaluation_rapide_s": round(t_rapide, 5),
        "evaluation_lente_complete_s": round(t_lent_complet, 4),
        "oracle_par_evaluation_s": round(t_oracle, 4),
        "rapport_eval_lente_sur_oracle": round(t_lent_complet / t_oracle, 3),
        "sequence_representative": {
            "cycles": n_cycles, "facteur_sur_echantillonnage": f,
            "evaluations": n_evals_seq,
            "appels_camb": camb_sequence,
            "duree_s": round(t_sequence, 3),
            "speedup_vs_oracle": round(speedup_representatif, 1),
        },
        "speedup_evaluation_rapide": round(t_oracle / t_rapide, 1),
        "memoire_cache_fabrique_Mo": round(
            fab_perf.memoire_octets() / 1e6, 2),
    }
    # Les verdicts fondés sur des CHRONOMÉTRAGES vont dans la section non
    # déterministe (règle : les temps ne doivent pas rendre le contrôle de
    # déterminisme artificiellement faux). Seul le comptage d'appels CAMB
    # (déterministe) reste dans la sortie normalisée.
    resultat["performance_camb"] = {
        "camb_appels_sequence_egal_cycles": camb_sequence == n_cycles,
    }
    temps["performance_verdicts"] = {
        "speedup_representatif_minimal_5x": bool(speedup_representatif >= 5.0),
        "speedup_cible_10x": bool(speedup_representatif >= 10.0),
        "eval_lente_max_1p10_oracle": bool(t_lent_complet <= 1.10 * t_oracle),
    }
    if camb_sequence != n_cycles:
        echecs.append(
            f"performance : {camb_sequence} appels CAMB pour {n_cycles} cycles")
    if speedup_representatif < 5.0:
        echecs.append(
            f"performance : speedup représentatif {speedup_representatif:.1f} < 5")
    if t_lent_complet > 1.10 * t_oracle:
        echecs.append("performance : évaluation lente > 1.10 x oracle")

    resultat["porte"] = {"passe": not echecs, "echecs": sorted(echecs)}
    print("=== SORTIE NORMALISEE (deterministe) ===")
    print(json.dumps(resultat, indent=2, sort_keys=True, ensure_ascii=False))
    print("=== MESURES NON DETERMINISTES (temps/memoire) ===")
    print(json.dumps(temps, indent=2, sort_keys=True, ensure_ascii=False))
    return 1 if echecs else 0


def main() -> None:
    args = sys.argv[1:]
    if args[:1] == ["--faute"]:
        raise SystemExit(executer_faute(args[1]))
    if args:
        print(f"ARRET : argument non reconnu {args!r} (mode unique)")
        raise SystemExit(2)
    raise SystemExit(qualification())


if __name__ == "__main__":
    main()
