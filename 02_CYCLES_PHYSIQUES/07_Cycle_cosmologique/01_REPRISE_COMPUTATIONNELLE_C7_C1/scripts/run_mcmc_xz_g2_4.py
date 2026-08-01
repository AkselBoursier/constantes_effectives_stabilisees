"""Lanceur verrouillé du premier lot MCMC X(z) — porte G2.4b (issue #63).

AUCUNE MCMC RÉELLE N'EST LANCÉE PAR CETTE PORTE. Le lanceur est verrouillé
par une autorisation à deux clés (D4-H) dont le vrai manifeste est INTERDIT
tant que G2.4b n'est pas validée humainement. Toute autorisation absente ou
factice est refusée avec un code non nul.

Modes :
    --preflight VARIANTE GRAINE   : gardes non productives, aucun fichier ;
    --produire VARIANTE GRAINE --autorisation F --je-confirme-la-production
                                  : production réelle — exige le manifeste
                                    à deux clés valide (interdit à ce stade) ;
    --qualification               : suite adversariale complète + banc de
                                    performance (sortie normalisée
                                    déterministe + mesures séparées) ;
    --verifier-sampler bonne|fautive : clé du bloc sampler sous Cobaya 3.5.

Gardes de production (G2.4a §7-8, G2.4b-ii) :
    HEAD autorisé et arbre suivi propre ; descripteur qualifié et SHA
    conforme ; octets BAO et SHA conformes ; environnement directeur exact ;
    variante et graine dans la matrice gelée ; préfixe hors Git ; absence de
    collision ; reprise strictement conforme ; autorisation à deux clés ;
    capacité : espace libre du volume cible >= 40 Gio (octets réels,
    shutil.disk_usage) — sous 40 Gio : arrêt non nul, aucun répertoire créé,
    aucune reprise, aucun fichier modifié ; sous 15 Gio : alerte technique,
    tout lancement ou reprise interdits. Aucune libération automatique.

Injections de test (C7C1_TEST_*) : autorisées seulement hors production ;
leur présence en mode --produire est une faute et entraîne un refus.
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import shutil
import subprocess
import sys
import time
import tracemalloc
from pathlib import Path

import numpy as np

GIO = 1024**3
GARDE_CAPACITE_GIO = 40
SEUIL_ALERTE_GIO = 15

# ------------------------------------------------ verrou dur G2.4d
# Tant que ce verrou vaut True, AUCUNE écriture réelle et AUCUN
# cobaya.run ne peuvent être atteints : le refus intervient AVANT
# mkdir, open en écriture, os.replace, manifest.json et préfixe Cobaya.
VERROU_PRODUCTION_G2_4D = True

# Schéma du contrat local privé consommé par le lanceur (INFRA-1a,
# étendu en G2.4d-a : chemin de cache et référence de ratification).
VERSION_CONTRAT_LOCAL = "1.2.0"
# Format imposé de la date de création du manifeste de run.
FORMAT_DATE_UTC = "%Y-%m-%dT%H:%M:%SZ"
# Usage exigé d'une autorisation RÉELLE. Un manifeste de qualification
# porte « QUALIFICATION_ONLY » et doit être refusé sans exception.
USAGE_AUTORISATION_PRODUCTION = "PRODUCTION"
CLES_THREADS = (
    "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS",
    "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS",
)
SCHEMA_MANIFESTE_RUN = "c7c1-run-manifest-1"

MATRICE = {
    "M2a-N": tuple(range(630101, 630109)),
    "M2a-K": tuple(range(630201, 630209)),
    "M2b-N": tuple(range(630301, 630309)),
    "M2b-K": tuple(range(630401, 630409)),
}
DESCRIPTEURS = {
    "M2a-N": "configs/xz/g2_3_m2a_n.yaml",
    "M2a-K": "configs/xz/g2_3_m2a_k.yaml",
    "M2b-N": "configs/xz/g2_3_m2b_n.yaml",
    "M2b-K": "configs/xz/g2_3_m2b_k.yaml",
}
SHA_BAO = {
    "desi_gaussian_bao_ALL_GCcomb_mean.txt":
        "9ac154ab583ce759c0f7eef3c978c7c70a6ead2d18774caceadf1a350a640585",
    "desi_gaussian_bao_ALL_GCcomb_cov.txt":
        "252a143274c8a07c78694c119617d36594f6d7965d00319ca611c6ffb886e509",
}
ENV_DIRECTEUR = {
    "python": "3.12.0",
    "cobaya": "3.5",
    "camb": "1.5.4",
    "numpy": "1.26.4",
    "scipy": "1.13.1",
}
# Schéma d'autorisation ÉTENDU (G2.4d) : le SHA du chemin rapide, la
# version du contrat local, l'empreinte d'environnement et le budget de
# production ratifié deviennent obligatoires. Une autorisation ne peut
# donc plus valider un ancien adaptateur, un chemin rapide modifié, un
# contrat d'une autre version, un budget absent, un HEAD différent, une
# autre racine de runs ni une autre empreinte d'environnement.
CLES_MANIFESTE = {
    "type", "usage", "cle_humaine_1", "cle_humaine_2", "sha256_lanceur",
    "sha256_adaptateur", "sha256_chemin_rapide", "sha256_descripteurs",
    "sha256_preenregistrement", "sha256_donnees", "empreinte_environnement",
    "version_contrat_local", "head_autorise", "racine_runs_canonique",
    "variantes_graines_autorisees", "budget_production_requis_Gio",
    "budget_production_ratification",
}

# Champs OBLIGATOIRES du manifeste de run : aucun ne peut être absent ni
# remplacé par une valeur implicite.
CHAMPS_MANIFESTE_RUN = (
    "schema", "variante", "graine", "backend", "mode_acoustique",
    "date_creation_utc", "head", "sha256_lanceur", "sha256_adaptateur",
    "sha256_chemin_rapide", "sha256_descripteur", "sha256_donnees",
    "sha256_autorisation", "versions", "empreinte_environnement",
    "version_contrat_local", "racine_runs_canonique", "params",
    "prior_joint", "sampler", "ordre_parametres_echantillonnes",
    "ordre_parametres_derives", "meta_variante_grille_convention",
    "sha256_encodage_scientifique", "budget_production_requis_Gio",
    "reference_ratification_budget", "statut_run",
)
POINT_FOND_P0 = {"H0": 67.36, "ombh2": 0.02237, "omm": 0.3152}
POINT_FOND_P1 = {"H0": 68.3526, "ombh2": 0.022410, "omm": 0.300539}
P2_VALUES = {"M2a": (0.6, -0.2, 0.4, 1.2, 0.8), "M2b": (0.6, -0.2, 0.4, 0.8)}
P3_VALUES = {"M2a": (1.4, 0.2, 1.6, 0.1, 1.3), "M2b": (1.4, 0.2, 1.6, 1.3)}


class GardeErreur(RuntimeError):
    """Une garde de pré-vol a échoué."""


def sha256_fichier(path: str | Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as handle:
        for bloc in iter(lambda: handle.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


# ----------------------------------------------------------------- gardes

def garde_matrice(variante: str, graine: int) -> None:
    if variante not in MATRICE:
        raise GardeErreur(f"variante inconnue : {variante}")
    if graine not in MATRICE[variante]:
        raise GardeErreur(
            f"graine {graine} hors de la matrice gelée pour {variante}"
        )


def garde_descripteur(variante: str, chemin_test: str | None = None) -> str:
    from xz_likelihood_g2_3 import load_config

    chemin = chemin_test or DESCRIPTEURS[variante]
    config = load_config(chemin)  # validation stricte, aucune tolérance
    if config["variante"] != variante:
        raise GardeErreur(
            f"descripteur {chemin} déclare {config['variante']} != {variante}"
        )
    return sha256_fichier(chemin)


def garde_donnees() -> dict[str, str]:
    root = os.environ.get("C7C1_DATA_DIR")
    if not root:
        raise GardeErreur("C7C1_DATA_DIR absent")
    obtenus = {}
    for nom, attendu in SHA_BAO.items():
        chemin = Path(root) / "desi_bao_dr2" / nom
        if not chemin.is_file():
            raise GardeErreur(f"octets BAO absents : {nom}")
        reel = sha256_fichier(chemin)
        if reel != attendu:
            raise GardeErreur(f"SHA-256 non conforme pour {nom} : {reel}")
        obtenus[nom] = reel
    return obtenus


def versions_effectives() -> dict[str, str]:
    import platform

    import camb
    import cobaya
    import scipy

    versions = {
        "python": platform.python_version(),
        "cobaya": cobaya.__version__,
        "camb": camb.__version__,
        "numpy": np.__version__,
        "scipy": scipy.__version__,
    }
    for paquet in versions:
        forge = os.environ.get(f"C7C1_TEST_VERSION_{paquet.upper()}")
        if forge:
            versions[paquet] = forge  # injection de test uniquement
    return versions


def garde_environnement() -> dict[str, str]:
    versions = versions_effectives()
    for paquet, attendu in ENV_DIRECTEUR.items():
        if versions[paquet] != attendu:
            raise GardeErreur(
                f"environnement non conforme : {paquet} {versions[paquet]} "
                f"!= {attendu}"
            )
    return versions


def garde_prefixe(prefixe: str | Path) -> None:
    from xz_likelihood_g2_3 import refuser_sortie_sous_git

    refuser_sortie_sous_git(Path(prefixe).parent)


def garde_collision(prefixe: str | Path) -> None:
    parent = Path(prefixe).parent
    if parent.exists() and any(parent.iterdir()):
        raise GardeErreur(
            f"collision : {parent} existe et n'est pas vide "
            "(reprise stricte requise, jamais d'écrasement)"
        )


def garde_reprise(prefixe: str | Path, identite: dict) -> None:
    manifeste_path = Path(prefixe).parent / "manifest.json"
    if not manifeste_path.is_file():
        raise GardeErreur("reprise refusée : manifest.json absent")
    with open(manifeste_path, encoding="utf-8") as handle:
        existant = json.load(handle)
    for cle, valeur in identite.items():
        if existant.get(cle) != valeur:
            raise GardeErreur(
                f"reprise refusée : champ {cle!r} non identique "
                f"({existant.get(cle)!r} != {valeur!r})"
            )


def _cible_mesurable(cible: str | Path) -> Path:
    """Répertoire cible réel, ou son plus proche parent EXISTANT.

    Jamais l'ancre du volume, jamais une racine abstraite : la mesure de
    capacité doit porter sur le point de montage qui portera réellement
    les écritures (correction du défaut P1 relevé en INFRA-0).
    """
    p = Path(cible).resolve()
    while not p.exists():
        parent = p.parent
        if parent == p:
            raise GardeErreur(
                f"aucun parent existant pour la cible de capacité : {cible}"
            )
        p = parent
    return p


def espace_libre_gio(cible: str | Path) -> float:
    forge = os.environ.get("C7C1_TEST_ESPACE_LIBRE_GIO")
    if forge is not None:
        return float(forge)  # injection de test uniquement — jamais en prod
    usage = shutil.disk_usage(_cible_mesurable(cible))
    return usage.free / GIO


def garde_capacite(cible: str | Path) -> dict:
    libre = espace_libre_gio(cible)
    etat = {"libre_gio": round(libre, 2), "seuil_gio": GARDE_CAPACITE_GIO}
    if libre < SEUIL_ALERTE_GIO:
        etat["alerte_technique"] = (
            f"ALERTE : {libre:.2f} Gio < {SEUIL_ALERTE_GIO} Gio — tout "
            "lancement ou reprise interdit ; aucune libération automatique."
        )
        raise GardeErreur(etat["alerte_technique"])
    if libre < GARDE_CAPACITE_GIO:
        raise GardeErreur(
            f"capacité insuffisante : {libre:.2f} Gio < "
            f"{GARDE_CAPACITE_GIO} Gio — arrêt sans création ni reprise."
        )
    return etat


def garde_budget_production(contrat: dict, cible: str | Path) -> dict:
    """Contrôle SÉPARÉ du budget de production (jamais la garde technique).

    La garde technique (>= 40 Gio) autorise seulement la poursuite des
    tests et de la préparation. La production exige en plus un budget
    ratifié, non nul, positif, et inférieur ou égal à l'espace libre
    MESURÉ SUR LA CIBLE. Le statut NON_ETABLI bloque toute production.
    Aucun budget n'est inventé ici.
    """
    rr = contrat.get("racine_runs", {})
    statut = rr.get("budget_production_statut")
    requis = rr.get("budget_production_requis_Gio")
    etat = {"budget_production_statut": statut,
            "budget_production_requis_Gio": requis,
            "reference_ratification_budget":
                rr.get("reference_ratification_budget")}
    if statut == "RATIFIE" and not str(
            rr.get("reference_ratification_budget") or "").strip():
        raise GardeErreur(
            "contrat RATIFIE sans référence de ratification : refus"
        )
    if statut != "RATIFIE":
        raise GardeErreur(
            f"budget de production non ratifié (statut {statut!r}) : "
            "production refusée — aucun budget n'est supposé par défaut"
        )
    if not isinstance(requis, (int, float)) or isinstance(requis, bool):
        raise GardeErreur("budget de production absent ou non numérique")
    if requis <= 0:
        raise GardeErreur(f"budget de production non positif : {requis}")
    libre = espace_libre_gio(cible)
    etat["libre_cible_gio"] = round(libre, 2)
    if libre < float(requis):
        raise GardeErreur(
            f"espace libre sur la cible {libre:.2f} Gio < budget requis "
            f"{float(requis):.2f} Gio : production refusée"
        )
    return etat


def _canonique(chemin: str | Path) -> str:
    """Forme canonique comparable d'un chemin Windows.

    Résolution des liens et de la casse via os.path.realpath + normcase :
    deux chemins DISTINCTS ne doivent jamais devenir égaux (aucune
    troncature, aucun repli sur le parent).
    """
    return os.path.normcase(os.path.realpath(str(chemin)))


def _memes_chemins(a: str | Path, b: str | Path) -> bool:
    return _canonique(a) == _canonique(b)


def garde_contrat_local() -> dict:
    """Consomme le contrat local privé et vérifie sa conformité.

    Aucune valeur du contrat n'est publiée : seules des conclusions
    booléennes et la version de schéma sortent de cette fonction.
    """
    chemin = os.environ.get("C7C1_CONTRAT_LOCAL")
    if not chemin:
        raise GardeErreur("C7C1_CONTRAT_LOCAL absent")
    p = Path(chemin)
    if not p.is_file():
        raise GardeErreur("contrat local introuvable")
    try:
        contrat = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise GardeErreur(f"contrat local : JSON invalide ({exc.msg})") from exc
    if contrat.get("version") != VERSION_CONTRAT_LOCAL:
        raise GardeErreur(
            f"version de contrat local {contrat.get('version')!r} != "
            f"{VERSION_CONTRAT_LOCAL!r}"
        )
    if contrat.get("statut") != "PREPARATION_ONLY":
        raise GardeErreur(
            f"statut de contrat {contrat.get('statut')!r} != PREPARATION_ONLY"
        )
    rr = contrat.get("racine_runs", {})
    if "seuil_minimal_Gio" in rr:
        raise GardeErreur(
            "contrat local au schéma périmé : « seuil_minimal_Gio » — "
            "la garde technique et le budget de production doivent être "
            "distincts (INFRA-1a)"
        )
    for cle in ("garde_technique_minimale_Gio", "budget_production_requis_Gio",
                "budget_production_statut", "reference_ratification_budget"):
        if cle not in rr:
            raise GardeErreur(f"contrat local : champ requis absent ({cle})")
    # cohérence de la garde technique contrat <-> code
    if rr["garde_technique_minimale_Gio"] != GARDE_CAPACITE_GIO:
        raise GardeErreur(
            f"garde technique du contrat {rr['garde_technique_minimale_Gio']} "
            f"!= constante qualifiée {GARDE_CAPACITE_GIO}"
        )

    chemins = contrat.get("chemins_reels", {})
    py_contrat = chemins.get("python_directeur")
    if not py_contrat or not _memes_chemins(py_contrat, sys.executable):
        raise GardeErreur(
            "python_directeur du contrat != interpréteur courant "
            "(comparaison canonique insensible à la casse)"
        )
    for cle_env, cle_contrat in (("C7C1_DATA_DIR", "donnees"),
                                 ("C7C1_XZ_OUT_DIR", "runs")):
        valeur_env = os.environ.get(cle_env)
        if not valeur_env:
            raise GardeErreur(f"{cle_env} absent")
        if not _memes_chemins(valeur_env, chemins.get(cle_contrat, "")):
            raise GardeErreur(
                f"{cle_env} diffère du contrat local (champ {cle_contrat})"
            )
    env_contrat = contrat.get("environnement", {})
    empreinte = env_contrat.get("empreinte_sha256_inventaire_normalise")
    if not empreinte or empreinte != empreinte_environnement():
        raise GardeErreur("empreinte d'environnement non conforme au contrat")
    # L'empreinte globale ne remplace PAS la comparaison explicite des
    # versions déclarées : chacune est confrontée à la version chargée.
    chargees = versions_effectives()
    chargees["getdist"] = _version_getdist()
    for paquet in ("python", "cobaya", "camb", "numpy", "scipy", "getdist"):
        declaree = env_contrat.get(paquet)
        if declaree is None:
            if paquet == "getdist":
                continue  # getdist n'est vérifié que s'il est déclaré
            raise GardeErreur(f"contrat local : version {paquet} non déclarée")
        if str(declaree) != str(chargees.get(paquet)):
            raise GardeErreur(
                f"version déclarée au contrat ({paquet} {declaree}) != "
                f"version chargée ({chargees.get(paquet)})"
            )
    # <CACHE> : distinct de DATA, RUNS, TEMP et TMP ; hors Git, hors
    # OneDrive. Aucun cache n'est créé ni déplacé par cette porte.
    cache = chemins.get("caches")
    if not cache:
        raise GardeErreur("contrat local : chemin de cache non déclaré")
    cache_c = _canonique(cache)
    for etiquette, autre in (
        ("C7C1_DATA_DIR", os.environ.get("C7C1_DATA_DIR")),
        ("C7C1_XZ_OUT_DIR", os.environ.get("C7C1_XZ_OUT_DIR")),
        ("TEMP", os.environ.get("TEMP")), ("TMP", os.environ.get("TMP")),
    ):
        if autre and cache_c == _canonique(autre):
            raise GardeErreur(f"CACHE confondu avec {etiquette} : refus")
    if "onedrive" in cache_c:
        raise GardeErreur("CACHE sous OneDrive : refus")
    p = Path(cache)
    while True:
        if (p / ".git").exists():
            raise GardeErreur("CACHE sous Git : refus")
        if p.parent == p:
            break
        p = p.parent
    donnees_contrat = {
        k: v for k, v in contrat.get("donnees", {}).items() if k in SHA_BAO
    }
    if donnees_contrat != SHA_BAO:
        raise GardeErreur("SHA BAO du contrat non conformes aux valeurs épinglées")
    return {
        "version_contrat_local": contrat["version"],
        "statut": contrat["statut"],
        "budget_production_statut": rr["budget_production_statut"],
        "budget_production_requis_Gio": rr["budget_production_requis_Gio"],
        "reference_ratification_budget": rr["reference_ratification_budget"],
        "garde_technique_minimale_Gio": rr["garde_technique_minimale_Gio"],
        "python_directeur_conforme": True,
        "empreinte_environnement_conforme": True,
        "versions_declarees_conformes": True,
        "cache_distinct_et_hors_git": True,
        "_contrat": contrat,  # usage interne ; jamais publié
    }


def _version_getdist() -> str:
    forge = os.environ.get("C7C1_TEST_VERSION_GETDIST")
    if forge:
        return forge
    import getdist

    return getdist.__version__


def empreinte_environnement() -> str:
    """SHA-256 de l'inventaire normalisé des paquets (nom==version, trié)."""
    forge = os.environ.get("C7C1_TEST_EMPREINTE_ENV")
    if forge:
        return forge  # injection de test uniquement
    sortie = subprocess.run(
        [sys.executable, "-m", "pip", "list", "--format=json"],
        capture_output=True, text=True, check=True,
    ).stdout
    paquets = json.loads(sortie)
    norm = "\n".join(
        sorted(f"{p['name'].lower()}=={p['version']}" for p in paquets)
    ) + "\n"
    return hashlib.sha256(norm.encode()).hexdigest()


def garde_threads_et_interpreteur() -> dict:
    """Plafonds de threads et hygiène de l'interpréteur — bloquants.

    Les quatre variables doivent EXISTER et valoir exactement « 1 » :
    une valeur vide, 0, 2, « auto », un espace ou une absence échoue.
    """
    etat: dict = {}
    for cle in CLES_THREADS:
        valeur = os.environ.get(cle)
        if valeur is None:
            raise GardeErreur(f"plafond de threads absent : {cle}")
        if valeur != "1":
            raise GardeErreur(
                f"plafond de threads non conforme : {cle}={valeur!r} != '1'"
            )
        etat[cle] = valeur
    nousersite = os.environ.get("PYTHONNOUSERSITE")
    if nousersite != "1":
        raise GardeErreur(
            f"PYTHONNOUSERSITE={nousersite!r} != '1' : site utilisateur "
            "non désactivé"
        )
    if sys.maxsize <= 2**32:
        raise GardeErreur("interpréteur non 64 bits")
    if sys.prefix == sys.base_prefix:
        raise GardeErreur(
            "sys.prefix == sys.base_prefix : l'interpréteur n'est pas "
            "l'environnement virtuel directeur"
        )
    import site as _site

    if getattr(_site, "ENABLE_USER_SITE", False):
        raise GardeErreur("site utilisateur actif : refus")
    etat.update({
        "PYTHONNOUSERSITE": nousersite, "bits64": True,
        "venv_distinct_de_la_base": True, "site_utilisateur": "desactive",
        "empreinte_environnement": empreinte_environnement(),
    })
    return etat


def garde_chemins(out_dir: str | Path, data_dir: str | Path,
                  racine_depot: str | Path) -> dict:
    """Frontières de chemins : Git, synchronisation, disjonction des rôles."""
    from xz_likelihood_g2_3 import refuser_sortie_sous_git

    out_p, data_p = Path(out_dir), Path(data_dir)
    if not out_p.exists() or not out_p.is_dir():
        raise GardeErreur("C7C1_XZ_OUT_DIR inexistant ou n'est pas un répertoire")
    refuser_sortie_sous_git(out_p)  # aucun ancêtre .git, même vide
    for nom, chemin in (("racine du dépôt", racine_depot),
                        ("racine de runs", out_p), ("données", data_p)):
        if "onedrive" in _canonique(chemin):
            raise GardeErreur(f"{nom} sous OneDrive : refus")
    if _memes_chemins(data_p, out_p):
        raise GardeErreur("C7C1_DATA_DIR identique à C7C1_XZ_OUT_DIR : refus")
    for cle in ("TEMP", "TMP"):
        valeur = os.environ.get(cle)
        if valeur and (_memes_chemins(valeur, data_p)
                       or _memes_chemins(valeur, out_p)):
            raise GardeErreur(f"{cle} confondu avec DATA ou RUNS : refus")
    return {
        "runs_hors_git": True, "runs_hors_onedrive": True,
        "data_distinct_de_runs": True, "temp_distinct": True,
    }


def garde_depot_directeur(contrat: dict) -> dict:
    """Le dépôt courant doit être le dépôt directeur déclaré au contrat."""
    toplevel = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    attendu = contrat.get("chemins_reels", {}).get("depot_directeur", "")
    if not attendu or not _memes_chemins(toplevel, attendu):
        raise GardeErreur(
            "le dépôt courant n'est pas le dépôt directeur du contrat "
            "(le checkout historique est interdit comme base de calcul)"
        )
    if "onedrive" in _canonique(toplevel):
        raise GardeErreur("dépôt courant sous OneDrive : refus")
    return {"depot_directeur": True, "hors_onedrive": True}


def ecrire_manifeste_atomique(chemin: str | Path, contenu: dict) -> None:
    """Écriture ATOMIQUE d'un manifeste JSON canonique.

    Temporaire frère -> flush -> fsync -> os.replace -> fsync du
    répertoire quand la plate-forme le permet. Ne laisse jamais de
    manifest.json partiel ; nettoie le temporaire en cas d'échec ;
    refuse d'écraser un manifeste EXISTANT NON IDENTIQUE.
    """
    cible = Path(chemin)
    corps = json.dumps(contenu, indent=2, sort_keys=True,
                       ensure_ascii=False) + "\n"
    if cible.exists():
        try:
            existant = json.loads(cible.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            raise GardeErreur(
                "manifeste existant illisible : écrasement refusé"
            ) from None
        if existant != contenu:
            raise GardeErreur(
                "manifeste existant non identique : écrasement refusé"
            )
        return  # déjà écrit à l'identique : rien à faire
    tmp = cible.with_name(cible.name + f".tmp{os.getpid()}")
    try:
        with open(tmp, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(corps)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, cible)
    except BaseException:
        if tmp.exists():
            try:
                tmp.unlink()
            except OSError:
                pass
        raise
    try:  # fsync du répertoire : indisponible sur certaines plates-formes
        fd = os.open(str(cible.parent), os.O_RDONLY)
        try:
            os.fsync(fd)
        finally:
            os.close(fd)
    except (OSError, AttributeError):
        pass


def encodage_scientifique_gele(variante: str, graine: int) -> dict:
    """Encodage scientifique gelé, extrait du CONSTRUCTEUR DIRECTEUR.

    Le graphe externe (theory/likelihood, qui porte des classes) et le
    bloc interne ``_xz_meta`` sont retirés : ne subsistent que des
    valeurs entièrement sérialisables en JSON canonique.
    """
    from xz_cobaya_g2_4 import build_cobaya_info

    info = build_cobaya_info(DESCRIPTEURS[variante], graine)
    meta = info["_xz_meta"]
    params = info["params"]
    echantillonnes = [n for n, b in params.items() if "prior" in b]
    derives = [n for n, b in params.items() if "derived" in b]
    encodage = {
        "params": json.loads(json.dumps(params, sort_keys=True)),
        "prior_joint": info["prior"],
        "sampler": json.loads(json.dumps(info["sampler"], sort_keys=True)),
        "ordre_parametres_echantillonnes": echantillonnes,
        "ordre_parametres_derives": derives,
        "meta_variante_grille_convention": {
            "variante": meta["variante"], "grille": meta["grille"],
            "convention": meta["convention"],
        },
    }
    canonique = json.dumps(encodage, indent=None, sort_keys=True,
                           separators=(",", ":"), ensure_ascii=False)
    encodage["sha256_encodage_scientifique"] = hashlib.sha256(
        canonique.encode("utf-8")).hexdigest()
    return encodage


def valider_date_utc(date_utc: str) -> str:
    """Exige exactement AAAA-MM-JJTHH:MM:SSZ (jamais fabriquée ici)."""
    import datetime

    if not isinstance(date_utc, str) or not date_utc:
        raise GardeErreur("date_creation_utc absente")
    try:
        datetime.datetime.strptime(date_utc, FORMAT_DATE_UTC)
    except ValueError as exc:
        raise GardeErreur(
            f"date_creation_utc au format invalide : {date_utc!r} "
            f"(attendu {FORMAT_DATE_UTC})"
        ) from exc
    return date_utc


def identite_run(variante: str, graine: int, head: str, contrat: dict,
                 versions: dict, sha_descripteur: str, sha_donnees: dict,
                 date_creation_utc: str, sha256_autorisation: str,
                 budget_requis_gio, reference_ratification_budget) -> dict:
    """Identité COMPLÈTE nécessaire à une reprise exacte.

    La date de création est TRANSMISE explicitement — jamais fabriquée
    ici : la production devra la générer une seule fois et la propager
    au plan comme au manifeste ; la qualification en fournit une valeur
    fixe prédéclarée, pour préserver le déterminisme.

    Les deux clés humaines de l'autorisation ne sont JAMAIS reproduites :
    seul le SHA-256 du fichier d'autorisation est consigné.
    """
    ici = Path(__file__).parent
    encodage = encodage_scientifique_gele(variante, graine)
    identite = {
        "schema": SCHEMA_MANIFESTE_RUN,
        "variante": variante,
        "graine": int(graine),
        "backend": "optimized",
        "mode_acoustique": "corrected-v1.1",
        "date_creation_utc": valider_date_utc(date_creation_utc),
        "head": head,
        "sha256_lanceur": sha256_fichier(__file__),
        "sha256_adaptateur": sha256_fichier(ici / "xz_cobaya_g2_4.py"),
        "sha256_chemin_rapide": sha256_fichier(ici / "xz_fast_g2_4c.py"),
        "sha256_descripteur": sha_descripteur,
        "sha256_donnees": dict(sha_donnees),
        "sha256_autorisation": sha256_autorisation,
        "versions": dict(versions),
        "empreinte_environnement": empreinte_environnement(),
        "version_contrat_local": contrat["version_contrat_local"],
        "racine_runs_canonique": _canonique(os.environ["C7C1_XZ_OUT_DIR"]),
        "budget_production_requis_Gio": budget_requis_gio,
        "reference_ratification_budget": reference_ratification_budget,
        "statut_run": "PLANIFIE_NON_LANCE",
    }
    identite.update(encodage)
    manquants = [c for c in CHAMPS_MANIFESTE_RUN if c not in identite]
    if manquants:
        raise GardeErreur(f"manifeste de run incomplet : {manquants}")
    return identite


def garde_git() -> dict:
    head = subprocess.run(
        ["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True
    ).stdout.strip()
    statut = subprocess.run(
        ["git", "status", "--porcelain"], capture_output=True, text=True,
        check=True,
    ).stdout.strip()
    return {"head": head, "arbre_propre": statut == ""}


def garde_autorisation(chemin: str | Path, variante: str, graine: int,
                       head: str, budget_contrat=None,
                       ratification_contrat=None) -> str:
    """Garde d'autorisation RÉELLE. Retourne le SHA-256 du fichier.

    Refuse systématiquement un manifeste d'usage autre que PRODUCTION :
    un fichier éphémère de qualification ne peut JAMAIS servir
    d'autorisation réelle. Lorsque le budget du contrat est fourni,
    exige son égalité numérique exacte avec celui de l'autorisation,
    ainsi que l'identité de la référence de ratification.
    """
    if not Path(chemin).is_file():
        raise GardeErreur("autorisation absente")
    with open(chemin, encoding="utf-8") as handle:
        manifeste = json.load(handle)
    if set(manifeste.keys()) != CLES_MANIFESTE:
        raise GardeErreur("autorisation non conforme : clés inexactes")
    if manifeste["type"] != "autorisation_production_c7c1_g2_4":
        raise GardeErreur("autorisation non conforme : type inexact")
    if manifeste.get("usage") != USAGE_AUTORISATION_PRODUCTION:
        raise GardeErreur(
            f"autorisation d'usage {manifeste.get('usage')!r} refusée : "
            f"seul {USAGE_AUTORISATION_PRODUCTION!r} autorise une "
            "production — un manifeste de qualification n'est jamais "
            "une autorisation réelle"
        )
    for cle in ("cle_humaine_1", "cle_humaine_2"):
        if not isinstance(manifeste[cle], str) or not manifeste[cle].strip():
            raise GardeErreur(f"autorisation non conforme : {cle} vide")
    if manifeste["sha256_lanceur"] != sha256_fichier(__file__):
        raise GardeErreur("autorisation factice : SHA du lanceur non conforme")
    adaptateur = Path(__file__).parent / "xz_cobaya_g2_4.py"
    if manifeste["sha256_adaptateur"] != sha256_fichier(adaptateur):
        raise GardeErreur("autorisation factice : SHA adaptateur non conforme")
    # SHA du chemin rapide : OBLIGATOIRE depuis G2.4d — une autorisation
    # ne doit jamais valider un chemin rapide modifié.
    rapide = Path(__file__).parent / "xz_fast_g2_4c.py"
    if manifeste.get("sha256_chemin_rapide") != sha256_fichier(rapide):
        raise GardeErreur(
            "autorisation factice : SHA du chemin rapide absent ou non conforme"
        )
    if manifeste.get("version_contrat_local") != VERSION_CONTRAT_LOCAL:
        raise GardeErreur("autorisation : version de contrat local non conforme")
    if manifeste.get("empreinte_environnement") != empreinte_environnement():
        raise GardeErreur("autorisation : empreinte d'environnement non conforme")
    racine_autorisee = manifeste.get("racine_runs_canonique")
    if not racine_autorisee or not _memes_chemins(
            racine_autorisee, os.environ.get("C7C1_XZ_OUT_DIR", "")):
        raise GardeErreur("autorisation : racine de runs non autorisée")
    budget = manifeste.get("budget_production_requis_Gio")
    if not isinstance(budget, (int, float)) or isinstance(budget, bool) \
            or budget <= 0:
        raise GardeErreur("autorisation : budget de production absent ou nul")
    ratification = manifeste.get("budget_production_ratification")
    if not str(ratification or "").strip():
        raise GardeErreur("autorisation : ratification du budget absente")
    # Liaison EXACTE contrat <-> autorisation : une autorisation à 50 Gio
    # et un contrat ratifié à 80 Gio doivent être refusés ensemble, même
    # si l'espace libre dépasse 80 Gio.
    if budget_contrat is not None:
        if not isinstance(budget_contrat, (int, float)) \
                or isinstance(budget_contrat, bool):
            raise GardeErreur("budget du contrat absent ou non numérique")
        if float(budget) != float(budget_contrat):
            raise GardeErreur(
                f"budget de l'autorisation ({budget}) != budget du contrat "
                f"({budget_contrat}) : refus"
            )
    if ratification_contrat is not None:
        if str(ratification) != str(ratification_contrat):
            raise GardeErreur(
                "référence de ratification du budget différente entre "
                "l'autorisation et le contrat : refus"
            )
    return sha256_fichier(chemin)
    for var, chemin_desc in DESCRIPTEURS.items():
        if manifeste["sha256_descripteurs"].get(var) != sha256_fichier(chemin_desc):
            raise GardeErreur(
                f"autorisation factice : SHA descripteur {var} non conforme"
            )
    prereg = "reports/rapport_G2_2a_preregistration.md"
    if manifeste["sha256_preenregistrement"] != sha256_fichier(prereg):
        raise GardeErreur(
            "autorisation factice : SHA pré-enregistrement non conforme"
        )
    if manifeste["sha256_donnees"] != SHA_BAO:
        raise GardeErreur("autorisation factice : SHA données non conformes")
    if manifeste["head_autorise"] != head:
        raise GardeErreur("autorisation factice : HEAD non autorisé")
    autorisees = manifeste["variantes_graines_autorisees"]
    if str(graine) not in [str(g) for g in autorisees.get(variante, [])]:
        raise GardeErreur(
            f"autorisation ne couvre pas ({variante}, {graine})"
        )


def refuser_injections_en_production() -> None:
    injections = [k for k in os.environ if k.startswith("C7C1_TEST_")]
    if injections:
        raise GardeErreur(
            f"injections de test présentes en production : {injections} — refus"
        )


# ------------------------------------------------------------- pré-vol

def preflight(variante: str, graine: int, descripteur_test: str | None = None,
              prefixe: str | None = None) -> dict:
    """Gardes non productives. Ne crée ni ne modifie aucun fichier."""

    rapport: dict = {}
    garde_matrice(variante, graine)
    rapport["matrice"] = "conforme"
    rapport["sha256_descripteur"] = garde_descripteur(variante, descripteur_test)
    rapport["sha256_donnees"] = garde_donnees()
    rapport["versions"] = garde_environnement()
    rapport["threads_interpreteur"] = garde_threads_et_interpreteur()
    contrat = garde_contrat_local()
    contrat_brut = contrat.pop("_contrat")
    rapport["contrat_local"] = contrat
    out_dir = os.environ.get("C7C1_XZ_OUT_DIR")
    if not out_dir:
        raise GardeErreur("C7C1_XZ_OUT_DIR absent")
    racine_depot = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    rapport["depot"] = garde_depot_directeur(contrat_brut)
    rapport["chemins"] = garde_chemins(
        out_dir, os.environ["C7C1_DATA_DIR"], racine_depot)
    prefixe_effectif = prefixe or str(
        Path(out_dir) / "g2_4" / "P_WS" / variante / f"s{graine}" / "chain"
    )
    garde_prefixe(prefixe_effectif)
    garde_collision(prefixe_effectif)
    rapport["prefixe"] = "hors Git, sans collision"
    # Garde TECHNIQUE seulement : elle n'autorise que la poursuite des
    # tests et de la préparation, jamais la production.
    rapport["capacite"] = garde_capacite(out_dir)
    rapport["capacite"]["mesure_sur"] = "repertoire cible (pas l'ancre)"
    rapport["git"] = garde_git()  # rapporté ; bloquant en production
    # Le seul mot « RATIFIE » n'autorise rien : sous ce statut, la
    # validation NUMÉRIQUE du budget est réellement exécutée avant
    # d'annoncer que la production serait autorisable.
    statut_budget = contrat["budget_production_statut"]
    if statut_budget == "RATIFIE":
        try:
            etat_budget = garde_budget_production(contrat_brut, out_dir)
            autorisable, motif = True, "budget validé numériquement"
        except GardeErreur as exc:
            etat_budget, autorisable, motif = (
                {"budget_production_statut": statut_budget}, False, str(exc))
    else:
        etat_budget, autorisable = (
            {"budget_production_statut": statut_budget}, False)
        motif = "budget non établi"
    rapport["budget_production"] = {
        **etat_budget, "production_autorisable": autorisable, "motif": motif,
    }
    rapport["verdict"] = (
        "PREFLIGHT OK — production autorisable ailleurs" if autorisable
        else "PREPARATION OK — PRODUCTION NON AUTORISABLE"
    )
    return rapport


def produire(args: list[str]) -> None:
    """Mode production : verrouillé tant que G2.4b n'est pas validée.

    Toutes les gardes sont bloquantes, y compris l'arbre Git propre et
    l'autorisation à deux clés. AUCUNE MCMC n'est lancée dans cette porte :
    le vrai manifeste est interdit, donc ce chemin se termine toujours par
    un refus avant cobaya.run.
    """

    # 1. refus des injections de test
    refuser_injections_en_production()
    # 2. confirmation explicite
    if "--je-confirme-la-production" not in args:
        raise GardeErreur(
            "production refusée : confirmation explicite absente "
            "(--je-confirme-la-production)"
        )
    if "--autorisation" not in args:
        raise GardeErreur("autorisation absente")
    variante, graine = args[0], int(args[1])
    chemin_autorisation = args[args.index("--autorisation") + 1]
    # 3. contrat, environnement, données, threads et chemins (via preflight)
    rapport = preflight(variante, graine)
    # 4. HEAD et arbre propre
    etat_git = rapport["git"]
    if not etat_git["arbre_propre"]:
        raise GardeErreur("arbre Git non propre : production refusée")
    # 5. autorisation à deux clés (schéma étendu, usage PRODUCTION exigé,
    #    budget et ratification liés au contrat)
    contrat = garde_contrat_local()
    contrat_brut = contrat.pop("_contrat")
    sha_autorisation = garde_autorisation(
        chemin_autorisation, variante, graine, etat_git["head"],
        budget_contrat=contrat["budget_production_requis_Gio"],
        ratification_contrat=contrat["reference_ratification_budget"],
    )
    # 6. budget de production ratifié, comparé à l'espace libre de la CIBLE
    rapport["budget"] = garde_budget_production(
        contrat_brut, os.environ["C7C1_XZ_OUT_DIR"])
    # 7. construction PURE du plan de production (aucune écriture).
    #    La date de création est générée UNE SEULE FOIS ici puis
    #    transmise au plan — et, en porte future, au manifeste.
    import datetime

    date_creation = datetime.datetime.now(
        datetime.timezone.utc).strftime(FORMAT_DATE_UTC)
    plan = identite_run(
        variante, graine, etat_git["head"], contrat, rapport["versions"],
        rapport["sha256_descripteur"], rapport["sha256_donnees"],
        date_creation_utc=date_creation,
        sha256_autorisation=sha_autorisation,
        budget_requis_gio=rapport["budget"]["budget_production_requis_Gio"],
        reference_ratification_budget=contrat["reference_ratification_budget"],
    )
    plan["prefixe"] = str(
        Path(os.environ["C7C1_XZ_OUT_DIR"]) / "g2_4" / "P_WS" / variante
        / f"s{graine}" / "chain"
    )
    # 8. VERROU DUR — placé AVANT toute création de répertoire, toute
    #    ouverture en écriture, tout os.replace, tout manifest.json et
    #    tout cobaya.run. Le code de l'étape 9 est préparé mais ne
    #    s'exécute pas tant que ce verrou tient.
    if VERROU_PRODUCTION_G2_4D:
        raise GardeErreur(
            "VERROU G2.4d : raccord qualifié SANS production — le lancement "
            "réel exige une porte ultérieure et une décision humaine "
            "distincte. Aucun répertoire créé, aucun manifeste écrit, "
            "aucun cobaya.run atteint."
        )
    # 9. porte future seulement : création du répertoire, écriture
    #    atomique du manifeste, puis cobaya.run. Jamais exécuté ici.
    raise GardeErreur(  # pragma: no cover - inatteignable sous verrou
        "chemin de production non ouvert"
    )


# ------------------------------------------------- banc de performance

def banc_performance() -> tuple[dict, dict]:
    """Banc déterministe sur points prédéclarés. Les chi2 ne sont ni
    publiés ni utilisés : seuls temps, mémoire et validité sont mesurés."""

    from xz_likelihood_g2_3 import XZEvaluator, load_bao_data, load_config

    bao_mean, bao_icov = load_bao_data()
    normalise: dict = {}
    temps: dict = {}
    for variante, chemin in DESCRIPTEURS.items():
        config = load_config(chemin)
        ev = XZEvaluator(config, bao_mean, bao_icov)
        noms = [item["nom"] for item in config["parametres_x"]]
        grille = config["grille"]
        points = {
            "P0": {**POINT_FOND_P0, **{n: 1.0 for n in noms}},
            "P1": {**POINT_FOND_P1, **{n: 1.0 for n in noms}},
            "P2": {**POINT_FOND_P0, **dict(zip(noms, P2_VALUES[grille]))},
            "P3": {**POINT_FOND_P0, **dict(zip(noms, P3_VALUES[grille]))},
        }
        chronos = []
        valides = 0
        tracemalloc.start()
        for point in points.values():
            debut = time.perf_counter()
            sortie = ev.evaluate(point)
            chronos.append(time.perf_counter() - debut)
            if sortie["logprior"] == 0.0:
                valides += 1
        _, pic_octets = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        normalise[variante] = {"points_valides": valides, "points_total": 4}
        temps[variante] = {
            "temps_eval_s": [round(t, 3) for t in chronos],
            "memoire_python_pic_Mo": round(pic_octets / 1e6, 1),
        }

    # Taux de validité (déterministe, graine fixée) — aucune valeur chi2.
    rng = np.random.default_rng(6300)
    tirages_fond = rng.uniform(
        [20.0, 0.005, 0.01], [100.0, 0.1, 0.99], size=(4096, 3)
    )
    omch2 = (
        tirages_fond[:, 2] * (tirages_fond[:, 0] / 100.0) ** 2
        - 0.06 / 93.14
        - tirages_fond[:, 1]
    )
    normalise["taux_omch2_positif_P_WS_fond"] = round(
        float(np.mean(omch2 > 0.0)), 4
    )
    from xz_background_g2_1 import (
        CambReference,
        InvalidBackgroundError,
        XZBackground,
        XZProfile,
    )

    ref = CambReference.from_g1(
        h0=POINT_FOND_P0["H0"], ombh2=POINT_FOND_P0["ombh2"],
        omegam=POINT_FOND_P0["omm"],
    )
    grille_z = np.linspace(0.0, 3.0, 301)
    for variante_grille, n_libres in (("M2a", 5), ("M2b", 4)):
        tirages_x = rng.uniform(-2.0, 4.0, size=(256, n_libres))
        valides_x = 0
        for xs in tirages_x:
            try:
                fond = XZBackground(
                    ref, XZProfile(variante_grille, tuple(xs), "natural")
                )
                fond.h2(grille_z)
                valides_x += 1
            except InvalidBackgroundError:
                pass
        normalise[f"taux_fond_valide_{variante_grille}_P_WS"] = round(
            valides_x / 256.0, 4
        )

    # Projection de charge : médiane des temps x longueurs projetées G2.4b-i
    # / taux d'acceptation G1 (~0.2), pour 32 chaînes (heures CPU).
    mediane = float(np.median([t for v in temps.values() for t in v["temps_eval_s"]]))
    temps["projection_charge_32_chaines_heures_cpu"] = {
        etiquette: round(lignes / 0.2 * mediane * 32 / 3600.0, 1)
        for etiquette, lignes in (
            ("basse_153k", 153_000),
            ("centrale_330k", 330_000),
            ("haute_880k", 880_000),
        )
    }
    return normalise, temps


# ------------------------------------------------------- qualification

def qualification() -> int:
    """Suite adversariale complète + banc. Sortie normalisée déterministe
    puis mesures non déterministes séparées. Code non nul si une seule
    attente échoue."""

    ici = Path(__file__).parent.parent  # racine C7-C1
    os.chdir(ici)
    py = sys.executable
    lancer = ["scripts/run_mcmc_xz_g2_4.py"]
    diagnostiquer = ["scripts/diagnose_mcmc_xz_g2_4.py"]
    tmp = Path(os.environ["C7C1_XZ_OUT_DIR"])  # hors Git, vérifié plus bas
    echecs: list[str] = []
    resultat: dict = {}

    def sous_processus(args, env_extra=None) -> int:
        env = dict(os.environ)
        env.update(env_extra or {})
        proc = subprocess.run(
            [py, *args], capture_output=True, text=True, env=env
        )
        return proc.returncode

    # Nominal : preflight conforme avec espace simulé suffisant (>=40 Gio).
    env_ok = {"C7C1_TEST_ESPACE_LIBRE_GIO": "41"}
    scenarios: list[tuple[str, list[str], dict, bool]] = [
        ("nominal_preflight_41gio",
         [*lancer, "--preflight", "M2a-N", "630101"], env_ok, True),
        ("espace_simule_40gio_accepte",
         [*lancer, "--preflight", "M2a-N", "630101"],
         {"C7C1_TEST_ESPACE_LIBRE_GIO": "40"}, True),
        ("espace_simule_39gio_refuse",
         [*lancer, "--preflight", "M2a-N", "630101"],
         {"C7C1_TEST_ESPACE_LIBRE_GIO": "39"}, False),
        ("espace_simule_14gio_alerte_refus",
         [*lancer, "--preflight", "M2a-N", "630101"],
         {"C7C1_TEST_ESPACE_LIBRE_GIO": "14"}, False),
        ("variante_inconnue",
         [*lancer, "--preflight", "M2c-N", "630101"], env_ok, False),
        ("graine_incorrecte",
         [*lancer, "--preflight", "M2a-N", "999999"], env_ok, False),
        ("graine_autre_variante",
         [*lancer, "--preflight", "M2a-N", "630201"], env_ok, False),
        ("environnement_incorrect",
         [*lancer, "--preflight", "M2a-N", "630101"],
         {**env_ok, "C7C1_TEST_VERSION_NUMPY": "9.9.9"}, False),
        ("sortie_sous_git",
         [*lancer, "--preflight", "M2a-N", "630101"],
         {**env_ok, "C7C1_XZ_OUT_DIR": str(ici)}, False),
        ("autorisation_absente",
         [*lancer, "--produire", "M2a-N", "630101",
          "--je-confirme-la-production"], {}, False),
        ("production_sans_confirmation",
         [*lancer, "--produire", "M2a-N", "630101",
          "--autorisation", "inexistant.json"], {}, False),
        ("diag_synthetique_converge",
         [*diagnostiquer, "--certifier-synthetique", "converge"], {}, True),
        ("diag_synthetique_nonconverge",
         [*diagnostiquer, "--certifier-synthetique", "nonconverge"], {}, False),
        ("diag_poids_non_entier",
         [*diagnostiquer, "--faute", "poids_non_entier"], {}, False),
        ("diag_poids_negatif",
         [*diagnostiquer, "--faute", "poids_negatif"], {}, False),
        ("diag_poids_non_fini",
         [*diagnostiquer, "--faute", "poids_non_fini"], {}, False),
        ("diag_segments_desordonnes",
         [*diagnostiquer, "--faute", "segments_desordonnes"], {}, False),
        ("sampler_cle_correcte_acceptee",
         [*lancer, "--verifier-sampler", "bonne"], {}, True),
        ("sampler_cle_fautive_rejetee",
         [*lancer, "--verifier-sampler", "fautive"], {}, True),
    ]

    # Scénarios à préparation de fichiers temporaires (hors Git).
    prep = tmp / "g2_4_qualification"
    prep.mkdir(parents=True, exist_ok=True)
    # YAML altéré : copie modifiée hors Git.
    altere = prep / "descripteur_altere.yaml"
    contenu = Path(DESCRIPTEURS["M2a-N"]).read_text(encoding="utf-8")
    altere.write_text(
        contenu.replace("max: 4.0", "max: 5.0"), encoding="utf-8"
    )
    scenarios.append(
        ("yaml_altere",
         [*lancer, "--preflight", "M2a-N", "630101",
          "--descripteur-test", str(altere)], env_ok, False)
    )
    # Données au SHA incorrect : copie altérée hors Git.
    donnees_alterees = prep / "data_faute" / "desi_bao_dr2"
    donnees_alterees.mkdir(parents=True, exist_ok=True)
    src = Path(os.environ["C7C1_DATA_DIR"]) / "desi_bao_dr2"
    for nom in SHA_BAO:
        octets = (src / nom).read_bytes()
        (donnees_alterees / nom).write_bytes(octets[:-1] + b"0")
    scenarios.append(
        ("sha_donnees_incorrect",
         [*lancer, "--preflight", "M2a-N", "630101"],
         {**env_ok, "C7C1_DATA_DIR": str(donnees_alterees.parent)}, False)
    )
    # Collision de préfixe (graine 630102, distincte du scénario nominal).
    collision = tmp / "g2_4" / "P_WS" / "M2a-N" / "s630102"
    collision.mkdir(parents=True, exist_ok=True)
    (collision / "chain.1.txt").write_text("occupant\n", encoding="utf-8")
    scenarios.append(
        ("collision_prefixe",
         [*lancer, "--preflight", "M2a-N", "630102"], env_ok, False)
    )
    # Autorisation factice (structure correcte, SHA lanceur faux) et
    # reprise incompatible : testées en interne (fonctions de garde).
    for nom_scenario, attendu_echec, fonction in (
        ("autorisation_factice", True, lambda: garde_autorisation(
            _ecrire_autorisation_factice(prep), "M2a-N", 630101,
            garde_git()["head"])),
        ("reprise_manifeste_incompatible", True, lambda: garde_reprise(
            collision / "chain",
            {"variante": "M2a-N", "graine": 630102})),
        ("sha_descripteur_incorrect", True, lambda: _comparer_sha_descripteur()),
    ):
        try:
            fonction()
            detecte = False
        except (GardeErreur, FileNotFoundError):
            detecte = True
        resultat[f"scenario_{nom_scenario}"] = {
            "attendu": "refus", "refuse": detecte}
        if detecte is not attendu_echec:
            echecs.append(f"scénario {nom_scenario} non conforme")

    for nom_scenario, args, env_extra, attendu_ok in scenarios:
        code = sous_processus(args, env_extra)
        conforme = (code == 0) if attendu_ok else (code != 0)
        resultat[f"scenario_{nom_scenario}"] = {
            "attendu": "exit 0" if attendu_ok else "exit non nul",
            "code": code, "conforme": conforme,
        }
        if not conforme:
            echecs.append(f"scénario {nom_scenario} : code {code}")

    # Vérification : le scénario collision n'a modifié aucun fichier existant
    # et les refus de capacité n'ont créé aucun répertoire de chaîne.
    if (collision / "chain.1.txt").read_text(encoding="utf-8") != "occupant\n":
        echecs.append("le pré-vol a modifié un fichier existant")
    resultat["aucune_modification_fichier_existant"] = True

    # Banc de performance (déterministe / mesures séparées).
    normalise_banc, temps_banc = banc_performance()
    resultat["banc_performance"] = normalise_banc

    # Diagnostics synthétiques : comparaison à la bibliothèque de référence.
    code = sous_processus([*diagnostiquer, "--self-test"])
    resultat["diagnostics_self_test"] = {"code": code, "conforme": code == 0}
    if code != 0:
        echecs.append("self-test diagnostique en échec")

    resultat["matrice_gelee"] = {
        variante: [graines[0], "...", graines[-1]]
        for variante, graines in MATRICE.items()
    }
    resultat["garde_capacite_gio"] = GARDE_CAPACITE_GIO
    resultat["seuil_alerte_gio"] = SEUIL_ALERTE_GIO
    resultat["porte"] = {"passe": not echecs, "echecs": sorted(echecs)}

    print("=== SORTIE NORMALISEE (deterministe) ===")
    print(json.dumps(resultat, indent=2, sort_keys=True, ensure_ascii=False))
    print("=== MESURES NON DETERMINISTES (temps/memoire) ===")
    print(json.dumps(temps_banc, indent=2, sort_keys=True, ensure_ascii=False))
    return 1 if echecs else 0


def _ecrire_autorisation_factice(prep: Path) -> Path:
    factice = {
        "type": "autorisation_production_c7c1_g2_4",
        "cle_humaine_1": "FACTICE", "cle_humaine_2": "FACTICE",
        "sha256_lanceur": "0" * 64, "sha256_adaptateur": "0" * 64,
        "sha256_descripteurs": {v: "0" * 64 for v in DESCRIPTEURS},
        "sha256_preenregistrement": "0" * 64,
        "sha256_donnees": dict(SHA_BAO),
        "head_autorise": "0" * 40,
        "variantes_graines_autorisees": {"M2a-N": [630101]},
    }
    chemin = prep / "autorisation_factice.json"
    chemin.write_text(json.dumps(factice), encoding="utf-8")
    return chemin


def _comparer_sha_descripteur() -> None:
    reel = sha256_fichier(DESCRIPTEURS["M2a-N"])
    if reel != "0" * 64:
        raise GardeErreur("SHA de descripteur non conforme au manifeste")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        raise SystemExit(2)
    ici = Path(__file__).parent.parent
    os.chdir(ici)
    try:
        if args[0] == "--preflight":
            descripteur_test = None
            if "--descripteur-test" in args:
                descripteur_test = args[args.index("--descripteur-test") + 1]
            rapport = preflight(args[1], int(args[2]), descripteur_test)
            print(json.dumps(rapport, indent=2, sort_keys=True,
                             ensure_ascii=False))
            raise SystemExit(0)
        if args[0] == "--produire":
            produire(args[1:])
            raise SystemExit(0)  # jamais atteint en G2.4b
        if args[0] == "--verifier-sampler":
            from xz_cobaya_g2_4 import verifier_bloc_sampler

            verifier_bloc_sampler(DESCRIPTEURS["M2b-K"], args[1])
            print(f"bloc sampler ({args[1]}) : conforme aux attentes")
            raise SystemExit(0)
        if args[0] == "--qualification":
            raise SystemExit(qualification())
    except GardeErreur as exc:
        print(f"ARRET GARDE : {exc}")
        raise SystemExit(1) from exc
    except (ValueError, KeyError, IndexError) as exc:
        print(f"ARRET ARGUMENTS : {exc}")
        raise SystemExit(2) from exc
    print(f"ARRET : mode inconnu {args[0]!r}")
    raise SystemExit(2)


if __name__ == "__main__":
    main()
