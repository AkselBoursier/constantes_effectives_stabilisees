"""Adaptateur Cobaya en mémoire pour les variantes X(z) — porte G2.4b.

Construit l'information Cobaya à partir d'un descripteur G2.3 IMMUABLE,
après passage obligatoire par ``validate_config`` (aucune tolérance,
aucune correction implicite). Aucun YAML Cobaya n'est écrit : tout est
en mémoire (D4-A).

Encodage exact (G2.4a §4, pré-enregistrement G2.2a §4-5) :

    H0    ~ U[20, 100] ;  ombh2 ~ U[0.005, 0.1] ;  omm ~ U[0.01, 0.99] ;
    X_i   ~ U[-2, 4] pour chaque amplitude libre ;
    omch2 = omm*(H0/100)^2 - mnu/93.14 - ombh2 ;  contrainte dure omch2 > 0 ;
    traitement acoustique : corrected (imposé par le descripteur validé).

La vraisemblance réutilise ``XZEvaluator`` (instrument G2.1/G2.3) et
expose séparément ``chi2_BAO``, ``chi2_CMB`` et ``chi2_total`` comme
paramètres dérivés auditables. logp = -0.5*(chi2_BAO + chi2_CMB) sur un
point valide ; -inf hors support, omch2 <= 0, fond non fini ou H_X² <= 0.

Le bloc sampler est le bloc G1 gelé, à la clé exacte acceptée par
Cobaya 3.5 (``oversample_power``). La vérification de clé est exécutée
par ``verifier_bloc_sampler`` : la clé correcte doit être acceptée et la
clé fautive ``over_sample_power`` doit être REJETÉE — toute correction
silencieuse est une faute.

Ce module ne lance aucun échantillonnage et ne produit aucun posterior.
"""

from __future__ import annotations

import copy
import math
from typing import Any

import numpy as np

from xz_likelihood_g2_3 import (
    PARAMETRES_FIXES,
    VARIANTES,
    XZEvaluator,
    load_bao_data,
    load_config,
)

# Bloc sampler G1 gelé (G2.4a §4.3). Clé validée pour Cobaya 3.5 :
# « oversample_power ». Aucune variante orthographique n'est acceptée.
SAMPLER_G1: dict[str, Any] = {
    "mcmc": {
        "drag": False,
        "oversample_power": 0.4,
        "proposal_scale": 1.9,
        "covmat": None,
        "temperature": 1,
        "Rminus1_stop": 0.01,
        "Rminus1_cl_stop": 0.02,
        "max_tries": 1000,
    }
}

# Règle d'initialisation qualifiée (G2.4a §10) — paramètres d'efficacité,
# pas des priors scientifiques : refs de fond G1 ; X_i : normale centrée
# en 1 strictement contenue dans P_WS ; proposition identique pour tous
# les nœuds d'une même grille.
REF_FOND = {
    "H0": {"dist": "norm", "loc": 67.36, "scale": 0.01},
    "ombh2": {"dist": "norm", "loc": 0.02237, "scale": 0.0001},
    "omm": {"dist": "norm", "loc": 0.3152, "scale": 0.001},
}
PROPOSAL_FOND = {"H0": 0.05, "ombh2": 0.0001, "omm": 0.0005}
REF_X = {"dist": "norm", "loc": 1.0, "scale": 0.5}
PROPOSAL_X = 0.05

_MNU = PARAMETRES_FIXES["mnu"]
_LAMBDA_OMCH2 = (
    f"lambda omm, H0, ombh2: omm*(H0/100)**2 - {_MNU}/93.14 - ombh2"
)

# --- mode acoustique directeur (amendement A1 ratifié, porte G2.4c-iii) ---
# Le descripteur validé porte le nom nu « corrected » : il est résolu
# EXPLICITEMENT vers corrected-v1.1. Aucun autre mode ne peut devenir
# directeur — ni par variable d'environnement, ni par repli, ni par
# correction silencieuse.
MODE_ACOUSTIQUE_DIRECTEUR = "corrected-v1.1"

# Étiquettes LaTeX gelées des dérivés chi2 (encodage G2.4b) : le chemin
# rapide ne les déclare pas, elles sont ré-injectées par le constructeur
# directeur pour préserver la parité exacte du bloc params.
LATEX_CHI2 = {
    "chi2_BAO": r"\chi^2_\mathrm{BAO}",
    "chi2_CMB": r"\chi^2_\mathrm{CMB}",
    "chi2_total": r"\chi^2_\mathrm{total}",
}
_MODES_REFUSES_COMME_DIRECTEUR = ("corrected-legacy", "fixed")


def _resoudre_mode_directeur(mode_descripteur: str) -> str:
    """Résout « corrected » -> « corrected-v1.1 » ; refuse tout le reste."""
    from xz_background_g2_1 import resolve_acoustic_mode

    if mode_descripteur in _MODES_REFUSES_COMME_DIRECTEUR:
        raise ValueError(
            f"mode acoustique {mode_descripteur!r} interdit comme mode "
            f"directeur : seul {MODE_ACOUSTIQUE_DIRECTEUR!r} est admis"
        )
    resolu = resolve_acoustic_mode(mode_descripteur)  # ValueError si inconnu
    if resolu != MODE_ACOUSTIQUE_DIRECTEUR:
        raise ValueError(
            f"mode acoustique résolu {resolu!r} != mode directeur "
            f"{MODE_ACOUSTIQUE_DIRECTEUR!r} : refus"
        )
    return resolu


class EvaluateurCacheBorne(XZEvaluator):
    """XZEvaluator avec cache CAMB borné (FIFO), pour éviter une
    croissance non bornée de la mémoire pendant un échantillonnage.
    Le calcul est identique ; seul le cache diffère (borne = 8)."""

    _BORNE = 8

    def __init__(self, config, bao_mean, bao_icov):
        super().__init__(config, bao_mean, bao_icov)
        # cache d'instance : indépendant du cache de classe partagé
        self._references = {}

    def _reference(self, h0, ombh2, omm):
        key = (h0, ombh2, omm)
        if key not in self._references:
            if len(self._references) >= self._BORNE:
                self._references.pop(next(iter(self._references)))
            from xz_background_g2_1 import CambReference

            self._references[key] = CambReference.from_g1(
                h0=h0, ombh2=ombh2, omegam=omm
            )
        return self._references[key]


def build_cobaya_info_legacy(
    descripteur: str,
    graine: int,
    bao_mean: np.ndarray | None = None,
    bao_icov: np.ndarray | None = None,
) -> dict[str, Any]:
    """ORACLE DE RÉGRESSION — ancien constructeur monobloc de G2.4b.

    Contenu scientifique STRICTEMENT INCHANGÉ depuis G2.4b : une seule
    vraisemblance externe qui reçoit H0, ombh2, omm ET les X_i, adossée
    à XZEvaluator. Conservé UNIQUEMENT pour la régression et la
    comparaison de performance ; il n'est PLUS le constructeur directeur
    et ne doit jamais être sélectionné par un repli implicite.

    ``graine`` est injectée dans le bloc sampler ; aucune sortie (output)
    n'est définie ici — c'est le lanceur qui l'ajoute après ses gardes.
    """

    config = load_config(descripteur)  # validate_config strict inclus
    if config["traitement_acoustique"] != "corrected":
        raise ValueError("traitement acoustique non 'corrected' : refus")
    if bao_mean is None or bao_icov is None:
        bao_mean, bao_icov = load_bao_data()
    evaluateur = EvaluateurCacheBorne(config, bao_mean, bao_icov)
    noms_x = [item["nom"] for item in config["parametres_x"]]
    input_params = ["H0", "ombh2", "omm", *noms_x]

    def vraisemblance_xz(_derived=None, **valeurs):
        # Convention Cobaya 3.5 (fonction externe avec output_params) :
        # retourner le tuple (logp, {dérivés}).
        point = {nom: float(valeurs[nom]) for nom in input_params}
        sortie = evaluateur.evaluate(point)
        if sortie["logprior"] == -math.inf:
            derives = {"chi2_BAO": np.nan, "chi2_CMB": np.nan,
                       "chi2_total": np.nan}
            return -np.inf, derives
        derives = {"chi2_BAO": sortie["chi2_BAO"],
                   "chi2_CMB": sortie["chi2_CMB"],
                   "chi2_total": sortie["chi2_total"]}
        return -0.5 * sortie["chi2_total"], derives

    params: dict[str, Any] = {
        "H0": {
            "prior": {"min": 20.0, "max": 100.0},
            "ref": dict(REF_FOND["H0"]),
            "proposal": PROPOSAL_FOND["H0"],
            "latex": "H_0",
        },
        "ombh2": {
            "prior": {"min": 0.005, "max": 0.1},
            "ref": dict(REF_FOND["ombh2"]),
            "proposal": PROPOSAL_FOND["ombh2"],
            "latex": r"\Omega_\mathrm{b} h^2",
        },
        "omm": {
            "prior": {"min": 0.01, "max": 0.99},
            "ref": dict(REF_FOND["omm"]),
            "proposal": PROPOSAL_FOND["omm"],
            "latex": r"\Omega_\mathrm{m}",
        },
    }
    for nom in noms_x:
        params[nom] = {
            "prior": {"min": -2.0, "max": 4.0},
            "ref": dict(REF_X),
            "proposal": PROPOSAL_X,
            "latex": nom,
        }
    # « derived » (et non « value ») : aucun composant ne consomme omch2 —
    # l'évaluateur recalcule la même formule en interne ; la clé derived
    # rend la coordonnée auditable dans les chaînes sans exiger d'usage.
    params["omch2"] = {"derived": _LAMBDA_OMCH2, "latex": r"\Omega_\mathrm{c} h^2"}
    for nom_chi2, latex in (
        ("chi2_BAO", r"\chi^2_\mathrm{BAO}"),
        ("chi2_CMB", r"\chi^2_\mathrm{CMB}"),
        ("chi2_total", r"\chi^2_\mathrm{total}"),
    ):
        params[nom_chi2] = {"derived": True, "latex": latex}

    sampler = copy.deepcopy(SAMPLER_G1)
    sampler["mcmc"]["seed"] = int(graine)

    info: dict[str, Any] = {
        "params": params,
        "likelihood": {
            "xz_g2_4": {
                "external": vraisemblance_xz,
                "input_params": list(input_params),
                "output_params": ["chi2_BAO", "chi2_CMB", "chi2_total"],
            }
        },
        "prior": {
            # Contrainte dure omch2 > 0, visible dans l'information même
            # (l'évaluateur la ré-applique aussi : double garde voulue).
            "omch2_positif": (
                f"lambda omm, H0, ombh2: 0.0 if "
                f"(omm*(H0/100)**2 - {_MNU}/93.14 - ombh2) > 0.0 else -np.inf"
            )
        },
        "sampler": sampler,
    }
    info["_xz_meta"] = {
        "variante": config["variante"],
        "grille": VARIANTES[config["variante"]][0],
        "convention": VARIANTES[config["variante"]][1],
        "graine": int(graine),
        "parametres_libres": input_params,
        "backend": "legacy",
        "acoustic_mode": MODE_ACOUSTIQUE_DIRECTEUR,
        "architecture": "monolithic-likelihood",
    }
    return info


def build_cobaya_info(
    descripteur: str,
    graine: int,
    bao_mean: np.ndarray | None = None,
    bao_icov: np.ndarray | None = None,
) -> dict[str, Any]:
    """CONSTRUCTEUR DIRECTEUR — architecture qualifiée G2.4c (porte G2.4d).

    Délègue la construction du graphe à ``xz_fast_g2_4c.build_info_optimisee``
    (source unique : aucune seconde implémentation du chemin rapide n'est
    recopiée ici) puis vérifie que le graphe produit est bien :

        theory     : ReferenceLenteXZ,      input_params = [H0, ombh2, omm]
        likelihood : VraisemblanceRapideXZ, input_params = X_i seulement,
                     requirements = {etat_lent_xz}

    Le mode acoustique directeur est ``corrected-v1.1`` : il est résolu
    explicitement depuis le nom nu « corrected » du descripteur validé.
    ``corrected-legacy``, ``fixed`` et tout mode inconnu sont REFUSÉS
    comme mode directeur — aucun repli, aucune variable implicite, aucune
    correction silencieuse ne peut ramener l'ancien chemin.
    """

    config = load_config(descripteur)  # validate_config strict inclus
    mode_descripteur = config["traitement_acoustique"]
    mode = _resoudre_mode_directeur(mode_descripteur)

    from xz_fast_g2_4c import MODE_ACOUSTIQUE_DIRECTEUR as _MODE_RAPIDE
    from xz_fast_g2_4c import build_info_optimisee

    if _MODE_RAPIDE != MODE_ACOUSTIQUE_DIRECTEUR:
        raise ValueError(
            f"chemin rapide en mode {_MODE_RAPIDE!r} != mode directeur "
            f"{MODE_ACOUSTIQUE_DIRECTEUR!r} : refus"
        )

    info = build_info_optimisee(descripteur, graine)

    # --- parité de l'encodage gelé : étiquettes LaTeX des dérivés ------
    # build_info_optimisee ne déclare que « derived: True » pour les trois
    # chi2 ; l'encodage gelé G2.4b leur associe une étiquette LaTeX. Elle
    # est ré-injectée ici (fichier autorisé) pour que le bloc params du
    # directeur soit STRICTEMENT identique à celui du legacy — sans quoi
    # les colonnes chi2 des chaînes perdraient leur étiquette.
    for nom_chi2, latex in LATEX_CHI2.items():
        bloc = info["params"].get(nom_chi2)
        if isinstance(bloc, dict) and "derived" in bloc:
            bloc.setdefault("latex", latex)

    # --- vérification structurelle du graphe produit (bloquante) -------
    theories = info.get("theory", {})
    if list(theories) != ["reference_lente_xz"]:
        raise ValueError(f"graphe inattendu : theory = {list(theories)}")
    bloc_theory = theories["reference_lente_xz"]
    if bloc_theory.get("external").__name__ != "ReferenceLenteXZ":
        raise ValueError("la Theory lente n'est pas ReferenceLenteXZ")
    if list(bloc_theory.get("input_params", [])) != ["H0", "ombh2", "omm"]:
        raise ValueError(
            f"input_params de la Theory : {bloc_theory.get('input_params')}"
        )
    vraisemblances = info.get("likelihood", {})
    if list(vraisemblances) != ["xz_rapide"]:
        raise ValueError(f"graphe inattendu : likelihood = {list(vraisemblances)}")
    bloc_like = vraisemblances["xz_rapide"]
    if bloc_like.get("external").__name__ != "VraisemblanceRapideXZ":
        raise ValueError("la Likelihood rapide n'est pas VraisemblanceRapideXZ")
    noms_x = [item["nom"] for item in config["parametres_x"]]
    if list(bloc_like.get("input_params", [])) != noms_x:
        raise ValueError(
            f"input_params de la Likelihood : {bloc_like.get('input_params')} "
            f"!= {noms_x} (les X_i seuls sont admis)"
        )
    for interdit in ("H0", "ombh2", "omm"):
        if interdit in bloc_like.get("input_params", []):
            raise ValueError(f"{interdit} ne doit pas entrer directement "
                             "dans la Likelihood rapide")
    # get_requirements ne dépend pas de l'état : on l'interroge sans
    # instancier le composant (une instanciation déclencherait son
    # initialize() et donc un chargement de descripteur).
    exigences = bloc_like["external"].get_requirements(None)
    if set(exigences) != {"etat_lent_xz"}:
        raise ValueError(f"requirements inattendus : {sorted(exigences)}")

    # --- bloc méta interne, jamais transmis à Cobaya -------------------
    info["_xz_meta"] = {
        "variante": config["variante"],
        "grille": VARIANTES[config["variante"]][0],
        "convention": VARIANTES[config["variante"]][1],
        "graine": int(graine),
        "parametres_libres": ["H0", "ombh2", "omm", *noms_x],
        "backend": "optimized",
        "acoustic_mode": mode,
        "architecture": "slow-theory/fast-likelihood",
        "oracle_regression": "build_cobaya_info_legacy",
    }
    return info


def info_pour_cobaya(info: dict[str, Any]) -> dict[str, Any]:
    """Copie de l'information sans le bloc méta interne (_xz_meta)."""
    out = dict(info)
    out.pop("_xz_meta", None)
    return out


def _signature_parite(info: dict[str, Any]) -> dict[str, Any]:
    """Signature comparable de l'information, indépendante du graphe.

    Extrait tout ce qui DOIT être identique entre le constructeur legacy
    et le constructeur directeur : paramètres échantillonnés, priors,
    refs, propositions, dérivés, prior joint, bloc sampler, graine, ordre
    des X_i et métadonnées de variante. Le graphe (une vraisemblance
    monobloc contre Theory lente + Likelihood rapide) est délibérément
    EXCLU : c'est la seule différence autorisée.
    """

    params = info["params"]
    echantillonnes = {
        nom: bloc for nom, bloc in params.items() if "prior" in bloc
    }
    derives = {
        nom: bloc for nom, bloc in params.items() if "derived" in bloc
    }
    meta = info.get("_xz_meta", {})
    return {
        "ordre_parametres_echantillonnes": list(echantillonnes),
        "priors": {n: b["prior"] for n, b in echantillonnes.items()},
        "refs": {n: b.get("ref") for n, b in echantillonnes.items()},
        "proposals": {n: b.get("proposal") for n, b in echantillonnes.items()},
        "latex": {n: b.get("latex") for n, b in echantillonnes.items()},
        "derives": {n: b["derived"] for n, b in derives.items()},
        "latex_derives": {n: b.get("latex") for n, b in derives.items()},
        "ordre_derives": list(derives),
        # comparaison INTÉGRALE du bloc params : aucun champ ne peut
        # diverger en silence (les valeurs non sérialisables — lambdas
        # de dérivation — sont comparées par leur représentation).
        "params_integral": {
            nom: {k: (v if isinstance(v, (str, int, float, bool, type(None),
                                          dict, list)) else repr(v))
                  for k, v in bloc.items()}
            for nom, bloc in params.items()
        },
        "prior_joint": info.get("prior"),
        "sampler": info.get("sampler"),
        "graine": info.get("sampler", {}).get("mcmc", {}).get("seed"),
        "noms_x": [n for n in echantillonnes if n.startswith("X")],
        "variante": meta.get("variante"),
        "grille": meta.get("grille"),
        "convention": meta.get("convention"),
        "parametres_libres": meta.get("parametres_libres"),
    }


def comparer_parite(descripteur: str, graine: int) -> dict[str, Any]:
    """Compare legacy et directeur sur tout ce qui doit être identique.

    Retourne {'identique': bool, 'differences': [...], 'graphes': {...}}.
    Toute différence hors graphe est une faute de porte.
    """

    legacy = build_cobaya_info_legacy(descripteur, graine)
    directeur = build_cobaya_info(descripteur, graine)
    sig_l = _signature_parite(legacy)
    sig_d = _signature_parite(directeur)
    differences = [
        {"champ": cle, "legacy": sig_l[cle], "directeur": sig_d[cle]}
        for cle in sig_l
        if sig_l[cle] != sig_d[cle]
    ]
    return {
        "identique": not differences,
        "differences": differences,
        "graphes": {
            "legacy": {
                "theory": sorted(legacy.get("theory", {})),
                "likelihood": sorted(legacy.get("likelihood", {})),
            },
            "directeur": {
                "theory": sorted(directeur.get("theory", {})),
                "likelihood": sorted(directeur.get("likelihood", {})),
            },
        },
        "backend_legacy": legacy["_xz_meta"]["backend"],
        "backend_directeur": directeur["_xz_meta"]["backend"],
        "acoustic_mode": directeur["_xz_meta"]["acoustic_mode"],
    }


def verifier_bloc_sampler(descripteur: str, mode: str) -> None:
    """Vérifie la clé exacte du bloc sampler sous Cobaya 3.5.

    mode='bonne'   : l'information gelée doit être ACCEPTÉE (test=True) ;
    mode='fautive' : la clé « over_sample_power » doit être REJETÉE —
                     si Cobaya l'accepte ou la corrige silencieusement,
                     une exception est levée (échec de qualification).
    Aucun échantillonnage : initialisation seulement (test=True).

    Depuis G2.4d, le CONSTRUCTEUR DIRECTEUR (architecture lente/rapide)
    est testé par défaut.
    """

    from cobaya.run import run

    info = info_pour_cobaya(build_cobaya_info(descripteur, graine=0))
    if mode == "bonne":
        run(info, test=True)
        return
    if mode == "fautive":
        info_faute = copy.deepcopy(info)
        # deepcopy ne copie pas les classes externes : les réinjecter.
        info_faute["likelihood"] = info["likelihood"]
        if "theory" in info:
            info_faute["theory"] = info["theory"]
        bloc = info_faute["sampler"]["mcmc"]
        bloc["over_sample_power"] = bloc.pop("oversample_power")
        try:
            run(info_faute, test=True)
        except Exception:
            return  # rejet attendu : conforme
        raise RuntimeError(
            "FAUTE NON DÉTECTÉE : Cobaya a accepté 'over_sample_power' — "
            "correction silencieuse interdite."
        )
    raise ValueError(f"mode inconnu : {mode}")
