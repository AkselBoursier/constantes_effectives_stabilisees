"""Qualification du franchissement SENT-0D — porte SENT-0D1 (#94, #63).

Éprouve le CONTRÔLE DE FLUX du franchissement technique borné du verrou,
SANS production : aucune MCMC, aucun ``cobaya.run`` réel, aucune
minimisation, aucun posterior, aucune autorisation privée réelle, aucun
répertoire de run réel, aucun ``manifest.json`` réel.

La constante ``VERROU_PRODUCTION_G2_4D`` reste True : SENT-0D n'ouvre
qu'un franchissement étroit — couple sentinelle codé (M2a-N/630101) +
autorisation privée au PÉRIMÈTRE EXACT portant la référence de
ratification sentinelle + intention CLI explicite
``--franchissement-sent0d SENT0D-2026-08-04-issue94-rat1``.

Le franchissement positif est prouvé PAR SENTINELLES : le chemin
traverse réellement l'étape 8 et la PREMIÈRE opération filesystem
post-verrou est interceptée par la sentinelle ``Path.mkdir`` AVANT toute
écriture réelle. Dans ``_acquerir_repertoire_run``, ce premier appel
peut être celui du PARENT (``exist_ok=True``) ; l'acquisition exclusive
du répertoire final demeure l'appel ultérieur ``exist_ok=False``, déjà
qualifié par SENT-0B/B1 — la preuve de FRANCHISSEMENT n'en dépend pas.

PORTE AUTO-BLOQUANTE : toute attente non satisfaite conduit à
SystemExit(1) après impression du JSON normalisé.

Modes :
    (aucun argument)  : qualification complète ;
    --faute NOM       : injecte la faute NOM ; exit 1 si elle est
                        détectée (attendu), 0 si elle passe inaperçue.
"""

from __future__ import annotations

import ast
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

VARIANTE_SENTINELLE = "M2a-N"
GRAINE_SENTINELLE = 630101
REFERENCE_ATTENDUE = "SENT0D-2026-08-04-issue94-rat1"


def _preparer():
    ici = Path(__file__).parent.parent
    os.chdir(ici)
    if "scripts" not in sys.path:
        sys.path.insert(0, "scripts")
    return ici


def _autorisation_sentinelle_memoire(lanceur) -> dict:
    """Autorisation NOMINALE SENT-0D, en mémoire — jamais sur disque.

    Périmètre EXACT (couple sentinelle seul) + référence de ratification
    sentinelle. Base : le constructeur nominal déjà qualifié de G2.4d.
    """
    from qualify_xz_launcher_g2_4d import _autorisation_nominale_memoire

    manifeste = _autorisation_nominale_memoire(
        lanceur, VARIANTE_SENTINELLE, GRAINE_SENTINELLE)
    manifeste["variantes_graines_autorisees"] = {
        VARIANTE_SENTINELLE: [GRAINE_SENTINELLE]}
    manifeste["reference_ratification_sentinelle"] = REFERENCE_ATTENDUE
    return manifeste


def _valider_sentinelle(lanceur, manifeste,
                        perimetre="exact", reference="exacte"):
    """Appelle le validateur pur avec les contraintes SENT-0D."""
    from qualify_xz_launcher_g2_4d import _support_mesure

    return lanceur._valider_contenu_autorisation(
        manifeste, VARIANTE_SENTINELLE, GRAINE_SENTINELLE,
        lanceur.garde_git()["head"],
        budget_contrat=lanceur.BUDGET_TOTAL_RATIFIE_GIO,
        ratification_contrat=lanceur.REFERENCE_RATIFICATION_BUDGET,
        support_attendu=_support_mesure(lanceur),
        perimetre_exact_attendu=(
            lanceur.PERIMETRE_EXACT_SENTINELLE if perimetre == "exact"
            else None),
        reference_sentinelle_attendue=(
            lanceur.REFERENCE_RATIFICATION_SENTINELLE if reference == "exacte"
            else None),
    )


def _produire_sous_sentinelles(lanceur, args_produire):
    """Exécute ``produire`` gardes amont satisfaites, sous sentinelles.

    Même harnais que la preuve de verrou G2.4d : SEULES les gardes que la
    qualification ne peut pas satisfaire réellement (arbre Git propre,
    budget déclaré, autorisation privée — interdite ici) sont substituées;
    contrat, environnement, données, threads, chemins, support et
    admission de capacité restent les VRAIES gardes. Rend (sentinelles
    atteintes, message d'arrêt).

    REJ-1 (#94) : depuis SENT-0E le préfixe sentinelle réel est
    légitimement occupé par un run ratifié — ``garde_collision``
    mordrait avant l'étape 8 et rendrait ces preuves vacantes. Une
    racine synthétique est impossible (le contrat local épingle la
    racine de runs, garde conservée) : ``garde_collision`` rejoint donc
    la famille des gardes substituées par ce harnais, restaurée dans le
    même ``finally``. La garde réelle reste qualifiée par SENT-0B
    (collision_prefixe_etape9, acquisition exclusive B1) et par le
    contrôle unitaire de REJ-1 ; les sentinelles filesystem interdisent
    de toute façon TOUTE écriture réelle.
    """
    from qualify_xz_launcher_g2_4d import _sentinelles

    head_reel = lanceur.garde_git()["head"]
    vrai_git = lanceur.garde_git
    vrai_budget = lanceur.garde_budget_production
    vraie_autorisation = lanceur.garde_autorisation
    vraie_collision = lanceur.garde_collision
    lanceur.garde_collision = lambda prefixe: None  # monde occupé (REJ-1)
    lanceur.garde_git = lambda: {"head": head_reel, "arbre_propre": True}
    lanceur.garde_budget_production = lambda contrat, cible: {
        "budget_production_statut": "RATIFIE_SIMULE_QUALIFICATION",
        "budget_production_requis_Gio": lanceur.BUDGET_TOTAL_RATIFIE_GIO,
        "reference_ratification_budget":
            lanceur.REFERENCE_RATIFICATION_BUDGET,
        "libre_cible_gio": None,
    }
    lanceur.garde_autorisation = lambda *a, **k: "0" * 64
    try:
        with _sentinelles() as appels:
            message = "AUCUNE EXCEPTION"
            try:
                lanceur.produire(list(args_produire))
            except BaseException as exc:  # noqa: BLE001
                message = f"{type(exc).__name__}: {exc}"
        return list(appels), message
    finally:
        lanceur.garde_git = vrai_git
        lanceur.garde_budget_production = vrai_budget
        lanceur.garde_autorisation = vraie_autorisation
        lanceur.garde_collision = vraie_collision


ARGS_SANS_FLAG = (VARIANTE_SENTINELLE, str(GRAINE_SENTINELLE),
                  "--je-confirme-la-production",
                  "--autorisation", "substituee_par_le_harnais")
ARGS_AVEC_FLAG = (*ARGS_SANS_FLAG,
                  "--franchissement-sent0d", REFERENCE_ATTENDUE)


# --------------------------------------------------------------- fautes

def executer_faute(nom: str) -> int:  # noqa: C901 - table de fautes
    """Chaque faute doit être détectée (exit 1). Exit 0 = non détectée."""
    _preparer()
    import run_mcmc_xz_g2_4 as lanceur
    from run_mcmc_xz_g2_4 import GardeErreur

    def _detecte_message(fn, fragment: str) -> int:
        try:
            fn()
            return 0
        except GardeErreur as exc:
            return 1 if fragment in str(exc) else 0
        except Exception:  # noqa: BLE001 - autre cause : non probant
            return 0

    # ---- intentions CLI --------------------------------------------------
    if nom == "flag_errone_accepte":
        return _detecte_message(
            lambda: lanceur._extraire_flag_franchissement(
                ["M2a-N", "630101", "--franchissement-sent0d",
                 "SENT0D-FANTAISIE"]),
            "référence incorrecte")
    if nom == "flag_sans_valeur_accepte":
        # valeur absente : le flag est suivi d'une autre option
        cas_a = _detecte_message(
            lambda: lanceur._extraire_flag_franchissement(
                ["M2a-N", "630101", "--franchissement-sent0d",
                 "--autorisation"]),
            "référence absente")
        # valeur absente : le flag est le dernier argument
        cas_b = _detecte_message(
            lambda: lanceur._extraire_flag_franchissement(
                ["M2a-N", "630101", "--franchissement-sent0d"]),
            "référence absente")
        return 1 if (cas_a == 1 and cas_b == 1) else 0
    if nom == "flag_duplique_accepte":
        return _detecte_message(
            lambda: lanceur._extraire_flag_franchissement(
                ["--franchissement-sent0d", REFERENCE_ATTENDUE,
                 "--franchissement-sent0d", REFERENCE_ATTENDUE]),
            "dupliqué")
    if nom == "flag_vide_accepte":
        return _detecte_message(
            lambda: lanceur._extraire_flag_franchissement(
                ["--franchissement-sent0d", " "]),
            "référence vide")

    # ---- garde de franchissement (étape 8) -------------------------------
    if nom == "sans_flag_ne_declenche_pas_le_verrou_historique":
        return _detecte_message(
            lambda: lanceur.garde_franchissement_sent0d(
                None, VARIANTE_SENTINELLE, GRAINE_SENTINELLE),
            "VERROU G2.4d")
    if nom == "franchissement_hors_couple_accepte":
        return _detecte_message(
            lambda: lanceur.garde_franchissement_sent0d(
                REFERENCE_ATTENDUE, "M2a-K", 630201),
            "hors périmètre sentinelle")
    if nom == "garde_franchissement_neutralisee":
        # MUTATION 5.3 : la garde est neutralisée. SANS flag, le chemin
        # doit alors atteindre la sentinelle post-verrou — preuve que la
        # garde réelle est bien ce qui bloque normalement.
        appels_avant, message_avant = _produire_sous_sentinelles(
            lanceur, ARGS_SANS_FLAG)
        bloque_avant = (not appels_avant) and "VERROU G2.4d" in message_avant
        vraie_garde = lanceur.garde_franchissement_sent0d
        lanceur.garde_franchissement_sent0d = lambda *a, **k: None
        try:
            appels_apres, message_apres = _produire_sous_sentinelles(
                lanceur, ARGS_SANS_FLAG)
        finally:
            lanceur.garde_franchissement_sent0d = vraie_garde
        traverse_apres = ("Path.mkdir" in appels_apres
                          and "SENTINELLE ATTEINTE" in message_apres)
        return 1 if (bloque_avant and traverse_apres) else 0

    # ---- autorisation : périmètre exact ---------------------------------
    if nom in ("perimetre_deux_graines_accepte",
               "perimetre_couple_plus_variante_accepte",
               "perimetre_autre_variante_seule_acceptee",
               "reference_sentinelle_absente_acceptee",
               "reference_sentinelle_erronee_acceptee"):
        m = _autorisation_sentinelle_memoire(lanceur)
        if nom == "perimetre_deux_graines_accepte":
            m["variantes_graines_autorisees"] = {
                VARIANTE_SENTINELLE: [GRAINE_SENTINELLE, 630102]}
            fragment = "périmètre de l'autorisation non exact"
        elif nom == "perimetre_couple_plus_variante_accepte":
            m["variantes_graines_autorisees"] = {
                VARIANTE_SENTINELLE: [GRAINE_SENTINELLE],
                "M2a-K": [630201]}
            fragment = "périmètre de l'autorisation non exact"
        elif nom == "perimetre_autre_variante_seule_acceptee":
            m["variantes_graines_autorisees"] = {"M2b-K": [630401]}
            # refusée en amont par la couverture du couple demandé — cause
            # exacte : variantes_graines_autorisees
            fragment = "variantes_graines_autorisees"
        elif nom == "reference_sentinelle_absente_acceptee":
            m.pop("reference_ratification_sentinelle")
            fragment = "reference_ratification_sentinelle"
        else:
            m["reference_ratification_sentinelle"] = "SENT0D-AUTRE"
            fragment = "reference_ratification_sentinelle"
        return _detecte_message(
            lambda: _valider_sentinelle(lanceur, m), fragment)
    if nom == "perimetre_exact_neutralise":
        # MUTATION 5.4 : même manifeste élargi, SANS la contrainte de
        # périmètre — il devient admissible. Preuve que la contrainte est
        # bien ce qui refuse, et non un contrôle fortuit.
        m = _autorisation_sentinelle_memoire(lanceur)
        m["variantes_graines_autorisees"] = {
            VARIANTE_SENTINELLE: [GRAINE_SENTINELLE, 630102]}
        refuse_avec = _detecte_message(
            lambda: _valider_sentinelle(lanceur, m),
            "périmètre de l'autorisation non exact")
        try:
            _valider_sentinelle(lanceur, m, perimetre=None)
            admis_sans = True
        except GardeErreur:
            admis_sans = False
        return 1 if (refuse_avec == 1 and admis_sans) else 0
    if nom == "cle_etrangere_acceptee":
        # Seule la clé optionnelle SENT-0D est tolérée : toute autre clé
        # étrangère doit rester refusée.
        m = _autorisation_sentinelle_memoire(lanceur)
        m["cle_inconnue"] = "interdite"
        return _detecte_message(
            lambda: _valider_sentinelle(lanceur, m), "clés inexactes")

    # ---- B3 : liaison SHA <-> octets validés -----------------------------
    if nom == "autorisation_sha_seconde_lecture":
        # Épreuve NON VACANTE de la lecture unique (B3, audit PR #96).
        # Un fichier A structurellement valide est écrit sous %TEMP% —
        # marqué QUALIFICATION_ONLY : pour ne jamais produire une
        # autorisation réelle, la validation PROFONDE est substituée par
        # un espion ; la chaîne éprouvée reste la VRAIE chaîne de
        # garde_autorisation (lecture des octets -> SHA -> décodage ->
        # parsing -> appel du validateur -> retour du SHA), et
        # sha256_fichier n'est PAS mocké. L'espion (1) vérifie que
        # l'objet reçu est exactement celui parsé des octets A — la
        # validation porte bien sur les octets lus — puis (2) remplace le
        # fichier sur disque par un contenu B AVANT que garde_autorisation
        # ne retourne. Attendus : SHA retourné == SHA(A) != SHA(B) et
        # fichier sur disque == B. L'ancienne implémentation à double
        # lecture (sha256_fichier(chemin) après validation) rendrait
        # SHA(B) : la faute échouerait.
        import hashlib

        with tempfile.TemporaryDirectory(prefix="c7c1_sent0d_") as tmp:
            manifeste_a = _autorisation_sentinelle_memoire(lanceur)
            manifeste_a["usage"] = "QUALIFICATION_ONLY"
            manifeste_a["cle_humaine_1"] = "QUALIFICATION_ONLY"
            manifeste_a["cle_humaine_2"] = "QUALIFICATION_ONLY"
            chemin = Path(tmp) / "autorisation_qualification_only.json"
            octets_a = json.dumps(manifeste_a, sort_keys=True,
                                  ensure_ascii=False).encode("utf-8")
            chemin.write_bytes(octets_a)
            sha_a = hashlib.sha256(octets_a).hexdigest()
            octets_b = json.dumps({"schema": "contenu_B_substitue"},
                                  sort_keys=True).encode("utf-8")
            sha_b = hashlib.sha256(octets_b).hexdigest()
            objet_a = json.loads(octets_a.decode("utf-8"))
            vrai_validateur = lanceur._valider_contenu_autorisation
            temoin = {"objet_recu_est_A": False}

            def espion(manifeste, *a, **k):
                temoin["objet_recu_est_A"] = (manifeste == objet_a)
                chemin.write_bytes(octets_b)  # mutation APRÈS validation
                return []

            lanceur._valider_contenu_autorisation = espion
            try:
                sha_retourne = lanceur.garde_autorisation(
                    chemin, VARIANTE_SENTINELLE, GRAINE_SENTINELLE,
                    lanceur.garde_git()["head"])
            finally:
                lanceur._valider_contenu_autorisation = vrai_validateur
            disque_apres = chemin.read_bytes()
        return 1 if (temoin["objet_recu_est_A"]
                     and sha_retourne == sha_a
                     and sha_retourne != sha_b
                     and disque_apres == octets_b) else 0
    if nom == "autorisation_utf8_invalide_acceptee":
        with tempfile.TemporaryDirectory(prefix="c7c1_sent0d_") as tmp:
            chemin = Path(tmp) / "autorisation.bin"
            chemin.write_bytes(b'{"type": "\xff\xfe invalide"}')
            return _detecte_message(
                lambda: lanceur.garde_autorisation(
                    chemin, VARIANTE_SENTINELLE, GRAINE_SENTINELLE, "0" * 40),
                "UTF-8 invalide")
    if nom == "autorisation_json_invalide_acceptee":
        with tempfile.TemporaryDirectory(prefix="c7c1_sent0d_") as tmp:
            chemin = Path(tmp) / "autorisation.json"
            chemin.write_text("{ ceci n'est pas du JSON", encoding="utf-8")
            return _detecte_message(
                lambda: lanceur.garde_autorisation(
                    chemin, VARIANTE_SENTINELLE, GRAINE_SENTINELLE, "0" * 40),
                "JSON invalide")

    # ---- verrou ----------------------------------------------------------
    if nom == "verrou_retire":
        source = Path("scripts/run_mcmc_xz_g2_4.py").read_text(
            encoding="utf-8")
        falsifie = source.replace("VERROU_PRODUCTION_G2_4D = True",
                                  "VERROU_PRODUCTION_G2_4D = False", 1)
        return 1 if _verrou_declare(falsifie) is False else 0
    if nom == "etape8_sans_garde_franchissement":
        # Contrôle statique : sous `if VERROU_PRODUCTION_G2_4D:` de
        # `produire`, l'appel DOIT être garde_franchissement_sent0d. La
        # faute simule une source où le bloc lèverait sans la garde.
        source = Path("scripts/run_mcmc_xz_g2_4.py").read_text(
            encoding="utf-8")
        reel = _etape8_appelle_la_garde(source)
        falsifie = source.replace(
            "garde_franchissement_sent0d(reference_franchissement, "
            "variante, graine)",
            "pass  # garde retiree", 1)
        mute = _etape8_appelle_la_garde(falsifie)
        return 1 if (reel is True and mute is False) else 0
    raise SystemExit(f"faute inconnue : {nom}")


FAUTES = (
    "flag_errone_accepte", "flag_sans_valeur_accepte",
    "flag_duplique_accepte", "flag_vide_accepte",
    "sans_flag_ne_declenche_pas_le_verrou_historique",
    "franchissement_hors_couple_accepte",
    "garde_franchissement_neutralisee",
    "perimetre_deux_graines_accepte",
    "perimetre_couple_plus_variante_accepte",
    "perimetre_autre_variante_seule_acceptee",
    "reference_sentinelle_absente_acceptee",
    "reference_sentinelle_erronee_acceptee",
    "perimetre_exact_neutralise", "cle_etrangere_acceptee",
    # B3 — liaison SHA <-> octets validés (audit PR #96)
    "autorisation_sha_seconde_lecture",
    "autorisation_utf8_invalide_acceptee",
    "autorisation_json_invalide_acceptee",
    "verrou_retire", "etape8_sans_garde_franchissement",
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


def _etape8_appelle_la_garde(source: str):
    """Vrai si, dans produire, le bloc `if VERROU_PRODUCTION_G2_4D:`
    appelle garde_franchissement_sent0d."""
    arbre = ast.parse(source)
    produire = next((n for n in ast.walk(arbre)
                     if isinstance(n, ast.FunctionDef)
                     and n.name == "produire"), None)
    if produire is None:
        return None
    for noeud in ast.walk(produire):
        if (isinstance(noeud, ast.If) and isinstance(noeud.test, ast.Name)
                and noeud.test.id == "VERROU_PRODUCTION_G2_4D"):
            appels = [c.func.id for c in ast.walk(noeud)
                      if isinstance(c, ast.Call)
                      and isinstance(c.func, ast.Name)]
            return "garde_franchissement_sent0d" in appels
    return None


# ---------------------------------------------------------- qualification

def qualification() -> int:  # noqa: C901 - porte de qualification
    _preparer()
    import run_mcmc_xz_g2_4 as lanceur
    from run_mcmc_xz_g2_4 import GardeErreur

    echecs: list[str] = []
    resultat: dict = {}

    # ---- 1. preuves statiques ------------------------------------------
    source = Path("scripts/run_mcmc_xz_g2_4.py").read_text(encoding="utf-8")
    resultat["statique"] = {
        "VERROU_PRODUCTION_G2_4D_source": _verrou_declare(source),
        "VERROU_PRODUCTION_G2_4D_charge": lanceur.VERROU_PRODUCTION_G2_4D,
        "reference_ratification_sentinelle":
            lanceur.REFERENCE_RATIFICATION_SENTINELLE,
        "perimetre_exact_sentinelle": {
            v: list(gs) for v, gs
            in lanceur.PERIMETRE_EXACT_SENTINELLE.items()},
        "etape8_appelle_la_garde": _etape8_appelle_la_garde(source),
    }
    if _verrou_declare(source) is not True:
        echecs.append("VERROU_PRODUCTION_G2_4D != True dans la source")
    if lanceur.VERROU_PRODUCTION_G2_4D is not True:
        echecs.append("VERROU_PRODUCTION_G2_4D != True chargé")
    if lanceur.REFERENCE_RATIFICATION_SENTINELLE != REFERENCE_ATTENDUE:
        echecs.append("référence de ratification sentinelle inattendue")
    if resultat["statique"]["perimetre_exact_sentinelle"] != {
            VARIANTE_SENTINELLE: [GRAINE_SENTINELLE]}:
        echecs.append("périmètre exact sentinelle inattendu")
    if _etape8_appelle_la_garde(source) is not True:
        echecs.append("l'étape 8 n'appelle pas garde_franchissement_sent0d")

    # ---- 2. verrou historique conservé (sans flag) ---------------------
    appels_hist, message_hist = _produire_sous_sentinelles(
        lanceur, ARGS_SANS_FLAG)
    resultat["verrou_historique"] = {
        "sentinelles_atteintes": appels_hist,
        "arret": message_hist[:140],
        "arret_exact_sur_verrou": "VERROU G2.4d" in message_hist,
    }
    if appels_hist:
        echecs.append(f"écriture/cobaya.run SANS flag : {appels_hist}")
    if "VERROU G2.4d" not in message_hist:
        echecs.append(
            f"le refus historique n'est pas le verrou : {message_hist[:100]}")

    # ---- 3. franchissement positif, PROUVÉ, sans écriture --------------
    appels_franchi, message_franchi = _produire_sous_sentinelles(
        lanceur, ARGS_AVEC_FLAG)
    resultat["franchissement_positif"] = {
        "sentinelles_atteintes": appels_franchi,
        "arret": message_franchi[:140],
        "etape8_franchie": "SENTINELLE ATTEINTE" in message_franchi,
        "premiere_operation_interceptee":
            appels_franchi == ["Path.mkdir"],
        "ecriture_reelle": False,
        "cobaya_run_reel": "cobaya.run" in appels_franchi,
    }
    if "SENTINELLE ATTEINTE" not in message_franchi:
        echecs.append(
            f"le franchissement n'atteint pas l'étape 9 : "
            f"{message_franchi[:120]}")
    if appels_franchi != ["Path.mkdir"]:
        echecs.append(
            f"première opération post-verrou inattendue : {appels_franchi} "
            "(attendu : exactement [Path.mkdir], première opération "
            "filesystem de _acquerir_repertoire_run)")
    if "cobaya.run" in appels_franchi:
        echecs.append("cobaya.run atteint : interdit dans cette passe")

    # ---- 4. flag erroné : refus SENT-0D, aucune écriture ---------------
    appels_errone, message_errone = _produire_sous_sentinelles(
        lanceur, (*ARGS_SANS_FLAG, "--franchissement-sent0d",
                  "SENT0D-FANTAISIE"))
    resultat["flag_errone"] = {
        "sentinelles_atteintes": appels_errone,
        "arret": message_errone[:140],
        "refus_sent0d_exact": "référence incorrecte" in message_errone,
    }
    if appels_errone:
        echecs.append(f"écriture avec flag erroné : {appels_errone}")
    if "référence incorrecte" not in message_errone:
        echecs.append(
            f"flag erroné : cause inexacte ({message_errone[:100]})")

    # ---- 5. autorisation : périmètre exact et référence ----------------
    nominal = _autorisation_sentinelle_memoire(lanceur)
    try:
        traverses = _valider_sentinelle(lanceur, nominal)
        groupes_sent0d = [g for g in ("perimetre_sentinelle",
                                      "reference_sentinelle")
                          if g in traverses]
        admissible = True
    except GardeErreur as exc:
        traverses, groupes_sent0d, admissible = [], [], False
        resultat["autorisation_nominale_motif"] = str(exc)[:140]
    # rétro-compatibilité : le MÊME manifeste, SANS contraintes SENT-0D,
    # reste admissible par le validateur général (clé optionnelle tolérée)
    try:
        _valider_sentinelle(lanceur, nominal, perimetre=None, reference=None)
        retro_ok = True
    except GardeErreur:
        retro_ok = False
    # et un manifeste SANS la clé optionnelle reste admissible aussi
    sans_cle = _autorisation_sentinelle_memoire(lanceur)
    sans_cle.pop("reference_ratification_sentinelle")
    try:
        _valider_sentinelle(lanceur, sans_cle, perimetre=None, reference=None)
        general_sans_cle_ok = True
    except GardeErreur:
        general_sans_cle_ok = False
    resultat["autorisation_sentinelle"] = {
        "nominale_admissible": admissible,
        "groupes_sent0d_traverses": groupes_sent0d,
        "meme_manifeste_admissible_hors_franchissement": retro_ok,
        "manifeste_sans_cle_optionnelle_admissible_general":
            general_sans_cle_ok,
    }
    if not admissible:
        echecs.append("l'autorisation sentinelle nominale est refusée")
    if groupes_sent0d != ["perimetre_sentinelle", "reference_sentinelle"]:
        echecs.append(f"groupes SENT-0D non traversés : {groupes_sent0d}")
    if not retro_ok or not general_sans_cle_ok:
        echecs.append("la qualification générale G2.4d serait cassée "
                      "rétrospectivement (clé optionnelle)")

    # ---- 6. fautes injectées (sous-processus) --------------------------
    resultat["fautes"] = {}
    for nom in FAUTES:
        proc = subprocess.run(
            [sys.executable, "scripts/qualify_xz_sent0d_unlock.py",
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
        "verrou": "VERROU_PRODUCTION_G2_4D = True — inchangé",
        "franchissement": "contrôle de flux qualifié ; AUCUNE écriture "
                          "réelle, AUCUN cobaya.run réel, AUCUNE "
                          "autorisation privée réelle",
        "couple": f"{VARIANTE_SENTINELLE} / {GRAINE_SENTINELLE} — seul "
                  "couple pouvant franchir ; 31 autres impossibles",
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
