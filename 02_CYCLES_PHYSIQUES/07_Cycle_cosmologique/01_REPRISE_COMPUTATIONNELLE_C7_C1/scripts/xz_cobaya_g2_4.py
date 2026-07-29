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


def build_cobaya_info(
    descripteur: str,
    graine: int,
    bao_mean: np.ndarray | None = None,
    bao_icov: np.ndarray | None = None,
) -> dict[str, Any]:
    """Information Cobaya complète, en mémoire, pour un descripteur G2.3.

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
    }
    return info


def info_pour_cobaya(info: dict[str, Any]) -> dict[str, Any]:
    """Copie de l'information sans le bloc méta interne (_xz_meta)."""
    out = dict(info)
    out.pop("_xz_meta", None)
    return out


def verifier_bloc_sampler(descripteur: str, mode: str) -> None:
    """Vérifie la clé exacte du bloc sampler sous Cobaya 3.5.

    mode='bonne'   : l'information gelée doit être ACCEPTÉE (test=True) ;
    mode='fautive' : la clé « over_sample_power » doit être REJETÉE —
                     si Cobaya l'accepte ou la corrige silencieusement,
                     une exception est levée (échec de qualification).
    Aucun échantillonnage : initialisation seulement (test=True).
    """

    from cobaya.run import run

    info = info_pour_cobaya(build_cobaya_info(descripteur, graine=0))
    if mode == "bonne":
        run(info, test=True)
        return
    if mode == "fautive":
        info_faute = copy.deepcopy(info)
        # deepcopy ne copie pas la fonction externe : la réinjecter.
        info_faute["likelihood"] = info["likelihood"]
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
