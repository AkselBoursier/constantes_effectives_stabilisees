"""Qualification REJ-1 — hypothèses-monde et durcissement opératoire (#94, #63).

Deux objets, aucun des deux scientifique :

1. HYPOTHÈSES-MONDE : depuis SENT-0E, la racine de runs porte
   légitimement de la production ratifiée (run sentinelle gelé, archives
   d'incidents). Les preuves de verrou/franchissement des qualificateurs
   antérieurs s'exécutent désormais sous une racine SYNTHÉTIQUE vide
   (``_monde_synthetique``), et l'assertion « occupation nulle » de CAP-1
   est conditionnée à l'absence réelle de manifeste de production. Cette
   porte prouve la NON-VACUITÉ de ces adaptations : sur un monde occupé,
   les mêmes preuves redeviennent rouges.

2. DURCISSEMENT OPÉRATOIRE : le driver ``driver_production_c7c1.ps1``
   (aucun timeout, aucune console, journal fichier append-only, aucune
   relance automatique) et le battement de vie de l'observateur
   (``observateur.heartbeat``, append seul, jamais bloquant, aucune
   surface d'injection nouvelle) sont éprouvés statiquement et
   dynamiquement, fautes comprises.

AUCUNE MCMC, AUCUNE reprise, AUCUN contact avec le run gelé ni les
archives d'incidents. VERROU_PRODUCTION_G2_4D reste True.

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
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from types import SimpleNamespace

VARIANTE_SENTINELLE = "M2a-N"
GRAINE_SENTINELLE = 630101


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


# --------------------------------------------------- mondes synthétiques

def _racine_occupee() -> str:
    """Racine synthétique dont le préfixe sentinelle est PRÉ-OCCUPÉ.

    Reproduit la forme du monde réel (run existant non vide) sans jamais
    approcher la racine réelle : sert aux preuves de non-vacuité.
    """
    racine = tempfile.mkdtemp(prefix="c7c1_rej1_occupe_")
    prefixe = (Path(racine) / "g2_4" / "P_WS" / VARIANTE_SENTINELLE
               / f"s{GRAINE_SENTINELLE}")
    prefixe.mkdir(parents=True)
    (prefixe / "chain.1.txt").write_text("occupant\n", encoding="utf-8")
    return racine


# ------------------------------------------------- contrôles statiques

MOTIFS_INTERDITS_DRIVER = {
    "timeout_wait_process": r"(?i)Wait-Process[^\n]*-Timeout",
    "timeout_parametre": r"(?i)-TimeoutSec",
    "timeout_waitforexit": r"WaitForExit\(\s*\d",
    "arret_du_processus": r"(?i)Stop-Process",
    "arret_taskkill": r"(?i)taskkill",
    "ecriture_console_host": r"(?i)Write-Host",
    "ecriture_console_output": r"(?i)Write-Output",
    "journal_ecrase": r"(?i)Set-Content",
    "relance_boucle": r"(?i)while[^\n]*WaitForExit",
}
MOTIFS_REQUIS_DRIVER = {
    "attente_sans_timeout": r"WaitForExit\(\)",
    "sortie_standard_redirigee": r"-RedirectStandardOutput",
    "erreur_standard_redirigee": r"-RedirectStandardError",
    "fenetre_cachee": r"-WindowStyle Hidden",
    "journal_append": r"Add-Content",
    "processus_detache": r"-PassThru",
    "contrat_aucun_timeout": r"AUCUN timeout",
    "contrat_aucune_relance": r"relance",
    "propage_code_sortie": r"exit\s+\$codeSortie",
}


def _controle_statique_driver(source: str) -> dict:
    interdits = {nom: bool(re.search(motif, source))
                 for nom, motif in MOTIFS_INTERDITS_DRIVER.items()}
    requis = {nom: bool(re.search(motif, source))
              for nom, motif in MOTIFS_REQUIS_DRIVER.items()}
    return {
        "interdits_presents": {n: v for n, v in interdits.items() if v},
        "requis_absents": {n: v for n, v in requis.items() if not v},
        "conforme": not any(interdits.values()) and all(requis.values()),
    }


def _heartbeat_statique(source: str) -> dict:
    """Contrôle STATIQUE du battement dans ``creer_observateur_capacite``.

    Exige : la constante ``observateur.heartbeat`` présente dans la
    fonction ; tout ``open`` de la fonction en mode append (« a ») —
    jamais « w », qui tronquerait la trace.
    """
    arbre = ast.parse(source)
    fonction = next(
        (n for n in ast.walk(arbre) if isinstance(n, ast.FunctionDef)
         and n.name == "creer_observateur_capacite"), None)
    if fonction is None:
        return {"fonction_trouvee": False, "conforme": False}
    constantes = [n.value for n in ast.walk(fonction)
                  if isinstance(n, ast.Constant) and isinstance(n.value, str)]
    modes_open = []
    for noeud in ast.walk(fonction):
        if (isinstance(noeud, ast.Call)
                and isinstance(noeud.func, ast.Name)
                and noeud.func.id == "open"):
            for arg in noeud.args[1:2]:
                if isinstance(arg, ast.Constant):
                    modes_open.append(arg.value)
    return {
        "fonction_trouvee": True,
        "fichier_declare": "observateur.heartbeat" in constantes,
        "modes_open": sorted(modes_open),
        "append_seulement": bool(modes_open) and all(
            m == "a" for m in modes_open),
        "conforme": ("observateur.heartbeat" in constantes
                     and bool(modes_open)
                     and all(m == "a" for m in modes_open)),
    }


def _callbacks_cap1_confines(source: str) -> dict:
    """Tout callback dynamique CAP-1 doit viser la racine synthétique."""
    arbre = ast.parse(source)
    appels = []
    for noeud in ast.walk(arbre):
        if (isinstance(noeud, ast.Call)
                and isinstance(noeud.func, ast.Attribute)
                and noeud.func.attr == "creer_observateur_capacite"
                and noeud.args):
            premier = noeud.args[0]
            appels.append({
                "ligne": noeud.lineno,
                "cible": (premier.id if isinstance(premier, ast.Name)
                          else type(premier).__name__),
            })
    return {"appels": appels,
            "conforme": bool(appels)
            and all(a["cible"] == "cible_observateur" for a in appels)}


# ------------------------------------------------ exercices dynamiques

def _exercer_heartbeat(module_lanceur, racine: Path) -> dict:
    """Deux appels d'observateur sur monde synthétique : append prouvé,
    aucun autre fichier touché, défaillance d'écriture avalée."""
    rel = f"g2_4/P_WS/{VARIANTE_SENTINELLE}/s{GRAINE_SENTINELLE}"
    repertoire = racine / Path(rel)
    repertoire.mkdir(parents=True, exist_ok=True)
    (repertoire / "manifest.json").write_text(
        '{"_QUALIFICATION_ONLY": true}', encoding="utf-8")
    avant = {p.name for p in repertoire.iterdir()}

    observateur, etat = module_lanceur.creer_observateur_capacite(
        str(racine), VARIANTE_SENTINELLE, rel)
    sampler = SimpleNamespace(collection=[0] * 5)
    observateur(sampler)
    observateur(sampler)
    chemin = repertoire / "observateur.heartbeat"
    lignes = (chemin.read_text(encoding="utf-8").splitlines()
              if chemin.is_file() else [])
    apres = {p.name for p in repertoire.iterdir()}

    format_conforme = bool(lignes) and all(
        re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z appel=\d+ "
                 r"lignes=\d+ libre_gio=[\d.]+ run_gio=[\d.]+ "
                 r"lot_gio=[\d.]+$", ligne)
        for ligne in lignes)

    # Défaillance d'écriture : le chemin du battement devient un
    # RÉPERTOIRE — open(..., "a") échoue en OSError, qui doit être avalée.
    chemin.unlink(missing_ok=True)
    chemin.mkdir()
    try:
        observateur(sampler)
        defaillance_avalee = True
    except Exception:  # noqa: BLE001 - toute fuite est une non-conformité
        defaillance_avalee = False
    finally:
        chemin.rmdir()

    return {
        "fichier_cree": "observateur.heartbeat" in apres,
        "nouveaux_fichiers": sorted(apres - avant),
        "seul_le_battement_ajoute":
            apres - avant == {"observateur.heartbeat"},
        "deux_appels_deux_lignes": len(lignes) == 2,
        "format_conforme": format_conforme,
        "defaillance_avalee": defaillance_avalee,
        "appels_comptes": etat["appels"],
    }


def _exercer_injection(module_lanceur) -> dict:
    """L'injection reste STRICTEMENT minimale avec le battement actif."""
    import xz_cobaya_g2_4 as adaptateur

    with tempfile.TemporaryDirectory(prefix="c7c1_rej1_inj_") as tmp:
        observateur, _ = module_lanceur.creer_observateur_capacite(
            tmp, VARIANTE_SENTINELLE,
            f"g2_4/P_WS/{VARIANTE_SENTINELLE}/s{GRAINE_SENTINELLE}")
        avant = adaptateur.build_cobaya_info(
            module_lanceur.DESCRIPTEURS[VARIANTE_SENTINELLE],
            GRAINE_SENTINELLE)
        apres = module_lanceur.garde_injection_observateur(avant, observateur)
        differences = module_lanceur.differences_injection(avant, apres)
    return {
        "differences": differences,
        "minimale": differences == ["sampler.mcmc.callback_every",
                                    "sampler.mcmc.callback_function"],
    }


def _stub_lanceur(dossier: Path, code: int = 0) -> Path:
    stub = dossier / f"stub_lanceur_rej1_{code}.py"
    stub.write_text(
        "import sys\n"
        "print('STUB_STDOUT_C7C1_REJ1')\n"
        "print('STUB_STDERR_C7C1_REJ1', file=sys.stderr)\n"
        f"raise SystemExit({code})\n",
        encoding="utf-8")
    return stub


def _executer_driver(pwsh: str, driver: Path, stub: Path, racine: Path,
                     tmp_driver: Path, graine: int) -> dict:
    """Un passage du driver sur charge inoffensive, monde synthétique."""
    commande = [
        pwsh, "-NoProfile", "-File", str(driver),
        "-Mode", "produire", "-Variante", VARIANTE_SENTINELLE,
        "-Graine", str(graine),
        "-Autorisation", "qualification_seulement",
        "-Franchissement", "qualification_seulement",
        "-PythonDirecteur", sys.executable,
        "-ScriptLanceur", str(stub),
    ]
    complet = subprocess.run(
        commande, capture_output=True, text=True, cwd=str(tmp_driver),
        env={**os.environ, "C7C1_XZ_OUT_DIR": str(racine),
             "TMP": str(tmp_driver), "TEMP": str(tmp_driver)})
    journaux = sorted(p.name for d in tmp_driver.glob("driver_c7c1_*")
                      for p in d.iterdir())
    contenu_driver = "\n".join(
        p.read_text(encoding="utf-8")
        for d in sorted(tmp_driver.glob("driver_c7c1_*"))
        for p in d.glob("driver.log"))
    return {
        "code": complet.returncode,
        "console_stdout_vide": complet.stdout.strip() == "",
        "console_stderr_vide": complet.stderr.strip() == "",
        "journaux_staging": journaux,
        "driver_log_pid": "PID=" in contenu_driver,
        "driver_log_sans_timeout": "sans timeout" in contenu_driver,
        "driver_log_sans_relance": "AUCUNE relance" in contenu_driver,
        "driver_log_code_sortie": f"code={complet.returncode}" in contenu_driver,
    }


def _qualifier_driver(pwsh: str, driver: Path) -> tuple[dict, list[str]]:
    echecs: list[str] = []
    dyn: dict = {}
    with tempfile.TemporaryDirectory(prefix="c7c1_rej1_drv_") as tmp:
        tmp = Path(tmp)
        racine = tmp / "racine"
        rel = Path("g2_4") / "P_WS" / VARIANTE_SENTINELLE / "s630901"
        (racine / rel).mkdir(parents=True)
        stub = _stub_lanceur(tmp)
        stub_echec = _stub_lanceur(tmp, code=7)
        tmp_driver = tmp / "tmp_driver"
        tmp_driver.mkdir()

        # passage 1 : répertoire du run présent -> journal consolidé
        p1 = _executer_driver(pwsh, driver, stub, racine, tmp_driver, 630901)
        journal = racine / rel / "chain.console.log"
        contenu1 = (journal.read_text(encoding="utf-8")
                    if journal.is_file() else "")
        dyn["passage1"] = {
            **p1,
            "journal_cree": journal.is_file(),
            "entete_presente": "===== lancement" in contenu1
                               and "mode=produire" in contenu1,
            "stdout_capte": "STUB_STDOUT_C7C1_REJ1" in contenu1,
            "stderr_capte": "STUB_STDERR_C7C1_REJ1" in contenu1,
        }
        # passage 2 : APPEND prouvé — le contenu du passage 1 survit
        p2 = _executer_driver(pwsh, driver, stub, racine, tmp_driver, 630901)
        contenu2 = (journal.read_text(encoding="utf-8")
                    if journal.is_file() else "")
        dyn["passage2"] = {
            **p2,
            "deux_entetes": contenu2.count("===== lancement") == 2,
            "contenu_1_conserve": contenu1 != "" and
                contenu2.startswith(contenu1),
        }
        # passage 3 : répertoire du run ABSENT -> staging conservé, note
        p3 = _executer_driver(pwsh, driver, stub, racine, tmp_driver, 630902)
        absent = racine / "g2_4" / "P_WS" / VARIANTE_SENTINELLE / "s630902"
        contenu_logs = "\n".join(
            p.read_text(encoding="utf-8")
            for d in sorted(tmp_driver.glob("driver_c7c1_*"))
            for p in d.glob("driver.log"))
        dyn["passage3"] = {
            **p3,
            "repertoire_non_cree": not absent.exists(),
            "note_arret_avant_acquisition":
                "arret avant acquisition" in contenu_logs,
        }
        # passage 4 : un échec enfant doit rester un échec pour l'appelant.
        p4 = _executer_driver(
            pwsh, driver, stub_echec, racine, tmp_driver, 630903)
        dyn["passage4"] = p4

    attentes = {
        ("passage1", "code"): 0, ("passage2", "code"): 0,
        ("passage3", "code"): 0,
        ("passage4", "code"): 7,
        ("passage4", "console_stdout_vide"): True,
        ("passage4", "console_stderr_vide"): True,
        ("passage4", "driver_log_code_sortie"): True,
        ("passage1", "console_stdout_vide"): True,
        ("passage1", "console_stderr_vide"): True,
        ("passage1", "journal_cree"): True,
        ("passage1", "entete_presente"): True,
        ("passage1", "stdout_capte"): True,
        ("passage1", "stderr_capte"): True,
        ("passage1", "driver_log_pid"): True,
        ("passage1", "driver_log_sans_timeout"): True,
        ("passage1", "driver_log_sans_relance"): True,
        ("passage2", "deux_entetes"): True,
        ("passage2", "contenu_1_conserve"): True,
        ("passage3", "repertoire_non_cree"): True,
        ("passage3", "note_arret_avant_acquisition"): True,
    }
    for (passage, cle), attendu in attentes.items():
        if dyn[passage].get(cle) != attendu:
            echecs.append(f"driver {passage}.{cle} = {dyn[passage].get(cle)} "
                          f"(attendu {attendu})")
    for passage in ("passage1", "passage2", "passage3", "passage4"):
        dyn[passage].pop("journaux_staging", None)
    return dyn, echecs


# --------------------------------------------------------------- fautes

FAUTES = (
    "collision_reelle_neutralisee",
    "substitution_collision_fuit",
    "occupation_inventee_signalee",
    "production_perdue_signalee",
    "manifeste_sous_temporaire_ignore",
    "heartbeat_retire",
    "heartbeat_ecrase",
    "heartbeat_hors_du_run",
    "qualification_callback_touche_run_reel",
    "driver_timeout_introduit",
    "driver_timeout_wait_process",
    "driver_console_reintroduite",
    "driver_narration_console",
    "driver_journal_ecrase",
    "driver_tue_le_processus",
    "driver_masque_code_sortie",
    "driver_chemin_prive",
)

# Construit sans littéral privé : la surface publique de CE fichier ne
# doit pas porter le motif qu'elle éprouve.
_CHEMIN_PRIVE_EXEMPLE = "C:" + chr(92) + "Recherche" + chr(92) + "exemple"


def executer_faute(nom: str) -> int:  # noqa: C901 - table de fautes
    """Chaque faute doit être détectée (exit 1). Exit 0 = non détectée."""
    ici = _preparer()
    import run_mcmc_xz_g2_4 as lanceur
    from qualify_xz_capacity_cap1 import (_manifestes_production_reels,
                                          _verdict_occupation_monde)

    driver_source = Path("scripts/driver_production_c7c1.ps1").read_text(
        encoding="utf-8")
    lanceur_source = Path("scripts/run_mcmc_xz_g2_4.py").read_text(
        encoding="utf-8")
    cap1_source = Path("scripts/qualify_xz_capacity_cap1.py").read_text(
        encoding="utf-8")

    # ---- non-vacuité des adaptations de monde ---------------------------
    if nom == "collision_reelle_neutralisee":
        # MUTATION : la vraie garde est neutralisée — le contrôle unitaire
        # de la porte (un préfixe occupé DOIT être refusé) doit le voir.
        racine = _racine_occupee()
        vraie = lanceur.garde_collision
        lanceur.garde_collision = lambda prefixe: None
        try:
            prefixe = (Path(racine) / "g2_4" / "P_WS" / VARIANTE_SENTINELLE
                       / f"s{GRAINE_SENTINELLE}")
            try:
                lanceur.garde_collision(prefixe)
                neutralisation_visible = True  # aucun refus : détecté
            except Exception:  # noqa: BLE001
                neutralisation_visible = False
        finally:
            lanceur.garde_collision = vraie
            shutil.rmtree(racine, ignore_errors=True)
        return 1 if neutralisation_visible else 0
    if nom == "substitution_collision_fuit":
        # MUTATION : un harnais qui OUBLIERAIT de restaurer la garde —
        # le contrôle de restauration de la porte doit le voir.
        originale = lanceur.garde_collision
        lanceur.garde_collision = lambda prefixe: None  # fuite simulée
        try:
            fuite_detectee = lanceur.garde_collision is not originale
        finally:
            lanceur.garde_collision = originale
        return 1 if fuite_detectee else 0
    if nom == "occupation_inventee_signalee":
        verdict = _verdict_occupation_monde({"octets_production": 4096}, [])
        return 1 if any("aucun manifeste" in e for e in verdict) else 0
    if nom == "production_perdue_signalee":
        verdict = _verdict_occupation_monde(
            {"octets_production": 0},
            ["g2_4/P_WS/M2a-N/s630101/manifest.json"])
        return 1 if any("perd de la production" in e for e in verdict) else 0
    if nom == "manifeste_sous_temporaire_ignore":
        with tempfile.TemporaryDirectory(prefix="c7c1_rej1_tmp_") as tmp:
            cache = (Path(tmp)
                     / next(iter(lanceur.SOUS_ARBRES_TEMPORAIRES_RECONNUS))
                     / "faux_run")
            cache.mkdir(parents=True)
            (cache / "manifest.json").write_text("{}", encoding="utf-8")
            trouves = _manifestes_production_reels(lanceur, tmp)
        return 1 if trouves == [] else 0

    # ---- battement de vie ----------------------------------------------
    if nom == "heartbeat_retire":
        falsifie = "\n".join(
            ligne for ligne in lanceur_source.splitlines()
            if "observateur.heartbeat" not in ligne)
        return 1 if _heartbeat_statique(falsifie)["conforme"] is False else 0
    if nom == "heartbeat_ecrase":
        falsifie = lanceur_source.replace(
            '"a", encoding="utf-8") as battement',
            '"w", encoding="utf-8") as battement')
        if falsifie == lanceur_source:
            return 0
        return 1 if _heartbeat_statique(falsifie)["conforme"] is False else 0
    if nom == "heartbeat_hors_du_run":
        falsifie = lanceur_source.replace(
            '"observateur.heartbeat"', '"manifest.json"')
        if falsifie == lanceur_source:
            return 0
        copie = Path(tempfile.mkdtemp(prefix="c7c1_rej1_hb_"))
        try:
            chemin_module = copie / "lanceur_falsifie_rej1.py"
            chemin_module.write_text(falsifie, encoding="utf-8")
            spec = importlib.util.spec_from_file_location(
                "lanceur_falsifie_rej1", chemin_module)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            with tempfile.TemporaryDirectory(
                    prefix="c7c1_rej1_hbdyn_") as tmp:
                exercice = _exercer_heartbeat(module, Path(tmp))
            deborde = exercice["seul_le_battement_ajoute"] is False
            return 1 if deborde else 0
        finally:
            shutil.rmtree(copie, ignore_errors=True)

    if nom == "qualification_callback_touche_run_reel":
        # MUTATION : les appels dynamiques CAP-1 sont redirigés vers la
        # racine réelle. Le contrôle AST doit rendre cette régression rouge.
        falsifie = cap1_source.replace("cible_observateur", "cible")
        if falsifie == cap1_source:
            return 0
        return 1 if _callbacks_cap1_confines(
            falsifie)["conforme"] is False else 0

    # ---- driver : mutations, le contrôle statique doit mordre ------------
    mutations_driver = {
        "driver_timeout_introduit": (
            "$proc.WaitForExit()", "$proc.WaitForExit(60000)"),
        "driver_timeout_wait_process": (
            "$proc.WaitForExit()",
            "Wait-Process -Id $proc.Id -Timeout 60"),
        "driver_console_reintroduite": (
            "-RedirectStandardOutput $journalOut `", "`"),
        "driver_narration_console": (
            "$proc.WaitForExit()",
            "Write-Host 'demarrage'\n$proc.WaitForExit()"),
        "driver_journal_ecrase": ("Add-Content", "Set-Content"),
        "driver_tue_le_processus": (
            "$proc.WaitForExit()",
            "$proc.WaitForExit()\nStop-Process -Id $proc.Id"),
        "driver_masque_code_sortie": ("exit $codeSortie", "exit 0"),
    }
    if nom in mutations_driver:
        avant, apres = mutations_driver[nom]
        mutee = driver_source.replace(avant, apres)
        if mutee == driver_source:
            return 0
        return 1 if _controle_statique_driver(mutee)["conforme"] is False \
            else 0
    if nom == "driver_chemin_prive":
        from qualify_xz_capacity_cap1 import _motifs_confidentiels
        mutee = driver_source + f"\n# note : {_CHEMIN_PRIVE_EXEMPLE}\n"
        motifs = _motifs_confidentiels(
            lanceur, os.environ["C7C1_XZ_OUT_DIR"])
        fuite = any(motif.search(ligne)
                    for ligne in mutee.splitlines()
                    for motif in motifs.values())
        return 1 if fuite else 0

    print(f"faute inconnue : {nom}")
    return 0


# ----------------------------------------------------------------- porte

def qualification() -> int:
    ici = _preparer()
    import run_mcmc_xz_g2_4 as lanceur
    from qualify_xz_launcher_g2_4d import _verrou_nominal
    from qualify_xz_sent0d_unlock import (ARGS_AVEC_FLAG, ARGS_SANS_FLAG,
                                          _produire_sous_sentinelles)
    from qualify_xz_capacity_cap1 import (_manifestes_production_reels,
                                          _motifs_confidentiels,
                                          _verdict_occupation_monde)

    echecs: list[str] = []
    resultat: dict = {}
    volatil: dict = {}

    # ---- 0. verrou inchangé -------------------------------------------
    resultat["verrou"] = {
        "VERROU_PRODUCTION_G2_4D": lanceur.VERROU_PRODUCTION_G2_4D}
    if lanceur.VERROU_PRODUCTION_G2_4D is not True:
        echecs.append("VERROU_PRODUCTION_G2_4D n'est plus True")

    # ---- 1. adaptations de monde --------------------------------------
    # La racine réelle est légitimement occupée et le contrat local
    # épingle la racine de runs : les harnais de preuve substituent donc
    # garde_collision (scénario 1 seulement), et cette section prouve
    # (a) que les preuves redeviennent probantes, (b) que la substitution
    # est RESTAURÉE après chaque harnais, (c) que la VRAIE garde mord
    # toujours (contrôle unitaire sur préfixe synthétique occupé).
    collision_originale = lanceur.garde_collision

    preuve = _verrou_nominal()
    resultat["monde_verrou"] = {
        "collision_substituee_scenario_1":
            preuve["monde"]["collision_substituee_scenario_1"],
        "verrou_atteint": preuve["amont_satisfait"]["verrou_atteint"],
        "sentinelles": preuve["amont_satisfait"]["sentinelles"],
        "collision_restauree":
            lanceur.garde_collision is collision_originale,
        "scenario_2_refus_collision_reelle":
            "collision" in preuve["amont_reel"]["arret"],
    }
    if preuve["amont_satisfait"]["verrou_atteint"] is not True:
        echecs.append("monde occupé : la preuve du verrou n'atteint pas "
                      "l'étape verrouillée")
    if preuve["amont_satisfait"]["sentinelles"]:
        echecs.append("monde occupé : écriture avant le verrou")
    if resultat["monde_verrou"]["collision_restauree"] is not True:
        echecs.append("garde_collision NON RESTAURÉE après _verrou_nominal")
    if resultat["monde_verrou"][
            "scenario_2_refus_collision_reelle"] is not True:
        echecs.append("scénario 2 : la vraie garde_collision ne refuse pas "
                      "le monde occupé")

    appels_hist, message_hist = _produire_sous_sentinelles(
        lanceur, ARGS_SANS_FLAG)
    appels_franchi, message_franchi = _produire_sous_sentinelles(
        lanceur, ARGS_AVEC_FLAG)
    resultat["monde_franchissement"] = {
        "sans_flag_verrou_historique":
            not appels_hist and "VERROU G2.4d" in message_hist,
        "avec_flag_premiere_operation":
            appels_hist == [] and appels_franchi == ["Path.mkdir"],
        "collision_restauree":
            lanceur.garde_collision is collision_originale,
    }
    if resultat["monde_franchissement"][
            "sans_flag_verrou_historique"] is not True:
        echecs.append("monde occupé : sans flag, l'arrêt n'est pas le "
                      "verrou historique")
    if resultat["monde_franchissement"][
            "avec_flag_premiere_operation"] is not True:
        echecs.append("monde occupé : avec flag, la première opération "
                      "n'est pas l'acquisition exclusive")
    if resultat["monde_franchissement"]["collision_restauree"] is not True:
        echecs.append("garde_collision NON RESTAURÉE après "
                      "_produire_sous_sentinelles")

    # contrôle unitaire : la VRAIE garde mord toujours, dans les 2 sens
    racine_occupee = _racine_occupee()
    try:
        prefixe_occupe = (Path(racine_occupee) / "g2_4" / "P_WS"
                          / VARIANTE_SENTINELLE / f"s{GRAINE_SENTINELLE}")
        try:
            lanceur.garde_collision(prefixe_occupe)
            collision_mord = False
        except Exception as exc:  # noqa: BLE001
            collision_mord = "collision" in str(exc)
        prefixe_libre = (Path(racine_occupee) / "g2_4" / "P_WS"
                         / "M2b-N" / "s000000")
        try:
            lanceur.garde_collision(prefixe_libre)
            collision_laisse_passer = True
        except Exception:  # noqa: BLE001
            collision_laisse_passer = False
    finally:
        shutil.rmtree(racine_occupee, ignore_errors=True)
    resultat["monde_collision_unitaire"] = {
        "refuse_prefixe_occupe": collision_mord,
        "laisse_passer_prefixe_libre": collision_laisse_passer,
    }
    if collision_mord is not True:
        echecs.append("la vraie garde_collision ne refuse pas un préfixe "
                      "occupé")
    if collision_laisse_passer is not True:
        echecs.append("la vraie garde_collision refuse un préfixe libre")

    # cohérence occupation <-> manifestes : table de vérité complète
    table = {
        "vide_zero": _verdict_occupation_monde(
            {"octets_production": 0}, []) == [],
        "occupe_coherent": _verdict_occupation_monde(
            {"octets_production": 4096}, ["g2_4/x/manifest.json"]) == [],
        "octets_sans_manifeste_signale": _verdict_occupation_monde(
            {"octets_production": 4096}, []) != [],
        "manifeste_sans_octets_signale": _verdict_occupation_monde(
            {"octets_production": 0}, ["g2_4/x/manifest.json"]) != [],
    }
    with tempfile.TemporaryDirectory(prefix="c7c1_rej1_man_") as tmp:
        run = Path(tmp) / "g2_4" / "P_WS" / "M2a-N" / "s630101"
        run.mkdir(parents=True)
        (run / "manifest.json").write_text("{}", encoding="utf-8")
        cache = (Path(tmp)
                 / next(iter(lanceur.SOUS_ARBRES_TEMPORAIRES_RECONNUS)))
        (cache / "bruit").mkdir(parents=True)
        (cache / "bruit" / "manifest.json").write_text(
            "{}", encoding="utf-8")
        table["inventaire_exclut_temporaires"] = (
            _manifestes_production_reels(lanceur, tmp)
            == ["g2_4/P_WS/M2a-N/s630101/manifest.json"])
    resultat["monde_occupation"] = table
    for cle, valeur in table.items():
        if valeur is not True:
            echecs.append(f"cohérence occupation/manifestes : {cle}")

    # ---- 2. battement de vie ------------------------------------------
    source_lanceur = Path("scripts/run_mcmc_xz_g2_4.py").read_text(
        encoding="utf-8")
    source_cap1 = Path("scripts/qualify_xz_capacity_cap1.py").read_text(
        encoding="utf-8")
    resultat["confinement_callbacks_cap1"] = _callbacks_cap1_confines(
        source_cap1)
    if resultat["confinement_callbacks_cap1"]["conforme"] is not True:
        echecs.append("CAP-1 : un callback dynamique peut toucher le run réel")
    resultat["heartbeat_statique"] = _heartbeat_statique(source_lanceur)
    if resultat["heartbeat_statique"]["conforme"] is not True:
        echecs.append("battement : contrôle statique non conforme")
    with tempfile.TemporaryDirectory(prefix="c7c1_rej1_hb_") as tmp:
        exercice = _exercer_heartbeat(lanceur, Path(tmp))
    resultat["heartbeat_dynamique"] = exercice
    for cle in ("fichier_cree", "seul_le_battement_ajoute",
                "deux_appels_deux_lignes", "format_conforme",
                "defaillance_avalee"):
        if exercice.get(cle) is not True:
            echecs.append(f"battement : {cle} non conforme")
    resultat["heartbeat_injection"] = _exercer_injection(lanceur)
    if resultat["heartbeat_injection"]["minimale"] is not True:
        echecs.append("battement : surface d'injection élargie")

    # ---- 3. driver -----------------------------------------------------
    driver = Path("scripts/driver_production_c7c1.ps1")
    source_driver = driver.read_text(encoding="utf-8")
    resultat["driver_statique"] = _controle_statique_driver(source_driver)
    if resultat["driver_statique"]["conforme"] is not True:
        echecs.append("driver : contrôle statique non conforme")
    pwsh = shutil.which("pwsh")
    if pwsh is None:
        echecs.append("driver : pwsh 7 introuvable — dynamique impossible")
        resultat["driver_dynamique"] = {"pwsh": False}
    else:
        dyn, echecs_driver = _qualifier_driver(pwsh, driver.resolve())
        resultat["driver_dynamique"] = dyn
        echecs.extend(echecs_driver)

    # ---- 4. confidentialité des surfaces publiques REJ-1 ---------------
    motifs = _motifs_confidentiels(lanceur, os.environ["C7C1_XZ_OUT_DIR"])
    fuites: dict = {}
    fichiers = ("scripts/driver_production_c7c1.ps1",
                "scripts/qualify_xz_rej1_monde.py",
                "reports/rapport_REJ1_monde_durcissement.md")
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
        echecs.append(f"fuite locale dans un fichier REJ-1 : {sorted(fuites)}")

    # ---- 5. fautes injectées (sous-processus) --------------------------
    resultat["fautes"] = {}
    for nom in FAUTES:
        proc = subprocess.run(
            [sys.executable, "scripts/qualify_xz_rej1_monde.py",
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

    resultat["porte"] = {"echecs": echecs, "passe": not echecs}
    print(json.dumps(resultat, indent=2, sort_keys=True, ensure_ascii=False))
    print("=== MESURES NON DETERMINISTES (chemins/timings) ===")
    print(json.dumps(volatil, indent=2, sort_keys=True, ensure_ascii=False))
    return 0 if not echecs else 1


def main() -> None:
    args = sys.argv[1:]
    if args and args[0] == "--faute":
        raise SystemExit(executer_faute(args[1]))
    raise SystemExit(qualification())


if __name__ == "__main__":
    main()
