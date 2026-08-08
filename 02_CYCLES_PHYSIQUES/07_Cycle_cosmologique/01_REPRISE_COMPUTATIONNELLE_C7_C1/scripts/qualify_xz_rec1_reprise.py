"""Qualification de la reprise — porte REC-1 (#94, #63).

Éprouve le chemin de REPRISE d'un run interrompu (états reprenables,
checkpoint, identité scientifique stricte, transition de HEAD ratifiée,
acquisition exclusive, EN_REPRISE, finalisation monotone) SANS AUCUNE
reprise réelle : aucun contact avec le run sentinelle en cours ni avec son
préfixe — tout se joue sur des arborescences SYNTHÉTIQUES sous %TEMP%,
avec le substitut contrôlé de ``cobaya.run`` (aucun échantillonnage,
aucune valeur scientifique).

Mesure d'occupation : ``mesurer_occupation_lot`` est substituée par un
stub DÉTERMINISTE pendant la qualification (occupation nulle), car un run
réel ratifié écrit actuellement sous la racine de runs — la fonction
réelle est qualifiée par CAP-1 et n'est pas l'objet de cette porte. Cette
substitution est déclarée ici et dans le rapport.

PORTE AUTO-BLOQUANTE : toute attente non satisfaite -> SystemExit(1).

Modes :
    (aucun argument)  : qualification complète ;
    --faute NOM       : exit 1 si la faute est détectée (attendu).
"""

from __future__ import annotations

import ast
import hashlib
import importlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from types import SimpleNamespace

VARIANTE = "M2a-N"
GRAINE = 630101
DATE_FIN_QUALIF = "2026-08-08T00:00:01Z"
HEAD_ORIGINE_AUTRE = "e" * 40

CHECKPOINT_VALIDE = (
    "sampler:\n  mcmc:\n    converged: false\n    Rminus1_last: 0.34\n"
    "    burn_in: 0\n    mpi_size: 1\n")


def _preparer():
    ici = Path(__file__).parent.parent
    os.chdir(ici)
    if "scripts" not in sys.path:
        sys.path.insert(0, "scripts")


def _stub_mesure(lanceur):
    """Occupation DÉTERMINISTE pour la qualification (déclaré, assumé)."""
    def _mesure(cible, verifier_stabilite=True):
        return {"octets_production": 0, "octets_temporaires_reconnus": 0,
                "octets_non_attribues": 0, "gio_production": 0.0,
                "gio_temporaires_reconnus": 0.0, "gio_non_attribues": 0.0,
                "runs_production": {}, "n_fichiers": 0,
                "liens_non_suivis": [], "taille_cluster_octets": 4096,
                "stabilite_verifiee": bool(verifier_stabilite)}
    lanceur.mesurer_occupation_lot = _mesure


class SubstitutCobaya:
    """Substitut contrôlé de cobaya.run — jamais un échantillonnage."""

    def __init__(self, comportement="nominal", converged=True):
        self.comportement = comportement
        self.converged = converged
        self.appels: list[dict] = []

    def __call__(self, info, **kwargs):
        self.appels.append({"output": info.get("output"),
                            "kwargs": dict(kwargs)})
        if self.comportement == "capacite":
            from run_mcmc_xz_g2_4 import ArretCapaciteC7C1

            raise ArretCapaciteC7C1("haute-eau simulée (substitut)")
        if self.comportement == "technique":
            raise RuntimeError("panne simulée (substitut)")
        return {}, SimpleNamespace(converged=self.converged)


def _run_synthetique(lanceur, tmp: Path, statut="PLANIFIE",
                     avec_checkpoint=True, head=None) -> Path:
    """Run SYNTHÉTIQUE interrompu sous %TEMP% — jamais le préfixe réel."""
    from qualify_xz_sentinel_sent0 import _manifeste_qualification

    rep = tmp / "g2_4_qualification" / "rec1" / "run"
    rep.mkdir(parents=True, exist_ok=True)
    manifeste = _manifeste_qualification(lanceur)
    if head is not None:
        manifeste["head"] = head
    chemin = rep / "manifest.json"
    lanceur.ecrire_manifeste_atomique(chemin, manifeste)
    if statut != "PLANIFIE":
        cible_statut = {
            "INTERRUPTION": lanceur.STATUT_RUN_INTERROMPU_CAPACITE,
            "CONVERGE": lanceur.STATUT_RUN_CONVERGE,
            "ECHEC": lanceur.STATUT_RUN_ECHEC_TECHNIQUE,
            "FSC": lanceur.STATUT_RUN_FIN_SANS_CONVERGENCE,
        }[statut]
        lanceur.mettre_a_jour_manifeste_runtime(chemin, {
            "statut_run": cible_statut,
            "converged_cobaya": cible_statut == lanceur.STATUT_RUN_CONVERGE,
            "date_fin_utc": DATE_FIN_QUALIF,
            "detail_fin": "etat synthetique de qualification"})
    if avec_checkpoint:
        (rep / "chain.checkpoint").write_text(CHECKPOINT_VALIDE,
                                              encoding="utf-8")
    (rep / "chain.1.txt").write_text("# occupant synthetique\n",
                                     encoding="utf-8")
    return rep / "chain"


def _evenement(lanceur, manifeste_head, head_reprise=None) -> dict:
    return {
        "date_utc": DATE_FIN_QUALIF,
        "head_origine": manifeste_head,
        "head_reprise": head_reprise or manifeste_head,
        "reference_ratification_reprise": "REC1-QUALIFICATION-ONLY",
        "sha256_autorisation_reprise": "0" * 64,
        "sha256_checkpoint_au_moment_de_la_reprise": "0" * 64,
    }


def _executer_reprise(lanceur, prefixe, comportement="nominal",
                      converged=True, head_origine=None):
    substitut = SubstitutCobaya(comportement, converged)
    cobaya_run_mod = importlib.import_module("cobaya.run")
    reel = cobaya_run_mod.run
    cobaya_run_mod.run = substitut
    try:
        with _env(C7C1_TEST_DATE_FIN_UTC=DATE_FIN_QUALIF):
            head = head_origine or lanceur.garde_git()["head"]
            info = {"likelihood": {}, "output": str(prefixe)}
            resultat = lanceur.executer_reprise_sentinelle(
                prefixe, info, _evenement(lanceur, head))
    finally:
        cobaya_run_mod.run = reel
    return resultat, substitut


import contextlib


@contextlib.contextmanager
def _env(**valeurs):
    anciennes = {c: os.environ.get(c) for c in valeurs}
    try:
        for cle, v in valeurs.items():
            if v is None:
                os.environ.pop(cle, None)
            else:
                os.environ[cle] = str(v)
        yield
    finally:
        for cle, v in anciennes.items():
            if v is None:
                os.environ.pop(cle, None)
            else:
                os.environ[cle] = v


# --------------------------------------------------------------- fautes

def executer_faute(nom: str) -> int:  # noqa: C901 - table de fautes
    _preparer()
    import run_mcmc_xz_g2_4 as lanceur
    from run_mcmc_xz_g2_4 import ArretCapaciteC7C1, GardeErreur

    _stub_mesure(lanceur)
    head = lanceur.garde_git()["head"]

    def _detecte_message(fn, fragment: str) -> int:
        try:
            fn()
            return 0
        except (GardeErreur, ArretCapaciteC7C1) as exc:
            return 1 if fragment in str(exc) else 0
        except Exception:  # noqa: BLE001
            return 0

    # ---- états et matière du run ---------------------------------------
    cas_garde = {
        "checkpoint_absent": (dict(avec_checkpoint=False),
                              "checkpoint Cobaya absent"),
        "statut_converge_repris": (dict(statut="CONVERGE"),
                                   "JAMAIS repris"),
        "statut_echec_technique_repris": (dict(statut="ECHEC"),
                                          "audit humain préalable"),
        "statut_fin_sans_convergence_repris": (dict(statut="FSC"),
                                               "audit humain préalable"),
        "identite_scientifique_differente": (dict(),
                                             "identité scientifique"),
        "donnees_differentes": (dict(), "données différentes"),
        "environnement_different": (dict(), "environnement différent"),
        "head_different_sans_ratification": (dict(head=HEAD_ORIGINE_AUTRE),
                                             "transition de HEAD non ratifiée"),
    }
    if nom in cas_garde:
        options, fragment = cas_garde[nom]
        with tempfile.TemporaryDirectory(prefix="c7c1_rec1_") as tmp:
            prefixe = _run_synthetique(lanceur, Path(tmp), **options)
            chemin = prefixe.parent / "manifest.json"
            m = json.loads(chemin.read_text(encoding="utf-8"))
            if nom == "identite_scientifique_differente":
                m["sha256_encodage_scientifique"] = "0" * 64
            elif nom == "donnees_differentes":
                m["sha256_donnees"] = {k: "0" * 64
                                       for k in m["sha256_donnees"]}
            elif nom == "environnement_different":
                m["empreinte_environnement"] = "0" * 64
            if nom in ("identite_scientifique_differente",
                       "donnees_differentes", "environnement_different"):
                lanceur._ecrire_atomique_brut(chemin, m)
            if nom == "head_different_sans_ratification":
                # la garde de reprise SIGNALE la transition ; c'est le
                # VALIDATEUR d'autorisation, sans entrée ratifiée, qui
                # refuse — même lecture que le reste de l'autorisation.
                from qualify_xz_sent0d_unlock import (
                    _autorisation_sentinelle_memoire)
                from qualify_xz_launcher_g2_4d import _support_mesure

                etat = lanceur.garde_reprise_rec1(prefixe, head)
                if not etat["transition_requise"]:
                    return 0
                autorisation = _autorisation_sentinelle_memoire(lanceur)
                autorisation["reference_ratification_reprise"] = \
                    "REC1-QUALIFICATION-ONLY"
                return _detecte_message(
                    lambda: lanceur._valider_contenu_autorisation(
                        autorisation, VARIANTE, GRAINE, head,
                        budget_contrat=lanceur.BUDGET_TOTAL_RATIFIE_GIO,
                        ratification_contrat=
                            lanceur.REFERENCE_RATIFICATION_BUDGET,
                        support_attendu=_support_mesure(lanceur),
                        perimetre_exact_attendu=
                            lanceur.PERIMETRE_EXACT_SENTINELLE,
                        reference_sentinelle_attendue=
                            lanceur.REFERENCE_RATIFICATION_SENTINELLE,
                        reference_reprise_attendue="REC1-QUALIFICATION-ONLY",
                        transition_head_attendue={
                            "origine": HEAD_ORIGINE_AUTRE, "reprise": head}),
                    fragment)
            return _detecte_message(
                lambda: lanceur.garde_reprise_rec1(prefixe, head), fragment)
    if nom == "checkpoint_vide":
        with tempfile.TemporaryDirectory(prefix="c7c1_rec1_") as tmp:
            prefixe = _run_synthetique(lanceur, Path(tmp))
            (prefixe.parent / "chain.checkpoint").write_text("  \n",
                                                             encoding="utf-8")
            return _detecte_message(
                lambda: lanceur.garde_reprise_rec1(prefixe, head),
                "checkpoint vide")
    if nom == "checkpoint_corrompu":
        with tempfile.TemporaryDirectory(prefix="c7c1_rec1_") as tmp:
            prefixe = _run_synthetique(lanceur, Path(tmp))
            (prefixe.parent / "chain.checkpoint").write_text(
                "pas un bloc sampler", encoding="utf-8")
            return _detecte_message(
                lambda: lanceur.garde_reprise_rec1(prefixe, head),
                "sans bloc sampler")
    if nom == "reprise_deja_en_cours":
        with tempfile.TemporaryDirectory(prefix="c7c1_rec1_") as tmp:
            prefixe = _run_synthetique(lanceur, Path(tmp))
            lanceur.enregistrer_reprise(prefixe.parent / "manifest.json",
                                        _evenement(lanceur, head))
            return _detecte_message(
                lambda: lanceur.garde_reprise_rec1(prefixe, head),
                "EN_REPRISE")
    if nom == "manifeste_absent":
        with tempfile.TemporaryDirectory(prefix="c7c1_rec1_") as tmp:
            rep = Path(tmp) / "vide"
            rep.mkdir()
            return _detecte_message(
                lambda: lanceur.garde_reprise_rec1(rep / "chain", head),
                "manifest.json absent")
    if nom == "manifeste_corrompu":
        with tempfile.TemporaryDirectory(prefix="c7c1_rec1_") as tmp:
            rep = Path(tmp) / "corrompu"
            rep.mkdir()
            (rep / "manifest.json").write_text("{ corrompu", encoding="utf-8")
            return _detecte_message(
                lambda: lanceur.garde_reprise_rec1(rep / "chain", head),
                "corrompu")

    # ---- autorisation / CLI ---------------------------------------------
    if nom == "reference_reprise_absente":
        from qualify_xz_sent0d_unlock import _autorisation_sentinelle_memoire
        from qualify_xz_launcher_g2_4d import _support_mesure

        autorisation = _autorisation_sentinelle_memoire(lanceur)
        # champ reference_ratification_reprise ABSENT
        return _detecte_message(
            lambda: lanceur._valider_contenu_autorisation(
                autorisation, VARIANTE, GRAINE, head,
                budget_contrat=lanceur.BUDGET_TOTAL_RATIFIE_GIO,
                ratification_contrat=lanceur.REFERENCE_RATIFICATION_BUDGET,
                support_attendu=_support_mesure(lanceur),
                perimetre_exact_attendu=lanceur.PERIMETRE_EXACT_SENTINELLE,
                reference_sentinelle_attendue=
                    lanceur.REFERENCE_RATIFICATION_SENTINELLE,
                reference_reprise_attendue="REC1-QUALIFICATION-ONLY"),
            "reference_ratification_reprise")
    if nom == "ratification_reprise_cli_absente":
        return _detecte_message(
            lambda: lanceur._extraire_flag_ratification_reprise(
                ["M2a-N", "630101"]),
            "ratification de reprise absente")
    if nom == "ratification_reprise_cli_dupliquee":
        return _detecte_message(
            lambda: lanceur._extraire_flag_ratification_reprise(
                ["--ratification-reprise", "A",
                 "--ratification-reprise", "A"]),
            "dupliqué")
    if nom == "reprise_hors_couple_sentinelle":
        head_reel = lanceur.garde_git()["head"]
        vrai_git = lanceur.garde_git
        lanceur.garde_git = lambda: {"head": head_reel, "arbre_propre": True}
        try:
            return _detecte_message(
                lambda: lanceur.reprendre(
                    ["M2a-K", "630201", "--je-confirme-la-reprise",
                     "--autorisation", "inexistant.json",
                     "--ratification-reprise", "REC1-X"]),
                "hors périmètre sentinelle")
        finally:
            lanceur.garde_git = vrai_git

    # ---- enregistrement et cycle de vie ---------------------------------
    if nom == "evenement_reprise_incomplet":
        with tempfile.TemporaryDirectory(prefix="c7c1_rec1_") as tmp:
            prefixe = _run_synthetique(lanceur, Path(tmp))
            e = _evenement(lanceur, head)
            e.pop("sha256_checkpoint_au_moment_de_la_reprise")
            return _detecte_message(
                lambda: lanceur.enregistrer_reprise(
                    prefixe.parent / "manifest.json", e),
                "événement de reprise incomplet")
    if nom == "evenement_head_origine_different":
        with tempfile.TemporaryDirectory(prefix="c7c1_rec1_") as tmp:
            prefixe = _run_synthetique(lanceur, Path(tmp))
            e = _evenement(lanceur, "f" * 40)
            return _detecte_message(
                lambda: lanceur.enregistrer_reprise(
                    prefixe.parent / "manifest.json", e),
                "head_origine != head du manifeste")
    if nom == "historique_non_liste":
        with tempfile.TemporaryDirectory(prefix="c7c1_rec1_") as tmp:
            prefixe = _run_synthetique(lanceur, Path(tmp))
            chemin = prefixe.parent / "manifest.json"
            m = json.loads(chemin.read_text(encoding="utf-8"))
            m["historique_reprises"] = "corrompu"
            lanceur._ecrire_atomique_brut(chemin, m)
            return _detecte_message(
                lambda: lanceur.enregistrer_reprise(
                    chemin, _evenement(lanceur, head)),
                "historique_reprises non conforme")
    if nom == "reprise_concurrente":
        with tempfile.TemporaryDirectory(prefix="c7c1_rec1_") as tmp:
            prefixe = _run_synthetique(lanceur, Path(tmp))
            lanceur._acquerir_verrou_reprise(prefixe.parent)
            return _detecte_message(
                lambda: lanceur._acquerir_verrou_reprise(prefixe.parent),
                "acquisition exclusive refusée")
    if nom == "double_finalisation_apres_reprise":
        with tempfile.TemporaryDirectory(prefix="c7c1_rec1_") as tmp:
            prefixe = _run_synthetique(lanceur, Path(tmp))
            _executer_reprise(lanceur, prefixe)  # finalise CONVERGE
            return _detecte_message(
                lambda: lanceur.mettre_a_jour_manifeste_runtime(
                    prefixe.parent / "manifest.json",
                    {"statut_run": lanceur.STATUT_RUN_CONVERGE,
                     "converged_cobaya": True,
                     "date_fin_utc": DATE_FIN_QUALIF,
                     "detail_fin": "seconde finalisation interdite"}),
                "jamais réécrit")
    if nom == "admission_cap1_refusee_en_reprise":
        with tempfile.TemporaryDirectory(prefix="c7c1_rec1_") as tmp:
            prefixe = _run_synthetique(lanceur, Path(tmp))
            with _env(C7C1_TEST_ESPACE_LIBRE_GIO="45"):
                return _detecte_message(
                    lambda: lanceur.garde_reprise_rec1(prefixe, head),
                    "admission refusée")
    if nom == "reprise_sans_checkpoint_ne_fabrique_rien":
        with tempfile.TemporaryDirectory(prefix="c7c1_rec1_") as tmp:
            prefixe = _run_synthetique(lanceur, Path(tmp),
                                       avec_checkpoint=False)
            refuse = _detecte_message(
                lambda: lanceur.garde_reprise_rec1(prefixe, head),
                "checkpoint Cobaya absent")
            toujours_absent = not (prefixe.parent
                                   / "chain.checkpoint").exists()
        return 1 if (refuse == 1 and toujours_absent) else 0
    if nom == "production_sur_prefixe_occupe_toujours_refusee":
        with tempfile.TemporaryDirectory(prefix="c7c1_rec1_") as tmp:
            prefixe = _run_synthetique(lanceur, Path(tmp))
            return _detecte_message(
                lambda: lanceur.garde_collision(prefixe), "collision")
    if nom == "garde_reprise_neutralisee":
        # MUTATION : garde neutralisée -> un run CONVERGE synthétique
        # atteint le substitut (la reprise d'un run convergé deviendrait
        # possible). Preuve que la garde réelle est ce qui bloque.
        with tempfile.TemporaryDirectory(prefix="c7c1_rec1_") as tmp:
            prefixe = _run_synthetique(lanceur, Path(tmp), statut="CONVERGE")
            avant = _detecte_message(
                lambda: lanceur.garde_reprise_rec1(prefixe, head),
                "JAMAIS repris")
            vraie = lanceur.garde_reprise_rec1
            lanceur.garde_reprise_rec1 = lambda p, h: {
                "manifeste": {}, "sha256_checkpoint": "0" * 64,
                "transition_requise": False}
            try:
                apres = _detecte_message(
                    lambda: lanceur.garde_reprise_rec1(prefixe, head),
                    "JAMAIS repris")
            finally:
                lanceur.garde_reprise_rec1 = vraie
        return 1 if (avant == 1 and apres == 0) else 0
    if nom == "verrou_retire":
        source = Path("scripts/run_mcmc_xz_g2_4.py").read_text(
            encoding="utf-8")
        falsifie = source.replace("VERROU_PRODUCTION_G2_4D = True",
                                  "VERROU_PRODUCTION_G2_4D = False", 1)
        for noeud in ast.parse(falsifie).body:
            if isinstance(noeud, ast.Assign):
                for c in noeud.targets:
                    if isinstance(c, ast.Name) \
                            and c.id == "VERROU_PRODUCTION_G2_4D":
                        return 1 if ast.literal_eval(noeud.value) is False \
                            else 0
        return 0
    raise SystemExit(f"faute inconnue : {nom}")


FAUTES = (
    "checkpoint_absent", "checkpoint_vide", "checkpoint_corrompu",
    "statut_converge_repris", "statut_echec_technique_repris",
    "statut_fin_sans_convergence_repris", "reprise_deja_en_cours",
    "manifeste_absent", "manifeste_corrompu",
    "identite_scientifique_differente", "donnees_differentes",
    "environnement_different", "head_different_sans_ratification",
    "reference_reprise_absente", "ratification_reprise_cli_absente",
    "ratification_reprise_cli_dupliquee", "reprise_hors_couple_sentinelle",
    "evenement_reprise_incomplet", "evenement_head_origine_different",
    "historique_non_liste", "reprise_concurrente",
    "double_finalisation_apres_reprise", "admission_cap1_refusee_en_reprise",
    "reprise_sans_checkpoint_ne_fabrique_rien",
    "production_sur_prefixe_occupe_toujours_refusee",
    "garde_reprise_neutralisee", "verrou_retire",
)


# ---------------------------------------------------------- qualification

def qualification() -> int:  # noqa: C901
    _preparer()
    import run_mcmc_xz_g2_4 as lanceur
    from run_mcmc_xz_g2_4 import ArretCapaciteC7C1, GardeErreur

    _stub_mesure(lanceur)
    echecs: list[str] = []
    resultat: dict = {}
    head = lanceur.garde_git()["head"]

    # ---- 1. statique ---------------------------------------------------
    source = Path("scripts/run_mcmc_xz_g2_4.py").read_text(encoding="utf-8")
    resultat["statique"] = {
        "VERROU_PRODUCTION_G2_4D": lanceur.VERROU_PRODUCTION_G2_4D,
        "statuts_reprenables": list(lanceur.STATUTS_RUN_REPRENABLES),
        "schema_reprise": lanceur.SCHEMA_MANIFESTE_REPRISE,
        "schema_reprise_reconnu": lanceur.SCHEMA_MANIFESTE_REPRISE
            in lanceur.SCHEMAS_MANIFESTE_RECONNUS,
        "cles_optionnelles_rec1": sorted(
            k for k in lanceur.CLES_MANIFESTE_OPTIONNELLES if "repris" in k),
        "creation_reste_au_schema_2":
            lanceur.SCHEMA_MANIFESTE_RUN == "c7c1-run-manifest-2",
    }
    if lanceur.VERROU_PRODUCTION_G2_4D is not True:
        echecs.append("VERROU_PRODUCTION_G2_4D != True")
    if lanceur.STATUTS_RUN_REPRENABLES != (
            lanceur.STATUT_RUN_PLANIFIE,
            lanceur.STATUT_RUN_INTERROMPU_CAPACITE):
        echecs.append("états reprenables inattendus")
    for cle, attendu in (("schema_reprise_reconnu", True),
                         ("creation_reste_au_schema_2", True)):
        if resultat["statique"][cle] is not attendu:
            echecs.append(f"statique : {cle} non conforme")

    # ---- 2. reprise nominale même HEAD (substitut, %TEMP%) -------------
    with tempfile.TemporaryDirectory(prefix="c7c1_rec1_") as tmp:
        prefixe = _run_synthetique(lanceur, Path(tmp))
        etat = lanceur.garde_reprise_rec1(prefixe, head)
        res, substitut = _executer_reprise(lanceur, prefixe)
        manifeste = json.loads((prefixe.parent / "manifest.json")
                               .read_text(encoding="utf-8"))
        verrous = sorted(p.name for p in prefixe.parent.iterdir()
                         if p.name.startswith(".reprise"))
        appel = substitut.appels[0] if substitut.appels else {}
        nominal = {
            "transition_requise": etat["transition_requise"],
            "statut_final": manifeste["statut_run"],
            "converged_cobaya": manifeste["converged_cobaya"],
            "schema_promu": manifeste["schema"],
            "n_reprises": len(manifeste["historique_reprises"]),
            "evenement_champs": sorted(manifeste["historique_reprises"][0]),
            "resume_kwarg": appel.get("kwargs", {}).get("resume"),
            "output_est_le_prefixe": appel.get("output") == str(prefixe),
            "verrou_clos": verrous == [".reprise.001.clos"],
            "identite_intacte": [c for c in lanceur.CHAMPS_MANIFESTE_RUN
                                 if c not in manifeste] == [],
        }
    resultat["reprise_nominale"] = nominal
    attendus = {
        "transition_requise": False, "statut_final": "CONVERGE",
        "converged_cobaya": True, "schema_promu": "c7c1-run-manifest-3",
        "n_reprises": 1, "resume_kwarg": True,
        "output_est_le_prefixe": True, "verrou_clos": True,
        "identite_intacte": True,
    }
    for cle, att in attendus.items():
        if nominal.get(cle) != att:
            echecs.append(f"reprise nominale : {cle} = {nominal.get(cle)!r} "
                          f"!= {att!r}")
    if nominal["evenement_champs"] != sorted(
            lanceur.CHAMPS_EVENEMENT_REPRISE):
        echecs.append("événement de reprise : champs inexacts")

    # ---- 3. cycle interruption -> reprise -> interruption -> reprise ---
    with tempfile.TemporaryDirectory(prefix="c7c1_rec1_") as tmp:
        prefixe = _run_synthetique(lanceur, Path(tmp), statut="INTERRUPTION")
        try:
            _executer_reprise(lanceur, prefixe, comportement="capacite")
            cycle1 = "AUCUNE_EXCEPTION"
        except ArretCapaciteC7C1:
            cycle1 = json.loads((prefixe.parent / "manifest.json")
                                .read_text(encoding="utf-8"))["statut_run"]
        # le run retombé en INTERRUPTION doit être reprenable À NOUVEAU
        lanceur.garde_reprise_rec1(prefixe, head)
        res2, _ = _executer_reprise(lanceur, prefixe)
        manifeste = json.loads((prefixe.parent / "manifest.json")
                               .read_text(encoding="utf-8"))
        verrous = sorted(p.name for p in prefixe.parent.iterdir()
                         if p.name.startswith(".reprise"))
        cycles = {
            "apres_reprise_1": cycle1,
            "apres_reprise_2": manifeste["statut_run"],
            "n_reprises": len(manifeste["historique_reprises"]),
            "historique_append_only":
                manifeste["historique_reprises"][0]["date_utc"]
                == DATE_FIN_QUALIF,
            "verrous_clos": verrous == [".reprise.001.clos",
                                        ".reprise.002.clos"],
        }
    resultat["cycle_interruption_reprise"] = cycles
    if cycles["apres_reprise_1"] != lanceur.STATUT_RUN_INTERROMPU_CAPACITE:
        echecs.append("cycle : l'interruption en reprise n'est pas "
                      "NON_CONVERGE_INTERRUPTION_CAPACITE")
    if cycles["apres_reprise_2"] != lanceur.STATUT_RUN_CONVERGE \
            or cycles["n_reprises"] != 2 or not cycles["verrous_clos"]:
        echecs.append(f"cycle de reprises non conforme : {cycles}")

    # ---- 4. transition de HEAD : refus sans ratification, admise avec --
    from qualify_xz_sent0d_unlock import _autorisation_sentinelle_memoire
    from qualify_xz_launcher_g2_4d import _support_mesure

    with tempfile.TemporaryDirectory(prefix="c7c1_rec1_") as tmp:
        prefixe = _run_synthetique(lanceur, Path(tmp),
                                   head=HEAD_ORIGINE_AUTRE)
        etat = lanceur.garde_reprise_rec1(prefixe, head)
    support = _support_mesure(lanceur)
    base_kwargs = dict(
        budget_contrat=lanceur.BUDGET_TOTAL_RATIFIE_GIO,
        ratification_contrat=lanceur.REFERENCE_RATIFICATION_BUDGET,
        support_attendu=support,
        perimetre_exact_attendu=lanceur.PERIMETRE_EXACT_SENTINELLE,
        reference_sentinelle_attendue=
            lanceur.REFERENCE_RATIFICATION_SENTINELLE,
        reference_reprise_attendue="REC1-QUALIFICATION-ONLY",
        transition_head_attendue={"origine": HEAD_ORIGINE_AUTRE,
                                  "reprise": head})
    autorisation = _autorisation_sentinelle_memoire(lanceur)
    autorisation["reference_ratification_reprise"] = "REC1-QUALIFICATION-ONLY"
    try:
        lanceur._valider_contenu_autorisation(
            autorisation, VARIANTE, GRAINE, head, **base_kwargs)
        sans_ratification = "ADMISE_A_TORT"
    except GardeErreur as exc:
        sans_ratification = ("REFUSEE_CAUSE_EXACTE"
                             if "transition de HEAD non ratifiée" in str(exc)
                             else f"REFUSEE_AUTRE: {exc}"[:80])
    autorisation["transitions_head_autorisees"] = [
        {"origine": HEAD_ORIGINE_AUTRE, "reprise": head}]
    traverses = lanceur._valider_contenu_autorisation(
        autorisation, VARIANTE, GRAINE, head, **base_kwargs)
    transition = {
        "transition_detectee_par_la_garde": etat["transition_requise"],
        "sans_ratification": sans_ratification,
        "avec_ratification_admise": "transition_head" in traverses
                                    and "reference_reprise" in traverses,
    }
    resultat["transition_head"] = transition
    if transition != {"transition_detectee_par_la_garde": True,
                      "sans_ratification": "REFUSEE_CAUSE_EXACTE",
                      "avec_ratification_admise": True}:
        echecs.append(f"transition de HEAD non conforme : {transition}")

    # ---- 5. rétro-compatibilité : validateur général inchangé ----------
    autorisation_simple = _autorisation_sentinelle_memoire(lanceur)
    try:
        lanceur._valider_contenu_autorisation(
            autorisation_simple, VARIANTE, GRAINE, head,
            budget_contrat=lanceur.BUDGET_TOTAL_RATIFIE_GIO,
            ratification_contrat=lanceur.REFERENCE_RATIFICATION_BUDGET,
            support_attendu=support,
            perimetre_exact_attendu=lanceur.PERIMETRE_EXACT_SENTINELLE,
            reference_sentinelle_attendue=
                lanceur.REFERENCE_RATIFICATION_SENTINELLE)
        retro = True
    except GardeErreur:
        retro = False
    resultat["retro_compatibilite_autorisation"] = retro
    if not retro:
        echecs.append("le validateur général est cassé par les clés REC-1")

    # ---- 6. fautes (sous-processus) ------------------------------------
    resultat["fautes"] = {}
    for nom in FAUTES:
        proc = subprocess.run(
            [sys.executable, "scripts/qualify_xz_rec1_reprise.py",
             "--faute", nom], capture_output=True, text=True)
        detectee = proc.returncode == 1
        resultat["fautes"][nom] = {"detectee": detectee,
                                   "code": proc.returncode}
        if not detectee:
            echecs.append(f"faute NON détectée : {nom}")
    resultat["fautes_resume"] = {
        "total": len(FAUTES),
        "detectees": sum(1 for v in resultat["fautes"].values()
                         if v["detectee"])}

    # ---- 7. confidentialité --------------------------------------------
    from qualify_xz_capacity_cap1 import _motifs_confidentiels

    motifs = _motifs_confidentiels(lanceur, os.environ["C7C1_XZ_OUT_DIR"])
    fuites: dict = {}
    for relatif in ("scripts/run_mcmc_xz_g2_4.py",
                    "scripts/qualify_xz_rec1_reprise.py",
                    "reports/rapport_REC1_reprise_qualifiee.md"):
        chemin = Path(relatif)
        if not chemin.is_file():
            continue
        texte = chemin.read_text(encoding="utf-8", errors="replace")
        for nom_motif, motif in motifs.items():
            for numero, ligne in enumerate(texte.splitlines(), 1):
                if motif.search(ligne):
                    fuites.setdefault(nom_motif, []).append(
                        f"{chemin.name}:{numero}")
    resultat["confidentialite"] = {"aucune_fuite": not fuites,
                                   "fuites": {k: v[:5] for k, v
                                              in sorted(fuites.items())}}
    if fuites:
        echecs.append(f"fuite locale : {sorted(fuites)}")

    resultat["rappel"] = {
        "reprise_reelle": "AUCUNE — substitut seulement, %TEMP% seulement",
        "run_sentinelle_en_cours": "JAMAIS touché (préfixe réel non visité)",
        "verrou": "VERROU_PRODUCTION_G2_4D = True",
        "mesure_occupation": "substituée par stub déterministe (déclaré) — "
                             "fonction réelle qualifiée par CAP-1",
    }
    resultat["porte"] = {"passe": not echecs, "echecs": sorted(echecs)}
    print("=== SORTIE NORMALISEE (deterministe) ===")
    print(json.dumps(resultat, indent=2, sort_keys=True, ensure_ascii=False))
    return 1 if echecs else 0


def main() -> None:
    args = sys.argv[1:]
    if args[:1] == ["--faute"]:
        raise SystemExit(executer_faute(args[1]))
    if args:
        print(f"ARRET : argument non reconnu {args!r}")
        raise SystemExit(2)
    raise SystemExit(qualification())


if __name__ == "__main__":
    main()
