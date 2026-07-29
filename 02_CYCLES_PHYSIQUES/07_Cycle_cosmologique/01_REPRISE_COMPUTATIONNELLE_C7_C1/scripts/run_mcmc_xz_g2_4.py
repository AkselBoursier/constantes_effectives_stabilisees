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
CLES_MANIFESTE = {
    "type", "cle_humaine_1", "cle_humaine_2", "sha256_lanceur",
    "sha256_adaptateur", "sha256_descripteurs", "sha256_preenregistrement",
    "sha256_donnees", "head_autorise", "variantes_graines_autorisees",
}
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


def espace_libre_gio(cible: str | Path) -> float:
    forge = os.environ.get("C7C1_TEST_ESPACE_LIBRE_GIO")
    if forge is not None:
        return float(forge)  # injection de test uniquement — jamais en prod
    usage = shutil.disk_usage(Path(cible).anchor or str(cible))
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
                       head: str) -> None:
    if not Path(chemin).is_file():
        raise GardeErreur("autorisation absente")
    with open(chemin, encoding="utf-8") as handle:
        manifeste = json.load(handle)
    if set(manifeste.keys()) != CLES_MANIFESTE:
        raise GardeErreur("autorisation non conforme : clés inexactes")
    if manifeste["type"] != "autorisation_production_c7c1_g2_4":
        raise GardeErreur("autorisation non conforme : type inexact")
    for cle in ("cle_humaine_1", "cle_humaine_2"):
        if not isinstance(manifeste[cle], str) or not manifeste[cle].strip():
            raise GardeErreur(f"autorisation non conforme : {cle} vide")
    if manifeste["sha256_lanceur"] != sha256_fichier(__file__):
        raise GardeErreur("autorisation factice : SHA du lanceur non conforme")
    adaptateur = Path(__file__).parent / "xz_cobaya_g2_4.py"
    if manifeste["sha256_adaptateur"] != sha256_fichier(adaptateur):
        raise GardeErreur("autorisation factice : SHA adaptateur non conforme")
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
    out_dir = os.environ.get("C7C1_XZ_OUT_DIR")
    if not out_dir:
        raise GardeErreur("C7C1_XZ_OUT_DIR absent")
    prefixe_effectif = prefixe or str(
        Path(out_dir) / "g2_4" / "P_WS" / variante / f"s{graine}" / "chain"
    )
    garde_prefixe(prefixe_effectif)
    garde_collision(prefixe_effectif)
    rapport["prefixe"] = "hors Git, sans collision"
    rapport["capacite"] = garde_capacite(out_dir)
    rapport["git"] = garde_git()  # rapporté ; bloquant en production
    rapport["verdict"] = "PREFLIGHT OK — aucune production effectuée"
    return rapport


def produire(args: list[str]) -> None:
    """Mode production : verrouillé tant que G2.4b n'est pas validée.

    Toutes les gardes sont bloquantes, y compris l'arbre Git propre et
    l'autorisation à deux clés. AUCUNE MCMC n'est lancée dans cette porte :
    le vrai manifeste est interdit, donc ce chemin se termine toujours par
    un refus avant cobaya.run.
    """

    refuser_injections_en_production()
    if "--je-confirme-la-production" not in args:
        raise GardeErreur(
            "production refusée : confirmation explicite absente "
            "(--je-confirme-la-production)"
        )
    if "--autorisation" not in args:
        raise GardeErreur("autorisation absente")
    variante, graine = args[0], int(args[1])
    chemin_autorisation = args[args.index("--autorisation") + 1]
    rapport = preflight(variante, graine)
    etat_git = rapport["git"]
    if not etat_git["arbre_propre"]:
        raise GardeErreur("arbre Git non propre : production refusée")
    garde_autorisation(chemin_autorisation, variante, graine, etat_git["head"])
    # Point jamais atteint en G2.4b : le vrai manifeste est interdit.
    raise GardeErreur(
        "verrou G2.4b : le lancement réel exige une validation humaine "
        "postérieure à la qualification — production refusée."
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
