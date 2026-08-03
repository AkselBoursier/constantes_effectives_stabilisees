"""Qualification du chemin de production sentinelle — SENT-0B (#94, #63).

Éprouve le chemin RÉEL de l'étape 9 (répertoire, manifeste atomique,
appel Cobaya, statuts de sortie) et le confinement sentinelle, SANS
AUCUNE PRODUCTION : aucune MCMC, aucun vrai ``cobaya.run``
d'échantillonnage, aucune minimisation, aucun posterior, aucune
autorisation réelle, aucun manifeste réel sous le préfixe de production.
Le chemin post-verrou est exercé exclusivement via un SUBSTITUT contrôlé
de Cobaya, sous des répertoires temporaires hors Git. Aucune valeur de
paramètre, aucun chi2 et aucun posterior ne sont générés ni publiés.

Le couple sentinelle (M2a-N, 630101) est PROPOSÉ, PAS AUTORISÉ :
``VERROU_PRODUCTION_G2_4D`` reste True et cette porte le prouve.

PORTE AUTO-BLOQUANTE : toute attente non satisfaite conduit à
SystemExit(1) après impression du JSON normalisé.

Modes :
    (aucun argument)  : qualification complète ;
    --faute NOM       : injecte la faute NOM ; exit 1 si elle est
                        détectée (attendu), 0 si elle passe inaperçue.
"""

from __future__ import annotations

import ast
import contextlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from types import SimpleNamespace

VARIANTE_SENTINELLE = "M2a-N"
GRAINE_SENTINELLE = 630101
DATE_QUALIFICATION_UTC = "2026-08-04T00:00:00Z"
DATE_FIN_QUALIFICATION_UTC = "2026-08-04T00:00:01Z"


def _preparer():
    ici = Path(__file__).parent.parent
    os.chdir(ici)
    if "scripts" not in sys.path:
        sys.path.insert(0, "scripts")
    return ici


@contextlib.contextmanager
def _env(**valeurs):
    anciennes = {c: os.environ.get(c) for c in valeurs}
    try:
        for cle, valeur in valeurs.items():
            if valeur is None:
                os.environ.pop(cle, None)
            else:
                os.environ[cle] = str(valeur)
        yield
    finally:
        for cle, valeur in anciennes.items():
            if valeur is None:
                os.environ.pop(cle, None)
            else:
                os.environ[cle] = valeur


# ------------------------------------------------- substitut de Cobaya

class SubstitutCobaya:
    """Substitut CONTRÔLÉ de ``cobaya.run`` — jamais un échantillonnage.

    Ne produit AUCUNE valeur de paramètre, AUCUN chi2, AUCUN posterior :
    il rend seulement un objet porteur d'un attribut ``converged`` (ou en
    est privé), ou lève l'exception demandée. Il enregistre l'information
    reçue pour vérification structurelle.
    """

    def __init__(self, comportement, converged=True):
        self.comportement = comportement
        self.converged = converged
        self.appels: list[dict] = []

    def __call__(self, info_cobaya, **kwargs):
        self.appels.append({
            "cles_info": sorted(k for k in info_cobaya if k != "_xz_meta"),
            "output": info_cobaya.get("output"),
            "kwargs": dict(kwargs),
        })
        if self.comportement == "capacite":
            from run_mcmc_xz_g2_4 import ArretCapaciteC7C1

            raise ArretCapaciteC7C1("haute-eau simulée (substitut)")
        if self.comportement == "technique":
            raise RuntimeError("panne technique simulée (substitut)")
        if self.comportement == "sans_attribut":
            return {}, SimpleNamespace()
        return {}, SimpleNamespace(converged=self.converged)


def _manifeste_qualification(lanceur) -> dict:
    """Identité de run COMPLÈTE, marquée QUALIFICATION_ONLY.

    Construite par la vraie ``identite_run`` : aucun champ d'identité
    n'est affaibli. Jamais écrite sous le préfixe de production — les
    tests la déposent sous %TEMP% hors Git.
    """
    contrat = lanceur.garde_contrat_local()
    contrat.pop("_contrat")
    support = lanceur.garde_support_actif(os.environ["C7C1_XZ_OUT_DIR"])
    identite = lanceur.identite_run(
        VARIANTE_SENTINELLE, GRAINE_SENTINELLE, lanceur.garde_git()["head"],
        contrat, lanceur.garde_environnement(),
        lanceur.garde_descripteur(VARIANTE_SENTINELLE),
        lanceur.garde_donnees(),
        date_creation_utc=DATE_QUALIFICATION_UTC,
        sha256_autorisation="0" * 64,
        budget_requis_gio=lanceur.BUDGET_TOTAL_RATIFIE_GIO,
        reference_ratification_budget=lanceur.REFERENCE_RATIFICATION_BUDGET,
        support_actif_identite_expurgee=support["identite_expurgee"])
    identite["_QUALIFICATION_ONLY"] = True
    return identite


def _info_execution(lanceur, prefixe: str) -> dict:
    """Information d'exécution comme l'étape 9 la construit réellement."""
    import xz_cobaya_g2_4 as adaptateur

    observateur, _ = lanceur.creer_observateur_capacite(
        os.environ["C7C1_XZ_OUT_DIR"], VARIANTE_SENTINELLE,
        f"g2_4/P_WS/{VARIANTE_SENTINELLE}/s{GRAINE_SENTINELLE}")
    info = adaptateur.info_pour_cobaya(lanceur.garde_injection_observateur(
        adaptateur.build_cobaya_info(
            lanceur.DESCRIPTEURS[VARIANTE_SENTINELLE], GRAINE_SENTINELLE),
        observateur))
    info["output"] = prefixe
    return info


def _executer_simule(lanceur, tmp: Path, comportement, converged=True,
                     manifeste=None):
    """Exécute l'étape 9 sous %TEMP% avec le substitut demandé.

    La substitution se fait UN NIVEAU SOUS le point d'appel du lanceur :
    ``cobaya.run.run`` est remplacé, si bien que le vrai
    ``_lancer_cobaya_production`` — et donc la convention G1 ``resume=True``
    — est réellement exercé. Charger le module ``cobaya.run`` n'exécute
    aucun échantillonnage ; seule sa fonction est remplacée, puis
    restaurée.
    """
    import importlib

    prefixe = tmp / "g2_4_qualification" / "sent0" / "run" / "chain"
    substitut = SubstitutCobaya(comportement, converged=converged)
    cobaya_run_mod = importlib.import_module("cobaya.run")
    reel = cobaya_run_mod.run
    cobaya_run_mod.run = substitut
    try:
        with _env(C7C1_TEST_DATE_FIN_UTC=DATE_FIN_QUALIFICATION_UTC):
            resultat = lanceur.executer_production_sentinelle(
                manifeste if manifeste is not None
                else _manifeste_qualification(lanceur),
                _info_execution(lanceur, str(prefixe)), prefixe)
    finally:
        cobaya_run_mod.run = reel
    return resultat, substitut, prefixe


# --------------------------------------------------------------- fautes

def executer_faute(nom: str) -> int:  # noqa: C901 - table de fautes
    """Chaque faute doit être détectée (exit 1). Exit 0 = non détectée."""
    _preparer()
    import run_mcmc_xz_g2_4 as lanceur
    from run_mcmc_xz_g2_4 import ArretCapaciteC7C1, GardeErreur

    def _detecte_message(fn, fragment: str) -> int:
        try:
            fn()
            return 0
        except (GardeErreur, ArretCapaciteC7C1) as exc:
            return 1 if fragment in str(exc) else 0
        except Exception:  # noqa: BLE001 - autre cause : non probant
            return 0

    # ---- confinement sentinelle -----------------------------------------
    if nom in ("sentinelle_630102_acceptee", "sentinelle_m2ak_acceptee",
               "sentinelle_m2bn_acceptee", "sentinelle_m2bk_acceptee"):
        couple = {
            "sentinelle_630102_acceptee": ("M2a-N", 630102),
            "sentinelle_m2ak_acceptee": ("M2a-K", 630201),
            "sentinelle_m2bn_acceptee": ("M2b-N", 630301),
            "sentinelle_m2bk_acceptee": ("M2b-K", 630401),
        }[nom]
        return _detecte_message(
            lambda: lanceur.garde_perimetre_sentinelle(*couple),
            "hors périmètre sentinelle")
    if nom == "garde_sentinelle_vacante":
        # MUTATION : la garde est neutralisée. Le refus « hors périmètre »
        # doit DISPARAÎTRE pour un couple non sentinelle — preuve que les
        # tests de confinement mordent sur la garde réelle, pas sur un
        # refus fortuit d'une autre garde.
        avant = _detecte_message(
            lambda: lanceur.garde_perimetre_sentinelle("M2a-K", 630201),
            "hors périmètre sentinelle")
        lanceur.garde_perimetre_sentinelle = lambda variante, graine: None
        apres = _detecte_message(
            lambda: lanceur.garde_perimetre_sentinelle("M2a-K", 630201),
            "hors périmètre sentinelle")
        return 1 if (avant == 1 and apres == 0) else 0
    if nom == "produire_hors_sentinelle_atteint_l_autorisation":
        # INTÉGRATION : dans `produire`, la garde 4 bis doit mordre AVANT
        # l'autorisation (étape 5). On satisfait l'arbre Git par le
        # harnais et on exige l'arrêt sur la cause sentinelle exacte.
        head_reel = lanceur.garde_git()["head"]
        vrai_git = lanceur.garde_git
        lanceur.garde_git = lambda: {"head": head_reel, "arbre_propre": True}
        try:
            return _detecte_message(
                lambda: lanceur.produire(
                    ["M2a-K", "630201", "--je-confirme-la-production",
                     "--autorisation", "inexistant.json"]),
                "hors périmètre sentinelle")
        finally:
            lanceur.garde_git = vrai_git

    # ---- statuts de sortie ----------------------------------------------
    if nom == "retour_sans_exception_classe_converge":
        # Le substitut rend la main SANS attribut converged : le statut
        # doit être FIN_SANS_CONVERGENCE — jamais CONVERGE.
        with tempfile.TemporaryDirectory(prefix="c7c1_sent0_") as tmp:
            resultat, _, _ = _executer_simule(
                lanceur, Path(tmp), "sans_attribut")
        return 1 if (resultat["statut_run"]
                     == lanceur.STATUT_RUN_FIN_SANS_CONVERGENCE
                     and resultat["converged_cobaya"] is False) else 0
    if nom == "converged_non_canonique_classe_converge":
        # converged = 1 (entier vrai) : PAS ``is True`` -> jamais CONVERGE.
        with tempfile.TemporaryDirectory(prefix="c7c1_sent0_") as tmp:
            resultat, _, _ = _executer_simule(
                lanceur, Path(tmp), "nominal", converged=1)
        return 1 if (resultat["statut_run"]
                     == lanceur.STATUT_RUN_FIN_SANS_CONVERGENCE) else 0
    if nom == "capacite_reclassee":
        with tempfile.TemporaryDirectory(prefix="c7c1_sent0_") as tmp:
            try:
                _executer_simule(lanceur, Path(tmp), "capacite")
                return 0  # l'exception aurait dû se propager
            except ArretCapaciteC7C1:
                manifeste = json.loads(
                    (Path(tmp) / "g2_4_qualification" / "sent0" / "run"
                     / "manifest.json").read_text(encoding="utf-8"))
            except Exception:  # noqa: BLE001 - reclassée : faute non détectée
                return 0
        return 1 if (manifeste["statut_run"]
                     == lanceur.STATUT_RUN_INTERROMPU_CAPACITE
                     and manifeste["converged_cobaya"] is False) else 0
    if nom == "echec_technique_reclasse":
        with tempfile.TemporaryDirectory(prefix="c7c1_sent0_") as tmp:
            try:
                _executer_simule(lanceur, Path(tmp), "technique")
                return 0
            except RuntimeError:
                manifeste = json.loads(
                    (Path(tmp) / "g2_4_qualification" / "sent0" / "run"
                     / "manifest.json").read_text(encoding="utf-8"))
            except Exception:  # noqa: BLE001
                return 0
        return 1 if (manifeste["statut_run"]
                     == lanceur.STATUT_RUN_ECHEC_TECHNIQUE
                     and manifeste["statut_run"]
                     != lanceur.STATUT_RUN_INTERROMPU_CAPACITE) else 0
    if nom == "traces_supprimees_apres_echec":
        # INJECTION : un nettoyage fautif efface le répertoire après une
        # panne. La détection = les traces existent avec le code réel et
        # disparaîtraient avec le nettoyage injecté.
        import shutil as _shutil

        with tempfile.TemporaryDirectory(prefix="c7c1_sent0_") as tmp:
            try:
                _executer_simule(lanceur, Path(tmp), "technique")
            except RuntimeError:
                pass
            repertoire = Path(tmp) / "g2_4_qualification" / "sent0" / "run"
            traces_conservees = (repertoire / "manifest.json").is_file()
            _shutil.rmtree(repertoire)  # le nettoyage FAUTIF simulé
            traces_apres_nettoyage = (repertoire / "manifest.json").is_file()
        return 1 if (traces_conservees and not traces_apres_nettoyage) else 0

    # ---- manifeste : cycle de vie ---------------------------------------
    if nom in ("converge_sans_drapeau_explicite", "interruption_reclassee",
               "champ_scientifique_modifie", "champ_runtime_inconnu",
               "manifeste_corrompu_mis_a_jour",
               "manifeste_non_conforme_mis_a_jour", "statut_final_reecrase"):
        with tempfile.TemporaryDirectory(prefix="c7c1_sent0_") as tmp:
            chemin = Path(tmp) / "manifest.json"
            manifeste = _manifeste_qualification(lanceur)
            if nom == "manifeste_corrompu_mis_a_jour":
                chemin.write_text("{ corrompu", encoding="utf-8")
                return _detecte_message(
                    lambda: lanceur.mettre_a_jour_manifeste_runtime(
                        chemin, {"statut_run":
                                 lanceur.STATUT_RUN_ECHEC_TECHNIQUE}),
                    "corrompu")
            if nom == "manifeste_non_conforme_mis_a_jour":
                ampute = {k: v for k, v in manifeste.items() if k != "params"}
                chemin.write_text(json.dumps(ampute), encoding="utf-8")
                return _detecte_message(
                    lambda: lanceur.mettre_a_jour_manifeste_runtime(
                        chemin, {"statut_run":
                                 lanceur.STATUT_RUN_ECHEC_TECHNIQUE}),
                    "non conforme")
            lanceur.ecrire_manifeste_atomique(chemin, manifeste)
            if nom == "converge_sans_drapeau_explicite":
                return _detecte_message(
                    lambda: lanceur.mettre_a_jour_manifeste_runtime(
                        chemin, {"statut_run": lanceur.STATUT_RUN_CONVERGE}),
                    "converged_cobaya is True")
            if nom == "interruption_reclassee":
                lanceur.mettre_a_jour_manifeste_runtime(chemin, {
                    "statut_run": lanceur.STATUT_RUN_INTERROMPU_CAPACITE,
                    "converged_cobaya": False,
                    "date_fin_utc": DATE_FIN_QUALIFICATION_UTC,
                    "detail_fin": "interruption simulee"})
                return _detecte_message(
                    lambda: lanceur.mettre_a_jour_manifeste_runtime(
                        chemin, {"statut_run": lanceur.STATUT_RUN_CONVERGE,
                                 "converged_cobaya": True}),
                    "jamais réécrit")
            if nom == "champ_scientifique_modifie":
                return _detecte_message(
                    lambda: lanceur.mettre_a_jour_manifeste_runtime(
                        chemin, {"statut_run":
                                 lanceur.STATUT_RUN_ECHEC_TECHNIQUE,
                                 "graine": 630102}),
                    "champs non runtime refusés")
            if nom == "champ_runtime_inconnu":
                return _detecte_message(
                    lambda: lanceur.mettre_a_jour_manifeste_runtime(
                        chemin, {"commentaire_libre": "interdit"}),
                    "champs non runtime refusés")
            if nom == "statut_final_reecrase":
                lanceur.mettre_a_jour_manifeste_runtime(chemin, {
                    "statut_run": lanceur.STATUT_RUN_ECHEC_TECHNIQUE,
                    "converged_cobaya": False,
                    "date_fin_utc": DATE_FIN_QUALIFICATION_UTC,
                    "detail_fin": "echec simule"})
                return _detecte_message(
                    lambda: lanceur.mettre_a_jour_manifeste_runtime(
                        chemin, {"statut_run":
                                 lanceur.STATUT_RUN_FIN_SANS_CONVERGENCE}),
                    "jamais réécrit")
    if nom == "collision_prefixe_etape9":
        with tempfile.TemporaryDirectory(prefix="c7c1_sent0_") as tmp:
            occupant = (Path(tmp) / "g2_4_qualification" / "sent0" / "run")
            occupant.mkdir(parents=True)
            (occupant / "chain.1.txt").write_text("occupant\n",
                                                  encoding="utf-8")
            try:
                _executer_simule(lanceur, Path(tmp), "nominal")
                detecte = 0
            except GardeErreur as exc:
                detecte = 1 if "collision" in str(exc) else 0
            intact = (occupant / "chain.1.txt").read_text(
                encoding="utf-8") == "occupant\n"
        return 1 if (detecte and intact) else 0
    if nom == "manifeste_existant_non_identique_etape9":
        # Un manifest.json étranger DANS le répertoire du run doit bloquer
        # l'étape 9 — d'abord par la collision, et, si celle-ci était
        # neutralisée, par le refus d'écrasement d'ecrire_manifeste_atomique.
        with tempfile.TemporaryDirectory(prefix="c7c1_sent0_") as tmp:
            repertoire = Path(tmp) / "g2_4_qualification" / "sent0" / "run"
            repertoire.mkdir(parents=True)
            (repertoire / "manifest.json").write_text(
                json.dumps({"schema": "etranger"}), encoding="utf-8")
            vraie_collision = lanceur.garde_collision
            lanceur.garde_collision = lambda prefixe: None  # neutralisée
            try:
                try:
                    _executer_simule(lanceur, Path(tmp), "nominal")
                    detecte = 0
                except GardeErreur as exc:
                    detecte = 1 if "écrasement refusé" in str(exc) else 0
                etranger = json.loads((repertoire / "manifest.json")
                                      .read_text(encoding="utf-8"))
            finally:
                lanceur.garde_collision = vraie_collision
        return 1 if (detecte and etranger == {"schema": "etranger"}) else 0

    # ---- verrou et écritures --------------------------------------------
    if nom == "verrou_retire":
        source = Path("scripts/run_mcmc_xz_g2_4.py").read_text(
            encoding="utf-8")
        falsifie = source.replace("VERROU_PRODUCTION_G2_4D = True",
                                  "VERROU_PRODUCTION_G2_4D = False", 1)
        return 1 if _verrou_declare(falsifie) is False else 0
    if nom == "cobaya_reel_appele":
        # Le point d'appel réel doit être INTERCEPTABLE : sous les
        # sentinelles, l'invoquer déclenche l'alarme. Prouve que la preuve
        # « aucun cobaya.run » n'est pas vacante.
        from qualify_xz_launcher_g2_4d import _sentinelles

        with _sentinelles() as appels:
            try:
                lanceur._lancer_cobaya_production({"likelihood": {}})
            except BaseException:  # noqa: BLE001
                pass
        return 1 if any("cobaya" in a for a in appels) else 0
    if nom == "ecriture_sous_verrou_atteinte":
        # INJECTION : un contournement écrirait avant le verrou ; les
        # sentinelles doivent le voir (reprise du motif G2.4d).
        from qualify_xz_launcher_g2_4d import _sentinelles

        with _sentinelles() as appels:
            try:
                cible = Path(tempfile.gettempdir()) / "c7c1_sent0_bypass"
                cible.mkdir(parents=True, exist_ok=True)
            except BaseException:  # noqa: BLE001
                pass
        return 1 if appels else 0
    raise SystemExit(f"faute inconnue : {nom}")


FAUTES = (
    "sentinelle_630102_acceptee", "sentinelle_m2ak_acceptee",
    "sentinelle_m2bn_acceptee", "sentinelle_m2bk_acceptee",
    "garde_sentinelle_vacante",
    "produire_hors_sentinelle_atteint_l_autorisation",
    "retour_sans_exception_classe_converge",
    "converged_non_canonique_classe_converge",
    "capacite_reclassee", "echec_technique_reclasse",
    "traces_supprimees_apres_echec",
    "converge_sans_drapeau_explicite", "interruption_reclassee",
    "champ_scientifique_modifie", "champ_runtime_inconnu",
    "manifeste_corrompu_mis_a_jour", "manifeste_non_conforme_mis_a_jour",
    "statut_final_reecrase", "collision_prefixe_etape9",
    "manifeste_existant_non_identique_etape9",
    "verrou_retire", "cobaya_reel_appele", "ecriture_sous_verrou_atteinte",
)


# ------------------------------------------------------------- statique

def _verrou_declare(source: str):
    for noeud in ast.parse(source).body:
        if isinstance(noeud, ast.Assign):
            for cible in noeud.targets:
                if (isinstance(cible, ast.Name)
                        and cible.id == "VERROU_PRODUCTION_G2_4D"):
                    return ast.literal_eval(noeud.value)
    return None


def _sentinelle_declaree(source: str):
    valeurs = {}
    for noeud in ast.parse(source).body:
        if isinstance(noeud, ast.Assign):
            for cible in noeud.targets:
                if isinstance(cible, ast.Name) and cible.id in (
                        "SENTINELLE_SENT0_VARIANTE", "SENTINELLE_SENT0_GRAINE"):
                    valeurs[cible.id] = ast.literal_eval(noeud.value)
    return valeurs


# ---------------------------------------------------------- qualification

def qualification() -> int:  # noqa: C901 - porte de qualification
    _preparer()
    import run_mcmc_xz_g2_4 as lanceur
    from qualify_xz_launcher_g2_4d import _verrou_nominal
    from run_mcmc_xz_g2_4 import ArretCapaciteC7C1, GardeErreur

    echecs: list[str] = []
    resultat: dict = {}

    # ---- 1. preuves statiques ------------------------------------------
    source = Path("scripts/run_mcmc_xz_g2_4.py").read_text(encoding="utf-8")
    declare = _sentinelle_declaree(source)
    resultat["statique"] = {
        "VERROU_PRODUCTION_G2_4D_source": _verrou_declare(source),
        "VERROU_PRODUCTION_G2_4D_charge": lanceur.VERROU_PRODUCTION_G2_4D,
        "sentinelle_declaree": declare,
        "statuts_finals": list(lanceur.STATUTS_RUN_FINALS),
        "champs_runtime_autorises": list(lanceur.CHAMPS_RUNTIME_AUTORISES),
    }
    if _verrou_declare(source) is not True:
        echecs.append("VERROU_PRODUCTION_G2_4D != True dans la source")
    if lanceur.VERROU_PRODUCTION_G2_4D is not True:
        echecs.append("VERROU_PRODUCTION_G2_4D != True chargé")
    if declare != {"SENTINELLE_SENT0_VARIANTE": VARIANTE_SENTINELLE,
                   "SENTINELLE_SENT0_GRAINE": GRAINE_SENTINELLE}:
        echecs.append(f"couple sentinelle déclaré inattendu : {declare}")

    # ---- 2. verrou dynamique : le CLI s'arrête AVANT toute écriture ----
    preuve = _verrou_nominal()
    sentinelles_atteintes = (preuve["amont_satisfait"]["sentinelles"]
                             + preuve["amont_reel"]["sentinelles"])
    resultat["verrou_dynamique"] = {
        "arret_amont_satisfait": preuve["amont_satisfait"]["arret"],
        "verrou_atteint": preuve["amont_satisfait"]["verrou_atteint"],
        "sentinelles_atteintes": sentinelles_atteintes,
        "qualification_only_rejetee": preuve["qualification_only_rejetee"],
    }
    if not preuve["amont_satisfait"]["verrou_atteint"]:
        echecs.append("preuve du verrou vacante : l'étape 8 n'est pas "
                      f"atteinte ({preuve['amont_satisfait']['arret']})")
    if sentinelles_atteintes:
        echecs.append(f"écriture ou cobaya.run AVANT le verrou : "
                      f"{sorted(set(sentinelles_atteintes))}")
    if preuve["qualification_only_rejetee"] is not True:
        echecs.append("QUALIFICATION_ONLY accepté par la vraie garde")

    # ---- 3. confinement : les 31 couples non sentinelles ---------------
    refus = {"total": 0, "refuses_cause_exacte": 0}
    for variante, graines in lanceur.MATRICE.items():
        for graine in graines:
            if (variante, graine) == (VARIANTE_SENTINELLE, GRAINE_SENTINELLE):
                continue
            refus["total"] += 1
            try:
                lanceur.garde_perimetre_sentinelle(variante, graine)
            except GardeErreur as exc:
                if "hors périmètre sentinelle" in str(exc):
                    refus["refuses_cause_exacte"] += 1
    try:
        lanceur.garde_perimetre_sentinelle(VARIANTE_SENTINELLE,
                                           GRAINE_SENTINELLE)
        sentinelle_admise = True
    except GardeErreur:
        sentinelle_admise = False
    resultat["confinement"] = {
        **refus, "couple_sentinelle_admis": sentinelle_admise,
        "preflight_quatre_variantes_reste_ouvert":
            "garde_perimetre_sentinelle" not in ast.dump(next(
                n for n in ast.walk(ast.parse(source))
                if isinstance(n, ast.FunctionDef) and n.name == "preflight")),
    }
    if refus["refuses_cause_exacte"] != 31 or refus["total"] != 31:
        echecs.append(f"confinement : {refus} != 31/31 refus exacts")
    if not sentinelle_admise:
        echecs.append("le couple sentinelle lui-même est refusé")
    if not resultat["confinement"]["preflight_quatre_variantes_reste_ouvert"]:
        echecs.append("la garde sentinelle contamine le preflight")

    # ---- 4. étape 9 nominale simulée (substitut, %TEMP%, hors Git) -----
    with tempfile.TemporaryDirectory(prefix="c7c1_sent0_") as tmp:
        resultat_nominal, substitut, prefixe = _executer_simule(
            lanceur, Path(tmp), "nominal", converged=True)
        repertoire = Path(prefixe).parent
        manifeste_final = json.loads(
            (repertoire / "manifest.json").read_text(encoding="utf-8"))
        objets = sorted(p.name for p in repertoire.iterdir())
        appel = substitut.appels[0] if substitut.appels else {}
        nominal = {
            "statut_final": manifeste_final["statut_run"],
            "converged_cobaya": manifeste_final["converged_cobaya"],
            "statut_retourne": resultat_nominal["statut_run"],
            "objets_crees": objets,
            "n_appels_substitut": len(substitut.appels),
            "resume_kwarg": appel.get("kwargs", {}).get("resume"),
            "output_transmis_est_le_prefixe":
                appel.get("output") == str(prefixe),
            "cles_info_transmises": appel.get("cles_info"),
            "date_creation_conservee":
                manifeste_final["date_creation_utc"] == DATE_QUALIFICATION_UTC,
            "identite_intacte":
                [c for c in lanceur.CHAMPS_MANIFESTE_RUN
                 if c not in manifeste_final] == [],
            "encodage_scientifique_conserve":
                manifeste_final["sha256_encodage_scientifique"]
                == lanceur.encodage_scientifique_gele(
                    VARIANTE_SENTINELLE, GRAINE_SENTINELLE)[
                    "sha256_encodage_scientifique"],
            "sous_temp_hors_git": True,
        }
    resultat["etape9_nominale"] = nominal
    if nominal["statut_final"] != lanceur.STATUT_RUN_CONVERGE:
        echecs.append("nominal simulé : statut != CONVERGE")
    if nominal["objets_crees"] != ["manifest.json"]:
        echecs.append(f"objets inattendus créés : {nominal['objets_crees']}")
    if nominal["n_appels_substitut"] != 1:
        echecs.append("le substitut n'a pas été appelé exactement une fois")
    if nominal["resume_kwarg"] is not True:
        echecs.append("convention G1 rompue : resume=True absent de l'appel")
    for cle in ("output_transmis_est_le_prefixe", "date_creation_conservee",
                "identite_intacte", "encodage_scientifique_conserve"):
        if nominal[cle] is not True:
            echecs.append(f"étape 9 nominale : {cle} non conforme")

    # ---- 5. étape 9 : trois autres sorties -----------------------------
    sorties = {}
    with tempfile.TemporaryDirectory(prefix="c7c1_sent0_") as tmp:
        resultat_fsc, _, _ = _executer_simule(
            lanceur, Path(tmp), "nominal", converged=False)
        sorties["retour_sans_convergence"] = resultat_fsc["statut_run"]
    with tempfile.TemporaryDirectory(prefix="c7c1_sent0_") as tmp:
        try:
            _executer_simule(lanceur, Path(tmp), "capacite")
            sorties["capacite"] = "AUCUNE_EXCEPTION"
        except ArretCapaciteC7C1:
            sorties["capacite"] = json.loads(
                (Path(tmp) / "g2_4_qualification" / "sent0" / "run"
                 / "manifest.json").read_text(encoding="utf-8"))["statut_run"]
    with tempfile.TemporaryDirectory(prefix="c7c1_sent0_") as tmp:
        try:
            _executer_simule(lanceur, Path(tmp), "technique")
            sorties["technique"] = "AUCUNE_EXCEPTION"
        except RuntimeError:
            manifeste_tech = json.loads(
                (Path(tmp) / "g2_4_qualification" / "sent0" / "run"
                 / "manifest.json").read_text(encoding="utf-8"))
            sorties["technique"] = manifeste_tech["statut_run"]
            sorties["traces_conservees_apres_echec"] = True
    resultat["etape9_sorties"] = sorties
    attendus = {
        "retour_sans_convergence": lanceur.STATUT_RUN_FIN_SANS_CONVERGENCE,
        "capacite": lanceur.STATUT_RUN_INTERROMPU_CAPACITE,
        "technique": lanceur.STATUT_RUN_ECHEC_TECHNIQUE,
    }
    for cle, attendu in attendus.items():
        if sorties.get(cle) != attendu:
            echecs.append(f"sortie {cle} : {sorties.get(cle)} != {attendu}")
    if sorties.get("traces_conservees_apres_echec") is not True:
        echecs.append("traces non conservées après échec technique")

    # ---- 6. observateur : injection minimale re-prouvée ----------------
    import xz_cobaya_g2_4 as adaptateur

    observateur, _ = lanceur.creer_observateur_capacite(
        os.environ["C7C1_XZ_OUT_DIR"], VARIANTE_SENTINELLE,
        f"g2_4/P_WS/{VARIANTE_SENTINELLE}/s{GRAINE_SENTINELLE}")
    info_avant = adaptateur.build_cobaya_info(
        lanceur.DESCRIPTEURS[VARIANTE_SENTINELLE], GRAINE_SENTINELLE)
    info_apres = lanceur.garde_injection_observateur(info_avant, observateur)
    differences = lanceur.differences_injection(info_avant, info_apres)
    resultat["observateur"] = {"differences": differences}
    if differences != ["sampler.mcmc.callback_every",
                       "sampler.mcmc.callback_function"]:
        echecs.append(f"injection non minimale : {differences}")

    # ---- 7. confidentialité des trois fichiers SENT-0 ------------------
    from qualify_xz_capacity_cap1 import _motifs_confidentiels

    motifs = _motifs_confidentiels(lanceur, os.environ["C7C1_XZ_OUT_DIR"])
    fuites: dict = {}
    fichiers = ("scripts/run_mcmc_xz_g2_4.py",
                "scripts/qualify_xz_sentinel_sent0.py",
                "reports/rapport_SENT0A_B_qualification_sentinelle.md")
    controles = []
    for relatif in fichiers:
        chemin = Path(relatif)
        if not chemin.is_file():
            continue  # le rapport peut ne pas exister au premier passage
        controles.append(chemin.name)
        texte = chemin.read_text(encoding="utf-8", errors="replace")
        for nom_motif, motif in motifs.items():
            for numero, ligne in enumerate(texte.splitlines(), 1):
                if motif.search(ligne):
                    fuites.setdefault(nom_motif, []).append(
                        f"{chemin.name}:{numero}")
    resultat["confidentialite"] = {
        "fichiers_controles": controles,
        "fuites": {k: v[:5] for k, v in sorted(fuites.items())},
        "aucune_fuite": not fuites,
    }
    if fuites:
        echecs.append(f"fuite locale dans un fichier SENT-0 : {sorted(fuites)}")

    # ---- 8. fautes injectées (sous-processus) --------------------------
    resultat["fautes"] = {}
    for nom in FAUTES:
        proc = subprocess.run(
            [sys.executable, "scripts/qualify_xz_sentinel_sent0.py",
             "--faute", nom], capture_output=True, text=True)
        detectee = proc.returncode == 1
        resultat["fautes"][nom] = {"detectee": detectee,
                                   "code": proc.returncode}
        if not detectee:
            echecs.append(f"faute NON détectée : {nom}")
    resultat["fautes_resume"] = {
        "total": len(FAUTES),
        "detectees": sum(1 for v in resultat["fautes"].values()
                         if v["detectee"]),
    }

    resultat["rappel"] = {
        "couple_sentinelle": f"{VARIANTE_SENTINELLE} / {GRAINE_SENTINELLE} "
                             "= PROPOSÉ, NON AUTORISÉ",
        "production_reelle": "FERMÉE",
        "mcmc_reelle_executee": False,
        "autorisation_reelle": False,
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
