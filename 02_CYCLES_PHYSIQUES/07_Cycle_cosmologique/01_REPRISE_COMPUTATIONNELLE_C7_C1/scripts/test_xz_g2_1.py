"""Tests I1–I7 de la porte G2.1 — instrument numérique X(z).

Aucun MCMC, aucune minimisation, aucun posterior et aucun choix de prior ne
sont réalisés.

Usage depuis la racine C7-C1 :

    python scripts/test_xz_g2_1.py --analytic-only
    python scripts/test_xz_g2_1.py --full

Le mode complet exige CAMB 1.5.4 et ``C7C1_DATA_DIR`` pointant vers les
13 composantes BAO officielles hors Git.
"""

from __future__ import annotations

import argparse
import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
from scipy.integrate import cumulative_trapezoid

from xz_background_g2_1 import (
    C_KM_S,
    NODES,
    CambReference,
    InvalidBackgroundError,
    XZBackground,
    XZProfile,
)

CMB_MU = np.array([0.01041, 0.02223, 0.14208])
CMB_COV = 1e-9 * np.array(
    [
        [0.006621, 0.12444, -1.1929],
        [0.12444, 21.344, -94.001],
        [-1.1929, -94.001, 1488.4],
    ]
)
CMB_ICOV = np.linalg.inv(CMB_COV)
BAO_REDSHIFTS = np.array(
    [0.295, 0.510, 0.510, 0.706, 0.706, 0.934, 0.934,
     1.321, 1.321, 1.484, 1.484, 2.330, 2.330]
)
BAO_KINDS = (
    "DV_over_rs", "DM_over_rs", "DH_over_rs", "DM_over_rs",
    "DH_over_rs", "DM_over_rs", "DH_over_rs", "DM_over_rs",
    "DH_over_rs", "DM_over_rs", "DH_over_rs", "DH_over_rs",
    "DM_over_rs",
)
REFERENCE_POINTS = {
    "g1_reference": dict(h0=67.36, ombh2=0.02237, omegam=0.3152),
    "g1_lcdm_map": dict(h0=68.3526, ombh2=0.022410, omegam=0.300539),
}


def rel_error(value: Any, reference: Any, floor: float = 1e-300) -> np.ndarray:
    value_arr = np.asarray(value, dtype=float)
    ref_arr = np.asarray(reference, dtype=float)
    return np.abs(value_arr - ref_arr) / np.maximum(np.abs(ref_arr), floor)


def chi2(vector: np.ndarray, mean: np.ndarray, icov: np.ndarray) -> float:
    residual = np.asarray(vector, dtype=float) - np.asarray(mean, dtype=float)
    return float(residual @ icov @ residual)


def load_bao_data() -> tuple[np.ndarray, np.ndarray]:
    root = os.environ.get("C7C1_DATA_DIR")
    if not root:
        raise RuntimeError("C7C1_DATA_DIR absent : octets BAO indisponibles.")
    base = Path(root) / "desi_bao_dr2"
    rows: list[tuple[float, float, str]] = []
    with (base / "desi_gaussian_bao_ALL_GCcomb_mean.txt").open(encoding="utf-8") as handle:
        for raw in handle:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            z, value, kind = line.split()
            rows.append((float(z), float(value), kind))
    if len(rows) != 13:
        raise RuntimeError(f"13 mesures BAO attendues, {len(rows)} lues.")
    z = np.array([r[0] for r in rows])
    kinds = tuple(r[2] for r in rows)
    if not np.array_equal(z, BAO_REDSHIFTS) or kinds != BAO_KINDS:
        raise RuntimeError("Ordre BAO différent du verrou G1.")
    cov = np.loadtxt(base / "desi_gaussian_bao_ALL_GCcomb_cov.txt")
    if cov.shape != (13, 13):
        raise RuntimeError(f"Covariance BAO non 13x13 : {cov.shape}")
    return np.array([r[1] for r in rows]), np.linalg.inv(cov)


@dataclass
class AnalyticReference:
    h0: float = 70.0
    omega_x0: float = 0.7
    ombh2: float = 0.022
    omch2: float = 0.12
    zstar: float = 1089.0
    zdrag: float = 1059.0
    rstar: float = 144.0
    rdrag: float = 147.0
    theta_star: float = 0.0104
    baryon_photon_ratio0: float = 900.0

    def hubble(self, z: float | np.ndarray) -> float | np.ndarray:
        arr = np.asarray(z, dtype=float)
        out = self.h0 * np.sqrt((1.0 - self.omega_x0) * (1.0 + arr) ** 3 + self.omega_x0)
        return float(out) if arr.ndim == 0 else out

    def comoving_distance(self, z: float | np.ndarray) -> float | np.ndarray:
        arr = np.asarray(z, dtype=float)
        values = []
        for zz in arr.reshape(-1):
            grid = np.linspace(0.0, float(zz), 20001)
            values.append(float(np.trapezoid(C_KM_S / self.hubble(grid), grid)))
        out = np.asarray(values).reshape(arr.shape)
        return float(out) if arr.ndim == 0 else out


def analytic_tests() -> dict[str, Any]:
    metrics: dict[str, Any] = {}
    dense = np.linspace(0.0, 2.33, 5001)

    interpolation: dict[str, Any] = {}
    for variant, nodes in NODES.items():
        for convention in ("natural", "not-a-knot"):
            free = tuple(0.85 + 0.12 * np.arange(1, len(nodes)))
            profile = XZProfile(variant, free, convention)
            node_error = float(np.max(np.abs(profile(nodes) - profile.values)))
            interpolation[f"{variant}_{convention}"] = {"node_abs_max": node_error}
            if node_error > 5e-13:
                raise AssertionError(f"Valeurs nodales manquées : {variant}/{convention}")

    polynomials = {
        "constant": lambda z: np.ones_like(z),
        "linear": lambda z: 1.0 - 0.2 * z,
        "quadratic": lambda z: 1.0 - 0.2 * z + 0.04 * z**2,
        "cubic": lambda z: 1.0 - 0.2 * z + 0.04 * z**2 - 0.005 * z**3,
    }
    poly_metrics: dict[str, float] = {}
    for variant, nodes in NODES.items():
        for name, func in polynomials.items():
            values = func(nodes)
            for convention in ("natural", "not-a-knot"):
                profile = XZProfile(variant, tuple(values[1:]), convention)
                error = float(np.max(np.abs(profile(dense) - func(dense))))
                poly_metrics[f"{variant}_{convention}_{name}"] = error
                exact = convention == "not-a-knot" or name in ("constant", "linear")
                if exact and error > 2e-11:
                    raise AssertionError(
                        f"Polynôme attendu exact : {variant}/{convention}/{name} = {error}"
                    )
    interpolation["polynomials_abs_max"] = poly_metrics
    metrics["I2_interpolation"] = interpolation

    boundary: dict[str, Any] = {}
    for convention in ("natural", "not-a-knot"):
        profile = XZProfile("M2a", (0.8, 1.2, 0.4, 1.5, -0.3), convention)
        zs = np.array([2.33, 2.3300001, 3.0, 10.0])
        error = float(np.max(np.abs(profile(zs) - profile.last_value)))
        boundary[convention] = {
            "constant_extension_abs_max": error,
            "left_derivative_at_2p33": float(profile.derivative(2.33, 1)),
            "right_derivative_defined": 0.0,
        }
        if error > 1e-14:
            raise AssertionError("Continuation haute non constante.")
    metrics["I3_boundary"] = boundary

    ref = AnalyticReference()
    signed = XZProfile("M2a", (0.5, -0.2, 0.3, 1.1, 0.6), "not-a-knot")
    signed_bg = XZBackground(ref, signed)
    grid = np.linspace(0.0, 2.33, 2001)
    h2_signed = np.asarray(signed_bg.h2(grid))
    if not np.all(np.isfinite(h2_signed)) or not np.all(h2_signed > 0.0):
        raise AssertionError("Le profil signé de contrôle devait rester valide.")

    invalid = XZProfile("M2a", (-20.0,) * 5, "not-a-knot")
    invalid_rejected = False
    try:
        XZBackground(ref, invalid).h2(grid)
    except InvalidBackgroundError:
        invalid_rejected = True
    if not invalid_rejected:
        raise AssertionError("Un fond H_X^2 <= 0 n'a pas été rejeté.")
    metrics["I4_signed_domain"] = {
        "signed_profile_min_X": float(np.min(signed(grid))),
        "signed_profile_min_H2": float(np.min(h2_signed)),
        "invalid_profile_rejected": invalid_rejected,
    }

    identity = XZProfile.constant("M2a", 1.0, "not-a-knot")
    default = XZBackground(ref, identity, epsabs=1e-8, epsrel=1e-10)
    tight = XZBackground(ref, identity, epsabs=1e-10, epsrel=1e-12, quad_limit=500)
    zcheck = np.array([0.295, 0.510, 0.934, 1.484, 2.33])
    dm_default = np.asarray(default.dm(zcheck))
    dm_tight = np.asarray(tight.dm(zcheck))
    fine = np.linspace(0.0, 2.33, 100001)
    dm_trap = cumulative_trapezoid(C_KM_S / default.hubble(fine), fine, initial=0.0)
    metrics["I1_I6_analytic_identity_stability"] = {
        "H_rel_max": float(np.max(rel_error(default.hubble(zcheck), ref.hubble(zcheck)))),
        "DM_default_vs_tight_rel_max": float(np.max(rel_error(dm_default, dm_tight))),
        "DM_quad_vs_trapezoid_rel_max": float(
            np.max(rel_error(dm_default, np.interp(zcheck, fine, dm_trap)))
        ),
    }

    values = (0.6, -0.15, 0.55, 1.35, 0.75)
    p_nat = XZProfile("M2a", values, "natural")
    p_nak = XZProfile("M2a", values, "not-a-knot")
    b_nat = XZBackground(ref, p_nat)
    b_nak = XZBackground(ref, p_nak)
    metrics["I5_spline_sensitivity_analytic"] = {
        "X_abs_max": float(np.max(np.abs(p_nat(dense) - p_nak(dense)))),
        "H_rel_max": float(np.max(rel_error(b_nat.hubble(zcheck), b_nak.hubble(zcheck)))),
        "DM_rel_max": float(np.max(rel_error(b_nat.dm(zcheck), b_nak.dm(zcheck)))),
    }
    return metrics


def reference_bao_vector(ref: CambReference) -> np.ndarray:
    dm = np.asarray(ref.comoving_distance(BAO_REDSHIFTS), dtype=float)
    dh = C_KM_S / np.asarray(ref.hubble(BAO_REDSHIFTS), dtype=float)
    dv = np.cbrt(BAO_REDSHIFTS * dm * dm * dh)
    out = np.empty(13)
    for i, kind in enumerate(BAO_KINDS):
        out[i] = {
            "DV_over_rs": dv[i] / ref.rdrag,
            "DM_over_rs": dm[i] / ref.rdrag,
            "DH_over_rs": dh[i] / ref.rdrag,
        }[kind]
    return out


def full_camb_tests() -> dict[str, Any]:
    bao_mean, bao_icov = load_bao_data()
    metrics: dict[str, Any] = {}
    identity_metrics: dict[str, Any] = {}

    for point_name, point in REFERENCE_POINTS.items():
        ref = CambReference.from_g1(**point)
        ref_bao = reference_bao_vector(ref)
        ref_bao_chi2 = chi2(ref_bao, bao_mean, bao_icov)
        ref_cmb = np.array([ref.theta_star, ref.ombh2, ref.ombh2 + ref.omch2])
        ref_cmb_chi2 = chi2(ref_cmb, CMB_MU, CMB_ICOV)
        for variant in ("M2a", "M2b"):
            for convention in ("natural", "not-a-knot"):
                bg = XZBackground(ref, XZProfile.constant(variant, 1.0, convention))
                bao_fixed = bg.bao_vector(BAO_REDSHIFTS, BAO_KINDS, "fixed")
                bao_corrected = bg.bao_vector(BAO_REDSHIFTS, BAO_KINDS, "corrected")
                cmb_fixed = bg.cmb_vector("fixed")
                cmb_corrected = bg.cmb_vector("corrected")
                identity_metrics[f"{point_name}_{variant}_{convention}"] = {
                    "H_rel_max": float(np.max(rel_error(bg.hubble(BAO_REDSHIFTS), ref.hubble(BAO_REDSHIFTS)))),
                    "DM_rel_max": float(np.max(rel_error(bg.dm(BAO_REDSHIFTS), ref.comoving_distance(BAO_REDSHIFTS)))),
                    "rdrag_fixed_abs": abs(bg.rdrag("fixed") - ref.rdrag),
                    "rdrag_corrected_abs": abs(bg.rdrag("corrected") - ref.rdrag),
                    "rstar_fixed_abs": abs(bg.rstar("fixed") - ref.rstar),
                    "rstar_corrected_abs": abs(bg.rstar("corrected") - ref.rstar),
                    "theta_fixed_abs": abs(bg.theta_star("fixed") - ref.theta_star),
                    "theta_corrected_abs": abs(bg.theta_star("corrected") - ref.theta_star),
                    "BAO_fixed_rel_max": float(np.max(rel_error(bao_fixed, ref_bao))),
                    "BAO_corrected_rel_max": float(np.max(rel_error(bao_corrected, ref_bao))),
                    "chi2_BAO_fixed_abs": abs(chi2(bao_fixed, bao_mean, bao_icov) - ref_bao_chi2),
                    "chi2_BAO_corrected_abs": abs(chi2(bao_corrected, bao_mean, bao_icov) - ref_bao_chi2),
                    "CMB_fixed_abs_max": float(np.max(np.abs(cmb_fixed - ref_cmb))),
                    "CMB_corrected_abs_max": float(np.max(np.abs(cmb_corrected - ref_cmb))),
                    "chi2_CMB_fixed_abs": abs(chi2(cmb_fixed, CMB_MU, CMB_ICOV) - ref_cmb_chi2),
                    "chi2_CMB_corrected_abs": abs(chi2(cmb_corrected, CMB_MU, CMB_ICOV) - ref_cmb_chi2),
                }
    metrics["I1_CAMB_identity"] = identity_metrics

    ref = CambReference.from_g1(**REFERENCE_POINTS["g1_lcdm_map"])
    profiles = {
        "positive_gentle": (0.9, 0.8, 0.9, 1.1, 1.0),
        "signed_crossing": (0.6, -0.2, 0.4, 1.2, 0.8),
        "oscillatory": (1.4, 0.2, 1.6, 0.1, 1.3),
    }
    sensitivity: dict[str, Any] = {}
    for name, values in profiles.items():
        p_nat = XZProfile("M2a", values, "natural")
        p_nak = XZProfile("M2a", values, "not-a-knot")
        b_nat = XZBackground(ref, p_nat)
        b_nak = XZBackground(ref, p_nak)
        bao_nat = b_nat.bao_vector(BAO_REDSHIFTS, BAO_KINDS, "fixed")
        bao_nak = b_nak.bao_vector(BAO_REDSHIFTS, BAO_KINDS, "fixed")
        dense = np.linspace(0.0, 2.33, 10001)
        item: dict[str, Any] = {
            "X_nat_min": float(np.min(p_nat(dense))),
            "X_nak_min": float(np.min(p_nak(dense))),
            "X_nat_nak_abs_max": float(np.max(np.abs(p_nat(dense) - p_nak(dense)))),
            "BAO_nat_nak_rel_max": float(np.max(rel_error(bao_nat, bao_nak))),
            "chi2_BAO_nat_minus_nak": chi2(bao_nat, bao_mean, bao_icov) - chi2(bao_nak, bao_mean, bao_icov),
        }
        for convention, bg in (("natural", b_nat), ("not-a-knot", b_nak)):
            fixed = bg.bao_vector(BAO_REDSHIFTS, BAO_KINDS, "fixed")
            corrected = bg.bao_vector(BAO_REDSHIFTS, BAO_KINDS, "corrected")
            item[f"{convention}_rdrag_corrected_minus_fixed"] = bg.rdrag("corrected") - bg.rdrag("fixed")
            item[f"{convention}_rstar_corrected_minus_fixed"] = bg.rstar("corrected") - bg.rstar("fixed")
            item[f"{convention}_theta_corrected_minus_fixed"] = bg.theta_star("corrected") - bg.theta_star("fixed")
            item[f"{convention}_BAO_corrected_vs_fixed_rel_max"] = float(np.max(rel_error(corrected, fixed)))
            item[f"{convention}_chi2_BAO_corrected_minus_fixed"] = chi2(corrected, bao_mean, bao_icov) - chi2(fixed, bao_mean, bao_icov)
        sensitivity[name] = item
    metrics["I4_I5_acoustic_and_spline_sensitivity"] = sensitivity

    profile = XZProfile("M2a", profiles["signed_crossing"], "not-a-knot")
    default = XZBackground(ref, profile, epsabs=1e-8, epsrel=1e-10, acoustic_zmax=1e7)
    tight = XZBackground(ref, profile, epsabs=1e-10, epsrel=1e-12, quad_limit=500, acoustic_zmax=1e8)
    low_tail = XZBackground(ref, profile, acoustic_zmax=1e6)
    z = np.unique(BAO_REDSHIFTS)
    metrics["I6_numerical_stability"] = {
        "H_default_vs_tight_rel_max": float(np.max(rel_error(default.hubble(z), tight.hubble(z)))),
        "DM_default_vs_tight_rel_max": float(np.max(rel_error(default.dm(z), tight.dm(z)))),
        "BAO_default_vs_tight_rel_max": float(np.max(rel_error(
            default.bao_vector(BAO_REDSHIFTS, BAO_KINDS, "corrected"),
            tight.bao_vector(BAO_REDSHIFTS, BAO_KINDS, "corrected"),
        ))),
        "rdrag_zmax_1e6_minus_1e7": low_tail.rdrag("corrected") - default.rdrag("corrected"),
        "rdrag_zmax_1e7_minus_1e8": default.rdrag("corrected") - tight.rdrag("corrected"),
        "rstar_zmax_1e6_minus_1e7": low_tail.rstar("corrected") - default.rstar("corrected"),
        "rstar_zmax_1e7_minus_1e8": default.rstar("corrected") - tight.rstar("corrected"),
    }
    return metrics


def main() -> None:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--analytic-only", action="store_true")
    mode.add_argument("--full", action="store_true")
    args = parser.parse_args()

    metrics: dict[str, Any] = {"analytic": analytic_tests()}
    if args.full:
        metrics["camb_full"] = full_camb_tests()
    print("# Sortie brute G2.1 — mesures I1–I7\n")
    print("Cette sortie ne constitue ni un posterior ni une préférence de modèle.\n")
    print("```json")
    print(json.dumps(metrics, indent=2, sort_keys=True, ensure_ascii=False))
    print("```")


if __name__ == "__main__":
    main()
