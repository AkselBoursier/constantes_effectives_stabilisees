"""Évaluateur déterministe des configurations X(z) — porte G2.3a (issue #63).

Réutilise `CambReference`, `XZProfile` et `XZBackground` de G2.1 (aucune
réimplémentation du fond). Charge une configuration déclarative
`configs/xz/g2_3_*.yaml`, la valide strictement, puis évalue un point
fourni et retourne :

    logprior, chi2_BAO, chi2_CMB, chi2_total,
    vecteur BAO (13), vecteur CMB (3), statut des contraintes.

Règles du logprior (pré-enregistrement G2.2a, §4-5) :
    0.0   à l'intérieur du support uniforme valide ;
    -inf  hors support, si omch2 <= 0, si le fond est non fini
          ou si H_X^2 <= 0.

AUCUNE fonction d'échantillonnage, de minimisation ou d'optimisation
n'existe dans ce module ; toute inférence exige une décision humaine
distincte (G2.3a).
"""

from __future__ import annotations

import math
import os
from pathlib import Path
from typing import Any

import numpy as np
import yaml

from xz_background_g2_1 import (
    NODES,
    CambReference,
    InvalidBackgroundError,
    XZBackground,
    XZProfile,
)

CMB_MU = np.array([0.01041, 0.02223, 0.14208])
CMB_COV = 1e-9 * np.array(
    [
        [0.006621, 0.12444, -1.1929],
        [0.12444, 21.344, -94.001],
        [-1.1929, -94.001, 1488.4],
    ]
)
CMB_ICOV = np.linalg.inv(CMB_COV)
BAO_REDSHIFTS = np.array(
    [0.295, 0.510, 0.510, 0.706, 0.706, 0.934, 0.934,
     1.321, 1.321, 1.484, 1.484, 2.330, 2.330]
)
BAO_KINDS = (
    "DV_over_rs", "DM_over_rs", "DH_over_rs", "DM_over_rs",
    "DH_over_rs", "DM_over_rs", "DH_over_rs", "DM_over_rs",
    "DH_over_rs", "DM_over_rs", "DH_over_rs", "DH_over_rs",
    "DM_over_rs",
)

VARIANTES = {
    "M2a-N": ("M2a", "natural"),
    "M2a-K": ("M2a", "not-a-knot"),
    "M2b-N": ("M2b", "natural"),
    "M2b-K": ("M2b", "not-a-knot"),
}
PRIOR_X = {"famille": "P_WS", "dist": "uniform", "min": -2.0, "max": 4.0}
PRIORS_FOND = {
    "H0": {"dist": "uniform", "min": 20.0, "max": 100.0},
    "ombh2": {"dist": "uniform", "min": 0.005, "max": 0.1},
    "omm": {"dist": "uniform", "min": 0.01, "max": 0.99},
}
PARAMETRES_FIXES = {"mnu": 0.06, "nnu": 3.044, "tau": 0.0544, "ns": 0.9649, "logA": 3.036}
CLES_REQUISES = {
    "lot", "variante", "grille", "convention_spline", "noeuds", "x0_fixe",
    "parametres_x", "priors_fond", "parametres_fixes", "contraintes_dures",
    "traitement_acoustique", "continuation", "graine", "sorties", "inference",
}
LOT = "c7-c1-g2_3"
CONTRAINTES_DURES = [
    "omch2 > 0",
    "H_X^2 fini et > 0 sur tout le domaine requis",
]
CONTINUATION = "X(z >= 2.33) = X(2.33)"
GRAINES_ATTENDUES = {"M2a-N": 6301, "M2a-K": 6302, "M2b-N": 6303, "M2b-K": 6304}
CLES_PARAM_X = {"nom", "noeud", "prior"}
CLES_SORTIES = {"regle", "variable_environnement", "note"}
CLES_INFERENCE = {"autorisee", "note"}
VARIABLE_SORTIE = "C7C1_XZ_OUT_DIR"


class ConfigError(ValueError):
    """Configuration G2.3 non conforme au schéma strict."""


class SortieSousGitError(RuntimeError):
    """Chemin de sortie refusé : un ancêtre contient un dépôt Git."""


def refuser_sortie_sous_git(path: str | Path) -> Path:
    """Garde de répertoire de sortie : lève SortieSousGitError si `path`
    (résolu) possède un ancêtre contenant `.git`. Retourne le chemin
    résolu si — et seulement si — il est hors de tout dépôt Git."""
    d = Path(path).resolve()
    for parent in [d, *d.parents]:
        if (parent / ".git").exists():
            raise SortieSousGitError(
                f"sortie refusée : {d} est sous le dépôt Git de {parent}"
            )
    return d


def load_bao_data() -> tuple[np.ndarray, np.ndarray]:
    root = os.environ.get("C7C1_DATA_DIR")
    if not root:
        raise RuntimeError("C7C1_DATA_DIR absent : octets BAO indisponibles.")
    base = Path(root) / "desi_bao_dr2"
    rows: list[tuple[float, float, str]] = []
    with (base / "desi_gaussian_bao_ALL_GCcomb_mean.txt").open(encoding="utf-8") as handle:
        for raw in handle:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            z, value, kind = line.split()
            rows.append((float(z), float(value), kind))
    if len(rows) != 13:
        raise RuntimeError(f"13 mesures BAO attendues, {len(rows)} lues.")
    z = np.array([r[0] for r in rows])
    kinds = tuple(r[2] for r in rows)
    if not np.array_equal(z, BAO_REDSHIFTS) or kinds != BAO_KINDS:
        raise RuntimeError("Ordre BAO différent du verrou G1.")
    cov = np.loadtxt(base / "desi_gaussian_bao_ALL_GCcomb_cov.txt")
    if cov.shape != (13, 13):
        raise RuntimeError(f"Covariance BAO non 13x13 : {cov.shape}")
    return np.array([r[1] for r in rows]), np.linalg.inv(cov)


def validate_config(raw: dict[str, Any]) -> dict[str, Any]:
    """Validation stricte du schéma déclaratif (contrôles C1/C2 de G2.3b)."""
    if set(raw.keys()) != CLES_REQUISES:
        manquantes = CLES_REQUISES - set(raw.keys())
        en_trop = set(raw.keys()) - CLES_REQUISES
        raise ConfigError(f"clés manquantes {sorted(manquantes)}, en trop {sorted(en_trop)}")
    if raw["lot"] != LOT:
        raise ConfigError(f"lot {raw['lot']!r} différent de {LOT!r}")
    if raw["contraintes_dures"] != CONTRAINTES_DURES:
        raise ConfigError("contraintes_dures non conformes au contrat exact")
    if raw["continuation"] != CONTINUATION:
        raise ConfigError(f"continuation {raw['continuation']!r} non conforme")
    sorties = raw["sorties"]
    if not isinstance(sorties, dict) or set(sorties.keys()) != CLES_SORTIES:
        raise ConfigError("bloc sorties : clés manquantes ou supplémentaires")
    if sorties["regle"] != "hors_git":
        raise ConfigError("sorties.regle doit valoir 'hors_git'")
    if sorties["variable_environnement"] != VARIABLE_SORTIE:
        raise ConfigError(
            f"sorties.variable_environnement doit valoir {VARIABLE_SORTIE!r}"
        )
    if not isinstance(sorties["note"], str) or not sorties["note"]:
        raise ConfigError("sorties.note doit être une chaîne non vide")
    inference = raw["inference"]
    if not isinstance(inference, dict) or set(inference.keys()) != CLES_INFERENCE:
        raise ConfigError("bloc inference : clés manquantes ou supplémentaires")
    if inference["autorisee"] is not False:
        raise ConfigError("inference.autorisee doit être exactement false")
    if not isinstance(inference["note"], str) or not inference["note"]:
        raise ConfigError("inference.note doit être une chaîne non vide")
    variante = raw["variante"]
    if variante not in VARIANTES:
        raise ConfigError(f"variante inconnue : {variante}")
    grille, convention = VARIANTES[variante]
    if raw["grille"] != grille:
        raise ConfigError(f"grille {raw['grille']} incohérente avec {variante}")
    if raw["convention_spline"] != convention:
        raise ConfigError(
            f"convention {raw['convention_spline']} incohérente avec {variante}"
        )
    noeuds = np.asarray(raw["noeuds"], dtype=float)
    if noeuds.shape != NODES[grille].shape or not np.array_equal(noeuds, NODES[grille]):
        raise ConfigError(f"nœuds non identiques à la grille verrouillée {grille}")
    if not np.all(np.diff(noeuds) > 0.0):
        raise ConfigError("nœuds non strictement croissants")
    if float(raw["x0_fixe"]) != 1.0:
        raise ConfigError("x0_fixe doit valoir exactement 1.0")
    px = raw["parametres_x"]
    if len(px) != len(noeuds) - 1:
        raise ConfigError(f"{len(noeuds) - 1} amplitudes libres attendues, {len(px)} déclarées")
    for i, item in enumerate(px, start=1):
        if not isinstance(item, dict) or set(item.keys()) != CLES_PARAM_X:
            raise ConfigError(
                f"amplitude {i} : clés manquantes ou supplémentaires"
            )
        if item["nom"] != f"X{i}":
            raise ConfigError(f"nom d'amplitude inattendu : {item['nom']} (attendu X{i})")
        if float(item["noeud"]) != float(noeuds[i]):
            raise ConfigError(
                f"{item['nom']} associé au nœud {item['noeud']} au lieu de {noeuds[i]}"
            )
        if item["prior"] != PRIOR_X:
            raise ConfigError(f"prior de {item['nom']} différent de P_WS U[-2,4]")
    if raw["priors_fond"] != PRIORS_FOND:
        raise ConfigError("priors de fond différents du verrou G1")
    if raw["parametres_fixes"] != PARAMETRES_FIXES:
        raise ConfigError("paramètres fixes différents du verrou G1")
    if raw["traitement_acoustique"] != "corrected":
        raise ConfigError("traitement acoustique directeur non 'corrected'")
    if not isinstance(raw["graine"], int):
        raise ConfigError("graine non entière")
    if raw["graine"] != GRAINES_ATTENDUES[variante]:
        raise ConfigError(
            f"graine {raw['graine']} différente de la graine attendue "
            f"{GRAINES_ATTENDUES[variante]} pour {variante}"
        )
    return raw


def load_config(path: str | Path) -> dict[str, Any]:
    with open(path, encoding="utf-8") as handle:
        raw = yaml.safe_load(handle)
    return validate_config(raw)


class XZEvaluator:
    """Évaluation déterministe d'un point sous une configuration validée."""

    _references: dict[tuple[float, float, float], CambReference] = {}

    def __init__(self, config: dict[str, Any], bao_mean: np.ndarray, bao_icov: np.ndarray):
        self.config = config
        self.grille, self.convention = VARIANTES[config["variante"]]
        self.noms_x = [item["nom"] for item in config["parametres_x"]]
        self.bao_mean = bao_mean
        self.bao_icov = bao_icov

    def _reference(self, h0: float, ombh2: float, omm: float) -> CambReference:
        key = (h0, ombh2, omm)
        if key not in self._references:
            self._references[key] = CambReference.from_g1(
                h0=h0, ombh2=ombh2, omegam=omm
            )
        return self._references[key]

    def evaluate(self, point: dict[str, float]) -> dict[str, Any]:
        h0 = float(point["H0"])
        ombh2 = float(point["ombh2"])
        omm = float(point["omm"])
        xs = [float(point[nom]) for nom in self.noms_x]
        fixes = self.config["parametres_fixes"]
        omch2 = omm * (h0 / 100.0) ** 2 - fixes["mnu"] / 93.14 - ombh2

        statut = {
            "dans_support_uniforme": bool(
                PRIORS_FOND["H0"]["min"] <= h0 <= PRIORS_FOND["H0"]["max"]
                and PRIORS_FOND["ombh2"]["min"] <= ombh2 <= PRIORS_FOND["ombh2"]["max"]
                and PRIORS_FOND["omm"]["min"] <= omm <= PRIORS_FOND["omm"]["max"]
                and all(PRIOR_X["min"] <= x <= PRIOR_X["max"] for x in xs)
            ),
            "omch2_positive": bool(omch2 > 0.0),
            "fond_valide": None,
        }
        resultat: dict[str, Any] = {
            "variante": self.config["variante"],
            "point": {"H0": h0, "ombh2": ombh2, "omm": omm,
                      **{n: x for n, x in zip(self.noms_x, xs)}},
            "omch2": omch2,
            "logprior": None,
            "chi2_BAO": None,
            "chi2_CMB": None,
            "chi2_total": None,
            "vecteur_BAO": None,
            "vecteur_CMB": None,
            "contraintes": statut,
        }
        if not statut["dans_support_uniforme"] or not statut["omch2_positive"]:
            resultat["logprior"] = -math.inf
            return resultat

        try:
            reference = self._reference(h0, ombh2, omm)
            profile = XZProfile(self.grille, tuple(xs), self.convention)
            background = XZBackground(reference, profile)
            bao = background.bao_vector(BAO_REDSHIFTS, BAO_KINDS, "corrected")
            cmb = background.cmb_vector("corrected")
        except InvalidBackgroundError:
            statut["fond_valide"] = False
            resultat["logprior"] = -math.inf
            return resultat
        if not (np.all(np.isfinite(bao)) and np.all(np.isfinite(cmb))):
            statut["fond_valide"] = False
            resultat["logprior"] = -math.inf
            return resultat

        statut["fond_valide"] = True
        r_bao = bao - self.bao_mean
        r_cmb = cmb - CMB_MU
        chi2_bao = float(r_bao @ self.bao_icov @ r_bao)
        chi2_cmb = float(r_cmb @ CMB_ICOV @ r_cmb)
        resultat.update(
            logprior=0.0,
            chi2_BAO=chi2_bao,
            chi2_CMB=chi2_cmb,
            chi2_total=chi2_bao + chi2_cmb,
            vecteur_BAO=[float(v) for v in bao],
            vecteur_CMB=[float(v) for v in cmb],
        )
        return resultat
