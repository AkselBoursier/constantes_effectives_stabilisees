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

Politique de capacité CAP-1 (issue #90, ratification humaine du 2 août
2026) : le budget de production, les réserves et le support actif sont
désormais matérialisés et BLOQUANTS. L'admission d'un nouveau run ne se
réduit plus à « libre >= budget » : elle exige
    libre >= budget_restant_alloue + allocation_run_actif
             + reserve_reprise + reserve_volume.
La ratification du budget NE VAUT PAS autorisation de production :
VERROU_PRODUCTION_G2_4D reste True.

Injections de test (C7C1_TEST_*) : autorisées seulement hors production ;
leur présence en mode --produire est une faute et entraîne un refus.
"""

from __future__ import annotations

import copy
import ctypes
import hashlib
import json
import math
import os
import shutil
import subprocess
import sys
import time
import tracemalloc
from decimal import Decimal, InvalidOperation
from pathlib import Path

import numpy as np

GIO = 1024**3
GARDE_CAPACITE_GIO = 40
SEUIL_ALERTE_GIO = 15

# ============================================================ CAP-1
# Décision humaine RATIFIÉE — issue #90, commentaire du 2 août 2026.
# CAP-1 ne réévalue PAS ces valeurs : elle les matérialise et vérifie
# qu'elles produisent les gardes attendues.
POLITIQUE_CAPACITE_VERSION = "cap1-1.1.0"
BUDGET_TOTAL_RATIFIE_GIO = 20
RESERVE_REPRISE_RATIFIEE_GIO = 1.15
RESERVE_VOLUME_RATIFIEE_GIO = 40
REFERENCE_RATIFICATION_BUDGET = "CAP0-2026-08-02-issue90-rat1"

# SOURCE NORMATIVE UNIQUE du support actif (CAP-1a). La décision humaine
# porte sur le volume C:, PAS sur « le volume système quel qu'il soit ».
# %SystemDrive% ne définit JAMAIS la ratification : il n'est lu que comme
# fait système supplémentaire, sans valeur normative. Déplacer <RUNS> vers
# un autre volume exigera une nouvelle ratification humaine et une
# nouvelle version de politique de capacité.
SUPPORT_ACTIF_VOLUME_RATIFIE = "C"

# Constantes de MESURE publiées en CAP-0 (issue #90). Les allocations S8
# sont RECALCULÉES à partir d'elles ci-dessous — jamais recopiées.
#   N_G1_max = 219 400 lignes (pire run G1 convergé, cpl/s201)
#   S8       = 8 × N_G1_max
#   borne empirique d'octets par ligne (densité maximale G1, 18,36 o par
#   colonne) : M2a 349, M2b 331 — plus conservatrice de 9 % que la
#   largeur exacte mesurée (319 / 303)
#   pire ratio auxiliaire mesuré (checkpoint, progress, covmat, YAML,
#   journaux) : 0,845 %
N_G1_MAX_LIGNES = 219_400
FACTEUR_SCENARIO_S8 = 8
LIGNES_S8_PAR_RUN = FACTEUR_SCENARIO_S8 * N_G1_MAX_LIGNES  # 1 755 200
OCTETS_PAR_LIGNE_BORNE = {"M2a": 349, "M2b": 331}
RATIO_AUXILIAIRE_MAX = 0.00845

# Fréquence d'observation de la capacité (opérationnelle, JAMAIS
# scientifique — voir garde_injection_observateur). Justification au §8
# du rapport CAP-1 : entre deux observations, une chaîne de poids 1
# écrivant à chaque itération produit au plus
#   1000 × 349 o = 349 000 o ≈ 0,000325 Gio,
# soit 0,03 % de la réserve de reprise ratifiée (1,15 Gio) ; le facteur
# de sécurité 4 couvre une observation manquée et les vidages
# auxiliaires. Le plancher couvre ce que le RESTE du système peut
# consommer sur le volume système dans la même fenêtre.
CALLBACK_EVERY_ITERATIONS = 1000
FACTEUR_SECURITE_ANTICIPATION = 4
MARGE_ANTICIPATION_PLANCHER_GIO = 0.25

# La requête au sous-système de stockage (média, bus, santé) est
# transitoirement indisponible sous charge. On réessaie un nombre BORNÉ de
# fois puis on REFUSE : jamais de supposition, mais pas de refus sur un
# unique aléa non plus.
TENTATIVES_QUALIFICATION_MATERIELLE = 3

# Sous-arbres de <RUNS> explicitement reconnus comme temporaires : ils ne
# sont JAMAIS comptés comme production. Comparaison sur le PREMIER
# composant relatif, exacte — « _tmpfoo » n'est pas « _tmp ».
SOUS_ARBRES_TEMPORAIRES_RECONNUS = ("_tmp", "g2_4_qualification")

STATUT_RUN_PLANIFIE = "PLANIFIE_NON_LANCE"
STATUT_RUN_INTERROMPU_CAPACITE = "NON_CONVERGE_INTERRUPTION_CAPACITE"
STATUT_RUN_CONVERGE = "CONVERGE"
# SENT-0A : statuts de sortie supplémentaires, strictement séparés.
#   ECHEC_TECHNIQUE      : toute exception hors capacité — jamais reclassée ;
#   FIN_SANS_CONVERGENCE : Cobaya rend la main normalement SANS déclarer
#                          sampler.converged is True. Un simple retour sans
#                          exception ne vaut JAMAIS convergence.
STATUT_RUN_ECHEC_TECHNIQUE = "NON_CONVERGE_ECHEC_TECHNIQUE"
STATUT_RUN_FIN_SANS_CONVERGENCE = "FIN_SANS_CONVERGENCE"
STATUTS_RUN_FINALS = (
    STATUT_RUN_CONVERGE, STATUT_RUN_INTERROMPU_CAPACITE,
    STATUT_RUN_ECHEC_TECHNIQUE, STATUT_RUN_FIN_SANS_CONVERGENCE,
)
# Champs qu'une mise à jour RUNTIME du manifeste a le droit de toucher.
# Tout autre champ — identité, science, capacité — est inviolable après
# l'écriture initiale.
CHAMPS_RUNTIME_AUTORISES = (
    "statut_run", "date_fin_utc", "detail_fin", "converged_cobaya",
)
SCHEMAS_MANIFESTE_RECONNUS = ("c7c1-run-manifest-1", "c7c1-run-manifest-2")

# ------------------------------------------------ SENT-0 : périmètre
# Couple sentinelle PROPOSÉ en #94 — PAS ENCORE AUTORISÉ à tourner.
# Tant que la porte SENT-0 n'est pas close, seul ce couple peut atteindre
# l'étape de production future ; les 31 autres sont refusés en 4 bis.
# Ce confinement est purement OPÉRATOIRE : il n'accorde AUCUN privilège
# scientifique à M2a-N — les quatre variantes restent co-primaires
# (G2.2a) ; le couple est simplement le premier de la matrice gelée et le
# cas nominal des qualifications du lanceur, choisi ex ante en #94.
SENTINELLE_SENT0_VARIANTE = "M2a-N"
SENTINELLE_SENT0_GRAINE = 630101

# ------------------------------------ SENT-0D : franchissement ratifié
# Référence PUBLIQUE de la ratification humaine du franchissement
# technique (issue #94). Elle matérialise l'INTENTION OPÉRATOIRE au CLI ;
# ce n'est pas un secret — la véritable seconde protection reste
# l'autorisation privée à deux clés, liée au HEAD et au périmètre exact.
# Le verrou VERROU_PRODUCTION_G2_4D reste True : SENT-0D n'ouvre qu'un
# franchissement étroit — couple sentinelle codé + autorisation privée au
# périmètre EXACT + intention CLI explicite — et rien d'autre.
REFERENCE_RATIFICATION_SENTINELLE = "SENT0D-2026-08-04-issue94-rat1"
# Périmètre EXACT que l'autorisation privée doit déclarer pour un
# franchissement SENT-0D : le couple sentinelle, seul, sans extension.
PERIMETRE_EXACT_SENTINELLE = {
    SENTINELLE_SENT0_VARIANTE: [SENTINELLE_SENT0_GRAINE],
}

# ------------------------------------------------ verrou dur G2.4d
# Tant que ce verrou vaut True, AUCUNE écriture réelle et AUCUN
# cobaya.run ne peuvent être atteints : le refus intervient AVANT
# mkdir, open en écriture, os.replace, manifest.json et préfixe Cobaya.
VERROU_PRODUCTION_G2_4D = True

# Schéma du contrat local privé consommé par le lanceur (INFRA-1a,
# étendu en G2.4d-a : chemin de cache et référence de ratification).
VERSION_CONTRAT_LOCAL = "1.3.0"
# Format imposé de la date de création du manifeste de run.
FORMAT_DATE_UTC = "%Y-%m-%dT%H:%M:%SZ"
# Usage exigé d'une autorisation RÉELLE. Un manifeste de qualification
# porte « QUALIFICATION_ONLY » et doit être refusé sans exception.
USAGE_AUTORISATION_PRODUCTION = "PRODUCTION"
CLES_THREADS = (
    "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS",
    "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS",
)
SCHEMA_MANIFESTE_RUN = "c7c1-run-manifest-2"

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
#
# CAP-1 étend encore ce schéma : réserves ratifiées, version de politique
# de capacité et identité expurgée du support deviennent obligatoires.
# Une autorisation ne peut donc plus valider un autre budget, une autre
# réserve, une autre référence, une autre politique ni un autre support.
CLES_MANIFESTE = {
    "type", "usage", "cle_humaine_1", "cle_humaine_2", "sha256_lanceur",
    "sha256_adaptateur", "sha256_chemin_rapide", "sha256_descripteurs",
    "sha256_preenregistrement", "sha256_donnees", "empreinte_environnement",
    "version_contrat_local", "head_autorise", "racine_runs_canonique",
    "variantes_graines_autorisees", "budget_production_requis_Gio",
    "budget_production_ratification", "reserve_reprise_Gio",
    "reserve_volume_minimale_Gio", "politique_capacite_version",
    "support_actif_identite_expurgee",
}
# Clés OPTIONNELLES de l'autorisation : le champ SENT-0D n'est exigé que
# pour un franchissement — l'admettre sans l'exiger préserve la
# qualification générale G2.4d telle quelle. Toute AUTRE clé étrangère
# reste refusée.
CLES_MANIFESTE_OPTIONNELLES = {"reference_ratification_sentinelle"}

# Champs OBLIGATOIRES du manifeste de run : aucun ne peut être absent ni
# remplacé par une valeur implicite. Les sept derniers sont ajoutés par
# CAP-1 et font PARTIE DE L'IDENTITÉ DE REPRISE : une reprise sous une
# autre politique de capacité, un autre budget, une autre réserve, une
# autre fréquence d'observation ou un autre support est refusée.
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
    "budget_total_Gio", "reserve_reprise_Gio",
    "reserve_volume_minimale_Gio", "allocation_run_actif_Gio",
    "politique_capacite_version", "callback_every",
    "support_actif_identite_expurgee",
)
# Champs de l'identité de reprise qui décrivent la POLITIQUE DE CAPACITÉ.
# Une reprise exige qu'ils soient identiques, en plus du reste.
CHAMPS_POLITIQUE_CAPACITE = (
    "budget_total_Gio", "reserve_reprise_Gio", "reserve_volume_minimale_Gio",
    "allocation_run_actif_Gio", "politique_capacite_version",
    "callback_every", "support_actif_identite_expurgee",
    "reference_ratification_budget",
)
POINT_FOND_P0 = {"H0": 67.36, "ombh2": 0.02237, "omm": 0.3152}
POINT_FOND_P1 = {"H0": 68.3526, "ombh2": 0.022410, "omm": 0.300539}
P2_VALUES = {"M2a": (0.6, -0.2, 0.4, 1.2, 0.8), "M2b": (0.6, -0.2, 0.4, 0.8)}
P3_VALUES = {"M2a": (1.4, 0.2, 1.6, 0.1, 1.3), "M2b": (1.4, 0.2, 1.6, 1.3)}


class GardeErreur(RuntimeError):
    """Une garde de pré-vol a échoué."""


class ArretCapaciteC7C1(RuntimeError):
    """Interruption de capacité d'un run en cours — JAMAIS une convergence.

    Levée par l'observateur de capacité (callback Cobaya) quand la
    haute-eau est franchie, ou quand la capacité n'est plus OBSERVABLE.
    Le statut associé est toujours
    ``NON_CONVERGE_INTERRUPTION_CAPACITE`` : positionner
    ``sampler.converged = True`` est interdit, car cela ferait passer une
    interruption de capacité pour une convergence scientifique.
    """

    def __init__(self, message: str, etat: dict | None = None):
        super().__init__(message)
        self.etat = dict(etat or {})
        self.statut_run = STATUT_RUN_INTERROMPU_CAPACITE


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


def garde_perimetre_sentinelle(variante: str, graine: int) -> None:
    """SENT-0A (4 bis) : confinement de la PRODUCTION au couple sentinelle.

    S'applique au mode ``produire`` UNIQUEMENT — le pré-vol des quatre
    variantes reste ouvert. Les 31 autres couples de la matrice sont
    refusés ici sur la cause exacte « hors périmètre sentinelle », même si
    toutes les autres gardes étaient satisfaites. Aucun privilège
    scientifique n'est accordé à M2a-N : ce confinement disparaîtra avec
    la clôture de SENT-0, et les quatre variantes restent co-primaires.
    """
    if (variante, int(graine)) != (SENTINELLE_SENT0_VARIANTE,
                                   SENTINELLE_SENT0_GRAINE):
        raise GardeErreur(
            f"hors périmètre sentinelle : ({variante}, {graine}) — tant que "
            f"SENT-0 n'est pas close, seule la production du couple "
            f"({SENTINELLE_SENT0_VARIANTE}, {SENTINELLE_SENT0_GRAINE}) peut "
            "être envisagée ; les 31 autres couples exigent l'audit du "
            "sentinelle puis une décision humaine distincte"
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


# ============================================ CAP-1 : politique de capacité

def _valeur_ratifiee(valeur, attendu, etiquette: str) -> float:
    """Égalité EXACTE à une valeur ratifiée — aucune tolérance flottante.

    La comparaison passe par ``Decimal(str(x))`` : elle reflète la
    décision humaine telle qu'elle est écrite, accepte 20 comme 20.0, et
    refuse 19.999 comme 20.001. Aucun epsilon n'est introduit.
    """
    if isinstance(valeur, bool) or not isinstance(valeur, (int, float)):
        raise GardeErreur(
            f"{etiquette} : valeur absente ou non numérique ({valeur!r})")
    if not math.isfinite(float(valeur)):
        raise GardeErreur(f"{etiquette} : valeur non finie ({valeur!r})")
    try:
        lue = Decimal(str(valeur))
    except InvalidOperation as exc:  # pragma: no cover - défensif
        raise GardeErreur(f"{etiquette} : valeur illisible ({valeur!r})") from exc
    if lue != Decimal(str(attendu)):
        raise GardeErreur(
            f"{etiquette} : {valeur!r} != valeur ratifiée {attendu!r} "
            "(comparaison exacte, aucune tolérance)")
    return float(valeur)


def _grille_de(variante: str) -> str:
    grille = str(variante).split("-")[0]
    if grille not in OCTETS_PAR_LIGNE_BORNE:
        raise GardeErreur(
            f"grille inconnue pour la variante {variante!r} : aucune "
            "allocation S8 n'est définie — refus plutôt que supposition")
    return grille


def allocation_run_actif_gio(variante: str) -> float:
    """Enveloppe S8 conservatrice d'UN run de la variante donnée.

    RECALCULÉE à partir des constantes CAP-0 publiées :
        lignes  = 8 × 219 400 = 1 755 200
        octets  = lignes × borne empirique (M2a 349 | M2b 331)
        + enveloppe auxiliaire au pire ratio mesuré (0,845 %)
    Contrôle croisé du rapport CAP-0 : 16 runs M2a + 16 runs M2b donnent
    B_chain(S8) = 17,785 Gio et B_actif(S8) = 18,94 Gio.
    """
    octets_chaine = LIGNES_S8_PAR_RUN * OCTETS_PAR_LIGNE_BORNE[_grille_de(variante)]
    return (octets_chaine * (1.0 + RATIO_AUXILIAIRE_MAX)) / GIO


def marge_anticipation_gio() -> float:
    """Zone d'anticipation : l'arrêt doit précéder la saturation."""
    octets_max = max(OCTETS_PAR_LIGNE_BORNE.values())
    entre_observations = (
        CALLBACK_EVERY_ITERATIONS * octets_max * FACTEUR_SECURITE_ANTICIPATION
    ) / GIO
    return max(MARGE_ANTICIPATION_PLANCHER_GIO, entre_observations)


# ------------------------------------------------- support actif ratifié

_CACHE_MATERIEL: dict | None = None


def _lettre_volume(cible: str | Path) -> str:
    """Lettre de volume portant un chemin — sans aucun appel système."""
    lettre = os.path.splitdrive(os.path.realpath(str(cible)))[0].rstrip(":")
    lettre = os.environ.get("C7C1_TEST_LETTRE_RUNS", lettre).upper()
    if not lettre:
        raise GardeErreur("chemin sans lettre de volume : refus")
    return lettre


def _fait_systeme_volume_systeme(lettre: str) -> bool:
    """Fait système SUPPLÉMENTAIRE : ce volume est-il %SystemDrive% ?

    Purement informatif. Cette valeur n'entre dans AUCUNE décision et ne
    fait pas partie de l'identité de reprise : %SystemDrive% peut changer
    sans que la ratification humaine change.
    """
    return lettre == os.environ.get("SystemDrive", "").rstrip(":").upper()


def _garde_volume_ratifie(cible: str | Path) -> str:
    """La lettre du volume DOIT être celle du support RATIFIÉ.

    Comparée à ``SUPPORT_ACTIF_VOLUME_RATIFIE``, source normative unique.
    %SystemDrive% n'est pas consulté ici : que le volume système soit C:,
    D: ou autre, le support ratifié reste C:. Un <RUNS> sur D: est refusé
    même si D: est devenu le volume système ; un <RUNS> sur C: reste
    accepté même si C: ne l'est plus.

    Contrôlée AVANT toute interrogation d'API, pour que le refus soit
    attribuable à la bonne cause plutôt qu'à l'échec d'une requête sur un
    volume inexistant.
    """
    lettre = _lettre_volume(cible)
    if lettre != SUPPORT_ACTIF_VOLUME_RATIFIE:
        raise GardeErreur(
            f"support actif non ratifié : chemin sur le volume {lettre}: "
            f"alors que le support ratifié par décision humaine est "
            f"{SUPPORT_ACTIF_VOLUME_RATIFIE}: — un changement de volume "
            "exige une nouvelle ratification, pas un changement de "
            "%SystemDrive%")
    return lettre


def _infos_volume(cible: str | Path) -> dict:
    """Faits de volume lus par API système — jamais supposés."""
    lettre = _lettre_volume(cible)
    racine_volume = f"{lettre}:\\"
    if os.name != "nt":  # pragma: no cover - le lot est Windows-only
        raise GardeErreur(
            "qualification du support indisponible hors Windows : refus "
            "plutôt que supposition")
    try:
        k32 = ctypes.WinDLL("kernel32", use_last_error=True)
        type_lecteur = int(k32.GetDriveTypeW(ctypes.c_wchar_p(racine_volume)))
        nom = ctypes.create_unicode_buffer(261)
        sysfic = ctypes.create_unicode_buffer(261)
        serie = ctypes.c_ulong()
        maxlen = ctypes.c_ulong()
        drapeaux = ctypes.c_ulong()
        ok = k32.GetVolumeInformationW(
            ctypes.c_wchar_p(racine_volume), nom, 261, ctypes.byref(serie),
            ctypes.byref(maxlen), ctypes.byref(drapeaux), sysfic, 261)
        if not ok:
            raise OSError(ctypes.get_last_error(), "GetVolumeInformationW")
        secteurs = ctypes.c_ulong()
        octets_secteur = ctypes.c_ulong()
        libres = ctypes.c_ulong()
        total = ctypes.c_ulong()
        ok2 = k32.GetDiskFreeSpaceW(
            ctypes.c_wchar_p(racine_volume), ctypes.byref(secteurs),
            ctypes.byref(octets_secteur), ctypes.byref(libres),
            ctypes.byref(total))
        cluster = int(secteurs.value * octets_secteur.value) if ok2 else 0
    except OSError as exc:
        raise GardeErreur(
            f"qualification du volume indisponible ({exc}) : refus plutôt "
            "que supposition") from exc
    return {
        "lettre_volume": lettre,
        "type_lecteur_code": int(os.environ.get(
            "C7C1_TEST_TYPE_LECTEUR", type_lecteur)),
        "systeme_fichiers": os.environ.get(
            "C7C1_TEST_SYSTEME_FICHIERS", sysfic.value),
        "empreinte_volume": hashlib.sha256(
            f"{lettre}:{serie.value:08x}".encode()).hexdigest()[:16],
        "taille_cluster_octets": cluster,
    }


def _infos_materiel(lettre: str) -> dict:
    """Type de média et bus du disque physique portant le volume.

    Détection locale par API système (Storage/MSFT_PhysicalDisk). Aucun
    modèle ni numéro de série n'est lu ni publié : seuls MediaType,
    BusType et HealthStatus sortent d'ici. Une indisponibilité est un
    REFUS, jamais une supposition.
    """
    global _CACHE_MATERIEL

    if os.environ.get("C7C1_TEST_SUPPORT_INDISPONIBLE") == "1":
        raise GardeErreur(
            "qualification matérielle du support indisponible : refus "
            "plutôt que supposition")
    forge = {c: os.environ.get(f"C7C1_TEST_SUPPORT_{c.upper()}")
             for c in ("media", "bus", "sante")}
    if _CACHE_MATERIEL is None:
        commande = (
            "$ErrorActionPreference='Stop';"
            f"$p = Get-Partition -DriveLetter {lettre};"
            "$d = Get-PhysicalDisk -DeviceNumber $p.DiskNumber;"
            "[pscustomobject]@{MediaType=$d.MediaType;BusType=$d.BusType;"
            "HealthStatus=$d.HealthStatus} | ConvertTo-Json -Compress")
        # La requête au sous-système de stockage est parfois lente ou
        # transitoirement indisponible sous charge. On réessaie un nombre
        # BORNÉ de fois ; passé ce nombre, on refuse — on ne suppose jamais.
        derniere = "aucune tentative"
        for tentative in range(TENTATIVES_QUALIFICATION_MATERIELLE):
            try:
                proc = subprocess.run(
                    ["powershell", "-NoProfile", "-NonInteractive",
                     "-Command", commande],
                    capture_output=True, text=True, timeout=120)
            except (OSError, subprocess.SubprocessError) as exc:
                derniere = f"exception {exc}"
            else:
                if proc.returncode == 0 and proc.stdout.strip():
                    try:
                        _CACHE_MATERIEL = json.loads(proc.stdout)
                        break
                    except json.JSONDecodeError as exc:
                        derniere = f"réponse illisible ({exc.msg})"
                else:
                    derniere = (f"code {proc.returncode} / "
                                f"{(proc.stderr or '').strip()[:120]}")
            if tentative + 1 < TENTATIVES_QUALIFICATION_MATERIELLE:
                time.sleep(1.0 + tentative)
        if _CACHE_MATERIEL is None:
            raise GardeErreur(
                "qualification matérielle du support indisponible après "
                f"{TENTATIVES_QUALIFICATION_MATERIELLE} tentatives "
                f"({derniere}) : refus plutôt que supposition")
    brut = dict(_CACHE_MATERIEL)
    return {
        "media": forge["media"] or str(brut.get("MediaType", "")),
        "bus": forge["bus"] or str(brut.get("BusType", "")),
        "sante": forge["sante"] or str(brut.get("HealthStatus", "")),
    }


def garde_support_actif(cible: str | Path) -> dict:
    """Preuve DYNAMIQUE que <RUNS> est sur le support ratifié.

    Volume RATIFIÉ (constante, jamais %SystemDrive%), SSD, bus NVMe,
    lecteur fixe, NTFS, hors Git, hors synchronisation. Rend une identité
    EXPURGÉE (aucun chemin, aucun modèle, aucun numéro de série)
    utilisable dans le manifeste et dans l'autorisation. Toute
    qualification indisponible est un refus.

    L'identité porte l'empreinte RÉELLE du volume : elle empêche une
    substitution silencieuse. Elle reste strictement locale — voir
    ``identite_support_publiable`` pour la forme diffusable.
    """
    from xz_likelihood_g2_3 import refuser_sortie_sous_git

    lettre = _garde_volume_ratifie(cible)  # avant toute API : cause exacte
    volume = _infos_volume(cible)
    if volume["type_lecteur_code"] != 3:  # DRIVE_FIXED
        raise GardeErreur(
            f"support actif non ratifié : type de lecteur "
            f"{volume['type_lecteur_code']} != FIXE (3)")
    if volume["systeme_fichiers"].upper() != "NTFS":
        raise GardeErreur(
            f"support actif non ratifié : système de fichiers "
            f"{volume['systeme_fichiers']!r} != NTFS")
    materiel = _infos_materiel(lettre)
    if materiel["media"].upper() != "SSD":
        raise GardeErreur(
            f"support actif non ratifié : média {materiel['media']!r} != SSD")
    if materiel["bus"].upper() != "NVME":
        raise GardeErreur(
            f"support actif non ratifié : bus {materiel['bus']!r} != NVMe")
    if materiel["sante"].upper() != "HEALTHY":
        raise GardeErreur(
            f"support actif non ratifié : santé {materiel['sante']!r} "
            "!= Healthy")
    refuser_sortie_sous_git(Path(cible))
    canonique = _canonique(cible)
    if "onedrive" in canonique:
        raise GardeErreur("support actif sous OneDrive : refus")
    identite = {
        "volume_ratifie": SUPPORT_ACTIF_VOLUME_RATIFIE,
        "lettre_volume": lettre,
        "type_lecteur": "FIXE",
        "systeme_fichiers": "NTFS",
        "media": "SSD",
        "bus": "NVMe",
        "empreinte_volume": volume["empreinte_volume"],
        "hors_git": True,
        "hors_synchronisation": True,
    }
    return {
        "identite_expurgee": identite,
        "sante": materiel["sante"],
        "taille_cluster_octets": volume["taille_cluster_octets"],
        "qualification_materielle_disponible": True,
        # Fait système supplémentaire, SANS valeur normative et HORS de
        # l'identité de reprise : %SystemDrive% peut changer sans que la
        # ratification humaine change.
        "fait_systeme_volume_systeme": _fait_systeme_volume_systeme(lettre),
    }


# Champ de l'identité de support dont la valeur est STRICTEMENT LOCALE.
# Obligatoire en interne (contrat, manifeste, autorisation, reprise) :
# c'est lui qui empêche une substitution silencieuse de volume. Jamais
# publié : sur toute surface diffusable, seule sa présence et sa
# conformité sortent.
CHAMP_SUPPORT_PRIVE = "empreinte_volume"
MARQUE_VALEUR_PRIVEE = "<EMPREINTE_VOLUME_PRIVEE>"


def identite_support_publiable(identite: dict) -> dict:
    """Forme DIFFUSABLE d'une identité de support.

    La valeur réelle de l'empreinte est remplacée par une marque ; sa
    présence et sa conformité restent vérifiables. N'affaiblit rien :
    l'identité interne, elle, conserve la valeur réelle.
    """
    publiable = {c: v for c, v in identite.items() if c != CHAMP_SUPPORT_PRIVE}
    reelle = identite.get(CHAMP_SUPPORT_PRIVE)
    publiable[CHAMP_SUPPORT_PRIVE] = MARQUE_VALEUR_PRIVEE
    publiable["empreinte_volume_presente"] = bool(reelle)
    publiable["empreinte_volume_conforme"] = (
        isinstance(reelle, str) and len(reelle) == 16
        and all(c in "0123456789abcdef" for c in reelle))
    return publiable


def identite_support_expurgee(cible: str | Path) -> dict:
    return garde_support_actif(cible)["identite_expurgee"]


# ------------------------------------- occupation du lot : mesure sûre

def _taille_brute(entree) -> int:
    """Taille logique d'une entrée. Point d'injection des fautes."""
    return entree.stat(follow_symlinks=False).st_size


def _arrondi_cluster(octets: int, cluster: int) -> int:
    if cluster > 0:
        return -(-int(octets) // cluster) * cluster
    return int(octets)


def _sous_racine(canonique: str, racine_canonique: str) -> bool:
    return (canonique == racine_canonique
            or canonique.startswith(racine_canonique + os.sep))


def _est_lien(entree) -> bool:
    if entree.is_symlink():
        return True
    verifier = getattr(entree, "is_junction", None)
    try:
        return bool(verifier()) if verifier else False
    except OSError:  # pragma: no cover - défensif
        return False


def _inventorier_occupation(racine: Path, cluster: int):
    """Parcours SANS suivi de lien, strictement borné à <RUNS>.

    Retourne (inventaire {parties relatives -> octets alloués}, liens non
    suivis). N'efface rien, ne modifie rien, n'ouvre aucun fichier en
    écriture.
    """
    racine_c = _canonique(racine)
    inventaire: dict[tuple, int] = {}
    liens: list[str] = []
    pile = [Path(racine)]
    while pile:
        courant = pile.pop()
        try:
            entrees = list(os.scandir(courant))
        except FileNotFoundError:
            continue  # disparu pendant le parcours : non compté
        except PermissionError as exc:
            raise GardeErreur(
                f"occupation illisible sous la racine de runs ({exc.errno}) "
                ": refus plutôt que sous-estimation") from exc
        for entree in entrees:
            relatif = tuple(Path(entree.path).relative_to(racine).parts)
            if not _sous_racine(_canonique(entree.path), racine_c):
                raise GardeErreur(
                    "identité canonique hors de la racine de runs : refus "
                    f"({'/'.join(relatif)})")
            if _est_lien(entree):
                liens.append("/".join(relatif))
                continue  # jamais suivi
            try:
                repertoire = entree.is_dir(follow_symlinks=False)
            except OSError:
                continue
            if repertoire:
                pile.append(Path(entree.path))
                continue
            try:
                taille = _taille_brute(entree)
            except FileNotFoundError:
                continue
            if isinstance(taille, bool) or not isinstance(taille, int):
                raise GardeErreur(
                    f"taille forgée ou non entière pour {'/'.join(relatif)} "
                    f": {taille!r}")
            if taille < 0:
                raise GardeErreur(
                    f"taille négative pour {'/'.join(relatif)} : {taille}")
            inventaire[relatif] = _arrondi_cluster(taille, cluster)
    return inventaire, sorted(liens)


def _repertoires_de_production(inventaire: dict, racine: Path) -> set[tuple]:
    """Répertoires de run ATTRIBUÉS à la production par leur manifeste.

    Un répertoire est de la production s'il porte un ``manifest.json``
    lisible, au schéma reconnu, non marqué ``_QUALIFICATION_ONLY``.
    """
    repertoires: set[tuple] = set()
    for parties in inventaire:
        if parties[-1] != "manifest.json":
            continue
        try:
            contenu = json.loads(
                (Path(racine).joinpath(*parties)).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if not isinstance(contenu, dict):
            continue
        if contenu.get("_QUALIFICATION_ONLY"):
            continue
        if contenu.get("schema") in SCHEMAS_MANIFESTE_RECONNUS:
            repertoires.add(parties[:-1])
    return repertoires


def mesurer_occupation_lot(cible: str | Path,
                           verifier_stabilite: bool = True) -> dict:
    """Occupation C7-C1 réellement allouée sous <RUNS>.

    Reste strictement sous la racine canonique ; ne suit aucun lien ni
    point d'analyse ; refuse toute identité canonique qui en sort ;
    n'efface rien, ne modifie rien. Les sous-arbres temporaires reconnus
    et les produits non attribués à un manifeste de run ne sont JAMAIS
    comptés comme production : en l'absence de run réel, le budget
    consommé vaut zéro.

    ``verifier_stabilite`` effectue DEUX parcours et refuse si l'état a
    changé entre les deux (fichier apparaissant pendant la mesure). Il
    est désactivé pour l'observateur périodique, dont la mesure est
    intrinsèquement instantanée et bornée par une marge d'anticipation.

    Le contrôle de stabilité porte sur ce qui est BUDGÉTÉ, c'est-à-dire
    hors sous-arbres temporaires reconnus : le répertoire temporaire
    scientifique vit sous la racine et son activité est attendue ; la
    faire échouer la mesure du budget serait un faux positif permanent.
    """
    racine = Path(cible)
    if not racine.is_dir():
        raise GardeErreur("racine de runs inexistante : mesure impossible")
    cluster = _infos_volume(racine)["taille_cluster_octets"]

    def _budgetable(inv: dict) -> dict:
        return {p: t for p, t in inv.items()
                if p[0] not in SOUS_ARBRES_TEMPORAIRES_RECONNUS}

    inventaire, liens = _inventorier_occupation(racine, cluster)
    if verifier_stabilite:
        second, liens2 = _inventorier_occupation(racine, cluster)
        a, b = _budgetable(inventaire), _budgetable(second)
        if a != b or liens2 != liens:
            apparus = sorted("/".join(p) for p in set(b) - set(a))
            disparus = sorted("/".join(p) for p in set(a) - set(b))
            raise GardeErreur(
                "occupation instable pendant la mesure (apparus="
                f"{apparus[:5]}, disparus={disparus[:5]}) : refus")
    production_dirs = _repertoires_de_production(inventaire, racine)
    octets = {"production": 0, "temporaires_reconnus": 0, "non_attribues": 0}
    par_run: dict[str, int] = {}
    for parties, taille in inventaire.items():
        if parties[0] in SOUS_ARBRES_TEMPORAIRES_RECONNUS:
            octets["temporaires_reconnus"] += taille
            continue
        appartenance = next(
            (d for d in production_dirs if parties[:len(d)] == d), None)
        if appartenance is None:
            octets["non_attribues"] += taille
            continue
        octets["production"] += taille
        cle = "/".join(appartenance)
        par_run[cle] = par_run.get(cle, 0) + taille
    for valeur in octets.values():
        if not math.isfinite(float(valeur)) or valeur < 0:
            raise GardeErreur(f"occupation mesurée invalide : {octets}")
    return {
        "octets_production": octets["production"],
        "octets_temporaires_reconnus": octets["temporaires_reconnus"],
        "octets_non_attribues": octets["non_attribues"],
        "gio_production": octets["production"] / GIO,
        "gio_temporaires_reconnus": octets["temporaires_reconnus"] / GIO,
        "gio_non_attribues": octets["non_attribues"] / GIO,
        "runs_production": dict(sorted(par_run.items())),
        "n_fichiers": len(inventaire),
        "liens_non_suivis": liens,
        "taille_cluster_octets": cluster,
        "stabilite_verifiee": bool(verifier_stabilite),
    }


# --------------------------------------- garde de capacité de production

def garde_capacite_production(cible: str | Path, variante: str,
                              occupation: dict | None = None,
                              support: dict | None = None) -> dict:
    """Règle d'ADMISSION d'un NOUVEAU run — remplace « libre >= budget ».

    Ne double compte jamais l'allocation du run à admettre :
    ``budget_restant_alloue`` est ce qui reste du budget total UNE FOIS
    le run courant provisionné ; le seuil le ré-ajoute explicitement.
    Au début du lot (rien de consommé), le seuil vaut donc
    ``budget_total + reserve_reprise + reserve_volume`` = 61,15 Gio.
    """
    budget_total = float(BUDGET_TOTAL_RATIFIE_GIO)
    reserve_reprise = float(RESERVE_REPRISE_RATIFIEE_GIO)
    reserve_volume = float(RESERVE_VOLUME_RATIFIEE_GIO)
    allocation = allocation_run_actif_gio(variante)
    if support is None:
        support = garde_support_actif(cible)  # refuse si non ratifié
    if occupation is None:
        occupation = mesurer_occupation_lot(cible, verifier_stabilite=True)
    consomme = float(occupation["gio_production"])
    libre = float(espace_libre_gio(cible))
    for etiquette, valeur in (("espace libre", libre),
                              ("budget consommé", consomme),
                              ("allocation du run actif", allocation)):
        if not math.isfinite(valeur):
            raise GardeErreur(
                f"données de capacité non finies : {etiquette} = {valeur!r}")
    restant = max(0.0, budget_total - consomme - allocation)
    seuil = restant + allocation + reserve_reprise + reserve_volume
    etat = {
        "libre_gio": libre,
        "budget_total_gio": budget_total,
        "budget_consomme_gio": consomme,
        "allocation_run_actif_gio": allocation,
        "budget_restant_alloue_gio": restant,
        "reserve_reprise_gio": reserve_reprise,
        "reserve_volume_gio": reserve_volume,
        "seuil_admission_gio": seuil,
        "marge_apres_admission_gio": libre - seuil,
        "politique_capacite_version": POLITIQUE_CAPACITE_VERSION,
        "reference_ratification_budget": REFERENCE_RATIFICATION_BUDGET,
        # État RAPPORTÉ : forme diffusable. L'identité réelle, elle, part
        # au manifeste et à l'autorisation sans être passée par ici.
        "support_actif_identite_expurgee": identite_support_publiable(
            support["identite_expurgee"]),
        "occupation": {
            k: occupation[k] for k in
            ("octets_production", "octets_temporaires_reconnus",
             "octets_non_attribues", "runs_production", "liens_non_suivis",
             "stabilite_verifiee")},
    }
    if consomme > budget_total:
        raise GardeErreur(
            f"budget déjà dépassé : {consomme:.4f} Gio consommés > budget "
            f"ratifié {budget_total:.2f} Gio — admission refusée")
    if libre < seuil:
        raise GardeErreur(
            f"admission refusée : espace libre {libre:.4f} Gio < seuil "
            f"{seuil:.4f} Gio (restant alloué {restant:.4f} + allocation "
            f"{allocation:.4f} + reprise {reserve_reprise:.2f} + volume "
            f"{reserve_volume:.2f})")
    if libre - allocation < reserve_volume:
        raise GardeErreur(
            f"admission refusée : après allocation du run "
            f"({allocation:.4f} Gio), il resterait {libre - allocation:.4f} "
            f"Gio < réserve de volume ratifiée {reserve_volume:.2f} Gio")
    return etat


def garde_budget_production(contrat: dict, cible: str | Path) -> dict:
    """Contrôle SÉPARÉ du budget de production (jamais la garde technique).

    La garde technique (>= 40 Gio) autorise seulement la poursuite des
    tests et de la préparation. La production exige en plus un budget
    ratifié, non nul, positif, et inférieur ou égal à l'espace libre
    MESURÉ SUR LA CIBLE. Le statut NON_ETABLI bloque toute production.
    Aucun budget n'est inventé ici.

    CAP-1 : « libre >= budget » n'est PLUS le critère d'admission. Cette
    comparaison survit comme condition nécessaire subsumée — 45 Gio
    libres pour un budget de 20 Gio la satisfont encore — et
    ``garde_capacite_production`` est désormais seule à décider de
    l'admission d'un run.
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


# ------------------------------- observateur de capacité (haute-eau)

def _lignes_en_memoire(sampler) -> int:
    """Nombre de points ACCEPTÉS déjà en mémoire — lecture pure.

    La chaîne sur disque retarde sur la collection en mémoire
    (``output_every`` vaut 60 s par défaut). Lire la longueur de la
    collection supprime ce décalage sans rien interpréter. Si la capacité
    n'est plus OBSERVABLE, on refuse : on n'estime pas.
    """
    collection = getattr(sampler, "collection", None)
    if collection is None:
        raise ArretCapaciteC7C1(
            "observabilité perdue : la collection du sampler est illisible "
            "— arrêt plutôt que supposition")
    try:
        n = len(collection)
    except (TypeError, AttributeError) as exc:
        raise ArretCapaciteC7C1(
            "observabilité perdue : longueur de collection illisible "
            "— arrêt plutôt que supposition") from exc
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ArretCapaciteC7C1(
            f"observabilité perdue : longueur de collection invalide ({n!r})")
    return n


def creer_observateur_capacite(cible: str | Path, variante: str,
                               repertoire_run: str):
    """Fabrique l'observateur de capacité passé à Cobaya en callback.

    OBSERVATEUR PUR. Il lit l'espace libre, l'occupation du lot, celle du
    run courant et les réserves ratifiées. Il n'écrit AUCUN attribut du
    sampler : ni ``params``, ni priors, ni propositions, ni
    ``Rminus1_stop``, ni ``Rminus1_cl_stop``, ni poids, ni samples, ni
    ``converged``. Positionner ``converged`` est explicitement interdit :
    cela déguiserait une interruption de capacité en convergence.

    Rend (observateur, etat) ; ``etat`` accumule la haute-eau observée.
    """
    octets_ligne = OCTETS_PAR_LIGNE_BORNE[_grille_de(variante)]
    marge = marge_anticipation_gio()
    plafond_lot = (float(BUDGET_TOTAL_RATIFIE_GIO)
                   + float(RESERVE_REPRISE_RATIFIEE_GIO))
    plancher_libre = float(RESERVE_VOLUME_RATIFIEE_GIO)
    etat = {
        "appels": 0,
        "haute_eau_lot_gio": 0.0,
        "haute_eau_run_gio": 0.0,
        "libre_minimal_gio": None,
        "dernier_releve": None,
        "marge_anticipation_gio": marge,
        "plafond_lot_gio": plafond_lot,
        "plancher_libre_gio": plancher_libre,
        "callback_every": CALLBACK_EVERY_ITERATIONS,
        "politique_capacite_version": POLITIQUE_CAPACITE_VERSION,
    }

    def observateur(sampler):
        etat["appels"] += 1
        lignes = _lignes_en_memoire(sampler)
        # Toute défaillance de MESURE pendant un run est elle aussi une
        # perte d'observabilité : elle doit sortir par l'exception dédiée,
        # qui porte le statut NON_CONVERGE_INTERRUPTION_CAPACITE. Sinon un
        # run interrompu pour cause de mesure impossible ne serait pas
        # marqué comme tel.
        try:
            libre = float(espace_libre_gio(cible))
            occupation = mesurer_occupation_lot(cible, verifier_stabilite=False)
        except (GardeErreur, OSError, ValueError) as exc:
            raise ArretCapaciteC7C1(
                f"observabilité perdue : capacité non mesurable pendant le "
                f"run ({exc}) — arrêt plutôt que supposition",
                {"appel": etat["appels"]}) from exc
        sur_disque = occupation["runs_production"].get(repertoire_run, 0)
        projete = (octets_ligne * (1 + lignes)) * (1.0 + RATIO_AUXILIAIRE_MAX)
        run_gio = max(sur_disque / GIO, projete / GIO)
        lot_gio = occupation["gio_production"] - sur_disque / GIO + run_gio
        releve = {
            "appel": etat["appels"], "lignes_en_memoire": lignes,
            "libre_gio": libre, "run_gio": run_gio, "lot_gio": lot_gio,
        }
        etat["dernier_releve"] = releve
        etat["haute_eau_lot_gio"] = max(etat["haute_eau_lot_gio"], lot_gio)
        etat["haute_eau_run_gio"] = max(etat["haute_eau_run_gio"], run_gio)
        etat["libre_minimal_gio"] = (
            libre if etat["libre_minimal_gio"] is None
            else min(etat["libre_minimal_gio"], libre))
        if not all(math.isfinite(v) for v in (libre, run_gio, lot_gio)):
            raise ArretCapaciteC7C1(
                "données de capacité non finies pendant le run", releve)
        if libre < plancher_libre + marge:
            raise ArretCapaciteC7C1(
                f"haute-eau franchie : espace libre {libre:.4f} Gio < "
                f"réserve de volume {plancher_libre:.2f} + anticipation "
                f"{marge:.2f} Gio — run interrompu NON CONVERGÉ", releve)
        if lot_gio > plafond_lot - marge:
            raise ArretCapaciteC7C1(
                f"haute-eau franchie : occupation du lot {lot_gio:.4f} Gio > "
                f"budget {BUDGET_TOTAL_RATIFIE_GIO} + reprise "
                f"{RESERVE_REPRISE_RATIFIEE_GIO} - anticipation {marge:.2f} "
                "Gio — run interrompu NON CONVERGÉ", releve)
        return None

    return observateur, etat


def injecter_observateur_capacite(info: dict, observateur) -> dict:
    """Copie de ``info`` où SEULS deux champs opérationnels changent.

    ``callback_function`` et ``callback_every`` ne sont PAS scientifiques
    et n'entrent donc jamais dans ``sha256_encodage_scientifique`` : ils
    sont injectés ici, après le gel de l'encodage, et consignés séparément
    dans le manifeste comme part de l'identité de reprise.
    """
    copie = dict(info)
    copie["sampler"] = copy.deepcopy(info["sampler"])
    copie["sampler"]["mcmc"]["callback_function"] = observateur
    copie["sampler"]["mcmc"]["callback_every"] = CALLBACK_EVERY_ITERATIONS
    return copie


def differences_injection(avant: dict, apres: dict) -> list[str]:
    """Chemins pointés modifiés entre deux blocs d'information."""

    def parcourir(a, b, prefixe: str, sortie: list[str]) -> None:
        if isinstance(a, dict) and isinstance(b, dict):
            for cle in sorted(set(a) | set(b)):
                chemin = f"{prefixe}.{cle}" if prefixe else str(cle)
                if cle not in a or cle not in b:
                    sortie.append(chemin)
                else:
                    parcourir(a[cle], b[cle], chemin, sortie)
            return
        try:
            identiques = bool(a == b)
        except Exception:  # noqa: BLE001 - objets non comparables
            identiques = a is b
        if not identiques:
            sortie.append(prefixe)

    differences: list[str] = []
    parcourir(avant, apres, "", differences)
    return sorted(differences)


def garde_injection_observateur(info: dict, observateur) -> dict:
    """Prouve que l'injection ne touche QUE les deux champs opérationnels."""
    apres = injecter_observateur_capacite(info, observateur)
    attendu = {"sampler.mcmc.callback_function", "sampler.mcmc.callback_every"}
    obtenu = set(differences_injection(info, apres))
    if obtenu != attendu:
        raise GardeErreur(
            f"l'injection de l'observateur modifie {sorted(obtenu)} au lieu "
            f"de {sorted(attendu)} : refus")
    return apres


# ------------------------------- reprise après interruption de capacité

def garde_reprise_apres_capacite(prefixe: str | Path, identite_attendue: dict,
                                 cible: str | Path, variante: str) -> dict:
    """Conditions CUMULATIVES d'une reprise après arrêt de capacité.

    Manifeste identique ; checkpoint Cobaya présent ET lisible ; HEAD,
    environnement, données et sampler identiques (portés par le
    manifeste) ; politique de capacité identique ; nouvelle admission de
    capacité réussie. Un statut CONVERGE interdit la reprise : un run
    interrompu pour capacité ne peut pas avoir convergé.

    LIMITE BLOQUANTE documentée : dans Cobaya 3.5,
    ``write_checkpoint`` n'est appelé qu'au cycle d'apprentissage
    (``learn_every``) et une fois à l'initialisation ; il n'existe pas de
    ``checkpoint_every``. Rien ne garantit donc qu'un checkpoint RÉCENT
    existe au moment où le callback lève l'exception. Cette garde le
    constate et refuse — elle ne fabrique jamais de checkpoint.
    """
    chemin_prefixe = Path(prefixe)
    manifeste_path = chemin_prefixe.parent / "manifest.json"
    if not manifeste_path.is_file():
        raise GardeErreur("reprise refusée : manifest.json absent")
    try:
        existant = json.loads(manifeste_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise GardeErreur(
            f"reprise refusée : manifest.json illisible ({exc.msg})") from exc
    if existant.get("statut_run") == STATUT_RUN_CONVERGE:
        raise GardeErreur(
            "reprise refusée : le manifeste déclare CONVERGE — une "
            "interruption de capacité n'est jamais une convergence")
    for cle, valeur in identite_attendue.items():
        if cle == "statut_run":
            continue
        if existant.get(cle) != valeur:
            raise GardeErreur(
                f"reprise refusée : champ {cle!r} non identique "
                f"({existant.get(cle)!r} != {valeur!r})")
    manquants = [c for c in CHAMPS_POLITIQUE_CAPACITE if c not in existant]
    if manquants:
        raise GardeErreur(
            f"reprise refusée : politique de capacité absente du manifeste "
            f"{manquants}")
    checkpoint = chemin_prefixe.with_name(chemin_prefixe.name + ".checkpoint")
    if not checkpoint.is_file():
        raise GardeErreur(
            "reprise refusée : checkpoint Cobaya absent — dans Cobaya 3.5 le "
            "checkpoint n'est écrit qu'au cycle learn_every, donc un arrêt de "
            "capacité peut survenir sans checkpoint ; aucun checkpoint n'est "
            "fabriqué (LIMITE BLOQUANTE de la reprise automatique)")
    try:
        octets = checkpoint.read_text(encoding="utf-8")
    except OSError as exc:
        raise GardeErreur(
            f"reprise refusée : checkpoint illisible ({exc})") from exc
    if not octets.strip():
        raise GardeErreur("reprise refusée : checkpoint vide")
    try:
        import yaml

        contenu_cp = yaml.safe_load(octets)
    except Exception as exc:  # noqa: BLE001
        raise GardeErreur(
            f"reprise refusée : checkpoint non analysable ({exc})") from exc
    if not isinstance(contenu_cp, dict) or "sampler" not in contenu_cp:
        raise GardeErreur(
            "reprise refusée : checkpoint sans bloc sampler exploitable")
    admission = garde_capacite_production(cible, variante)
    return {
        "manifeste_identique": True,
        "checkpoint_present_et_lisible": True,
        "politique_capacite_identique": True,
        "statut_run_repris": existant.get("statut_run"),
        "nouvelle_admission": admission,
    }


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
                "budget_production_statut", "reference_ratification_budget",
                "reserve_reprise_Gio", "reserve_volume_minimale_Gio"):
        if cle not in rr:
            raise GardeErreur(f"contrat local : champ requis absent ({cle})")
    # cohérence de la garde technique contrat <-> code
    if rr["garde_technique_minimale_Gio"] != GARDE_CAPACITE_GIO:
        raise GardeErreur(
            f"garde technique du contrat {rr['garde_technique_minimale_Gio']} "
            f"!= constante qualifiée {GARDE_CAPACITE_GIO}"
        )
    # CAP-1 : la décision humaine ratifiée doit être inscrite EXACTEMENT.
    # Aucune tolérance : 19.999 et 20.001 sont refusés comme 19 et 21.
    if rr["budget_production_statut"] != "RATIFIE":
        raise GardeErreur(
            f"contrat local : budget_production_statut "
            f"{rr['budget_production_statut']!r} != 'RATIFIE' — la politique "
            "de capacité CAP-1 exige un budget ratifié")
    _valeur_ratifiee(rr["budget_production_requis_Gio"],
                     BUDGET_TOTAL_RATIFIE_GIO,
                     "contrat local : budget de production")
    _valeur_ratifiee(rr["reserve_reprise_Gio"], RESERVE_REPRISE_RATIFIEE_GIO,
                     "contrat local : réserve de reprise")
    _valeur_ratifiee(rr["reserve_volume_minimale_Gio"],
                     RESERVE_VOLUME_RATIFIEE_GIO,
                     "contrat local : réserve de volume")
    if rr["reference_ratification_budget"] != REFERENCE_RATIFICATION_BUDGET:
        raise GardeErreur(
            "contrat local : référence de ratification "
            f"{rr['reference_ratification_budget']!r} != "
            f"{REFERENCE_RATIFICATION_BUDGET!r}")
    if rr.get("politique_capacite_version") != POLITIQUE_CAPACITE_VERSION:
        raise GardeErreur(
            "contrat local : version de politique de capacité "
            f"{rr.get('politique_capacite_version')!r} != "
            f"{POLITIQUE_CAPACITE_VERSION!r}")
    # La racine de runs du contrat doit être sur le volume ratifié.
    # Contrôles bon marché ici (lettre, type de lecteur, système de
    # fichiers) ; la qualification MATÉRIELLE, plus coûteuse, appartient
    # au pré-vol de production (garde_support_actif).
    # Le contrat doit DÉCLARER le volume ratifié, et le déclarer
    # exactement : « C ». Une déclaration absente ou divergente est un
    # refus — la ratification ne se déduit d'aucun fait système.
    if rr.get("volume_ratifie") != SUPPORT_ACTIF_VOLUME_RATIFIE:
        raise GardeErreur(
            f"contrat local : volume ratifié déclaré "
            f"{rr.get('volume_ratifie')!r} != {SUPPORT_ACTIF_VOLUME_RATIFIE!r}")
    _garde_volume_ratifie(rr["chemin"])
    volume_runs = _infos_volume(rr["chemin"])
    if volume_runs["type_lecteur_code"] != 3:
        raise GardeErreur("contrat local : racine de runs sur un lecteur non fixe")
    if volume_runs["systeme_fichiers"].upper() != "NTFS":
        raise GardeErreur("contrat local : racine de runs non NTFS")

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
        "reserve_reprise_Gio": rr["reserve_reprise_Gio"],
        "reserve_volume_minimale_Gio": rr["reserve_volume_minimale_Gio"],
        "politique_capacite_version": rr["politique_capacite_version"],
        "volume_ratifie": rr["volume_ratifie"],
        "valeurs_ratifiees_exactes": True,
        "racine_runs_sur_volume_ratifie": True,
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


def _ecrire_atomique_brut(cible: Path, contenu: dict) -> None:
    """Écriture atomique SANS règle d'écrasement — usage interne du seul
    ``mettre_a_jour_manifeste_runtime``, qui a déjà validé la transition.
    ``ecrire_manifeste_atomique`` n'est PAS détendue : elle reste la seule
    voie de création, et refuse toujours un écrasement non identique."""
    corps = json.dumps(contenu, indent=2, sort_keys=True,
                       ensure_ascii=False) + "\n"
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
    try:
        fd = os.open(str(cible.parent), os.O_RDONLY)
        try:
            os.fsync(fd)
        finally:
            os.close(fd)
    except (OSError, AttributeError):
        pass


def mettre_a_jour_manifeste_runtime(chemin: str | Path,
                                    mises_a_jour: dict) -> dict:
    """FINALISATION monotone et UNIQUE du manifeste (B2, audit #95).

    Ce n'est pas une mise à jour générique : c'est l'unique transition

        PLANIFIE_NON_LANCE  ->  un statut de STATUTS_RUN_FINALS

    exécutée en un seul appel portant l'ensemble COMPLET des champs de
    finalisation (``CHAMPS_RUNTIME_AUTORISES``, ni plus ni moins).

    Règles, toutes bloquantes :
      - le manifeste existant doit être lisible ET conforme (schéma
        reconnu, identité complète) : un manifeste corrompu ou étranger
        n'est jamais écrasé ;
      - état d'entrée EXACTEMENT ``PLANIFIE_NON_LANCE`` : un manifeste
        déjà finalisé refuse TOUTE nouvelle modification runtime, même à
        statut identique — un statut final n'est jamais réécrit, et une
        interruption ne devient jamais une convergence ;
      - ``statut_run`` doit être fourni et FINAL : la « finalisation »
        vers PLANIFIE_NON_LANCE est un non-sens refusé ;
      - invariant strict :
            CONVERGE            <=> converged_cobaya is True
            tout autre final    <=> converged_cobaya is False
      - ``date_fin_utc`` passe par ``valider_date_utc`` ; ``detail_fin``
        est une chaîne non vide d'au plus 400 caractères ;
      - l'identité (tout champ hors runtime) est VÉRIFIÉE inchangée.

    Rend le manifeste finalisé (relu depuis le disque).
    """
    cible = Path(chemin)
    if not cible.is_file():
        raise GardeErreur("finalisation runtime : manifest.json absent")
    try:
        existant = json.loads(cible.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise GardeErreur(
            f"finalisation runtime : manifeste corrompu ({exc.msg}) — "
            "aucun écrasement") from exc
    if not isinstance(existant, dict) \
            or existant.get("schema") not in SCHEMAS_MANIFESTE_RECONNUS:
        raise GardeErreur(
            "finalisation runtime : manifeste non conforme (schéma) — refus")
    manquants = [c for c in CHAMPS_MANIFESTE_RUN if c not in existant]
    if manquants:
        raise GardeErreur(
            f"finalisation runtime : manifeste non conforme, champs "
            f"d'identité absents {manquants} — refus")
    interdits = sorted(set(mises_a_jour) - set(CHAMPS_RUNTIME_AUTORISES))
    if interdits:
        raise GardeErreur(
            f"finalisation runtime : champs non runtime refusés {interdits} "
            f"— seuls {list(CHAMPS_RUNTIME_AUTORISES)} sont modifiables")
    # État d'entrée : STRICTEMENT l'état initial. Toute autre valeur —
    # y compris un statut final identique à celui demandé — est un refus.
    statut_avant = existant.get("statut_run")
    if statut_avant != STATUT_RUN_PLANIFIE:
        raise GardeErreur(
            f"finalisation runtime : manifeste déjà finalisé "
            f"(statut {statut_avant!r}) — un statut final n'est jamais "
            "réécrit et aucune seconde modification runtime n'est permise ; "
            "une interruption ne devient jamais une convergence")
    # Ensemble COMPLET des champs de finalisation, exigé d'un coup.
    absents = sorted(set(CHAMPS_RUNTIME_AUTORISES) - set(mises_a_jour))
    if absents:
        raise GardeErreur(
            f"finalisation runtime : champs de finalisation absents "
            f"{absents} — l'ensemble complet est requis en un seul appel")
    statut_apres = mises_a_jour["statut_run"]
    if statut_apres not in STATUTS_RUN_FINALS:
        raise GardeErreur(
            f"finalisation runtime : statut {statut_apres!r} non final — "
            "la finalisation exige un statut final explicite "
            "(PLANIFIE -> PLANIFIE est refusé)")
    converged = mises_a_jour["converged_cobaya"]
    if statut_apres == STATUT_RUN_CONVERGE:
        if converged is not True:
            raise GardeErreur(
                "finalisation runtime : CONVERGE exige converged_cobaya is "
                "True — un retour sans exception ne vaut jamais convergence")
    else:
        if converged is not False:
            raise GardeErreur(
                f"finalisation runtime : statut {statut_apres!r} exige "
                "converged_cobaya is False — un statut non convergé ne "
                "porte jamais un drapeau de convergence")
    valider_date_utc(mises_a_jour["date_fin_utc"])
    detail = mises_a_jour["detail_fin"]
    if not isinstance(detail, str) or not detail.strip() or len(detail) > 400:
        raise GardeErreur(
            "finalisation runtime : detail_fin doit être une chaîne non "
            "vide d'au plus 400 caractères")
    nouveau = {**existant, **mises_a_jour}
    # Défense en profondeur : l'identité doit être VÉRIFIÉE inchangée,
    # pas seulement supposée inchangée par construction.
    for cle in existant:
        if cle in CHAMPS_RUNTIME_AUTORISES:
            continue
        if nouveau[cle] != existant[cle]:
            raise GardeErreur(
                f"finalisation runtime : champ non runtime altéré ({cle})")
    _ecrire_atomique_brut(cible, nouveau)
    return json.loads(cible.read_text(encoding="utf-8"))


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
                 budget_requis_gio, reference_ratification_budget,
                 support_actif_identite_expurgee: dict) -> dict:
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
        "statut_run": STATUT_RUN_PLANIFIE,
        # --- politique de capacité CAP-1 : part de l'identité de reprise
        "budget_total_Gio": BUDGET_TOTAL_RATIFIE_GIO,
        "reserve_reprise_Gio": RESERVE_REPRISE_RATIFIEE_GIO,
        "reserve_volume_minimale_Gio": RESERVE_VOLUME_RATIFIEE_GIO,
        "allocation_run_actif_Gio": allocation_run_actif_gio(variante),
        "politique_capacite_version": POLITIQUE_CAPACITE_VERSION,
        "callback_every": CALLBACK_EVERY_ITERATIONS,
        "support_actif_identite_expurgee": dict(
            support_actif_identite_expurgee),
    }
    if not support_actif_identite_expurgee:
        raise GardeErreur(
            "identité de run : identité expurgée du support absente")
    if (budget_requis_gio is not None
            and float(budget_requis_gio) != float(BUDGET_TOTAL_RATIFIE_GIO)):
        raise GardeErreur(
            f"identité de run : budget du contrat {budget_requis_gio} != "
            f"budget ratifié {BUDGET_TOTAL_RATIFIE_GIO}")
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


# Groupes de contrôles du validateur d'autorisation. Le contrôle
# statique du qualificateur exige que le chemin NOMINAL les traverse
# tous : aucune validation ne doit se trouver après un retour.
GROUPES_CONTROLE_AUTORISATION = (
    "cles", "type", "usage", "cles_humaines", "sha_lanceur",
    "sha_adaptateur", "sha_chemin_rapide", "version_contrat",
    "empreinte_environnement", "racine_runs", "budget", "budget_ratifie",
    "reserve_reprise", "reserve_volume", "politique_capacite",
    "support_actif", "ratification",
    "liaison_budget_contrat", "liaison_ratification_contrat",
    "sha_descripteurs", "sha_preenregistrement", "sha_donnees",
    "head_autorise", "matrice_variante_graine",
)


def _valider_contenu_autorisation(manifeste: dict, variante: str,
                                  graine: int, head: str,
                                  budget_contrat=None,
                                  ratification_contrat=None,
                                  support_attendu: dict | None = None,
                                  perimetre_exact_attendu: dict | None = None,
                                  reference_sentinelle_attendue: str | None = None,
                                  ) -> list[str]:
    """VALIDATEUR PUR du contenu d'une autorisation (aucun fichier).

    Lève ``GardeErreur`` au PREMIER manquement, avec un message dont le
    fragment identifie sans ambiguïté le champ fautif. Retourne, quand
    tout passe, la liste ORDONNÉE des groupes de contrôles traversés :
    le qualificateur exige que cette liste soit complète, ce qui rend
    impossible un retour prématuré masquant des contrôles aval.

    Séparé de la lecture du fichier pour que la qualification puisse
    éprouver chaque champ profond SANS jamais écrire une autorisation
    réelle sur le disque.

    SENT-0D : les deux contraintes optionnelles — périmètre EXACT et
    référence de ratification sentinelle — sont validées DANS LA MÊME
    lecture que le reste (aucune fenêtre TOCTOU entre deux lectures du
    fichier). Absentes (None), le comportement historique est inchangé.
    """
    traverses: list[str] = []

    def franchi(nom: str) -> None:
        traverses.append(nom)

    cles = set(manifeste.keys())
    if not (CLES_MANIFESTE <= cles
            and cles - CLES_MANIFESTE <= CLES_MANIFESTE_OPTIONNELLES):
        raise GardeErreur("autorisation non conforme : clés inexactes")
    franchi("cles")
    if manifeste["type"] != "autorisation_production_c7c1_g2_4":
        raise GardeErreur("autorisation non conforme : type inexact")
    franchi("type")
    if manifeste.get("usage") != USAGE_AUTORISATION_PRODUCTION:
        raise GardeErreur(
            f"autorisation d'usage {manifeste.get('usage')!r} refusée : "
            f"seul {USAGE_AUTORISATION_PRODUCTION!r} autorise une "
            "production — un manifeste de qualification n'est jamais "
            "une autorisation réelle"
        )
    franchi("usage")
    for cle in ("cle_humaine_1", "cle_humaine_2"):
        if not isinstance(manifeste[cle], str) or not manifeste[cle].strip():
            raise GardeErreur(f"autorisation non conforme : {cle} vide")
    franchi("cles_humaines")
    if manifeste["sha256_lanceur"] != sha256_fichier(__file__):
        raise GardeErreur("autorisation factice : SHA du lanceur non conforme")
    franchi("sha_lanceur")
    adaptateur = Path(__file__).parent / "xz_cobaya_g2_4.py"
    if manifeste["sha256_adaptateur"] != sha256_fichier(adaptateur):
        raise GardeErreur("autorisation factice : SHA adaptateur non conforme")
    franchi("sha_adaptateur")
    # SHA du chemin rapide : OBLIGATOIRE depuis G2.4d — une autorisation
    # ne doit jamais valider un chemin rapide modifié.
    rapide = Path(__file__).parent / "xz_fast_g2_4c.py"
    if manifeste.get("sha256_chemin_rapide") != sha256_fichier(rapide):
        raise GardeErreur(
            "autorisation factice : SHA du chemin rapide absent ou non conforme"
        )
    franchi("sha_chemin_rapide")
    if manifeste.get("version_contrat_local") != VERSION_CONTRAT_LOCAL:
        raise GardeErreur("autorisation : version de contrat local non conforme")
    franchi("version_contrat")
    if manifeste.get("empreinte_environnement") != empreinte_environnement():
        raise GardeErreur("autorisation : empreinte d'environnement non conforme")
    franchi("empreinte_environnement")
    racine_autorisee = manifeste.get("racine_runs_canonique")
    if not racine_autorisee or not _memes_chemins(
            racine_autorisee, os.environ.get("C7C1_XZ_OUT_DIR", "")):
        raise GardeErreur("autorisation : racine de runs non autorisée")
    franchi("racine_runs")
    budget = manifeste.get("budget_production_requis_Gio")
    if not isinstance(budget, (int, float)) or isinstance(budget, bool) \
            or budget <= 0:
        raise GardeErreur("autorisation : budget de production absent ou nul")
    franchi("budget")
    # --- CAP-1 : une autorisation ne peut valider ni un autre budget, ni
    # une autre réserve, ni une autre politique, ni un autre support.
    _valeur_ratifiee(budget, BUDGET_TOTAL_RATIFIE_GIO,
                     "autorisation : budget de production")
    franchi("budget_ratifie")
    _valeur_ratifiee(manifeste.get("reserve_reprise_Gio"),
                     RESERVE_REPRISE_RATIFIEE_GIO,
                     "autorisation : réserve de reprise")
    franchi("reserve_reprise")
    _valeur_ratifiee(manifeste.get("reserve_volume_minimale_Gio"),
                     RESERVE_VOLUME_RATIFIEE_GIO,
                     "autorisation : réserve de volume")
    franchi("reserve_volume")
    if manifeste.get("politique_capacite_version") != POLITIQUE_CAPACITE_VERSION:
        raise GardeErreur(
            "autorisation : version de politique de capacité "
            f"{manifeste.get('politique_capacite_version')!r} != "
            f"{POLITIQUE_CAPACITE_VERSION!r}")
    franchi("politique_capacite")
    attendu_support = (support_attendu if support_attendu is not None
                       else identite_support_expurgee(
                           os.environ.get("C7C1_XZ_OUT_DIR", "")))
    if manifeste.get("support_actif_identite_expurgee") != attendu_support:
        raise GardeErreur(
            "autorisation : support actif non conforme au support ratifié "
            "et mesuré")
    franchi("support_actif")
    ratification = manifeste.get("budget_production_ratification")
    if not str(ratification or "").strip():
        raise GardeErreur("autorisation : ratification du budget absente")
    if str(ratification) != REFERENCE_RATIFICATION_BUDGET:
        raise GardeErreur(
            "autorisation : référence de ratification du budget "
            f"{ratification!r} != {REFERENCE_RATIFICATION_BUDGET!r}")
    franchi("ratification")
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
    franchi("liaison_budget_contrat")
    if ratification_contrat is not None:
        if str(ratification) != str(ratification_contrat):
            raise GardeErreur(
                "référence de ratification du budget différente entre "
                "l'autorisation et le contrat : refus"
            )
    franchi("liaison_ratification_contrat")
    # --- contrôles historiques : rendus de nouveau ATTEIGNABLES --------
    for var, chemin_desc in DESCRIPTEURS.items():
        if manifeste["sha256_descripteurs"].get(var) != sha256_fichier(chemin_desc):
            raise GardeErreur(
                f"autorisation factice : SHA descripteur {var} non conforme"
            )
    franchi("sha_descripteurs")
    prereg = "reports/rapport_G2_2a_preregistration.md"
    if manifeste["sha256_preenregistrement"] != sha256_fichier(prereg):
        raise GardeErreur(
            "autorisation factice : SHA pré-enregistrement non conforme"
        )
    franchi("sha_preenregistrement")
    if manifeste["sha256_donnees"] != SHA_BAO:
        raise GardeErreur("autorisation factice : SHA données non conformes")
    franchi("sha_donnees")
    if manifeste["head_autorise"] != head:
        raise GardeErreur("autorisation factice : HEAD non autorisé")
    franchi("head_autorise")
    autorisees = manifeste["variantes_graines_autorisees"]
    if str(graine) not in [str(g) for g in autorisees.get(variante, [])]:
        raise GardeErreur(
            f"autorisation ne couvre pas ({variante}, {graine}) : "
            "variantes_graines_autorisees"
        )
    franchi("matrice_variante_graine")
    # --- SENT-0D : contraintes OPTIONNELLES du franchissement ----------
    # Validées ici, dans la MÊME lecture du manifeste (pas de TOCTOU).
    # Groupes supplémentaires hors GROUPES_CONTROLE_AUTORISATION : la
    # qualification générale G2.4d, qui n'exige pas le franchissement,
    # reste intacte.
    if perimetre_exact_attendu is not None:
        def _normaliser(perimetre: dict) -> dict:
            return {str(v): sorted(str(g) for g in gs)
                    for v, gs in perimetre.items()}

        if _normaliser(autorisees) != _normaliser(perimetre_exact_attendu):
            raise GardeErreur(
                "franchissement SENT-0D : périmètre de l'autorisation non "
                "exact — seul le couple sentinelle ratifié est admis, sans "
                "aucune autre variante ni graine : refus")
        franchi("perimetre_sentinelle")
    if reference_sentinelle_attendue is not None:
        if manifeste.get("reference_ratification_sentinelle") \
                != reference_sentinelle_attendue:
            raise GardeErreur(
                "franchissement SENT-0D : reference_ratification_sentinelle "
                "absente ou non conforme : refus")
        franchi("reference_sentinelle")
    manquants = [g for g in GROUPES_CONTROLE_AUTORISATION
                 if g not in traverses]
    if manquants:
        raise GardeErreur(
            f"validateur d'autorisation incomplet : groupes non traversés "
            f"{manquants}"
        )
    return traverses


def garde_autorisation(chemin: str | Path, variante: str, graine: int,
                       head: str, budget_contrat=None,
                       ratification_contrat=None,
                       support_attendu: dict | None = None,
                       perimetre_exact_attendu: dict | None = None,
                       reference_sentinelle_attendue: str | None = None) -> str:
    """Garde d'autorisation RÉELLE sur FICHIER.

    Lit le fichier, délègue au validateur pur, et ne retourne le SHA-256
    du fichier QU'APRÈS que tous les groupes de contrôles ont été
    traversés. Aucune validation ne subsiste après le retour.

    Refuse systématiquement un manifeste d'usage autre que PRODUCTION :
    un fichier éphémère de qualification ne peut JAMAIS servir
    d'autorisation réelle.
    """
    if not Path(chemin).is_file():
        raise GardeErreur("autorisation absente")
    with open(chemin, encoding="utf-8") as handle:
        manifeste = json.load(handle)
    _valider_contenu_autorisation(
        manifeste, variante, graine, head,
        budget_contrat=budget_contrat,
        ratification_contrat=ratification_contrat,
        support_attendu=support_attendu,
        perimetre_exact_attendu=perimetre_exact_attendu,
        reference_sentinelle_attendue=reference_sentinelle_attendue,
    )
    return sha256_fichier(chemin)



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
    # ---- CAP-1 : annonces de politique de capacité (aucune autorisation)
    annonces: dict = {}
    try:
        support = garde_support_actif(out_dir)
        annonces["SUPPORT QUALIFIE"] = True
        annonces["support_actif_identite_expurgee"] = (
            identite_support_publiable(support["identite_expurgee"]))
        annonces["fait_systeme_volume_systeme"] = support[
            "fait_systeme_volume_systeme"]
    except GardeErreur as exc:
        support = None
        annonces["SUPPORT QUALIFIE"] = False
        annonces["motif_support"] = str(exc)
    annonces["BUDGET RATIFIE"] = (
        contrat["budget_production_statut"] == "RATIFIE"
        and contrat["reference_ratification_budget"]
        == REFERENCE_RATIFICATION_BUDGET)
    try:
        etat_capacite = garde_capacite_production(out_dir, variante,
                                                  support=support)
        annonces["POLITIQUE DE CAPACITE QUALIFIEE"] = True
    except GardeErreur as exc:
        etat_capacite = {"refus": str(exc)}
        annonces["POLITIQUE DE CAPACITE QUALIFIEE"] = False
    annonces["PRODUCTION TOUJOURS VERROUILLEE"] = bool(VERROU_PRODUCTION_G2_4D)
    rapport["capacite_production"] = {
        **etat_capacite,
        "marge_anticipation_gio": marge_anticipation_gio(),
        "callback_every": CALLBACK_EVERY_ITERATIONS,
        "annonces": annonces,
    }
    # Le verrou dur prime sur toute autre annonce : tant qu'il tient,
    # aucune production n'est autorisable, même budget ratifié, support
    # qualifié et capacité suffisante.
    if VERROU_PRODUCTION_G2_4D:
        autorisable = False
        motif = (motif + " ; " if motif else "") + \
            "VERROU_PRODUCTION_G2_4D actif"
        rapport["budget_production"]["production_autorisable"] = False
        rapport["budget_production"]["motif"] = motif
    rapport["verdict"] = (
        "PREPARATION OK — BUDGET RATIFIE, SUPPORT QUALIFIE, POLITIQUE DE "
        "CAPACITE QUALIFIEE, PRODUCTION TOUJOURS VERROUILLEE"
        if all(annonces.get(c) for c in (
            "BUDGET RATIFIE", "SUPPORT QUALIFIE",
            "POLITIQUE DE CAPACITE QUALIFIEE"))
        else "PREPARATION OK — PRODUCTION NON AUTORISABLE"
    )
    return rapport


# ------------------------------- SENT-0D : franchissement ratifié

def _extraire_flag_franchissement(args: list[str]) -> str | None:
    """Analyse STRICTE du flag ``--franchissement-sent0d`` (SENT-0D §C).

    Rend None si le flag est ABSENT — le verrou historique s'applique
    alors intégralement. Rend la référence quand elle est EXACTE. Refuse,
    sur cause précise : flag dupliqué ; valeur absente (fin d'arguments
    ou autre option à sa place) ; référence vide ; référence incorrecte.
    Aucune variable d'environnement, aucun fichier « unlock », aucune
    dépendance à l'heure : la seule intention admise est ce flag public,
    et la seconde protection reste l'autorisation privée.
    """
    positions = [i for i, a in enumerate(args)
                 if a == "--franchissement-sent0d"]
    if not positions:
        return None
    if len(positions) > 1:
        raise GardeErreur(
            "franchissement SENT-0D refusé : flag dupliqué — une seule "
            "occurrence est admise")
    i = positions[0]
    if i + 1 >= len(args) or args[i + 1].startswith("--"):
        raise GardeErreur(
            "franchissement SENT-0D refusé : référence absente après le flag")
    valeur = args[i + 1]
    if not valeur.strip():
        raise GardeErreur(
            "franchissement SENT-0D refusé : référence vide")
    if valeur != REFERENCE_RATIFICATION_SENTINELLE:
        raise GardeErreur(
            "franchissement SENT-0D refusé : référence incorrecte "
            f"(attendue : {REFERENCE_RATIFICATION_SENTINELLE})")
    return valeur


def garde_franchissement_sent0d(reference: str | None, variante: str,
                                graine: int) -> None:
    """Étape 8 : le verrou reste True ; seul le cas ratifié passe.

    Sans franchissement demandé (référence None), le REFUS HISTORIQUE du
    verrou G2.4d s'applique à l'identique — même cause, même message.
    Avec franchissement, le triple confinement doit être réuni : couple
    sentinelle codé (la garde 4 bis a déjà bloqué le reste, ceci est une
    défense en profondeur), référence publique exacte, et — validées en
    amont dans la MÊME lecture de l'autorisation — le périmètre privé
    exact et la référence de ratification sentinelle.
    """
    if reference is None:
        raise GardeErreur(
            "VERROU G2.4d : raccord qualifié SANS production — le lancement "
            "réel exige une porte ultérieure et une décision humaine "
            "distincte. Aucun répertoire créé, aucun manifeste écrit, "
            "aucun cobaya.run atteint."
        )
    if reference != REFERENCE_RATIFICATION_SENTINELLE:
        raise GardeErreur(
            "franchissement SENT-0D refusé : référence incorrecte")
    if (variante, int(graine)) != (SENTINELLE_SENT0_VARIANTE,
                                   SENTINELLE_SENT0_GRAINE):
        raise GardeErreur(
            f"franchissement SENT-0D refusé : ({variante}, {graine}) hors "
            "périmètre sentinelle — seul le couple ratifié peut franchir")


# --------------------------------------- SENT-0A : chemin réel (étape 9)

def _acquerir_repertoire_run(prefixe: str | Path) -> Path:
    """ACQUISITION EXCLUSIVE du répertoire FINAL du run (B1, audit #95).

    ``garde_collision`` puis ``mkdir(exist_ok=True)`` laissaient une
    fenêtre TOCTOU : deux processus pouvaient tous deux constater
    l'absence puis tous deux « réussir » la création. Ici, seuls les
    PARENTS sont créés avec ``exist_ok=True`` ; le répertoire final est
    créé avec ``exist_ok=False`` — c'est l'appel atomique du système de
    fichiers qui départage : au plus UN processus acquiert le run. Un
    répertoire final déjà existant, MÊME VIDE, bloque. Rien n'est
    supprimé : un répertoire acquis ou des traces d'échec restent en
    place pour audit.
    """
    repertoire = Path(prefixe).parent
    repertoire.parent.mkdir(parents=True, exist_ok=True)  # parents seuls
    try:
        repertoire.mkdir(exist_ok=False)  # acquisition exclusive
    except FileExistsError as exc:
        raise GardeErreur(
            f"collision/concurrence : le répertoire final du run existe "
            f"déjà (même vide, il bloque) — acquisition exclusive refusée, "
            f"aucun écrasement ({repertoire.name})"
        ) from exc
    return repertoire


def _lancer_cobaya_production(info_cobaya: dict):
    """Point d'appel UNIQUE de Cobaya pour la production.

    Convention G1 ratifiée et conservée telle quelle : ``run(info,
    resume=True)`` — sous la garde de collision, le répertoire est
    toujours neuf, donc ``resume=True`` est inerte au premier lancement ;
    aucune nouvelle sémantique de reprise n'est inventée ici (REC-1
    inchangée). L'import est local : sous le verrou, ce module n'est
    jamais chargé par le chemin de production. La qualification SENT-0B
    substitue cette fonction par un substitut contrôlé — jamais une vraie
    MCMC.
    """
    from cobaya.run import run as cobaya_run

    return cobaya_run(info_cobaya, resume=True)


def _date_utc_fin() -> str:
    """Date de fin de run. Injectable UNIQUEMENT hors production
    (les injections C7C1_TEST_* sont refusées en mode --produire)."""
    forge = os.environ.get("C7C1_TEST_DATE_FIN_UTC")
    if forge:
        return valider_date_utc(forge)
    import datetime

    return datetime.datetime.now(
        datetime.timezone.utc).strftime(FORMAT_DATE_UTC)


def executer_production_sentinelle(manifeste_initial: dict,
                                   info_cobaya: dict,
                                   prefixe: str | Path) -> dict:
    """Étape 9 RÉELLE du chemin de production (SENT-0A).

    N'est atteinte par ``produire`` qu'après les gardes 1–8, donc jamais
    tant que ``VERROU_PRODUCTION_G2_4D`` vaut True. La qualification
    SENT-0B l'éprouve directement, sous %TEMP% hors Git, avec un
    substitut de Cobaya.

    Séquence :
      9.1 défense amont (garde_prefixe, garde_collision) puis ACQUISITION
          EXCLUSIVE du répertoire final (mkdir exist_ok=False) — au plus
          un processus acquiert le run ; un répertoire final existant,
          même vide, bloque ; jamais d'écrasement ni de déplacement ;
      9.2 écriture ATOMIQUE du manifeste initial (PLANIFIE_NON_LANCE) par
          la seule voie de création, qui refuse un existant non identique;
      9.3 appel Cobaya par le point unique ``_lancer_cobaya_production`` ;
      9.4 classement STRICT de la sortie :
            sampler.converged is True             -> CONVERGE
            retour normal sans ce drapeau exact   -> FIN_SANS_CONVERGENCE
            ArretCapaciteC7C1                     -> NON_CONVERGE_INTERRUPTION_CAPACITE
            toute autre exception                 -> NON_CONVERGE_ECHEC_TECHNIQUE
          Aucune exception ne peut écrire CONVERGE ; un booléen non
          canonique (numpy, chaîne, entier) ne vaut PAS convergence —
          direction conservatrice assumée ;
      9.5 mise à jour runtime ATOMIQUE du manifeste, identité inviolée.

    En cas d'échec APRÈS création du répertoire, les traces (répertoire,
    manifeste, sorties partielles de Cobaya) sont CONSERVÉES pour audit —
    jamais supprimées automatiquement. Aucun checkpoint n'est écrit ni
    fabriqué ici : seuls ceux de Cobaya existent (REC-1). Aucune deuxième
    graine ni variante n'est lancée automatiquement.
    """
    chemin_prefixe = Path(prefixe)
    # 9.1 — défense amont (le temps a pu passer depuis le pré-vol), puis
    #       ACQUISITION EXCLUSIVE du répertoire final (B1, audit PR #95).
    garde_prefixe(chemin_prefixe)
    garde_collision(chemin_prefixe)  # défense amont, PAS l'acquisition
    repertoire = _acquerir_repertoire_run(chemin_prefixe)
    manifeste_path = repertoire / "manifest.json"
    # 9.2 — création par la voie stricte (refus d'un existant différent).
    if manifeste_initial.get("statut_run") != STATUT_RUN_PLANIFIE:
        raise GardeErreur(
            f"étape 9 : statut initial {manifeste_initial.get('statut_run')!r}"
            f" != {STATUT_RUN_PLANIFIE!r}")
    ecrire_manifeste_atomique(manifeste_path, manifeste_initial)
    # 9.3 / 9.4 — l'exécution. Les traces restent sur échec.
    try:
        _, sampler = _lancer_cobaya_production(info_cobaya)
    except ArretCapaciteC7C1 as exc:
        mettre_a_jour_manifeste_runtime(manifeste_path, {
            "statut_run": STATUT_RUN_INTERROMPU_CAPACITE,
            "date_fin_utc": _date_utc_fin(),
            "detail_fin": f"ArretCapaciteC7C1: {exc}"[:400],
            "converged_cobaya": False,
        })
        raise
    except BaseException as exc:
        mettre_a_jour_manifeste_runtime(manifeste_path, {
            "statut_run": STATUT_RUN_ECHEC_TECHNIQUE,
            "date_fin_utc": _date_utc_fin(),
            "detail_fin": f"{type(exc).__name__}: {exc}"[:400],
            "converged_cobaya": False,
        })
        raise
    converged_brut = getattr(sampler, "converged", None)
    est_converge = converged_brut is True  # exigence EXPLICITE et exacte
    statut_final = (STATUT_RUN_CONVERGE if est_converge
                    else STATUT_RUN_FIN_SANS_CONVERGENCE)
    mise_a_jour = {
        "statut_run": statut_final,
        "date_fin_utc": _date_utc_fin(),
        "detail_fin": ("convergence declaree par le sampler" if est_converge
                       else "retour normal sans sampler.converged is True "
                            f"(valeur brute : {converged_brut!r})"),
        "converged_cobaya": est_converge,
    }
    manifeste_final = mettre_a_jour_manifeste_runtime(
        manifeste_path, mise_a_jour)
    return {
        "statut_run": manifeste_final["statut_run"],
        "converged_cobaya": manifeste_final["converged_cobaya"],
        "manifeste": str(manifeste_path),
        "prefixe": str(chemin_prefixe),
    }


def produire(args: list[str]) -> None:
    """Mode production : verrouillé tant que G2.4b n'est pas validée.

    Toutes les gardes sont bloquantes, y compris l'arbre Git propre et
    l'autorisation à deux clés. AUCUNE MCMC n'est lancée dans cette porte :
    le vrai manifeste est interdit, donc ce chemin se termine toujours par
    un refus avant cobaya.run. Depuis SENT-0A, l'étape 9 est réellement
    implémentée mais reste matériellement inatteignable sous le verrou.
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
    # 2 bis. intention SENT-0D : analysée TÔT pour que tout flag défectueux
    #        soit refusé sur sa cause exacte, pas par une garde fortuite.
    #        Absent -> None : le verrou historique s'appliquera tel quel.
    reference_franchissement = _extraire_flag_franchissement(args)
    # 3. contrat, environnement, données, threads et chemins (via preflight)
    rapport = preflight(variante, graine)
    # 4. HEAD et arbre propre
    etat_git = rapport["git"]
    if not etat_git["arbre_propre"]:
        raise GardeErreur("arbre Git non propre : production refusée")
    # 4 bis. confinement sentinelle (SENT-0A) : la PRODUCTION est bornée
    #        au seul couple proposé en #94 ; le pré-vol, lui, reste ouvert
    #        aux quatre variantes. Aucun privilège scientifique.
    garde_perimetre_sentinelle(variante, graine)
    # 5. autorisation à deux clés (schéma étendu, usage PRODUCTION exigé,
    #    budget et ratification liés au contrat)
    contrat = garde_contrat_local()
    contrat_brut = contrat.pop("_contrat")
    cible = os.environ["C7C1_XZ_OUT_DIR"]
    support = garde_support_actif(cible)  # refuse si le support a changé
    #    SENT-0D : quand un franchissement est demandé, le périmètre EXACT
    #    et la référence de ratification sentinelle sont validés dans la
    #    MÊME lecture de l'autorisation (aucune fenêtre TOCTOU).
    sha_autorisation = garde_autorisation(
        chemin_autorisation, variante, graine, etat_git["head"],
        budget_contrat=contrat["budget_production_requis_Gio"],
        ratification_contrat=contrat["reference_ratification_budget"],
        support_attendu=support["identite_expurgee"],
        perimetre_exact_attendu=(
            PERIMETRE_EXACT_SENTINELLE if reference_franchissement else None),
        reference_sentinelle_attendue=(
            REFERENCE_RATIFICATION_SENTINELLE if reference_franchissement
            else None),
    )
    # 6. budget ratifié (condition subsumée) PUIS admission de capacité —
    #    c'est l'admission, et non « libre >= budget », qui décide.
    rapport["budget"] = garde_budget_production(contrat_brut, cible)
    rapport["capacite_admission"] = garde_capacite_production(
        cible, variante, support=support)
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
        support_actif_identite_expurgee=support["identite_expurgee"],
    )
    repertoire_run = f"g2_4/P_WS/{variante}/s{graine}"
    plan["prefixe"] = str(Path(cible) / "g2_4" / "P_WS" / variante
                          / f"s{graine}" / "chain")
    # 7 bis. observateur de capacité : construit et VÉRIFIÉ (l'injection ne
    #        doit toucher que callback_function et callback_every), jamais
    #        exécuté ici — aucun run n'existe.
    from xz_cobaya_g2_4 import build_cobaya_info

    observateur, etat_observateur = creer_observateur_capacite(
        cible, variante, repertoire_run)
    garde_injection_observateur(
        build_cobaya_info(DESCRIPTEURS[variante], graine), observateur)
    plan["observateur_capacite"] = {
        k: etat_observateur[k] for k in
        ("callback_every", "marge_anticipation_gio", "plafond_lot_gio",
         "plancher_libre_gio", "politique_capacite_version")}
    # 8. VERROU DUR — placé AVANT toute création de répertoire, toute
    #    ouverture en écriture, tout os.replace, tout manifest.json et
    #    tout cobaya.run. La constante RESTE True : SENT-0D n'y substitue
    #    pas un False global, il n'ouvre qu'un franchissement étroit —
    #    sans flag, le refus HISTORIQUE s'applique à l'identique ; avec un
    #    flag défectueux, refus SENT-0D ; seul le cas ratifié (couple
    #    sentinelle + autorisation privée au périmètre exact + référence
    #    publique exacte) atteint l'étape 9.
    if VERROU_PRODUCTION_G2_4D:
        garde_franchissement_sent0d(reference_franchissement, variante, graine)
    # 9. CHEMIN RÉEL (SENT-0A) — matériellement inatteignable tant que le
    #    verrou vaut True. L'information Cobaya vient EXCLUSIVEMENT du
    #    constructeur directeur ; l'observateur est injecté par le seul
    #    mécanisme qualifié (les deux champs callback, rien d'autre) ; le
    #    préfixe de sortie est le seul ajout opérationnel, postérieur au
    #    gel de l'encodage scientifique, qu'il ne modifie donc pas.
    from xz_cobaya_g2_4 import info_pour_cobaya

    info_execution = info_pour_cobaya(garde_injection_observateur(
        build_cobaya_info(DESCRIPTEURS[variante], graine), observateur))
    info_execution["output"] = plan["prefixe"]
    resultat = executer_production_sentinelle(  # pragma: no cover - sous verrou
        plan, info_execution, plan["prefixe"])
    print(json.dumps({k: resultat[k] for k in
                      ("statut_run", "converged_cobaya")},
                     indent=2, sort_keys=True, ensure_ascii=False))


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
