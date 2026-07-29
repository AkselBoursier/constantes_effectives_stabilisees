"""Qualification des configurations X(z) — porte G2.3a (issue #63).

MODE UNIQUE : qualification déterministe sur points fixes. Aucun mode
MCMC, échantillonnage, minimisation ou optimisation n'existe ; toute
option de ce type est explicitement refusée à l'entrée.

Contrôles exécutés (G2.3b) :
  C1 : schéma strict des quatre YAML ;
  C2 : ordre exact nœuds / paramètres X_i (inclus dans la validation) ;
  C3 : points fixes P0-P3 + sondes hors support (logprior 0 / -inf) ;
  C4 : identité P0/P1 avec LambdaCDM aux seuils T8 ;
  C5 : ré-exécution complète de T8-T12 (suite I1-I9) ;
  C6 : assemblage indépendant d'un vecteur BAO et du vecteur CMB ;
  C7 : fautes injectées (nœuds permutés ; division thetastar/100
       supprimée), détection obligatoire ;
  C8 : refus de toute sortie sous un ancêtre Git.

Sortie : JSON trié sur stdout, sans horodatage ni aléa — deux exécutions
doivent être bit à bit identiques.

PORTE AUTO-BLOQUANTE (G2.3d) : si un seul contrôle échoue, la commande
se termine avec un code de sortie NON NUL après impression du JSON — un
`false` inscrit dans la sortie ne suffit jamais. Auto-test du chemin
d'échec : `C7C1_QUALIF_TEST_ECHEC=1` injecte un échec synthétique et doit
produire un code non nul (hors passes nominales).

Usage depuis la racine C7-C1 :
    python scripts/qualify_xz_configs_g2_3.py
"""

from __future__ import annotations

import json
import math
import os
import subprocess
import sys

import numpy as np

FORBIDDEN_OPTIONS = {
    "--mcmc", "--sample", "--sampling", "--minimize", "--minimise",
    "--optimize", "--optimise", "--fit", "--posterior", "--chain",
}

CONFIGS = [
    "configs/xz/g2_3_m2a_n.yaml",
    "configs/xz/g2_3_m2a_k.yaml",
    "configs/xz/g2_3_m2b_n.yaml",
    "configs/xz/g2_3_m2b_k.yaml",
]

# Points fixes prédéclarés (G2.3b §Points fixes ; valeurs gelées avant la
# première exécution). P2/P3 : profils G2.1 (M2a) ; adaptation M2b par
# suppression de l'amplitude du nœud 4/3 (règle déclarée au rapport).
POINT_FOND_P0 = {"H0": 67.36, "ombh2": 0.02237, "omm": 0.3152}
POINT_FOND_P1 = {"H0": 68.3526, "ombh2": 0.022410, "omm": 0.300539}
P2_VALUES = {"M2a": (0.6, -0.2, 0.4, 1.2, 0.8), "M2b": (0.6, -0.2, 0.4, 0.8)}
P3_VALUES = {"M2a": (1.4, 0.2, 1.6, 0.1, 1.3), "M2b": (1.4, 0.2, 1.6, 1.3)}

# Seuils T8 ratifiés (rapport G2.1 §4).
T8 = {
    "BAO_rel": 1e-13,
    "theta_abs": 1e-9,
    "chi2_BAO_abs": 1e-10,
    "chi2_CMB_abs": 1e-3,
}
# Seuils T9-T12 ratifiés, appliqués à la sortie I1-I9.
T9_T12 = {
    "T9_noeuds": 1e-14,
    "T9_polynomes": 1e-13,
    "T10_continuation": 1e-14,
    "T11_BAO_default_tight": 1e-12,
    "T11_DM_quad_trapezes": 1e-8,
    "T11_rdrag_zmax": 1e-10,
    "T11_DM_zstar": 1e-8,
    "T11_theta": 1e-10,
    "T11_chi2_CMB_stress": 2e-2,
    "T11_I8_X": 1e-12,
    "T11_I8_H": 1e-13,
    "T11_I8_DM_bao": 1e-13,
    "T11_I8_eds": 1e-13,
    "T12_chi2_BAO_corr_fixed": 1e-8,
    "T12_rdrag_corr_fixed": 1e-10,
}


def refuser_options_interdites() -> None:
    presentes = FORBIDDEN_OPTIONS.intersection(sys.argv[1:])
    if presentes:
        print(
            "ARRET — options refusées en G2.3a (aucune inférence autorisée) : "
            + " ".join(sorted(presentes))
        )
        raise SystemExit(2)
    if len(sys.argv) > 1:
        print(f"ARRET — argument non reconnu : {sys.argv[1:]} (mode unique)")
        raise SystemExit(2)


# Tolérances d'ingénierie du contrôle d'assemblage C6 (G2.3d §4).
# Gardes d'assemblage, pas des seuils scientifiques.
TOL_C6_BAO_ABS = 1e-12
TOL_C6_CMB_ABS = 1e-14

VARIANTES_ATTENDUES = {"M2a-N", "M2a-K", "M2b-N", "M2b-K"}


def main() -> None:
    refuser_options_interdites()

    import copy

    from xz_likelihood_g2_3 import (
        CMB_ICOV,
        CMB_MU,
        BAO_KINDS,
        BAO_REDSHIFTS,
        GRAINES_ATTENDUES,
        ConfigError,
        SortieSousGitError,
        XZEvaluator,
        load_bao_data,
        load_config,
        refuser_sortie_sous_git,
        validate_config,
    )
    from test_xz_g2_1 import reference_bao_vector
    from xz_background_g2_1 import CambReference, XZBackground, XZProfile

    resultat: dict = {}
    echecs: list[str] = []
    bao_mean, bao_icov = load_bao_data()

    # C1/C2 — schéma strict et ordre exact.
    schema: dict = {}
    configs = {}
    for rel in CONFIGS:
        cfg = load_config(rel)
        configs[cfg["variante"]] = cfg
        schema[cfg["variante"]] = {
            "fichier": rel.split("/")[-1],
            "grille": cfg["grille"],
            "convention": cfg["convention_spline"],
            "nb_amplitudes": len(cfg["parametres_x"]),
            "graine": cfg["graine"],
            "valide": True,
        }
    graines = [cfg["graine"] for cfg in configs.values()]
    schema["graines_distinctes"] = len(set(graines)) == len(graines)
    resultat["C1_C2_schema"] = schema
    if set(configs.keys()) != VARIANTES_ATTENDUES or len(CONFIGS) != 4:
        echecs.append("C1: les quatre variantes exactes ne sont pas présentes une fois chacune")
    if not schema["graines_distinctes"]:
        echecs.append("C1: graines non distinctes")
    for variante, cfg in configs.items():
        if cfg["graine"] != GRAINES_ATTENDUES[variante]:
            echecs.append(f"C1: graine inexacte pour {variante}")

    # C3 — points fixes et sondes de support.
    evaluations: dict = {}
    identites: dict = {}
    for variante, cfg in sorted(configs.items()):
        ev = XZEvaluator(cfg, bao_mean, bao_icov)
        grille = cfg["grille"]
        noms = [item["nom"] for item in cfg["parametres_x"]]
        unite = {nom: 1.0 for nom in noms}
        points = {
            "P0": {**POINT_FOND_P0, **unite},
            "P1": {**POINT_FOND_P1, **unite},
            "P2": {**POINT_FOND_P0, **dict(zip(noms, P2_VALUES[grille]))},
            "P3": {**POINT_FOND_P0, **dict(zip(noms, P3_VALUES[grille]))},
        }
        sortie_points = {}
        for nom_point, point in points.items():
            out = ev.evaluate(point)
            sortie_points[nom_point] = {
                "logprior": out["logprior"],
                "chi2_BAO": out["chi2_BAO"],
                "chi2_CMB": out["chi2_CMB"],
                "chi2_total": out["chi2_total"],
                "contraintes": out["contraintes"],
            }
        # sondes hors support / invalides
        sondes = {
            "X_hors_support_haut": {**POINT_FOND_P0, **unite, noms[0]: 4.5},
            "X_hors_support_bas": {**POINT_FOND_P0, **unite, noms[0]: -2.5},
            "omch2_negatif": {"H0": 20.0, "ombh2": 0.09, "omm": 0.01, **unite},
            "fond_invalide": {**POINT_FOND_P0, **{nom: -2.0 for nom in noms}},
        }
        for nom_sonde, point in sondes.items():
            out = ev.evaluate(point)
            sortie_points[nom_sonde] = {
                "logprior": out["logprior"],
                "contraintes": out["contraintes"],
            }
        evaluations[variante] = sortie_points
        for nom_point in ("P0", "P1", "P2", "P3"):
            if sortie_points[nom_point]["logprior"] != 0.0:
                echecs.append(f"C3: logprior({nom_point}) != 0.0 pour {variante}")
        for nom_sonde in sondes:
            if sortie_points[nom_sonde]["logprior"] != -math.inf:
                echecs.append(f"C3: logprior({nom_sonde}) != -inf pour {variante}")

        # C4 — identité P0/P1 avec LambdaCDM aux seuils T8.
        idv = {}
        for nom_point, fond in (("P0", POINT_FOND_P0), ("P1", POINT_FOND_P1)):
            ref = CambReference.from_g1(
                h0=fond["H0"], ombh2=fond["ombh2"], omegam=fond["omm"]
            )
            ref_bao = reference_bao_vector(ref)
            ref_cmb = np.array(
                [ref.theta_star, ref.ombh2, ref.ombh2 + ref.omch2]
            )
            out = ev.evaluate({**fond, **unite})
            bao = np.asarray(out["vecteur_BAO"], dtype=float)
            cmb = np.asarray(out["vecteur_CMB"], dtype=float)
            r_ref_bao = ref_bao - bao_mean
            r_ref_cmb = ref_cmb - CMB_MU
            mesures = {
                "BAO_rel_max": float(np.max(np.abs(bao - ref_bao) / np.abs(ref_bao))),
                "theta_abs": float(abs(cmb[0] - ref_cmb[0])),
                "chi2_BAO_abs": float(
                    abs(out["chi2_BAO"] - float(r_ref_bao @ bao_icov @ r_ref_bao))
                ),
                "chi2_CMB_abs": float(
                    abs(out["chi2_CMB"] - float(r_ref_cmb @ CMB_ICOV @ r_ref_cmb))
                ),
            }
            idv[nom_point] = {
                "mesures": mesures,
                "T8_passe": bool(
                    mesures["BAO_rel_max"] <= T8["BAO_rel"]
                    and mesures["theta_abs"] <= T8["theta_abs"]
                    and mesures["chi2_BAO_abs"] <= T8["chi2_BAO_abs"]
                    and mesures["chi2_CMB_abs"] <= T8["chi2_CMB_abs"]
                ),
            }
        identites[variante] = idv
        for nom_point, item in idv.items():
            if not item["T8_passe"]:
                echecs.append(f"C4: identité T8 échouée ({variante}, {nom_point})")
    resultat["C3_points_fixes"] = evaluations
    resultat["C4_identite_T8"] = identites

    # C5 — ré-exécution complète de T8-T12 (suite I1-I9).
    proc = subprocess.run(
        [sys.executable, "scripts/test_xz_g2_1.py", "--full"],
        capture_output=True, text=True, check=True,
    )
    corps = proc.stdout[proc.stdout.index("```json") + 7 : proc.stdout.rindex("```")]
    i19 = json.loads(corps)
    ident = i19["camb_full"]["I1_CAMB_identity"]
    stab = i19["camb_full"]["I6_numerical_stability"]
    sens = i19["camb_full"]["I4_I5_acoustic_and_spline_sensitivity"]
    ind = i19["camb_full"]["I8_independent_path"]
    adv = i19["camb_full"]["I9_adversarial"]
    poly = i19["analytic"]["I2_interpolation"]["polynomials_abs_max"]
    borne = i19["analytic"]["I3_boundary"]
    mesures_t = {
        "T8_theta_abs": max(v["theta_corrected_abs"] for v in ident.values()),
        "T8_chi2_CMB_abs": max(v["chi2_CMB_corrected_abs"] for v in ident.values()),
        "T8_BAO_rel": max(v["BAO_corrected_rel_max"] for v in ident.values()),
        "T8_chi2_BAO_abs": max(v["chi2_BAO_corrected_abs"] for v in ident.values()),
        "T9_noeuds": max(
            v["node_abs_max"]
            for k, v in i19["analytic"]["I2_interpolation"].items()
            if k != "polynomials_abs_max"
        ),
        "T9_polynomes": max(
            v for k, v in poly.items()
            if "not-a-knot" in k or k.endswith(("constant", "linear"))
        ),
        "T10_continuation": max(
            v["constant_extension_abs_max"] for v in borne.values()
        ),
        "T11_BAO_default_tight": stab["BAO_default_vs_tight_rel_max"],
        "T11_rdrag_zmax": abs(stab["rdrag_zmax_1e7_minus_1e8"]),
        "T11_DM_zstar": max(
            v["DM_zstar_rel"] for v in stab["CMB_default_vs_tight"].values()
        ),
        "T11_theta": max(
            v["theta_corrected_abs"] for v in stab["CMB_default_vs_tight"].values()
        ),
        "T11_chi2_CMB_stress": max(
            v["chi2_CMB_corrected_abs"] for v in stab["CMB_default_vs_tight"].values()
        ),
        "T11_I8_X": max(
            v["X_scipy_vs_manuel_abs_max"]
            for k, v in ind.items() if k != "eds_calibration"
        ),
        "T11_I8_H": max(
            v["H_rel_max"] for k, v in ind.items() if k != "eds_calibration"
        ),
        "T11_I8_DM_bao": max(
            v["DM_bao_rel_max"] for k, v in ind.items() if k != "eds_calibration"
        ),
        "T11_I8_eds": max(ind["eds_calibration"].values()),
        "T12_chi2_BAO_corr_fixed": max(
            max(
                abs(v["natural_chi2_BAO_corrected_minus_fixed"]),
                abs(v["not-a-knot_chi2_BAO_corrected_minus_fixed"]),
            )
            for v in sens.values()
        ),
        "T12_rdrag_corr_fixed": max(
            max(
                abs(v["natural_rdrag_corrected_minus_fixed"]),
                abs(v["not-a-knot_rdrag_corrected_minus_fixed"]),
            )
            for v in sens.values()
        ),
        "I9_toutes_fautes_detectees": adv["toutes_fautes_detectees"],
    }
    seuils_ok = {
        "T8": bool(
            mesures_t["T8_theta_abs"] <= T8["theta_abs"]
            and mesures_t["T8_chi2_CMB_abs"] <= T8["chi2_CMB_abs"]
            and mesures_t["T8_BAO_rel"] <= T8["BAO_rel"]
            and mesures_t["T8_chi2_BAO_abs"] <= T8["chi2_BAO_abs"]
        ),
        "T9": bool(
            mesures_t["T9_noeuds"] <= T9_T12["T9_noeuds"]
            and mesures_t["T9_polynomes"] <= T9_T12["T9_polynomes"]
        ),
        "T10": bool(mesures_t["T10_continuation"] <= T9_T12["T10_continuation"]),
        "T11": bool(
            mesures_t["T11_BAO_default_tight"] <= T9_T12["T11_BAO_default_tight"]
            and mesures_t["T11_rdrag_zmax"] <= T9_T12["T11_rdrag_zmax"]
            and mesures_t["T11_DM_zstar"] <= T9_T12["T11_DM_zstar"]
            and mesures_t["T11_theta"] <= T9_T12["T11_theta"]
            and mesures_t["T11_chi2_CMB_stress"] <= T9_T12["T11_chi2_CMB_stress"]
            and mesures_t["T11_I8_X"] <= T9_T12["T11_I8_X"]
            and mesures_t["T11_I8_H"] <= T9_T12["T11_I8_H"]
            and mesures_t["T11_I8_DM_bao"] <= T9_T12["T11_I8_DM_bao"]
            and mesures_t["T11_I8_eds"] <= T9_T12["T11_I8_eds"]
            and mesures_t["I9_toutes_fautes_detectees"]
        ),
        "T12": bool(
            mesures_t["T12_chi2_BAO_corr_fixed"] <= T9_T12["T12_chi2_BAO_corr_fixed"]
            and mesures_t["T12_rdrag_corr_fixed"] <= T9_T12["T12_rdrag_corr_fixed"]
        ),
    }
    resultat["C5_T8_T12"] = {"mesures": mesures_t, "verdicts": seuils_ok}
    for nom_t, ok in seuils_ok.items():
        if not ok:
            echecs.append(f"C5: {nom_t} FAUX dans la ré-exécution I1-I9")
    if not mesures_t["I9_toutes_fautes_detectees"]:
        echecs.append("C5: fautes I9 non toutes détectées")

    # C6 — assemblage indépendant d'un vecteur BAO et du vecteur CMB
    # (sans bao_vector ni cmb_vector), à P0 et P2 sous M2a-N.
    cfg = configs["M2a-N"]
    ev = XZEvaluator(cfg, bao_mean, bao_icov)
    noms = [item["nom"] for item in cfg["parametres_x"]]
    controle_assemblage = {}
    for nom_point, xs in (
        ("P0", (1.0,) * 5),
        ("P2", P2_VALUES["M2a"]),
    ):
        point = {**POINT_FOND_P0, **dict(zip(noms, xs))}
        out = ev.evaluate(point)
        ref = CambReference.from_g1(
            h0=POINT_FOND_P0["H0"], ombh2=POINT_FOND_P0["ombh2"],
            omegam=POINT_FOND_P0["omm"],
        )
        profil = XZProfile("M2a", tuple(xs), "natural")
        fond = XZBackground(ref, profil)
        rd = fond.rdrag("corrected")
        assemblage = []
        for z, kind in zip(BAO_REDSHIFTS, BAO_KINDS):
            dm = float(fond.dm(float(z)))
            dh = float(fond.dh(float(z)))
            if kind == "DM_over_rs":
                assemblage.append(dm / rd)
            elif kind == "DH_over_rs":
                assemblage.append(dh / rd)
            else:
                assemblage.append((float(z) * dm * dm * dh) ** (1.0 / 3.0) / rd)
        cmb_assemblage = [
            fond.rstar("corrected") / float(fond.dm(ref.zstar)),
            ref.ombh2,
            ref.ombh2 + ref.omch2,
        ]
        bao_abs = float(
            np.max(np.abs(np.array(assemblage) - np.array(out["vecteur_BAO"])))
        )
        cmb_abs = float(
            np.max(np.abs(np.array(cmb_assemblage) - np.array(out["vecteur_CMB"])))
        )
        controle_assemblage[nom_point] = {
            "BAO_abs_max": bao_abs,
            "BAO_tolerance": TOL_C6_BAO_ABS,
            "CMB_abs_max": cmb_abs,
            "CMB_tolerance": TOL_C6_CMB_ABS,
            "dans_tolerances": bool(
                bao_abs <= TOL_C6_BAO_ABS and cmb_abs <= TOL_C6_CMB_ABS
            ),
        }
        if not controle_assemblage[nom_point]["dans_tolerances"]:
            echecs.append(f"C6: assemblage hors tolérances ({nom_point})")
    resultat["C6_assemblage_independant"] = controle_assemblage

    # C7 — fautes injectées.
    fautes = {}
    brut = dict(load_config(CONFIGS[0]))
    noeuds_permutes = list(brut["noeuds"])
    noeuds_permutes[1], noeuds_permutes[2] = noeuds_permutes[2], noeuds_permutes[1]
    brut_faute = {**brut, "noeuds": noeuds_permutes}
    try:
        validate_config(brut_faute)
        fautes["FQ1_noeuds_permutes"] = {"detectee": False}
    except ConfigError as exc:
        fautes["FQ1_noeuds_permutes"] = {
            "detectee": True,
            "garde": "validation stricte du schéma (C1/C2)",
            "message": str(exc),
        }
    # FQ2 : suppression de la division thetastar/100 dans le vecteur CMB.
    ref0 = CambReference.from_g1(
        h0=POINT_FOND_P0["H0"], ombh2=POINT_FOND_P0["ombh2"],
        omegam=POINT_FOND_P0["omm"],
    )
    fond0 = XZBackground(ref0, XZProfile.constant("M2a", 1.0, "natural"))
    cmb_faute = np.array(
        [fond0.theta_star("corrected") * 100.0, ref0.ombh2, ref0.ombh2 + ref0.omch2]
    )
    r_faute = cmb_faute - CMB_MU
    chi2_faute = float(r_faute @ CMB_ICOV @ r_faute)
    r_ok = fond0.cmb_vector("corrected") - CMB_MU
    chi2_ok = float(r_ok @ CMB_ICOV @ r_ok)
    fautes["FQ2_thetastar_sans_division"] = {
        "garde": "identité T8 sur chi2_CMB (seuil 1e-3)",
        "chi2_CMB_faute": chi2_faute,
        "chi2_CMB_correct": chi2_ok,
        "detectee": bool(abs(chi2_faute - chi2_ok) > T8["chi2_CMB_abs"]),
    }
    # FQ3 : continuation altérée — validate_config doit rejeter.
    brut_fq3 = copy.deepcopy(load_config(CONFIGS[0]))
    brut_fq3["continuation"] = "X(z >= 2.33) = extrapolation cubique"
    try:
        validate_config(brut_fq3)
        fautes["FQ3_continuation_alteree"] = {"detectee": False}
    except ConfigError as exc:
        fautes["FQ3_continuation_alteree"] = {
            "detectee": True,
            "garde": "validation stricte du contrat YAML",
            "message": str(exc),
        }
    # FQ4 : variable de sortie altérée — validate_config doit rejeter.
    brut_fq4 = copy.deepcopy(load_config(CONFIGS[0]))
    brut_fq4["sorties"]["variable_environnement"] = "TMPDIR"
    try:
        validate_config(brut_fq4)
        fautes["FQ4_variable_sortie_alteree"] = {"detectee": False}
    except ConfigError as exc:
        fautes["FQ4_variable_sortie_alteree"] = {
            "detectee": True,
            "garde": "validation stricte du contrat YAML",
            "message": str(exc),
        }
    resultat["C7_fautes_injectees"] = fautes
    for nom_faute, item in fautes.items():
        if not item["detectee"]:
            echecs.append(f"C7: {nom_faute} NON détectée")

    # C8 — refus de toute sortie sous un ancêtre Git (par exception).
    try:
        refuser_sortie_sous_git(".")
        racine_refusee = False
    except SortieSousGitError:
        racine_refusee = True
    try:
        refuser_sortie_sous_git(os.environ["C7C1_DATA_DIR"])
        externe_accepte = True
    except SortieSousGitError:
        externe_accepte = False
    resultat["C8_sorties_hors_git"] = {
        "racine_depot_refusee_par_exception": racine_refusee,
        "repertoire_externe_accepte": externe_accepte,
    }
    if not racine_refusee:
        echecs.append("C8: la racine du dépôt n'a pas levé SortieSousGitError")
    if not externe_accepte:
        echecs.append("C8: le répertoire externe a été refusé à tort")

    resultat["environnement"] = {
        "python": sys.version.split()[0],
        "camb": __import__("camb").__version__,
        "numpy": np.__version__,
        "scipy": __import__("scipy").__version__,
    }
    resultat["garde_inference"] = (
        "aucun mode MCMC/échantillonnage/minimisation/optimisation n'existe ; "
        "options interdites refusées à l'entrée"
    )

    # Auto-test du chemin d'échec (hors passes nominales) : un échec
    # synthétique doit produire un code de sortie non nul.
    if os.environ.get("C7C1_QUALIF_TEST_ECHEC"):
        echecs.append("TEST: échec synthétique injecté (C7C1_QUALIF_TEST_ECHEC)")

    resultat["porte"] = {"passe": not echecs, "echecs": sorted(echecs)}

    print("# Qualification G2.3a — sortie déterministe")
    print("```json")
    print(json.dumps(resultat, indent=2, sort_keys=True, ensure_ascii=False))
    print("```")
    if echecs:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
