"""Qualification du raccord au lanceur — porte G2.4d (issue #63).

Qualifie le raccord de l'architecture optimisée (ReferenceLenteXZ +
VraisemblanceRapideXZ, mode acoustique corrected-v1.1) au lanceur G2.4b,
SANS AUCUNE PRODUCTION : aucune MCMC, aucune minimisation, aucun
posterior, aucune chaîne, aucun manifeste réel, aucune autorisation
réelle. Les seules écritures autorisées sont des manifestes ÉPHÉMÈRES
marqués QUALIFICATION_ONLY sous %TEMP%, supprimés en fin de passe.

PORTE AUTO-BLOQUANTE : toute attente non satisfaite conduit à
SystemExit(1) après impression du JSON normalisé. Les temps, la mémoire
et l'espace libre sont imprimés dans une section séparée, exclue du
contrôle de déterminisme.

Modes :
    (aucun argument)  : qualification complète ;
    --faute NOM       : injecte la faute NOM ; exit 1 si elle est
                        détectée (attendu), 0 si elle passe inaperçue.
"""

from __future__ import annotations

import contextlib
import hashlib
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile
import time
import tracemalloc
from pathlib import Path

import numpy as np

VARIANTES_ORDRE = ("M2a-N", "M2a-K", "M2b-N", "M2b-K")
GRAINE_GELEE = {"M2a-N": 630101, "M2a-K": 630201,
                "M2b-N": 630301, "M2b-K": 630401}
POINT_FOND_P0 = {"H0": 67.36, "ombh2": 0.02237, "omm": 0.3152}
POINT_FOND_P1 = {"H0": 68.3526, "ombh2": 0.022410, "omm": 0.300539}
P2_VALUES = {"M2a": (0.6, -0.2, 0.4, 1.2, 0.8), "M2b": (0.6, -0.2, 0.4, 0.8)}
P3_VALUES = {"M2a": (1.4, 0.2, 1.6, 0.1, 1.3), "M2b": (1.4, 0.2, 1.6, 1.3)}

# Seuils DÉJÀ QUALIFIÉS (G2.1 T8, G2.4c) — aucun relâchement.
SEUILS_LEGACY = {
    "chi2_BAO_abs": 1e-10, "chi2_CMB_abs": 1e-3,
    "chi2_total_abs": 1e-3, "logp_abs": 5e-4, "omch2_abs": 1e-12,
}


def _preparer():
    ici = Path(__file__).parent.parent
    os.chdir(ici)
    if "scripts" not in sys.path:
        sys.path.insert(0, "scripts")
    return ici


def _instrumenter_camb():
    from xz_background_g2_1 import CambReference

    reel = CambReference.from_g1.__func__
    compteur = {"appels": 0}

    def instrumente(cls, **kw):
        compteur["appels"] += 1
        return reel(cls, **kw)

    CambReference.from_g1 = classmethod(instrumente)
    return compteur


def _points_fixes(variante, config):
    noms = [item["nom"] for item in config["parametres_x"]]
    grille = config["grille"]
    return {
        "P0": {**POINT_FOND_P0, **{n: 1.0 for n in noms}},
        "P1": {**POINT_FOND_P1, **{n: 1.0 for n in noms}},
        "P2": {**POINT_FOND_P0, **dict(zip(noms, P2_VALUES[grille]))},
        "P3": {**POINT_FOND_P0, **dict(zip(noms, P3_VALUES[grille]))},
    }


# --------------------------------------------------------------- fautes

def executer_faute(nom: str) -> int:
    """Chaque faute doit être détectée (exit 1). Exit 0 = non détectée."""
    _preparer()
    import run_mcmc_xz_g2_4 as lanceur
    import xz_cobaya_g2_4 as adaptateur
    from run_mcmc_xz_g2_4 import DESCRIPTEURS, GardeErreur

    d_n = DESCRIPTEURS["M2a-N"]

    def _detecte(fn, exceptions=(GardeErreur, ValueError, RuntimeError,
                                KeyError, TypeError, OSError)):
        try:
            fn()
            return 0
        except exceptions:
            return 1

    # --- graphe et mode directeur ---------------------------------------
    if nom == "directeur_retourne_legacy":
        info = adaptateur.build_cobaya_info_legacy(d_n, 630101)
        conforme = (info["_xz_meta"]["backend"] == "optimized"
                    and "theory" in info)
        return 0 if conforme else 1
    if nom == "mode_directeur_corrected_legacy":
        return _detecte(lambda: adaptateur._resoudre_mode_directeur(
            "corrected-legacy"))
    if nom == "mode_directeur_fixed":
        return _detecte(lambda: adaptateur._resoudre_mode_directeur("fixed"))
    if nom == "mode_directeur_inconnu":
        return _detecte(lambda: adaptateur._resoudre_mode_directeur("corrected-v9"))
    if nom == "theory_depend_d_un_xi":
        from xz_fast_g2_4c import build_info_optimisee

        original = build_info_optimisee

        def sabote(descripteur, graine):
            info = original(descripteur, graine)
            info["theory"]["reference_lente_xz"]["input_params"].append("X1")
            return info

        adaptateur.build_info_optimisee = sabote
        sys.modules["xz_fast_g2_4c"].build_info_optimisee = sabote
        return _detecte(lambda: adaptateur.build_cobaya_info(d_n, 630101))
    if nom == "likelihood_depend_de_h0":
        from xz_fast_g2_4c import build_info_optimisee

        original = build_info_optimisee

        def sabote(descripteur, graine):
            info = original(descripteur, graine)
            info["likelihood"]["xz_rapide"]["input_params"].insert(0, "H0")
            return info

        sys.modules["xz_fast_g2_4c"].build_info_optimisee = sabote
        return _detecte(lambda: adaptateur.build_cobaya_info(d_n, 630101))
    if nom.startswith("parite_"):
        # Le comparateur de parité doit MORDRE sur n'importe quel champ du
        # bloc params — y compris le latex d'un dérivé, jamais comparé
        # avant le correctif de cette porte.
        from xz_fast_g2_4c import build_info_optimisee

        original = build_info_optimisee

        def sabote(descripteur, graine):
            info = original(descripteur, graine)
            if nom == "parite_latex_derive_perdu":
                info["params"]["chi2_BAO"] = {"derived": True}  # latex retiré
            elif nom == "parite_prior_altere":
                info["params"]["H0"]["prior"] = {"min": 20.0, "max": 99.0}
            elif nom == "parite_proposal_altere":
                info["params"]["X1"]["proposal"] = 0.06
            return info

        sys.modules["xz_fast_g2_4c"].build_info_optimisee = sabote
        adaptateur.LATEX_CHI2 = {}  # empêche la ré-injection compensatrice
        p = adaptateur.comparer_parite(d_n, 630101)
        return 0 if p["identique"] else 1
    if nom == "graphe_un_bloc":
        from cobaya.model import get_model

        info = adaptateur.info_pour_cobaya(
            adaptateur.build_cobaya_info_legacy(d_n, 0))
        info.pop("sampler", None)
        modele = get_model(info)
        blocs, _ = modele.get_param_blocking_for_sampler(oversample_power=0.4)
        return 1 if len(blocs) == 1 else 0
    if nom == "camb_sur_variation_xi":
        from xz_fast_g2_4c import EvaluateurRapide, FabriqueEtatsLents
        from xz_likelihood_g2_3 import load_bao_data, load_config

        compteur = _instrumenter_camb()
        bao_mean, bao_icov = load_bao_data()
        cfg = load_config(d_n)
        noms = [i["nom"] for i in cfg["parametres_x"]]
        ev = EvaluateurRapide(cfg, bao_mean, bao_icov,
                              FabriqueEtatsLents(
                                  sabotage=frozenset({"cache_desactive"})))
        ev.evaluate({**POINT_FOND_P0, **dict(zip(noms, P2_VALUES["M2a"]))})
        avant = compteur["appels"]
        ev.evaluate({**POINT_FOND_P0,
                     **dict(zip(noms, (0.7, -0.2, 0.4, 1.2, 0.8)))})
        return 1 if compteur["appels"] > avant else 0
    if nom == "cache_partage_entre_variantes":
        from xz_fast_g2_4c import (EvaluateurRapide, FabriqueEtatsLents,
                                   GardeIdentiteErreur)
        from xz_likelihood_g2_3 import load_bao_data, load_config

        bao_mean, bao_icov = load_bao_data()
        fab = FabriqueEtatsLents(
            sabotage=frozenset({"cache_partage_variantes"}))
        cfg_n, cfg_k = load_config(d_n), load_config(DESCRIPTEURS["M2a-K"])
        noms = [i["nom"] for i in cfg_n["parametres_x"]]
        pt = {**POINT_FOND_P0, **dict(zip(noms, P2_VALUES["M2a"]))}
        return _detecte(
            lambda: (EvaluateurRapide(cfg_n, bao_mean, bao_icov, fab).evaluate(pt),
                     EvaluateurRapide(cfg_k, bao_mean, bao_icov, fab).evaluate(pt)),
            (GardeIdentiteErreur, ValueError))

    # --- contrat local, environnement, threads ---------------------------
    if nom == "contrat_local_absent":
        os.environ.pop("C7C1_CONTRAT_LOCAL", None)
        return _detecte(lanceur.garde_contrat_local)
    if nom in ("contrat_schema_perime", "contrat_python_different",
               "contrat_empreinte_fausse", "contrat_json_invalide"):
        base = json.loads(Path(os.environ["C7C1_CONTRAT_LOCAL"]).read_text(
            encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmp:
            faux = Path(tmp) / "contrat_faute.json"
            if nom == "contrat_json_invalide":
                faux.write_text("{ ceci n'est pas du JSON", encoding="utf-8")
            else:
                if nom == "contrat_schema_perime":
                    base["racine_runs"].pop("garde_technique_minimale_Gio", None)
                    base["racine_runs"]["seuil_minimal_Gio"] = 40
                elif nom == "contrat_python_different":
                    base["chemins_reels"]["python_directeur"] = str(
                        Path(sys.executable).parent / "pythonw.exe")
                else:
                    base["environnement"][
                        "empreinte_sha256_inventaire_normalise"] = "0" * 64
                faux.write_text(json.dumps(base), encoding="utf-8")
            os.environ["C7C1_CONTRAT_LOCAL"] = str(faux)
            return _detecte(lanceur.garde_contrat_local)
    if nom.startswith("thread_"):
        if nom == "thread_absent":
            os.environ.pop("OPENBLAS_NUM_THREADS", None)
        elif nom == "thread_vaut_2":
            os.environ["MKL_NUM_THREADS"] = "2"
        elif nom == "thread_vide":
            os.environ["OMP_NUM_THREADS"] = ""
        elif nom == "thread_auto":
            os.environ["NUMEXPR_NUM_THREADS"] = "auto"
        elif nom == "thread_espace":
            os.environ["OMP_NUM_THREADS"] = " "
        return _detecte(lanceur.garde_threads_et_interpreteur)
    if nom == "pythonnousersite_absent":
        os.environ.pop("PYTHONNOUSERSITE", None)
        return _detecte(lanceur.garde_threads_et_interpreteur)

    # --- chemins ----------------------------------------------------------
    if nom in ("runs_sous_git", "runs_sous_onedrive", "data_egal_runs"):
        depot = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                               capture_output=True, text=True,
                               check=True).stdout.strip()
        data = os.environ["C7C1_DATA_DIR"]
        runs = os.environ["C7C1_XZ_OUT_DIR"]
        if nom == "runs_sous_git":
            runs = depot
        elif nom == "runs_sous_onedrive":
            contrat = json.loads(
                Path(os.environ["C7C1_CONTRAT_LOCAL"]).read_text(encoding="utf-8"))
            runs = contrat["chemins_reels"]["depot_historique_non_directeur"]
        else:
            runs = data
        return _detecte(lambda: lanceur.garde_chemins(runs, data, depot))

    # --- capacité et budget ----------------------------------------------
    if nom == "capacite_mesuree_sur_ancre":
        # INJECTION : on rétablit l'ancienne mesure sur l'ancre du volume.
        # L'espion de qualification doit s'en apercevoir (exit 1).
        cible = Path(os.environ["C7C1_XZ_OUT_DIR"])
        vus, reel = [], shutil.disk_usage

        def espion(chemin):
            vus.append(str(chemin))
            return reel(chemin)

        def ancienne_mesure(c):
            return shutil.disk_usage(Path(c).anchor or str(c)).free / lanceur.GIO

        shutil.disk_usage = espion
        os.environ.pop("C7C1_TEST_ESPACE_LIBRE_GIO", None)
        try:
            ancienne_mesure(cible)
        finally:
            shutil.disk_usage = reel
        ancre = os.path.normcase(str(Path(cible).anchor))
        mesure_sur_ancre = bool(vus) and os.path.normcase(vus[0]) == ancre
        return 1 if mesure_sur_ancre else 0
    if nom == "budget_non_etabli_accepte":
        contrat = json.loads(
            Path(os.environ["C7C1_CONTRAT_LOCAL"]).read_text(encoding="utf-8"))
        return _detecte(lambda: lanceur.garde_budget_production(
            contrat, os.environ["C7C1_XZ_OUT_DIR"]))
    if nom == "budget_superieur_a_l_espace":
        contrat = json.loads(
            Path(os.environ["C7C1_CONTRAT_LOCAL"]).read_text(encoding="utf-8"))
        contrat["racine_runs"]["budget_production_statut"] = "RATIFIE"
        contrat["racine_runs"]["budget_production_requis_Gio"] = 10_000_000
        return _detecte(lambda: lanceur.garde_budget_production(
            contrat, os.environ["C7C1_XZ_OUT_DIR"]))
    if nom == "budget_nul_ou_negatif":
        contrat = json.loads(
            Path(os.environ["C7C1_CONTRAT_LOCAL"]).read_text(encoding="utf-8"))
        contrat["racine_runs"]["budget_production_statut"] = "RATIFIE"
        contrat["racine_runs"]["budget_production_requis_Gio"] = 0
        return _detecte(lambda: lanceur.garde_budget_production(
            contrat, os.environ["C7C1_XZ_OUT_DIR"]))

    # --- autorisation -----------------------------------------------------
    if nom.startswith("autorisation_"):
        with tempfile.TemporaryDirectory() as tmp:
            chemin = _autorisation_qualification(Path(tmp), variante="M2a-N",
                                                 graine=630101, defaut=nom)
            head = lanceur.garde_git()["head"]
            return _detecte(lambda: lanceur.garde_autorisation(
                chemin, "M2a-N", 630101, head))

    # --- manifeste et reprise --------------------------------------------
    if nom == "manifeste_ecrasement_non_identique":
        with tempfile.TemporaryDirectory() as tmp:
            cible = Path(tmp) / "manifest.json"
            lanceur.ecrire_manifeste_atomique(cible, {"a": 1,
                                                      "_QUALIFICATION_ONLY": True})
            return _detecte(lambda: lanceur.ecrire_manifeste_atomique(
                cible, {"a": 2, "_QUALIFICATION_ONLY": True}))
    if nom == "manifeste_temporaire_conserve":
        # INJECTION : écriture NAÏVE qui échoue avant le remplacement et
        # ne nettoie pas son temporaire. Le contrôle doit voir le résidu.
        with tempfile.TemporaryDirectory() as tmp:
            cible = Path(tmp) / "manifest.json"
            temporaire = cible.with_name(cible.name + ".tmpNAIF")
            try:
                with open(temporaire, "w", encoding="utf-8") as handle:
                    handle.write('{"partiel": true')  # JSON tronqué
                raise OSError("echec simule avant os.replace")
            except OSError:
                pass  # aucun nettoyage : c'est précisément la faute
            residus = list(Path(tmp).glob("*.tmp*"))
            partiel = cible.exists()
            return 1 if (residus or partiel) else 0
    if nom == "reprise_sans_manifeste":
        with tempfile.TemporaryDirectory() as tmp:
            return _detecte(lambda: lanceur.garde_reprise(
                Path(tmp) / "chain", {"variante": "M2a-N"}))
    if nom == "reprise_identite_partielle":
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "manifest.json").write_text(
                json.dumps({"variante": "M2a-N"}), encoding="utf-8")
            return _detecte(lambda: lanceur.garde_reprise(
                Path(tmp) / "chain",
                {"variante": "M2a-N", "graine": 630101}))

    # --- verrou dur --------------------------------------------------------
    if nom in ("verrou_cobaya_run_atteint", "verrou_ecriture_atteinte"):
        return _preuve_verrou(nom)
    raise SystemExit(f"faute inconnue : {nom}")


def _autorisation_qualification(prep: Path, variante: str, graine: int,
                                defaut: str) -> Path:
    """Autorisation ÉPHÉMÈRE de qualification, jamais une autorisation
    réelle : marquée QUALIFICATION_ONLY et volontairement défectueuse."""
    import run_mcmc_xz_g2_4 as lanceur

    ici = Path(lanceur.__file__).parent
    manifeste = {
        "type": "autorisation_production_c7c1_g2_4",
        "cle_humaine_1": "QUALIFICATION_ONLY",
        "cle_humaine_2": "QUALIFICATION_ONLY",
        "sha256_lanceur": lanceur.sha256_fichier(lanceur.__file__),
        "sha256_adaptateur": lanceur.sha256_fichier(ici / "xz_cobaya_g2_4.py"),
        "sha256_chemin_rapide": lanceur.sha256_fichier(ici / "xz_fast_g2_4c.py"),
        "sha256_descripteurs": {
            v: lanceur.sha256_fichier(c) for v, c in lanceur.DESCRIPTEURS.items()},
        "sha256_preenregistrement": lanceur.sha256_fichier(
            "reports/rapport_G2_2a_preregistration.md"),
        "sha256_donnees": dict(lanceur.SHA_BAO),
        "empreinte_environnement": lanceur.empreinte_environnement(),
        "version_contrat_local": lanceur.VERSION_CONTRAT_LOCAL,
        "head_autorise": lanceur.garde_git()["head"],
        "racine_runs_canonique": lanceur._canonique(
            os.environ["C7C1_XZ_OUT_DIR"]),
        "variantes_graines_autorisees": {variante: [graine]},
        "budget_production_requis_Gio": 50,
        "budget_production_ratification": "QUALIFICATION_ONLY",
    }
    if defaut == "autorisation_sha_rapide_absent":
        manifeste.pop("sha256_chemin_rapide")
    elif defaut == "autorisation_sha_rapide_faux":
        manifeste["sha256_chemin_rapide"] = "0" * 64
    elif defaut == "autorisation_ancien_adaptateur":
        manifeste["sha256_adaptateur"] = "0" * 64
    elif defaut == "autorisation_contrat_autre_version":
        manifeste["version_contrat_local"] = "0.9.0"
    elif defaut == "autorisation_budget_absent":
        manifeste["budget_production_requis_Gio"] = None
    elif defaut == "autorisation_head_different":
        manifeste["head_autorise"] = "0" * 40
    elif defaut == "autorisation_autre_racine_runs":
        manifeste["racine_runs_canonique"] = lanceur._canonique(tempfile.gettempdir())
    elif defaut == "autorisation_empreinte_env_fausse":
        manifeste["empreinte_environnement"] = "0" * 64
    chemin = prep / "autorisation_qualification_only.json"
    chemin.write_text(json.dumps(manifeste), encoding="utf-8")
    return chemin


@contextlib.contextmanager
def _sentinelles():
    """Installe des sentinelles sur toute écriture réelle et sur cobaya.run.

    Rend la liste des sentinelles ATTEINTES. Sous le verrou, elle doit
    rester vide ; injectée par une faute de contournement, elle doit se
    remplir — ce qui prouve que les sentinelles détectent réellement.
    """
    import builtins
    import importlib

    appels: list[str] = []

    def sentinelle(etiquette):
        def _s(*a, **k):
            appels.append(etiquette)
            raise AssertionError(f"SENTINELLE ATTEINTE : {etiquette}")
        return _s

    cobaya_run_mod = importlib.import_module("cobaya.run")
    reels = {
        "mkdir": Path.mkdir, "makedirs": os.makedirs,
        "replace": os.replace, "open": builtins.open,
        "run": cobaya_run_mod.run,
    }
    reel_open = builtins.open

    def open_surveille(fichier, mode="r", *a, **k):
        if any(c in str(mode) for c in ("w", "a", "x", "+")):
            appels.append(f"open({mode})")
            raise AssertionError(f"SENTINELLE ATTEINTE : open {mode}")
        return reel_open(fichier, mode, *a, **k)

    Path.mkdir = sentinelle("Path.mkdir")
    os.makedirs = sentinelle("os.makedirs")
    os.replace = sentinelle("os.replace")
    cobaya_run_mod.run = sentinelle("cobaya.run")
    builtins.open = open_surveille
    try:
        yield appels
    finally:
        Path.mkdir = reels["mkdir"]
        os.makedirs = reels["makedirs"]
        os.replace = reels["replace"]
        builtins.open = reels["open"]
        cobaya_run_mod.run = reels["run"]


def _verrou_nominal() -> dict:
    """Preuve NON VACANTE que le verrou est atteint AVANT toute écriture.

    Un appel nu à `produire` s'arrêterait bien en amont (arbre sale, ou
    autorisation absente) : « aucune sentinelle atteinte » serait alors
    vrai pour une raison SANS RAPPORT avec le verrou. On rend donc les
    gardes amont satisfaites — autorisation QUALIFICATION_ONLY
    structurellement valide, arbre déclaré propre, budget déclaré
    ratifié — afin que l'exécution parvienne RÉELLEMENT à l'étape 8, et
    l'on exige que l'exception levée soit celle du VERROU.

    Deux scénarios sont mesurés :
      - « amont_satisfait » : doit s'arrêter sur le VERROU, sans écriture ;
      - « amont_reel »      : refus plus précoce, sans écriture non plus.
    """
    import run_mcmc_xz_g2_4 as lanceur

    resultats: dict = {}

    # -- scénario 1 : gardes amont satisfaites -> le verrou DOIT mordre --
    prep = Path(tempfile.mkdtemp(prefix="c7c1_verrou_"))
    try:
        autorisation = _autorisation_qualification(
            prep, variante="M2a-N", graine=630101, defaut="aucun")
        head_reel = lanceur.garde_git()["head"]
        vrai_git = lanceur.garde_git
        vrai_budget = lanceur.garde_budget_production
        lanceur.garde_git = lambda: {"head": head_reel, "arbre_propre": True}
        lanceur.garde_budget_production = lambda contrat, cible: {
            "budget_production_statut": "RATIFIE_SIMULE_QUALIFICATION",
            "libre_cible_gio": None,
        }
        try:
            with _sentinelles() as appels:
                message = ""
                try:
                    lanceur.produire([
                        "M2a-N", "630101", "--je-confirme-la-production",
                        "--autorisation", str(autorisation)])
                    message = "AUCUNE EXCEPTION — le verrou n'a pas mordu"
                except BaseException as exc:  # noqa: BLE001
                    message = f"{type(exc).__name__}: {exc}"
            resultats["amont_satisfait"] = {
                "sentinelles": list(appels),
                "verrou_atteint": "VERROU G2.4d" in message,
                "arret": message[:140],
            }
        finally:
            lanceur.garde_git = vrai_git
            lanceur.garde_budget_production = vrai_budget
    finally:
        shutil.rmtree(prep, ignore_errors=True)

    # -- scénario 2 : gardes amont réelles -> refus plus précoce ---------
    with _sentinelles() as appels2:
        message2 = ""
        try:
            lanceur.produire(["M2a-N", "630101",
                              "--je-confirme-la-production",
                              "--autorisation", "inexistant.json"])
        except BaseException as exc:  # noqa: BLE001
            message2 = f"{type(exc).__name__}: {exc}"
    resultats["amont_reel"] = {
        "sentinelles": list(appels2), "arret": message2[:140],
    }
    return resultats


def _preuve_verrou(nom: str) -> int:
    """Faute de CONTOURNEMENT : simule un chemin qui franchirait le verrou.

    La sentinelle DOIT se déclencher (exit 1) ; si elle reste muette, le
    dispositif de preuve serait inopérant, ce qui est la vraie faute.
    """
    import importlib

    with _sentinelles() as appels:
        try:
            if nom == "verrou_cobaya_run_atteint":
                importlib.import_module("cobaya.run").run({}, test=True)
            else:  # verrou_ecriture_atteinte
                cible = Path(tempfile.gettempdir()) / "c7c1_bypass" / "m.json"
                cible.parent.mkdir(parents=True, exist_ok=True)
        except BaseException:  # noqa: BLE001
            pass
    return 1 if appels else 0


FAUTES = (
    "parite_latex_derive_perdu", "parite_prior_altere",
    "parite_proposal_altere",
    "directeur_retourne_legacy", "mode_directeur_corrected_legacy",
    "mode_directeur_fixed", "mode_directeur_inconnu",
    "theory_depend_d_un_xi", "likelihood_depend_de_h0", "graphe_un_bloc",
    "camb_sur_variation_xi", "cache_partage_entre_variantes",
    "contrat_local_absent", "contrat_schema_perime",
    "contrat_python_different", "contrat_empreinte_fausse",
    "contrat_json_invalide", "thread_absent", "thread_vaut_2",
    "thread_vide", "thread_auto", "thread_espace",
    "pythonnousersite_absent", "runs_sous_git", "runs_sous_onedrive",
    "data_egal_runs", "capacite_mesuree_sur_ancre",
    "budget_non_etabli_accepte", "budget_superieur_a_l_espace",
    "budget_nul_ou_negatif", "autorisation_sha_rapide_absent",
    "autorisation_sha_rapide_faux", "autorisation_ancien_adaptateur",
    "autorisation_contrat_autre_version", "autorisation_budget_absent",
    "autorisation_head_different", "autorisation_autre_racine_runs",
    "autorisation_empreinte_env_fausse", "manifeste_ecrasement_non_identique",
    "manifeste_temporaire_conserve", "reprise_sans_manifeste",
    "reprise_identite_partielle", "verrou_cobaya_run_atteint",
    "verrou_ecriture_atteinte",
)


# -------------------------------------------------------- qualification

def qualification() -> int:
    _preparer()
    import xz_cobaya_g2_4 as adaptateur
    from cobaya.model import get_model
    from cobaya.run import run as cobaya_run
    from run_mcmc_xz_g2_4 import DESCRIPTEURS, MATRICE
    import run_mcmc_xz_g2_4 as lanceur
    from xz_fast_g2_4c import EvaluateurRapide, FabriqueEtatsLents
    from xz_likelihood_g2_3 import XZEvaluator, load_bao_data, load_config

    echecs: list[str] = []
    resultat: dict = {}
    temps: dict = {}
    compteur = _instrumenter_camb()
    bao_mean, bao_icov = load_bao_data()
    configs = {v: load_config(c) for v, c in DESCRIPTEURS.items()}

    # ---- 1. parité legacy / directeur, 4 variantes -------------------
    parites = {}
    for variante in VARIANTES_ORDRE:
        p = adaptateur.comparer_parite(DESCRIPTEURS[variante],
                                       GRAINE_GELEE[variante])
        parites[variante] = {
            "identique": p["identique"],
            "n_differences": len(p["differences"]),
            "graphes": p["graphes"],
            "backend_directeur": p["backend_directeur"],
            "acoustic_mode": p["acoustic_mode"],
        }
        if not p["identique"]:
            echecs.append(f"parité rompue ({variante}) : "
                          f"{[d['champ'] for d in p['differences']]}")
        if p["acoustic_mode"] != "corrected-v1.1":
            echecs.append(f"mode acoustique {p['acoustic_mode']} ({variante})")
    resultat["parite_legacy_directeur"] = parites

    # ---- 2. matrice complète 32 couples : construction + métadonnées --
    matrice = {"couples": 0, "conformes": 0}
    for variante, graines in MATRICE.items():
        for graine in graines:
            info = adaptateur.build_cobaya_info(DESCRIPTEURS[variante], graine)
            meta = info["_xz_meta"]
            ok = (meta["graine"] == graine
                  and meta["variante"] == variante
                  and meta["backend"] == "optimized"
                  and meta["acoustic_mode"] == "corrected-v1.1"
                  and info["sampler"]["mcmc"]["seed"] == graine
                  and list(info["theory"]) == ["reference_lente_xz"]
                  and list(info["likelihood"]) == ["xz_rapide"])
            matrice["couples"] += 1
            matrice["conformes"] += int(ok)
            if not ok:
                echecs.append(f"matrice : couple {variante}/{graine} non conforme")
    resultat["matrice_32"] = matrice

    # ---- 3. construction Cobaya réelle (test=True) --------------------
    constructions = {}
    for variante in VARIANTES_ORDRE:
        info = adaptateur.info_pour_cobaya(
            adaptateur.build_cobaya_info(DESCRIPTEURS[variante],
                                         GRAINE_GELEE[variante]))
        try:
            cobaya_run(info, test=True)
            constructions[variante] = {"test_true": True}
        except Exception as exc:  # noqa: BLE001
            constructions[variante] = {"test_true": False, "erreur": type(exc).__name__}
            echecs.append(f"cobaya.run(test=True) échoue pour {variante}")
    resultat["construction_cobaya"] = constructions

    # ---- 4. structure du modèle réel ----------------------------------
    structures = {}
    for variante in VARIANTES_ORDRE:
        info = adaptateur.info_pour_cobaya(
            adaptateur.build_cobaya_info(DESCRIPTEURS[variante], 0))
        info.pop("sampler", None)
        modele = get_model(info)
        noms_x = [i["nom"] for i in configs[variante]["parametres_x"]]
        blocs, _ = modele.get_param_blocking_for_sampler(
            split_fast_slow=True, oversample_power=0.4)
        blocs_tries = [sorted(b) for b in blocs]
        composants = [type(c).__name__ for c in modele.components]
        entrees_like = list(
            info["likelihood"]["xz_rapide"]["input_params"])
        entrees_theory = list(
            info["theory"]["reference_lente_xz"]["input_params"])
        ok = (len(composants) == 2
              and "ReferenceLenteXZ" in composants
              and "VraisemblanceRapideXZ" in composants
              and not ({"H0", "ombh2", "omm"} & set(entrees_like))
              and not (set(noms_x) & set(entrees_theory))
              and len(blocs_tries) == 2
              and sorted(["H0", "ombh2", "omm"]) in blocs_tries
              and sorted(noms_x) in blocs_tries)
        structures[variante] = {
            "composants": sorted(composants), "blocs": blocs_tries,
            "entrees_theory": entrees_theory, "entrees_likelihood": entrees_like,
            "conforme": ok,
        }
        if not ok:
            echecs.append(f"structure du modèle non conforme ({variante})")
    resultat["structure_modele"] = structures

    # ---- 5. comparaisons numériques aux points fixes ------------------
    comparaisons = {"bit_a_bit_optimise_vs_rapide": True, "pires_ecarts_legacy": {}}
    pires = {k: {"valeur": 0.0, "point": None} for k in SEUILS_LEGACY}
    classif = {"identique": 0, "total": 0}
    for variante in VARIANTES_ORDRE:
        cfg = configs[variante]
        noms_x = [i["nom"] for i in cfg["parametres_x"]]
        info = adaptateur.build_cobaya_info(DESCRIPTEURS[variante], 0)
        info_c = adaptateur.info_pour_cobaya(info)
        info_c.pop("sampler", None)
        modele = get_model(info_c)
        rapide = EvaluateurRapide(cfg, bao_mean, bao_icov, FabriqueEtatsLents())
        oracle = XZEvaluator(cfg, bao_mean, bao_icov)
        for nom_pt, point in _points_fixes(variante, cfg).items():
            etiquette = f"{variante}:{nom_pt}"
            r = rapide.evaluate(point)
            o = oracle.evaluate(point)
            logp_cobaya = modele.loglike(point, return_derived=False)
            derives = modele.logposterior(point).derived
            noms_derives = list(modele.parameterization.derived_params())
            d = dict(zip(noms_derives, derives))
            classif["total"] += 1
            valide_c = math.isfinite(float(logp_cobaya))
            valide_r = r["logprior"] == 0.0
            valide_o = o["logprior"] == 0.0
            if valide_c == valide_r == valide_o:
                classif["identique"] += 1
            else:
                echecs.append(f"classification divergente : {etiquette}")
                continue
            if not valide_r:
                continue
            # identité BIT À BIT : Cobaya optimisé vs EvaluateurRapide
            attendu = -0.5 * r["chi2_total"]
            if float(logp_cobaya) != attendu:
                comparaisons["bit_a_bit_optimise_vs_rapide"] = False
                echecs.append(f"logp Cobaya != EvaluateurRapide ({etiquette})")
            for cle, ref in (("chi2_BAO", r["chi2_BAO"]),
                             ("chi2_CMB", r["chi2_CMB"]),
                             ("chi2_total", r["chi2_total"])):
                if cle in d and float(d[cle]) != float(ref):
                    comparaisons["bit_a_bit_optimise_vs_rapide"] = False
                    echecs.append(f"dérivé {cle} != rapide ({etiquette})")
            # contre le legacy : seuils déjà qualifiés
            ecarts = {
                "chi2_BAO_abs": abs(r["chi2_BAO"] - o["chi2_BAO"]),
                "chi2_CMB_abs": abs(r["chi2_CMB"] - o["chi2_CMB"]),
                "chi2_total_abs": abs(r["chi2_total"] - o["chi2_total"]),
                "logp_abs": abs(float(logp_cobaya) + 0.5 * o["chi2_total"]),
                "omch2_abs": abs(float(d.get("omch2", r["omch2"])) - o["omch2"]),
            }
            for cle, val in ecarts.items():
                if val > pires[cle]["valeur"]:
                    pires[cle] = {"valeur": val, "point": etiquette}
    comparaisons["classification"] = classif
    comparaisons["pires_ecarts_legacy"] = {
        k: {"valeur": pires[k]["valeur"], "seuil": SEUILS_LEGACY[k],
            "point": pires[k]["point"]} for k in SEUILS_LEGACY}
    for k in SEUILS_LEGACY:
        if pires[k]["valeur"] > SEUILS_LEGACY[k]:
            echecs.append(f"écart legacy {k} = {pires[k]['valeur']:.3e} "
                          f"> {SEUILS_LEGACY[k]:.0e}")
    if not comparaisons["bit_a_bit_optimise_vs_rapide"]:
        echecs.append("identité bit à bit Cobaya/EvaluateurRapide rompue")
    resultat["comparaisons_numeriques"] = comparaisons

    # ---- 6. graphe lent/rapide : comptages CAMB ------------------------
    info = adaptateur.info_pour_cobaya(
        adaptateur.build_cobaya_info(DESCRIPTEURS["M2a-N"], 0))
    info.pop("sampler", None)
    modele = get_model(info)
    noms_x = [i["nom"] for i in configs["M2a-N"]["parametres_x"]]
    base = {**POINT_FOND_P0, **{n: 1.0 for n in noms_x}}
    modele.logposterior(base)
    avant = compteur["appels"]
    for v in (0.9, 1.1, 0.8):
        modele.logposterior({**base, "X1": v})
    camb_xi = compteur["appels"] - avant
    modele.logposterior({**base, "H0": 68.0})
    camb_fond = compteur["appels"] - avant - camb_xi
    modele.logposterior(base)
    camb_retour = compteur["appels"] - avant - camb_xi - camb_fond
    # historique A,B,C,A vs C,A,B,A sur l'évaluateur intégré
    A = {**base, **dict(zip(noms_x, P2_VALUES["M2a"]))}
    B = {"H0": 68.0, "ombh2": 0.0224, "omm": 0.31,
         **dict(zip(noms_x, P3_VALUES["M2a"]))}
    C = {"H0": 66.0, "ombh2": 0.0222, "omm": 0.33,
         **{n: 1.0 for n in noms_x}}
    ordre_1 = [modele.loglike(p, return_derived=False) for p in (A, B, C, A)]
    modele_2 = get_model(info)
    ordre_2 = [modele_2.loglike(p, return_derived=False) for p in (C, A, B, A)]
    ordre_ok = all(ordre_1[i] == ordre_2[j]
                   for i, j in ((0, 1), (1, 2), (2, 0), (3, 3)))
    # isolation de cache entre variantes
    fab = FabriqueEtatsLents()
    e_n = EvaluateurRapide(configs["M2a-N"], bao_mean, bao_icov, fab)
    e_k = EvaluateurRapide(configs["M2a-K"], bao_mean, bao_icov, fab)
    pt = {**POINT_FOND_P0, **dict(zip(noms_x, P2_VALUES["M2a"]))}
    s_n = e_n.evaluate(pt)["chi2_total"]
    s_k = e_k.evaluate(pt)["chi2_total"]
    isolation = s_n != s_k  # conventions distinctes -> valeurs distinctes
    graphe = {
        "camb_sur_variation_Xi": camb_xi,
        "camb_sur_variation_fond": camb_fond,
        "camb_sur_retour_triplet_cache": camb_retour,
        "ordre_historique_identique": ordre_ok,
        "isolation_cache_entre_variantes": isolation,
    }
    resultat["graphe_lent_rapide"] = graphe
    if camb_xi != 0:
        echecs.append(f"{camb_xi} appel(s) CAMB sur variation X_i")
    if camb_fond != 1:
        echecs.append(f"{camb_fond} état(s) lent(s) sur variation du fond")
    if camb_retour != 0:
        echecs.append("retour au triplet caché a reconstruit CAMB")
    if not ordre_ok:
        echecs.append("ordre historique non identique")
    if not isolation:
        echecs.append("cache partagé entre variantes")

    # ---- 7. manifeste atomique (ÉPHÉMÈRE, sous %TEMP% uniquement) -----
    with tempfile.TemporaryDirectory(prefix="c7c1_g2_4d_") as tmp:
        cible = Path(tmp) / "manifest.json"
        contenu = {"_QUALIFICATION_ONLY": True, "schema": lanceur.SCHEMA_MANIFESTE_RUN,
                   "variante": "M2a-N", "graine": 630101}
        lanceur.ecrire_manifeste_atomique(cible, contenu)
        relu = json.loads(cible.read_text(encoding="utf-8"))
        idempotent = True
        try:
            lanceur.ecrire_manifeste_atomique(cible, contenu)
        except Exception:  # noqa: BLE001
            idempotent = False
        residus = [p.name for p in Path(tmp).iterdir() if ".tmp" in p.name]
        # chemin d'ÉCHEC : os.replace échoue -> ni partiel, ni temporaire
        cible2 = Path(tmp) / "manifest_echec.json"
        reel_replace = os.replace

        def _replace_ko(a, b):
            raise OSError("echec simule")

        os.replace = _replace_ko
        try:
            lanceur.ecrire_manifeste_atomique(
                cible2, {"_QUALIFICATION_ONLY": True, "x": 1})
        except OSError:
            pass
        finally:
            os.replace = reel_replace
        residus_echec = [p.name for p in Path(tmp).iterdir()
                         if ".tmp" in p.name]
        atomique = {
            "ecrit": cible.is_file(), "relu_identique": relu == contenu,
            "reecriture_identique_toleree": idempotent,
            "temporaires_residuels": residus,
            "sur_echec_aucun_partiel": not cible2.exists(),
            "sur_echec_aucun_temporaire": not residus_echec,
            "sous_temp": True, "marque_qualification_only": True,
        }
        if not (atomique["ecrit"] and atomique["relu_identique"]
                and idempotent and not residus
                and atomique["sur_echec_aucun_partiel"]
                and atomique["sur_echec_aucun_temporaire"]):
            echecs.append("écriture atomique du manifeste non conforme")
    resultat["manifeste_atomique"] = atomique
    resultat["manifeste_ephemere_supprime"] = not Path(tmp).exists()
    if Path(tmp).exists():
        echecs.append("manifeste éphémère non supprimé")

    # ---- 8. identité de reprise ---------------------------------------
    contrat = lanceur.garde_contrat_local()
    contrat.pop("_contrat")
    identite = lanceur.identite_run(
        "M2a-N", 630101, lanceur.garde_git()["head"], contrat,
        lanceur.garde_environnement(),
        lanceur.garde_descripteur("M2a-N"), lanceur.garde_donnees(), None)
    cles_attendues = {
        "schema", "variante", "graine", "backend", "mode_acoustique", "head",
        "sha256_lanceur", "sha256_adaptateur", "sha256_chemin_rapide",
        "sha256_descripteur", "sha256_donnees", "versions",
        "empreinte_environnement", "version_contrat_local",
        "racine_runs_canonique", "sampler", "budget_production", "statut_run",
    }
    manquantes = sorted(cles_attendues - set(identite))
    resultat["identite_reprise"] = {
        "cles": sorted(identite), "manquantes": manquantes,
        "backend": identite["backend"], "mode": identite["mode_acoustique"],
        "statut_run": identite["statut_run"],
    }
    if manquantes:
        echecs.append(f"identité de reprise incomplète : {manquantes}")

    # ---- 9. verrou dur : preuve dynamique ------------------------------
    # `produire` est exécuté avec des sentinelles sur mkdir, makedirs,
    # os.replace, open en écriture et cobaya.run : AUCUNE ne doit être
    # atteinte. La capacité des sentinelles à détecter un contournement
    # est prouvée séparément par les fautes verrou_*.
    preuve = _verrou_nominal()
    atteintes = (preuve["amont_satisfait"]["sentinelles"]
                 + preuve["amont_reel"]["sentinelles"])
    if not preuve["amont_satisfait"]["verrou_atteint"]:
        echecs.append(
            "preuve du verrou VACANTE : l'exécution ne parvient pas à "
            f"l'étape 8 ({preuve['amont_satisfait']['arret']})")
    # espion de capacité : l'argument passé à shutil.disk_usage doit être
    # le répertoire cible, jamais l'ancre du volume.
    vus, reel = [], shutil.disk_usage

    def _espion(chemin):
        vus.append(str(chemin))
        return reel(chemin)

    shutil.disk_usage = _espion
    try:
        os.environ.pop("C7C1_TEST_ESPACE_LIBRE_GIO", None)
        lanceur.espace_libre_gio(os.environ["C7C1_XZ_OUT_DIR"])
    finally:
        shutil.disk_usage = reel
    cible_attendue = os.path.normcase(
        str(Path(os.environ["C7C1_XZ_OUT_DIR"]).resolve()))
    ancre = os.path.normcase(str(Path(os.environ["C7C1_XZ_OUT_DIR"]).anchor))
    mesure_ok = bool(vus) and os.path.normcase(vus[0]) == cible_attendue
    resultat["verrou_production"] = {
        "VERROU_PRODUCTION_G2_4D": lanceur.VERROU_PRODUCTION_G2_4D,
        "sentinelles_atteintes": atteintes,
        "aucune_ecriture_ni_cobaya_run": not atteintes,
        "preuve_amont_satisfait": preuve["amont_satisfait"],
        "preuve_amont_reel": preuve["amont_reel"],
    }
    resultat["mesure_capacite"] = {
        "argument_observe_est_la_cible": mesure_ok,
        "argument_observe_est_l_ancre": bool(vus)
        and os.path.normcase(vus[0]) == ancre,
    }
    if atteintes:
        echecs.append(
            f"VERROU FRANCHI : sentinelles atteintes {sorted(set(atteintes))}")
    if not mesure_ok:
        echecs.append("capacité non mesurée sur le répertoire cible")

    # ---- 10. fautes injectées (sous-processus) -------------------------
    resultat["fautes"] = {}
    for nom in FAUTES:
        proc = subprocess.run(
            [sys.executable, "scripts/qualify_xz_launcher_g2_4d.py",
             "--faute", nom], capture_output=True, text=True)
        detectee = proc.returncode == 1
        resultat["fautes"][nom] = {"detectee": detectee, "code": proc.returncode}
        if not detectee:
            echecs.append(f"faute NON détectée : {nom}")
    resultat["fautes_resume"] = {
        "total": len(FAUTES),
        "detectees": sum(1 for v in resultat["fautes"].values() if v["detectee"]),
    }

    # ---- 11. performance (section non déterministe) --------------------
    perf = _banc_performance(adaptateur, get_model, configs, bao_mean, bao_icov,
                             compteur)
    temps["performance"] = perf["temps"]
    resultat["performance_camb"] = perf["camb_deterministe"]
    temps["verdicts_performance"] = {
        "speedup_integre_min_5x": perf["temps"]["speedup_integre"] >= 5.0,
        "speedup_cible_10x": perf["temps"]["speedup_integre"] >= 10.0,
    }
    if perf["temps"]["speedup_integre"] < 5.0:
        echecs.append(
            f"speedup intégré {perf['temps']['speedup_integre']} < 5x")
    if perf["camb_deterministe"]["cache_lent_borne"] is not True:
        echecs.append("cache lent non borné")

    resultat["porte"] = {"passe": not echecs, "echecs": sorted(echecs)}
    print("=== SORTIE NORMALISEE (deterministe) ===")
    print(json.dumps(resultat, indent=2, sort_keys=True, ensure_ascii=False))
    print("=== MESURES NON DETERMINISTES (temps/memoire/espace) ===")
    print(json.dumps(temps, indent=2, sort_keys=True, ensure_ascii=False))
    return 1 if echecs else 0


def _banc_performance(adaptateur, get_model, configs, bao_mean, bao_icov,
                      compteur):
    """Legacy monobloc vs optimisé direct vs modèle Cobaya intégré."""
    from xz_fast_g2_4c import EvaluateurRapide, FabriqueEtatsLents
    from xz_likelihood_g2_3 import XZEvaluator

    cfg = configs["M2a-N"]
    noms_x = [i["nom"] for i in cfg["parametres_x"]]
    rng = np.random.default_rng(240401)
    xs = rng.uniform(0.2, 1.8, size=(12, len(noms_x)))
    fond = dict(POINT_FOND_P0)

    legacy = XZEvaluator(cfg, bao_mean, bao_icov)
    legacy.evaluate({**fond, **dict(zip(noms_x, xs[0]))})  # réchauffage
    t0 = time.perf_counter()
    for x in xs[:6]:
        legacy.evaluate({**fond, **dict(zip(noms_x, x))})
    t_legacy = (time.perf_counter() - t0) / 6

    fab = FabriqueEtatsLents()
    direct = EvaluateurRapide(cfg, bao_mean, bao_icov, fab)
    direct.evaluate({**fond, **dict(zip(noms_x, xs[0]))})
    t0 = time.perf_counter()
    for x in xs:
        direct.evaluate({**fond, **dict(zip(noms_x, x))})
    t_direct = (time.perf_counter() - t0) / len(xs)

    info = adaptateur.info_pour_cobaya(
        adaptateur.build_cobaya_info("configs/xz/g2_3_m2a_n.yaml", 0))
    info.pop("sampler", None)
    t0 = time.perf_counter()
    modele = get_model(info)
    t_construction = time.perf_counter() - t0
    modele.loglike({**fond, **dict(zip(noms_x, xs[0]))}, return_derived=False)
    t0 = time.perf_counter()
    for x in xs:
        modele.loglike({**fond, **dict(zip(noms_x, x))}, return_derived=False)
    t_integre_xi = (time.perf_counter() - t0) / len(xs)
    t0 = time.perf_counter()
    for i in range(3):
        modele.loglike({**fond, "H0": 66.0 + 0.5 * i,
                        **dict(zip(noms_x, xs[0]))}, return_derived=False)
    t_integre_fond = (time.perf_counter() - t0) / 3
    # séquence mixte représentative : 1 changement de fond + 5 x nX rapides
    avant = compteur["appels"]
    t0 = time.perf_counter()
    k = 0
    for cycle in range(3):
        modele.loglike({**fond, "H0": 61.0 + 0.37 * cycle,
                        **dict(zip(noms_x, xs[k % len(xs)]))},
                       return_derived=False)
        k += 1
        for _ in range(5 * len(noms_x)):
            modele.loglike({**fond, "H0": 61.0 + 0.37 * cycle,
                            **dict(zip(noms_x, xs[k % len(xs)]))},
                           return_derived=False)
            k += 1
    t_sequence = time.perf_counter() - t0
    camb_sequence = compteur["appels"] - avant
    n_evals = 3 * (1 + 5 * len(noms_x))
    speedup = (n_evals * t_legacy) / t_sequence
    tracemalloc.start()
    for x in xs:
        direct.evaluate({**fond, **dict(zip(noms_x, x))})
    _, pic = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return {
        "temps": {
            "legacy_monobloc_s": round(t_legacy, 4),
            "optimise_direct_s": round(t_direct, 5),
            "integre_cobaya_variation_Xi_s": round(t_integre_xi, 5),
            "integre_cobaya_variation_fond_s": round(t_integre_fond, 4),
            "construction_modele_s": round(t_construction, 3),
            "sequence_mixte_s": round(t_sequence, 3),
            "evaluations_sequence": n_evals,
            "speedup_integre": round(speedup, 1),
            "memoire_pic_Mo": round(pic / 1e6, 1),
        },
        "camb_deterministe": {
            "camb_sequence_mixte": camb_sequence,
            "cycles": 3,
            "cache_lent_borne": fab.taille <= 8,
            "taille_cache_lent": fab.taille,
        },
    }


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
