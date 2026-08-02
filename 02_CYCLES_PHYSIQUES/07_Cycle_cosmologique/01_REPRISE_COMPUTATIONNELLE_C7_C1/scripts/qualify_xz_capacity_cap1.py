"""Qualification de la politique de capacité — porte CAP-1 (issues #90/#63).

Matérialise et éprouve la décision humaine RATIFIÉE du 2 août 2026 :

    budget_production_requis_Gio  = 20
    reserve_reprise_Gio           = 1.15
    reserve_volume_minimale_Gio   = 40
    support_actif                 = volume C: portant la racine de runs
    reference_ratification_budget = CAP0-2026-08-02-issue90-rat1

CAP-1 ne réévalue AUCUNE de ces valeurs. Elle vérifie qu'elles produisent
les gardes attendues.

AUCUNE PRODUCTION : aucune MCMC, aucune minimisation, aucun posterior,
aucune chaîne, aucun manifeste réel, aucune autorisation réelle, aucun
retrait de VERROU_PRODUCTION_G2_4D. Les seules écritures sont des
arborescences SYNTHÉTIQUES sous %TEMP%, supprimées en fin de passe ; la
racine de runs réelle n'est jamais modifiée.

Modes :
    (aucun argument)  : qualification complète ;
    --faute NOM       : injecte la faute NOM ; exit 1 si elle est
                        détectée (attendu), 0 si elle passe inaperçue.
"""

from __future__ import annotations

import ast
import contextlib
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

VARIANTE_TEST = "M2a-N"
GRAINE_TEST = 630101
DATE_QUALIFICATION_UTC = "2026-08-02T00:00:00Z"


def _preparer():
    ici = Path(__file__).parent.parent
    os.chdir(ici)
    if "scripts" not in sys.path:
        sys.path.insert(0, "scripts")
    return ici


# ------------------------------------------------------------- doublures

class CollectionDoublure:
    """Collection de sampler minimale : seule sa LONGUEUR est observée."""

    def __init__(self, n: int):
        self._n = int(n)

    def __len__(self) -> int:
        return self._n


class SamplerEspion:
    """Doublure de sampler qui ENREGISTRE toute écriture d'attribut.

    L'observateur de capacité doit être un pur lecteur : la liste des
    écritures doit rester vide, et aucune valeur ne doit changer. Les
    attributs reproduits sont ceux qu'il serait le plus grave de muter.
    """

    _CHAMPS = ("converged", "Rminus1_stop", "Rminus1_cl_stop",
               "proposal_scale", "max_samples", "weight", "burn_in_left")

    def __init__(self, lignes: int):
        object.__setattr__(self, "ecritures", [])
        object.__setattr__(self, "collection", CollectionDoublure(lignes))
        etat = {"converged": False, "Rminus1_stop": 0.01,
                "Rminus1_cl_stop": 0.02, "proposal_scale": 1.9,
                "max_samples": math.inf, "weight": 1, "burn_in_left": 0}
        for cle, valeur in etat.items():
            object.__setattr__(self, cle, valeur)
        object.__setattr__(self, "_reference", dict(etat))

    def __setattr__(self, nom, valeur):
        self.ecritures.append(nom)
        object.__setattr__(self, nom, valeur)

    def mutations(self) -> list[str]:
        """Champs dont la VALEUR a changé, écriture enregistrée ou non."""
        return sorted(
            c for c in self._CHAMPS
            if getattr(self, c) != self._reference[c]
            and not (isinstance(self._reference[c], float)
                     and math.isinf(self._reference[c])
                     and math.isinf(getattr(self, c))))


@contextlib.contextmanager
def _env(**valeurs):
    """Fixe des variables d'environnement puis les restaure exactement."""
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


def _arbre_synthetique(racine: Path, production: bool = True,
                       octets: int = 4096) -> Path:
    """Arborescence de run SYNTHÉTIQUE sous %TEMP%.

    Marquée par un manifeste au schéma reconnu quand ``production`` est
    vrai. Jamais écrite dans la racine de runs réelle.
    """
    import run_mcmc_xz_g2_4 as lanceur

    run = racine / "g2_4" / "P_WS" / VARIANTE_TEST / f"s{GRAINE_TEST}"
    run.mkdir(parents=True, exist_ok=True)
    (run / "chain.1.txt").write_bytes(b"x" * octets)
    if production:
        (run / "manifest.json").write_text(
            json.dumps({"schema": lanceur.SCHEMA_MANIFESTE_RUN,
                        "variante": VARIANTE_TEST}), encoding="utf-8")
    return run


def _identite_synthetique(lanceur, statut=None, politique=None) -> dict:
    """Identité de reprise minimale, cohérente avec la politique CAP-1."""
    identite = {
        "schema": lanceur.SCHEMA_MANIFESTE_RUN,
        "variante": VARIANTE_TEST,
        "graine": GRAINE_TEST,
        "budget_total_Gio": lanceur.BUDGET_TOTAL_RATIFIE_GIO,
        "reserve_reprise_Gio": lanceur.RESERVE_REPRISE_RATIFIEE_GIO,
        "reserve_volume_minimale_Gio": lanceur.RESERVE_VOLUME_RATIFIEE_GIO,
        "allocation_run_actif_Gio":
            lanceur.allocation_run_actif_gio(VARIANTE_TEST),
        "politique_capacite_version":
            politique or lanceur.POLITIQUE_CAPACITE_VERSION,
        "callback_every": lanceur.CALLBACK_EVERY_ITERATIONS,
        "support_actif_identite_expurgee":
            lanceur.identite_support_expurgee(os.environ["C7C1_XZ_OUT_DIR"]),
        "reference_ratification_budget":
            lanceur.REFERENCE_RATIFICATION_BUDGET,
    }
    identite["statut_run"] = statut or lanceur.STATUT_RUN_INTERROMPU_CAPACITE
    return identite


def _run_repris(lanceur, racine: Path, *, checkpoint: str | None,
                statut=None, politique=None) -> tuple[Path, dict]:
    """Run SYNTHÉTIQUE interrompu, prêt pour la garde de reprise."""
    run = racine / "reprise"
    run.mkdir(parents=True, exist_ok=True)
    identite = _identite_synthetique(lanceur, statut=statut, politique=politique)
    (run / "manifest.json").write_text(
        json.dumps(identite, sort_keys=True), encoding="utf-8")
    if checkpoint is not None:
        (run / "chain.checkpoint").write_text(checkpoint, encoding="utf-8")
    attendue = _identite_synthetique(lanceur)
    return run / "chain", attendue


CHECKPOINT_VALIDE = (
    "sampler:\n  mcmc:\n    converged: false\n    Rminus1_last: 0.34\n"
    "    burn_in: 0\n    mpi_size: 1\n")


def _contrat_modifie(lanceur, tmp: Path, **remplacements) -> str:
    """Copie du contrat privé avec des valeurs de capacité altérées."""
    base = json.loads(
        Path(os.environ["C7C1_CONTRAT_LOCAL"]).read_text(encoding="utf-8"))
    for cle, valeur in remplacements.items():
        if cle == "version":
            base["version"] = valeur
        else:
            base["racine_runs"][cle] = valeur
    faux = tmp / "contrat_cap1_faute.json"
    faux.write_text(json.dumps(base), encoding="utf-8")
    return str(faux)


# --------------------------------------------------------------- fautes

FAUTES_CONTRAT = {
    "contrat_budget_19_999": {"budget_production_requis_Gio": 19.999},
    "contrat_budget_20_001": {"budget_production_requis_Gio": 20.001},
    "contrat_reprise_1_14": {"reserve_reprise_Gio": 1.14},
    "contrat_reprise_1_16": {"reserve_reprise_Gio": 1.16},
    "contrat_volume_39": {"reserve_volume_minimale_Gio": 39},
    "contrat_volume_41": {"reserve_volume_minimale_Gio": 41},
    "contrat_reference_autre": {
        "reference_ratification_budget": "CAP0-AUTRE-REFERENCE"},
    "contrat_statut_non_etabli": {"budget_production_statut": "NON_ETABLI"},
    "contrat_ancienne_version_1_2_0": {"version": "1.2.0"},
    "contrat_politique_autre": {"politique_capacite_version": "cap1-0.9.0"},
}

FAUTES_SUPPORT = {
    "support_autre_volume": {"C7C1_TEST_LETTRE_RUNS": "D"},
    "support_non_fixe": {"C7C1_TEST_TYPE_LECTEUR": "2"},
    "support_non_ntfs": {"C7C1_TEST_SYSTEME_FICHIERS": "FAT32"},
    "support_media_hdd": {"C7C1_TEST_SUPPORT_MEDIA": "HDD"},
    "support_bus_usb": {"C7C1_TEST_SUPPORT_BUS": "USB"},
    "support_sante_degradee": {"C7C1_TEST_SUPPORT_SANTE": "Warning"},
    "support_indisponible": {"C7C1_TEST_SUPPORT_INDISPONIBLE": "1"},
}

FAUTES_AUTORISATION = {
    "autorisation_budget_non_ratifie":
        ("budget_production_requis_Gio", 25, "budget de production"),
    "autorisation_reserve_reprise_autre":
        ("reserve_reprise_Gio", 2.0, "réserve de reprise"),
    "autorisation_reserve_volume_autre":
        ("reserve_volume_minimale_Gio", 60, "réserve de volume"),
    "autorisation_politique_autre":
        ("politique_capacite_version", "cap1-0.0.1", "politique de capacité"),
    "autorisation_support_autre":
        ("support_actif_identite_expurgee", {"lettre_volume": "D"},
         "support actif"),
    "autorisation_reference_autre":
        ("budget_production_ratification", "CAP0-FANTAISIE",
         "référence de ratification"),
}


def executer_faute(nom: str) -> int:  # noqa: C901 - table de fautes
    """Chaque faute doit être détectée (exit 1). Exit 0 = non détectée."""
    _preparer()
    import run_mcmc_xz_g2_4 as lanceur
    from run_mcmc_xz_g2_4 import ArretCapaciteC7C1, GardeErreur

    cible = os.environ["C7C1_XZ_OUT_DIR"]

    def _detecte(fn, exceptions=(GardeErreur, ArretCapaciteC7C1, ValueError,
                                 OSError, KeyError, TypeError)):
        try:
            fn()
            return 0
        except exceptions:
            return 1

    def _detecte_message(fn, fragment: str) -> int:
        try:
            fn()
            return 0
        except (GardeErreur, ArretCapaciteC7C1) as exc:
            return 1 if fragment in str(exc) else 0
        except Exception:  # noqa: BLE001 - autre cause : non probant
            return 0

    # ---- contrat privé : valeurs ratifiées exactes --------------------
    if nom in FAUTES_CONTRAT:
        with tempfile.TemporaryDirectory() as tmp:
            faux = _contrat_modifie(lanceur, Path(tmp), **FAUTES_CONTRAT[nom])
            with _env(C7C1_CONTRAT_LOCAL=faux):
                return _detecte(lanceur.garde_contrat_local)

    # ---- support actif ------------------------------------------------
    if nom in FAUTES_SUPPORT:
        with _env(**FAUTES_SUPPORT[nom]):
            return _detecte_message(
                lambda: lanceur.garde_support_actif(cible),
                "support" if nom != "support_indisponible" else "indisponible")
    if nom == "support_sous_git":
        depot = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                               capture_output=True, text=True,
                               check=True).stdout.strip()
        return _detecte(lambda: lanceur.garde_support_actif(depot))
    if nom == "support_sous_onedrive":
        contrat = json.loads(Path(
            os.environ["C7C1_CONTRAT_LOCAL"]).read_text(encoding="utf-8"))
        ailleurs = contrat["chemins_reels"]["depot_historique_non_directeur"]
        return _detecte(lambda: lanceur.garde_support_actif(ailleurs))

    # ---- mesure d'occupation ------------------------------------------
    if nom == "taille_negative":
        with tempfile.TemporaryDirectory() as tmp:
            _arbre_synthetique(Path(tmp))
            lanceur._taille_brute = lambda e: -1
            return _detecte_message(
                lambda: lanceur.mesurer_occupation_lot(tmp), "négative")
    if nom == "taille_forgee":
        with tempfile.TemporaryDirectory() as tmp:
            _arbre_synthetique(Path(tmp))
            lanceur._taille_brute = lambda e: "4096"  # valeur forgée
            return _detecte_message(
                lambda: lanceur.mesurer_occupation_lot(tmp), "forgée")
    if nom == "fichier_apparait_pendant_le_scan":
        with tempfile.TemporaryDirectory() as tmp:
            _arbre_synthetique(Path(tmp))
            reel = lanceur._inventorier_occupation
            passages = {"n": 0}

            def instable(racine, cluster):
                resultat = reel(racine, cluster)
                passages["n"] += 1
                if passages["n"] == 1:  # un fichier apparaît entre les passes
                    (Path(tmp) / "apparu.txt").write_bytes(b"z" * 512)
                return resultat

            lanceur._inventorier_occupation = instable
            return _detecte_message(
                lambda: lanceur.mesurer_occupation_lot(tmp), "instable")
    if nom == "identite_canonique_hors_racine":
        # Cause DISTINCTE du point d'analyse : une entrée ordinaire dont
        # l'identité canonique résout hors de la racine (forme que
        # realpath déplierait, p. ex. un point de montage). Éprouve le
        # contrôle _sous_racine sans dépendre d'un privilège de lien.
        with tempfile.TemporaryDirectory() as tmp:
            _arbre_synthetique(Path(tmp))
            piege = Path(tmp) / "hors_racine.bin"
            piege.write_bytes(b"h" * 256)
            dehors = os.path.join(os.path.dirname(tmp.rstrip("\\/")),
                                  "ailleurs_cap1", "hors_racine.bin")
            reel_canonique = lanceur._canonique

            def canonique_devie(chemin):
                if str(chemin).endswith("hors_racine.bin"):
                    return os.path.normcase(dehors)
                return reel_canonique(chemin)

            lanceur._canonique = canonique_devie
            return _detecte_message(
                lambda: lanceur.mesurer_occupation_lot(tmp),
                "hors de la racine de runs")
    if nom == "lien_interne_suivi_double_compte":
        # INJECTION : _est_lien est neutralisé, donc une jonction INTERNE
        # est parcourue. La mesure double alors l'occupation et invente un
        # run fantôme — un budget sur-compté ABAISSE le seuil d'admission,
        # donc relâche la garde. C'est le seul test qui exerce _est_lien.
        with tempfile.TemporaryDirectory() as tmp:
            run = _arbre_synthetique(Path(tmp))
            lien = run.parent / "jonction_interne"
            cree = subprocess.run(
                ["cmd", "/c", "mklink", "/J", str(lien), str(run)],
                capture_output=True, text=True)
            if cree.returncode != 0:
                print(f"JONCTION INTERNE NON CREABLE : {cree.stderr[:120]}")
                return 0
            try:
                avant = lanceur.mesurer_occupation_lot(tmp)
                lanceur._est_lien = lambda entree: False
                apres = lanceur.mesurer_occupation_lot(tmp)
            finally:
                with contextlib.suppress(OSError):
                    os.rmdir(lien)
            rel = "g2_4/P_WS/" + VARIANTE_TEST + "/jonction_interne"
            return 1 if (avant["liens_non_suivis"] == [rel]
                         and apres["liens_non_suivis"] == []
                         and apres["octets_production"]
                         > avant["octets_production"]) else 0
    if nom == "point_analyse_sortant":
        with tempfile.TemporaryDirectory() as tmp:
            _arbre_synthetique(Path(tmp))
            with tempfile.TemporaryDirectory() as dehors:
                (Path(dehors) / "gros.bin").write_bytes(b"y" * 8192)
                lien = Path(tmp) / "jonction_sortante"
                cree = subprocess.run(
                    ["cmd", "/c", "mklink", "/J", str(lien), dehors],
                    capture_output=True, text=True)
                if cree.returncode != 0:
                    # Sans point d'analyse testable, la faute est déclarée
                    # NON ÉPROUVÉE plutôt que faussement validée.
                    print(f"POINT D'ANALYSE NON CREABLE : {cree.stderr[:120]}")
                    return 0
                try:
                    return _detecte_message(
                        lambda: lanceur.mesurer_occupation_lot(tmp),
                        "hors de la racine de runs")
                finally:
                    # Le point d'analyse est retiré AVANT tout nettoyage
                    # récursif : rien hors de l'arbre de test n'est touché.
                    with contextlib.suppress(OSError):
                        os.rmdir(lien)
    if nom == "temporaire_qualification_compte_comme_production":
        # INJECTION : on retire « g2_4_qualification » des temporaires
        # reconnus. Un répertoire de qualification porteur d'un manifeste
        # serait alors compté comme production — c'est la faute.
        with tempfile.TemporaryDirectory() as tmp:
            qualif = Path(tmp) / "g2_4_qualification" / "run"
            qualif.mkdir(parents=True)
            (qualif / "chain.1.txt").write_bytes(b"q" * 4096)
            (qualif / "manifest.json").write_text(
                json.dumps({"schema": lanceur.SCHEMA_MANIFESTE_RUN}),
                encoding="utf-8")
            avant = lanceur.mesurer_occupation_lot(tmp)["octets_production"]
            lanceur.SOUS_ARBRES_TEMPORAIRES_RECONNUS = ()
            apres = lanceur.mesurer_occupation_lot(tmp)["octets_production"]
            return 1 if (avant == 0 and apres > 0) else 0
    if nom == "budget_deja_depasse":
        occupation = {"gio_production": 25.0, "octets_production": 0,
                      "octets_temporaires_reconnus": 0,
                      "octets_non_attribues": 0, "runs_production": {},
                      "liens_non_suivis": [], "stabilite_verifiee": True}
        return _detecte_message(
            lambda: lanceur.garde_capacite_production(
                cible, VARIANTE_TEST, occupation=occupation),
            "budget déjà dépassé")

    # ---- admission ------------------------------------------------------
    if nom in ("libre_seuil_moins_un_octet", "libre_45_gio_refuse"):
        seuil = _seuil_admission(lanceur, cible)
        libre = (seuil - 1.0 / lanceur.GIO
                 if nom == "libre_seuil_moins_un_octet" else 45.0)
        with _env(C7C1_TEST_ESPACE_LIBRE_GIO=repr(libre)):
            return _detecte_message(
                lambda: lanceur.garde_capacite_production(cible, VARIANTE_TEST),
                "admission refusée")
    if nom == "ancienne_regle_acceptait_45_gio":
        # INJECTION : on rétablit l'ANCIENNE sémantique d'admission
        # (libre >= 40 technique ET libre >= budget). Avec 45 Gio libres et
        # un budget de 20 Gio, elle accepte — c'est précisément le défaut
        # que CAP-1 ferme.
        contrat = json.loads(Path(
            os.environ["C7C1_CONTRAT_LOCAL"]).read_text(encoding="utf-8"))
        with _env(C7C1_TEST_ESPACE_LIBRE_GIO="45"):
            ancienne_accepte = True
            try:
                lanceur.garde_capacite(cible)
                lanceur.garde_budget_production(contrat, cible)
            except GardeErreur:
                ancienne_accepte = False
            nouvelle_refuse = False
            try:
                lanceur.garde_capacite_production(cible, VARIANTE_TEST)
            except GardeErreur:
                nouvelle_refuse = True
        return 1 if (ancienne_accepte and nouvelle_refuse) else 0
    if nom == "grille_inconnue_allouee_par_defaut":
        return _detecte_message(
            lambda: lanceur.allocation_run_actif_gio("M9z-Q"),
            "grille inconnue")

    # ---- observateur de capacité ----------------------------------------
    if nom == "callback_modifie_converged":
        # INJECTION : un observateur FAUTIF qui déguise une interruption de
        # capacité en convergence. L'espion doit s'en apercevoir.
        espion = SamplerEspion(lignes=10)

        def observateur_fautif(sampler):
            sampler.converged = True

        observateur_fautif(espion)
        return 1 if ("converged" in espion.ecritures
                     and "converged" in espion.mutations()) else 0
    if nom == "anticipation_absente_laisse_saturer":
        # INJECTION : on annule la zone d'anticipation. À 40,1 Gio libres —
        # au-dessus de la réserve de 40 Gio, mais dans la zone où le run
        # peut encore écrire avant la prochaine observation — l'observateur
        # RÉEL doit s'arrêter, l'observateur sans anticipation non. C'est
        # exactement le défaut que la marge ferme.
        reel, _ = lanceur.creer_observateur_capacite(
            cible, VARIANTE_TEST, "g2_4/P_WS/M2a-N/s630101")
        lanceur.MARGE_ANTICIPATION_PLANCHER_GIO = 0.0
        lanceur.FACTEUR_SECURITE_ANTICIPATION = 0
        sans_marge, _ = lanceur.creer_observateur_capacite(
            cible, VARIANTE_TEST, "g2_4/P_WS/M2a-N/s630101")
        with _env(C7C1_TEST_ESPACE_LIBRE_GIO="40.1"):
            reel_arrete = False
            try:
                reel(SamplerEspion(lignes=10))
            except ArretCapaciteC7C1:
                reel_arrete = True
            defaut_laisse_passer = True
            try:
                sans_marge(SamplerEspion(lignes=10))
            except ArretCapaciteC7C1:
                defaut_laisse_passer = False
        return 1 if (reel_arrete and defaut_laisse_passer) else 0
    if nom == "callback_sous_haute_eau_sans_arret":
        observateur, _ = lanceur.creer_observateur_capacite(
            cible, VARIANTE_TEST, "g2_4/P_WS/M2a-N/s630101")
        espion = SamplerEspion(lignes=10)
        with _env(C7C1_TEST_ESPACE_LIBRE_GIO="39"):
            return _detecte_message(lambda: observateur(espion),
                                    "haute-eau franchie")
    if nom == "callback_lot_au_dela_du_plafond":
        observateur, _ = lanceur.creer_observateur_capacite(
            cible, VARIANTE_TEST, "g2_4/P_WS/M2a-N/s630101")
        # 65 M lignes x 349 o ≈ 21,1 Gio : au-delà de 20 + 1,15 − 0,25.
        espion = SamplerEspion(lignes=65_000_000)
        with _env(C7C1_TEST_ESPACE_LIBRE_GIO="99"):
            return _detecte_message(lambda: observateur(espion),
                                    "haute-eau franchie")
    if nom == "callback_mesure_impossible_non_marquee":
        # INJECTION : la mesure d'occupation échoue pendant le run. La
        # défaillance doit sortir par l'exception DÉDIÉE, porteuse du statut
        # d'interruption — et non par une GardeErreur nue qui laisserait le
        # run sans statut de capacité.
        observateur, _ = lanceur.creer_observateur_capacite(
            cible, VARIANTE_TEST, "g2_4/P_WS/M2a-N/s630101")

        def mesure_ko(_cible, verifier_stabilite=True):
            raise lanceur.GardeErreur("volume illisible (simulé)")

        lanceur.mesurer_occupation_lot = mesure_ko
        try:
            observateur(SamplerEspion(lignes=10))
            return 0
        except ArretCapaciteC7C1 as exc:
            return 1 if (exc.statut_run
                         == lanceur.STATUT_RUN_INTERROMPU_CAPACITE) else 0
        except GardeErreur:
            return 0  # exception NON dédiée : le défaut subsiste
    if nom == "callback_observabilite_perdue":
        observateur, _ = lanceur.creer_observateur_capacite(
            cible, VARIANTE_TEST, "g2_4/P_WS/M2a-N/s630101")

        class SansCollection:
            pass

        return _detecte_message(lambda: observateur(SansCollection()),
                                "observabilité perdue")
    if nom == "injection_modifie_le_sampler":
        # INJECTION : une injection FAUTIVE qui touche aussi la proposition.
        import xz_cobaya_g2_4 as adaptateur

        info = adaptateur.build_cobaya_info(
            lanceur.DESCRIPTEURS[VARIANTE_TEST], GRAINE_TEST)
        reelle = lanceur.injecter_observateur_capacite

        def injection_fautive(info_, obs):
            copie = reelle(info_, obs)
            copie["sampler"]["mcmc"]["proposal_scale"] = 2.5
            return copie

        lanceur.injecter_observateur_capacite = injection_fautive
        return _detecte_message(
            lambda: lanceur.garde_injection_observateur(info, lambda s: None),
            "l'injection de l'observateur modifie")

    # ---- reprise après interruption de capacité --------------------------
    if nom.startswith("reprise_"):
        with tempfile.TemporaryDirectory() as tmp:
            if nom == "reprise_sans_checkpoint":
                prefixe, attendue = _run_repris(
                    lanceur, Path(tmp), checkpoint=None)
                fragment = "checkpoint Cobaya absent"
            elif nom == "reprise_checkpoint_vide":
                prefixe, attendue = _run_repris(
                    lanceur, Path(tmp), checkpoint="   \n")
                fragment = "checkpoint vide"
            elif nom == "reprise_checkpoint_illisible":
                prefixe, attendue = _run_repris(
                    lanceur, Path(tmp), checkpoint="ceci n'est pas un bloc")
                fragment = "checkpoint sans bloc sampler"
            elif nom == "reprise_statut_converge":
                prefixe, attendue = _run_repris(
                    lanceur, Path(tmp), checkpoint=CHECKPOINT_VALIDE,
                    statut=lanceur.STATUT_RUN_CONVERGE)
                fragment = "déclare CONVERGE"
            elif nom == "reprise_politique_differente":
                prefixe, attendue = _run_repris(
                    lanceur, Path(tmp), checkpoint=CHECKPOINT_VALIDE,
                    politique="cap1-0.0.1")
                fragment = "politique_capacite_version"
            else:
                raise SystemExit(f"faute inconnue : {nom}")
            return _detecte_message(
                lambda: lanceur.garde_reprise_apres_capacite(
                    prefixe, attendue, cible, VARIANTE_TEST), fragment)

    # ---- autorisation : champs de capacité --------------------------------
    if nom in FAUTES_AUTORISATION:
        from qualify_xz_launcher_g2_4d import (_autorisation_nominale_memoire,
                                               _support_mesure)

        champ, valeur, fragment = FAUTES_AUTORISATION[nom]
        manifeste = _autorisation_nominale_memoire(
            lanceur, VARIANTE_TEST, GRAINE_TEST)
        manifeste[champ] = valeur
        # Le support est mesuré HORS de la fonction éprouvée : une
        # indisponibilité matérielle ne doit jamais pouvoir se déguiser en
        # « faute non détectée ». Elle remonterait ici en exception nue.
        support_t = _support_mesure(lanceur)
        head_t = lanceur.garde_git()["head"]
        return _detecte_message(
            lambda: lanceur._valider_contenu_autorisation(
                manifeste, VARIANTE_TEST, GRAINE_TEST, head_t,
                budget_contrat=lanceur.BUDGET_TOTAL_RATIFIE_GIO,
                ratification_contrat=lanceur.REFERENCE_RATIFICATION_BUDGET,
                support_attendu=support_t), fragment)

    # ---- verrou -----------------------------------------------------------
    if nom == "verrou_retire":
        # INJECTION : le verrou est simulé abaissé ; le contrôle statique
        # de la porte doit s'en apercevoir.
        source = Path("scripts/run_mcmc_xz_g2_4.py").read_text(encoding="utf-8")
        falsifie = source.replace("VERROU_PRODUCTION_G2_4D = True",
                                  "VERROU_PRODUCTION_G2_4D = False", 1)
        return 1 if _verrou_declare(falsifie) is False else 0
    raise SystemExit(f"faute inconnue : {nom}")


FAUTES = (
    *sorted(FAUTES_CONTRAT),
    *sorted(FAUTES_SUPPORT),
    "support_sous_git", "support_sous_onedrive",
    "taille_negative", "taille_forgee", "fichier_apparait_pendant_le_scan",
    "identite_canonique_hors_racine", "point_analyse_sortant",
    "lien_interne_suivi_double_compte",
    "temporaire_qualification_compte_comme_production", "budget_deja_depasse",
    "libre_seuil_moins_un_octet", "libre_45_gio_refuse",
    "ancienne_regle_acceptait_45_gio", "grille_inconnue_allouee_par_defaut",
    "callback_modifie_converged", "anticipation_absente_laisse_saturer",
    "callback_sous_haute_eau_sans_arret", "callback_lot_au_dela_du_plafond",
    "callback_observabilite_perdue", "callback_mesure_impossible_non_marquee",
    "injection_modifie_le_sampler",
    "reprise_sans_checkpoint", "reprise_checkpoint_vide",
    "reprise_checkpoint_illisible", "reprise_statut_converge",
    "reprise_politique_differente",
    *sorted(FAUTES_AUTORISATION),
    "verrou_retire",
)


# ------------------------------------------------------------- utilitaires

def _seuil_admission(lanceur, cible) -> float:
    """Seuil d'admission courant, lu de la garde elle-même."""
    with _env(C7C1_TEST_ESPACE_LIBRE_GIO="1000000"):
        return lanceur.garde_capacite_production(
            cible, VARIANTE_TEST)["seuil_admission_gio"]


def _verrou_declare(source: str):
    """Valeur littérale de VERROU_PRODUCTION_G2_4D dans une source."""
    for noeud in ast.parse(source).body:
        if isinstance(noeud, ast.Assign):
            for cible in noeud.targets:
                if (isinstance(cible, ast.Name)
                        and cible.id == "VERROU_PRODUCTION_G2_4D"):
                    return ast.literal_eval(noeud.value)
    return None


def _aucune_ecriture_sampler(source: str) -> dict:
    """Contrôle STATIQUE : aucune affectation d'attribut de sampler.

    Interdit en particulier ``sampler.converged = True`` — qui ferait
    passer une interruption de capacité pour une convergence — et, plus
    largement, toute affectation d'attribut sur le paramètre du callback.
    """
    arbre = ast.parse(source)
    affectations_converged: list[int] = []
    affectations_sampler: list[str] = []
    for noeud in ast.walk(arbre):
        cibles = []
        if isinstance(noeud, ast.Assign):
            cibles = list(noeud.targets)
        elif isinstance(noeud, (ast.AugAssign, ast.AnnAssign)):
            cibles = [noeud.target]
        for cible in cibles:
            if not isinstance(cible, ast.Attribute):
                continue
            if cible.attr == "converged":
                affectations_converged.append(cible.lineno)
            if (isinstance(cible.value, ast.Name)
                    and cible.value.id == "sampler"):
                affectations_sampler.append(f"{cible.value.id}.{cible.attr}")
    return {
        "affectations_converged": affectations_converged,
        "affectations_sur_sampler": sorted(set(affectations_sampler)),
    }


# ---------------------------------------------------------- qualification

def qualification() -> int:  # noqa: C901 - porte de qualification
    _preparer()
    import run_mcmc_xz_g2_4 as lanceur
    import xz_cobaya_g2_4 as adaptateur
    from qualify_xz_launcher_g2_4d import (_autorisation_nominale_memoire,
                                           _support_mesure)
    from run_mcmc_xz_g2_4 import ArretCapaciteC7C1, GardeErreur

    echecs: list[str] = []
    resultat: dict = {}
    volatil: dict = {}
    cible = os.environ["C7C1_XZ_OUT_DIR"]

    # ---- 1. politique ratifiée, matérialisée --------------------------
    allocations = {g: lanceur.allocation_run_actif_gio(f"{g}-N")
                   for g in ("M2a", "M2b")}
    b_chain_s8 = (16 * lanceur.LIGNES_S8_PAR_RUN
                  * lanceur.OCTETS_PAR_LIGNE_BORNE["M2a"]
                  + 16 * lanceur.LIGNES_S8_PAR_RUN
                  * lanceur.OCTETS_PAR_LIGNE_BORNE["M2b"]) / lanceur.GIO
    politique = {
        "budget_total_Gio": lanceur.BUDGET_TOTAL_RATIFIE_GIO,
        "reserve_reprise_Gio": lanceur.RESERVE_REPRISE_RATIFIEE_GIO,
        "reserve_volume_minimale_Gio": lanceur.RESERVE_VOLUME_RATIFIEE_GIO,
        "reference_ratification_budget":
            lanceur.REFERENCE_RATIFICATION_BUDGET,
        "politique_capacite_version": lanceur.POLITIQUE_CAPACITE_VERSION,
        "lignes_S8_par_run": lanceur.LIGNES_S8_PAR_RUN,
        "octets_par_ligne_borne": dict(lanceur.OCTETS_PAR_LIGNE_BORNE),
        "ratio_auxiliaire_max": lanceur.RATIO_AUXILIAIRE_MAX,
        "allocation_run_actif_Gio": allocations,
        "controle_croise_B_chain_S8_Gio": round(b_chain_s8, 3),
        "callback_every": lanceur.CALLBACK_EVERY_ITERATIONS,
        "marge_anticipation_Gio": lanceur.marge_anticipation_gio(),
    }
    # Contrôle croisé avec le rapport CAP-0 publié : 17,785 Gio.
    if abs(b_chain_s8 - 17.785) > 0.001:
        echecs.append(f"B_chain(S8) recalculé {b_chain_s8:.4f} != 17,785 Gio")
    resultat["politique_ratifiee"] = politique

    # ---- 2. contrat privé : conformité, sans exposer son contenu ------
    contrat = lanceur.garde_contrat_local()
    contrat.pop("_contrat")
    conforme_contrat = {
        "version_conforme":
            contrat["version_contrat_local"] == lanceur.VERSION_CONTRAT_LOCAL,
        "statut_preparation_only": contrat["statut"] == "PREPARATION_ONLY",
        "budget_ratifie": contrat["budget_production_statut"] == "RATIFIE",
        "budget_exact": float(contrat["budget_production_requis_Gio"])
            == float(lanceur.BUDGET_TOTAL_RATIFIE_GIO),
        "reserve_reprise_exacte": float(contrat["reserve_reprise_Gio"])
            == float(lanceur.RESERVE_REPRISE_RATIFIEE_GIO),
        "reserve_volume_exacte":
            float(contrat["reserve_volume_minimale_Gio"])
            == float(lanceur.RESERVE_VOLUME_RATIFIEE_GIO),
        "reference_conforme": contrat["reference_ratification_budget"]
            == lanceur.REFERENCE_RATIFICATION_BUDGET,
        "racine_runs_sur_volume_ratifie":
            contrat["racine_runs_sur_volume_ratifie"],
        "garde_technique_independante_conservee":
            contrat["garde_technique_minimale_Gio"]
            == lanceur.GARDE_CAPACITE_GIO,
    }
    resultat["contrat_prive"] = conforme_contrat
    for cle, valeur in conforme_contrat.items():
        if valeur is not True:
            echecs.append(f"contrat privé : {cle} non conforme")

    # ---- 3. occupation du lot : mesure sûre ---------------------------
    occupation = lanceur.mesurer_occupation_lot(cible, verifier_stabilite=True)
    resultat["occupation_lot"] = {
        "octets_production": occupation["octets_production"],
        "octets_non_attribues": occupation["octets_non_attribues"],
        "runs_production": occupation["runs_production"],
        "liens_non_suivis": occupation["liens_non_suivis"],
        "stabilite_verifiee": occupation["stabilite_verifiee"],
        "zero_en_absence_de_run": occupation["octets_production"] == 0,
        "temporaires_reconnus_declares":
            list(lanceur.SOUS_ARBRES_TEMPORAIRES_RECONNUS),
    }
    # L'occupation des temporaires reconnus est VOLATILE (le TEMP
    # scientifique vit sous la racine) : elle est mesurée et publiée, mais
    # hors de la section soumise au contrôle de déterminisme.
    volatil["octets_temporaires_reconnus"] = \
        occupation["octets_temporaires_reconnus"]
    if occupation["octets_production"] != 0:
        echecs.append(
            "budget consommé non nul alors qu'aucun run réel n'existe : "
            f"{occupation['octets_production']} octets")
    # attribution sur arborescence SYNTHÉTIQUE (jamais dans <RUNS> réel)
    with tempfile.TemporaryDirectory(prefix="c7c1_cap1_occ_") as tmp:
        _arbre_synthetique(Path(tmp), production=True, octets=4096)
        qualif = Path(tmp) / "g2_4_qualification" / "bruit"
        qualif.mkdir(parents=True)
        (qualif / "data.bin").write_bytes(b"t" * 8192)
        (Path(tmp) / "orphelin.txt").write_bytes(b"o" * 100)
        # Jonction INTERNE : elle doit être enregistrée et NON parcourue —
        # sinon le run serait compté deux fois. Propriété assertée ici, et
        # non simplement publiée.
        run_synth = (Path(tmp) / "g2_4" / "P_WS" / VARIANTE_TEST
                     / f"s{GRAINE_TEST}")
        lien_interne = run_synth.parent / "jonction_interne"
        cree = subprocess.run(
            ["cmd", "/c", "mklink", "/J", str(lien_interne), str(run_synth)],
            capture_output=True, text=True)
        rel_lien = f"g2_4/P_WS/{VARIANTE_TEST}/jonction_interne"
        try:
            synth = lanceur.mesurer_occupation_lot(tmp)
        finally:
            if cree.returncode == 0:
                with contextlib.suppress(OSError):
                    os.rmdir(lien_interne)
        attribution = {
            "production_octets": synth["octets_production"],
            "temporaires_octets": synth["octets_temporaires_reconnus"],
            "non_attribues_octets": synth["octets_non_attribues"],
            "runs_detectes": sorted(synth["runs_production"]),
            "cluster_octets": synth["taille_cluster_octets"],
            "jonction_interne_creable": cree.returncode == 0,
            "liens_non_suivis": synth["liens_non_suivis"],
        }
        lien_ok = (synth["liens_non_suivis"] == [rel_lien]
                   if cree.returncode == 0 else True)
        ok_attrib = (synth["octets_production"] > 0
                     and synth["octets_temporaires_reconnus"] > 0
                     and synth["octets_non_attribues"] > 0
                     and lien_ok
                     and sorted(synth["runs_production"])
                     == [f"g2_4/P_WS/{VARIANTE_TEST}/s{GRAINE_TEST}"])
        attribution["lien_interne_enregistre_non_suivi"] = lien_ok
        attribution["conforme"] = ok_attrib
    resultat["attribution_synthetique"] = attribution
    if not ok_attrib:
        echecs.append("attribution production / temporaire / non attribué "
                      "non conforme sur l'arborescence synthétique")

    # ---- 4. admission : seuil exact, seuil − 1 octet, 45 Gio ----------
    seuil = _seuil_admission(lanceur, cible)
    admission: dict = {"seuil_admission_gio": seuil}
    with _env(C7C1_TEST_ESPACE_LIBRE_GIO=repr(seuil)):
        try:
            etat = lanceur.garde_capacite_production(cible, VARIANTE_TEST)
            admission["seuil_exact_accepte"] = True
            admission["marge_au_seuil_gio"] = etat["marge_apres_admission_gio"]
        except GardeErreur as exc:
            admission["seuil_exact_accepte"] = False
            admission["motif"] = str(exc)
    for etiquette, libre in (("seuil_moins_un_octet", seuil - 1.0 / lanceur.GIO),
                             ("quarante_cinq_gio", 45.0),
                             ("trente_neuf_gio", 39.0)):
        with _env(C7C1_TEST_ESPACE_LIBRE_GIO=repr(libre)):
            try:
                lanceur.garde_capacite_production(cible, VARIANTE_TEST)
                admission[f"{etiquette}_refuse"] = False
            except GardeErreur:
                admission[f"{etiquette}_refuse"] = True
    # L'ancienne paire de gardes acceptait 45 Gio : preuve du changement.
    contrat_brut = json.loads(
        Path(os.environ["C7C1_CONTRAT_LOCAL"]).read_text(encoding="utf-8"))
    with _env(C7C1_TEST_ESPACE_LIBRE_GIO="45"):
        try:
            lanceur.garde_capacite(cible)
            lanceur.garde_budget_production(contrat_brut, cible)
            admission["ancienne_paire_acceptait_45_gio"] = True
        except GardeErreur:
            admission["ancienne_paire_acceptait_45_gio"] = False
    # Subsomption : seuil − allocation = restant + reprise + volume >= volume,
    # donc la troisième condition de refus est INATTEIGNABLE sous les
    # constantes ratifiées. Elle est conservée en défense en profondeur et
    # ce fait est publié plutôt que masqué par un test de complaisance.
    admission["condition_reserve_volume_subsumee"] = (
        seuil - allocations["M2a"]
        >= float(lanceur.RESERVE_VOLUME_RATIFIEE_GIO))
    admission["budget_depasse_refuse"] = True
    try:
        lanceur.garde_capacite_production(
            cible, VARIANTE_TEST,
            occupation={"gio_production": 25.0, "octets_production": 0,
                        "octets_temporaires_reconnus": 0,
                        "octets_non_attribues": 0, "runs_production": {},
                        "liens_non_suivis": [], "stabilite_verifiee": True})
        admission["budget_depasse_refuse"] = False
    except GardeErreur:
        pass
    resultat["admission"] = admission
    attentes_admission = {
        "seuil_exact_accepte": True, "seuil_moins_un_octet_refuse": True,
        "quarante_cinq_gio_refuse": True, "trente_neuf_gio_refuse": True,
        "ancienne_paire_acceptait_45_gio": True,
        "condition_reserve_volume_subsumee": True,
        "budget_depasse_refuse": True,
    }
    for cle, attendu in attentes_admission.items():
        if admission.get(cle) is not attendu:
            echecs.append(f"admission : {cle} = {admission.get(cle)} "
                          f"(attendu {attendu})")
    if abs(seuil - 61.15) > 1e-9:
        echecs.append(f"seuil initial {seuil} != 61,15 Gio ratifiés")

    # ---- 5. support actif ----------------------------------------------
    support = lanceur.garde_support_actif(cible)
    resultat["support_actif"] = {
        "identite_expurgee": support["identite_expurgee"],
        "qualification_materielle_disponible":
            support["qualification_materielle_disponible"],
        "aucun_modele_ni_numero_de_serie": not any(
            c in support["identite_expurgee"]
            for c in ("modele", "model", "serial", "numero_serie")),
    }
    if not resultat["support_actif"]["aucun_modele_ni_numero_de_serie"]:
        echecs.append("l'identité du support publie un modèle ou un numéro")

    # ---- 6. observateur : lecture pure, haute-eau -----------------------
    source_lanceur = Path("scripts/run_mcmc_xz_g2_4.py").read_text(
        encoding="utf-8")
    statique = _aucune_ecriture_sampler(source_lanceur)
    observateur, etat_obs = lanceur.creer_observateur_capacite(
        cible, VARIANTE_TEST, f"g2_4/P_WS/{VARIANTE_TEST}/s{GRAINE_TEST}")
    espion = SamplerEspion(lignes=12_345)
    # Contrôle POSITIF : bien au-dessus de la haute-eau, l'observateur doit
    # rendre la main sans exception ET sans mutation.
    with _env(C7C1_TEST_ESPACE_LIBRE_GIO="99"):
        try:
            retour = observateur(espion)
            exception_injustifiee = None
        except ArretCapaciteC7C1 as exc:
            retour, exception_injustifiee = "EXCEPTION", str(exc)[:120]
    sous_haute_eau = {}
    espion_bas = SamplerEspion(lignes=12_345)
    with _env(C7C1_TEST_ESPACE_LIBRE_GIO="39"):
        try:
            observateur(espion_bas)
            sous_haute_eau["exception"] = None
        except ArretCapaciteC7C1 as exc:
            sous_haute_eau = {"exception": type(exc).__name__,
                              "statut_run": exc.statut_run,
                              "message": str(exc)[:120]}
    espion_lot = SamplerEspion(lignes=65_000_000)
    with _env(C7C1_TEST_ESPACE_LIBRE_GIO="99"):
        try:
            observateur(espion_lot)
            plafond_lot = None
        except ArretCapaciteC7C1 as exc:
            plafond_lot = str(exc)[:120]
    resultat["observateur_capacite"] = {
        "retour_hors_haute_eau": retour,
        "exception_injustifiee_hors_haute_eau": exception_injustifiee,
        "ecritures_attribut_sampler": espion.ecritures,
        "mutations_valeurs": espion.mutations(),
        "ecritures_sous_haute_eau": espion_bas.ecritures,
        "mutations_sous_haute_eau": espion_bas.mutations(),
        "exception_sous_haute_eau": sous_haute_eau,
        "exception_plafond_lot": plafond_lot,
        "controle_statique": statique,
        "haute_eau_lot_gio": etat_obs["haute_eau_lot_gio"],
        "haute_eau_run_gio": etat_obs["haute_eau_run_gio"],
        "callback_every": etat_obs["callback_every"],
        "marge_anticipation_gio": etat_obs["marge_anticipation_gio"],
        "plafond_lot_gio": etat_obs["plafond_lot_gio"],
        "plancher_libre_gio": etat_obs["plancher_libre_gio"],
    }
    if espion.ecritures or espion.mutations():
        echecs.append(f"l'observateur écrit sur le sampler : "
                      f"{espion.ecritures} / {espion.mutations()}")
    if exception_injustifiee is not None:
        echecs.append(f"exception injustifiée hors haute-eau : "
                      f"{exception_injustifiee}")
    if espion_bas.ecritures or espion_bas.mutations():
        echecs.append("l'observateur mute le sampler au moment de l'arrêt")
    if sous_haute_eau.get("exception") != "ArretCapaciteC7C1":
        echecs.append("aucune exception dédiée sous la haute-eau")
    if sous_haute_eau.get("statut_run") != lanceur.STATUT_RUN_INTERROMPU_CAPACITE:
        echecs.append("le statut d'interruption n'est pas "
                      "NON_CONVERGE_INTERRUPTION_CAPACITE")
    if plafond_lot is None:
        echecs.append("le plafond d'occupation du lot ne déclenche pas l'arrêt")
    if statique["affectations_converged"] or statique["affectations_sur_sampler"]:
        echecs.append(f"affectation interdite détectée statiquement : "
                      f"{statique}")

    # ---- 7. injection : opérationnelle, jamais scientifique -------------
    info = adaptateur.build_cobaya_info(
        lanceur.DESCRIPTEURS[VARIANTE_TEST], GRAINE_TEST)
    apres = lanceur.garde_injection_observateur(info, observateur)
    encodage = lanceur.encodage_scientifique_gele(VARIANTE_TEST, GRAINE_TEST)
    injection = {
        "differences": lanceur.differences_injection(info, apres),
        "callback_absent_de_l_encodage_scientifique":
            "callback" not in json.dumps(encodage["sampler"]),
        "sha256_encodage_scientifique":
            encodage["sha256_encodage_scientifique"],
        "sampler_original_intact":
            "callback_function" not in info["sampler"]["mcmc"],
        "callback_every_injecte":
            apres["sampler"]["mcmc"]["callback_every"]
            == lanceur.CALLBACK_EVERY_ITERATIONS,
    }
    resultat["injection_observateur"] = injection
    if injection["differences"] != ["sampler.mcmc.callback_every",
                                    "sampler.mcmc.callback_function"]:
        echecs.append(f"injection non minimale : {injection['differences']}")
    for cle in ("callback_absent_de_l_encodage_scientifique",
                "sampler_original_intact", "callback_every_injecte"):
        if injection[cle] is not True:
            echecs.append(f"injection : {cle} non conforme")

    # ---- 8. reprise après interruption de capacité ----------------------
    with tempfile.TemporaryDirectory(prefix="c7c1_cap1_rep_") as tmp:
        prefixe, attendue = _run_repris(lanceur, Path(tmp),
                                        checkpoint=CHECKPOINT_VALIDE)
        reprise = {"nominale_acceptee": True}
        try:
            etat_reprise = lanceur.garde_reprise_apres_capacite(
                prefixe, attendue, cible, VARIANTE_TEST)
            reprise["statut_run_repris"] = etat_reprise["statut_run_repris"]
            reprise["nouvelle_admission_seuil_gio"] = \
                etat_reprise["nouvelle_admission"]["seuil_admission_gio"]
        except GardeErreur as exc:
            reprise["nominale_acceptee"] = False
            reprise["motif"] = str(exc)[:160]
        sans_cp, attendue2 = _run_repris(
            lanceur, Path(tmp) / "bis", checkpoint=None)
        try:
            lanceur.garde_reprise_apres_capacite(
                sans_cp, attendue2, cible, VARIANTE_TEST)
            reprise["sans_checkpoint_refusee"] = False
        except GardeErreur as exc:
            reprise["sans_checkpoint_refusee"] = True
            reprise["motif_sans_checkpoint"] = str(exc)[:200]
    reprise["limite_bloquante_documentee"] = (
        "Cobaya 3.5 n'écrit le checkpoint qu'au cycle learn_every (et une "
        "fois à l'initialisation) ; il n'existe pas de checkpoint_every. "
        "Un arrêt de capacité peut donc survenir sans checkpoint récent : "
        "la reprise automatique est alors IMPOSSIBLE et la garde refuse. "
        "Aucun checkpoint n'est fabriqué.")
    reprise["statut_jamais_converge"] = (
        lanceur.STATUT_RUN_INTERROMPU_CAPACITE != lanceur.STATUT_RUN_CONVERGE)
    resultat["reprise_apres_capacite"] = reprise
    for cle in ("nominale_acceptee", "sans_checkpoint_refusee",
                "statut_jamais_converge"):
        if reprise.get(cle) is not True:
            echecs.append(f"reprise : {cle} non conforme")

    # ---- 9. manifeste de run : champs de capacité -----------------------
    identite = lanceur.identite_run(
        VARIANTE_TEST, GRAINE_TEST, lanceur.garde_git()["head"], contrat,
        lanceur.garde_environnement(),
        lanceur.garde_descripteur(VARIANTE_TEST), lanceur.garde_donnees(),
        date_creation_utc=DATE_QUALIFICATION_UTC,
        sha256_autorisation="0" * 64,
        budget_requis_gio=lanceur.BUDGET_TOTAL_RATIFIE_GIO,
        reference_ratification_budget=lanceur.REFERENCE_RATIFICATION_BUDGET,
        support_actif_identite_expurgee=support["identite_expurgee"])
    manquants = [c for c in lanceur.CHAMPS_MANIFESTE_RUN if c not in identite]
    resultat["manifeste_run"] = {
        "schema": identite["schema"],
        "champs_manquants": manquants,
        "n_champs": len(lanceur.CHAMPS_MANIFESTE_RUN),
        "champs_politique_capacite": {
            c: identite[c] for c in lanceur.CHAMPS_POLITIQUE_CAPACITE},
        "statut_run": identite["statut_run"],
        "aucun_manifeste_reel_ecrit": True,
    }
    if manquants:
        echecs.append(f"manifeste de run : champs manquants {manquants}")
    if identite["schema"] != "c7c1-run-manifest-2":
        echecs.append(f"schéma de manifeste non bumpé : {identite['schema']}")

    # ---- 10. autorisation : contrôle positif ----------------------------
    nominal = _autorisation_nominale_memoire(
        lanceur, VARIANTE_TEST, GRAINE_TEST)
    traverses = lanceur._valider_contenu_autorisation(
        nominal, VARIANTE_TEST, GRAINE_TEST, lanceur.garde_git()["head"],
        budget_contrat=lanceur.BUDGET_TOTAL_RATIFIE_GIO,
        ratification_contrat=lanceur.REFERENCE_RATIFICATION_BUDGET,
        support_attendu=_support_mesure(lanceur))
    groupes_manquants = [g for g in lanceur.GROUPES_CONTROLE_AUTORISATION
                         if g not in traverses]
    resultat["autorisation"] = {
        "groupes_traverses": traverses,
        "groupes_manquants": groupes_manquants,
        "groupes_capacite_presents": [
            g for g in ("budget_ratifie", "reserve_reprise", "reserve_volume",
                        "politique_capacite", "support_actif")
            if g in traverses],
        "aucune_autorisation_reelle": True,
    }
    if groupes_manquants:
        echecs.append(f"autorisation : groupes non traversés "
                      f"{groupes_manquants}")

    # ---- 11. verrou : déclaré et dynamique -------------------------------
    from qualify_xz_launcher_g2_4d import _verrou_nominal

    preuve = _verrou_nominal()
    sentinelles = (preuve["amont_satisfait"]["sentinelles"]
                   + preuve["amont_reel"]["sentinelles"])
    resultat["verrou"] = {
        "VERROU_PRODUCTION_G2_4D": lanceur.VERROU_PRODUCTION_G2_4D,
        "declare_dans_la_source": _verrou_declare(source_lanceur),
        "sentinelles_atteintes": sentinelles,
        "verrou_atteint_amont_satisfait":
            preuve["amont_satisfait"]["verrou_atteint"],
        "arret_amont_satisfait": preuve["amont_satisfait"]["arret"],
        "qualification_only_rejetee": preuve["qualification_only_rejetee"],
    }
    if lanceur.VERROU_PRODUCTION_G2_4D is not True:
        echecs.append("VERROU_PRODUCTION_G2_4D n'est plus True")
    if _verrou_declare(source_lanceur) is not True:
        echecs.append("VERROU_PRODUCTION_G2_4D non déclaré True dans la source")
    if sentinelles:
        echecs.append(f"VERROU FRANCHI : {sorted(set(sentinelles))}")
    if not preuve["amont_satisfait"]["verrou_atteint"]:
        echecs.append("preuve du verrou vacante : l'étape verrouillée n'est "
                      "pas atteinte malgré budget, support et capacité")

    # ---- 12. fautes injectées (sous-processus) ---------------------------
    resultat["fautes"] = {}
    for nom in FAUTES:
        proc = subprocess.run(
            [sys.executable, "scripts/qualify_xz_capacity_cap1.py",
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

    # ---- mesures volatiles (hors contrôle de déterminisme) ---------------
    volatil["espace_libre_reel_gio"] = round(
        lanceur.espace_libre_gio(cible), 3)
    volatil["marge_apres_admission_reelle_gio"] = round(
        lanceur.espace_libre_gio(cible) - seuil, 3)

    resultat["porte"] = {"passe": not echecs, "echecs": sorted(echecs)}
    print("=== SORTIE NORMALISEE (deterministe) ===")
    print(json.dumps(resultat, indent=2, sort_keys=True, ensure_ascii=False))
    print("=== MESURES NON DETERMINISTES (espace libre) ===")
    print(json.dumps(volatil, indent=2, sort_keys=True, ensure_ascii=False))
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
