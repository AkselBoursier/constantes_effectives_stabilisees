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


# ---------------------------------------------------------------------------
# Voie indépendante I8 (règle épistémique R1/R2/R3) : aucun appel aux méthodes
# de XZBackground ni à scipy.interpolate ; seules dépendances partagées avec le
# calcul principal : les valeurs nodales du profil et l'objet H_ref (déclarées).
# ---------------------------------------------------------------------------

def manual_spline(nodes, values, convention, constant_tail=True):
    """Spline cubique par résolution directe du système des moments
    (numpy.linalg.solve). Chemin algébrique distinct de scipy CubicSpline.
    `constant_tail=False` sert uniquement au test adversarial « raccord
    supprimé » (extrapolation cubique du dernier segment)."""
    x = np.asarray(nodes, dtype=float)
    y = np.asarray(values, dtype=float)
    n = len(x) - 1
    h = np.diff(x)
    A = np.zeros((n + 1, n + 1))
    b = np.zeros(n + 1)
    for i in range(1, n):
        A[i, i - 1] = h[i - 1] / 6.0
        A[i, i] = (h[i - 1] + h[i]) / 3.0
        A[i, i + 1] = h[i] / 6.0
        b[i] = (y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1]
    if convention == "natural":
        A[0, 0] = 1.0
        A[n, n] = 1.0
    elif convention == "not-a-knot":
        A[0, 0] = h[1]
        A[0, 1] = -(h[0] + h[1])
        A[0, 2] = h[0]
        A[n, n - 2] = h[n - 1]
        A[n, n - 1] = -(h[n - 2] + h[n - 1])
        A[n, n] = h[n - 2]
    else:
        raise ValueError(f"convention inconnue : {convention}")
    moments = np.linalg.solve(A, b)

    def evaluate(z):
        arr = np.asarray(z, dtype=float).reshape(-1)
        out = np.empty_like(arr)
        for k, zz in enumerate(arr):
            if constant_tail and zz >= x[-1]:
                out[k] = y[-1]
                continue
            i = int(np.searchsorted(x, min(zz, x[-1]), side="right") - 1)
            i = max(0, min(i, n - 1))
            hi = h[i]
            out[k] = (
                moments[i] * (x[i + 1] - zz) ** 3 / (6.0 * hi)
                + moments[i + 1] * (zz - x[i]) ** 3 / (6.0 * hi)
                + (y[i] - moments[i] * hi**2 / 6.0) * (x[i + 1] - zz) / hi
                + (y[i + 1] - moments[i + 1] * hi**2 / 6.0) * (zz - x[i]) / hi
            )
        return out

    return evaluate


def simpson_fixed(f, lo, hi, n=20000):
    if n % 2:
        n += 1
    grid = np.linspace(lo, hi, n + 1)
    vals = np.asarray(f(grid), dtype=float)
    step = (hi - lo) / n
    return float(
        step / 3.0 * (vals[0] + vals[-1] + 4.0 * vals[1:-1:2].sum() + 2.0 * vals[2:-2:2].sum())
    )


def dm_independent(h_of_z, z_end, n=20000):
    """D_M par Simpson composite en variable u = sqrt(a), a = 1/(1+z),
    avec césure explicite à z = 2.33 : variable, intégrateur et
    discrétisation tous distincts de XZBackground._dm_scalar (quad en z)."""

    def integrand(u):
        u = np.asarray(u, dtype=float)
        zz = 1.0 / (u * u) - 1.0
        return 2.0 * C_KM_S / (u**3 * np.asarray(h_of_z(zz), dtype=float))

    u_end = 1.0 / np.sqrt(1.0 + z_end)
    u_cut = 1.0 / np.sqrt(1.0 + 2.33)
    if z_end > 2.33:
        return simpson_fixed(integrand, u_end, u_cut, n) + simpson_fixed(
            integrand, u_cut, 1.0, n
        )
    return simpson_fixed(integrand, u_end, 1.0, n)


def eds_calibration() -> dict[str, float]:
    """Étalonnage R3 de l'intégrateur indépendant sur une solution
    analytique exacte : Einstein-de Sitter, H = H0 (1+z)^{3/2},
    D_M = (2c/H0)(1 - 1/sqrt(1+z))."""
    h0 = 70.0

    def h_eds(z):
        return h0 * (1.0 + np.asarray(z, dtype=float)) ** 1.5

    out = {}
    for z_end in (2.33, 1089.0):
        exact = 2.0 * C_KM_S / h0 * (1.0 - 1.0 / np.sqrt(1.0 + z_end))
        num = dm_independent(h_eds, z_end)
        out[f"z{z_end}_rel"] = float(abs(num - exact) / exact)
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

    # Complément G2.1d : stabilité default/tight des grandeurs CMB pour des
    # profils X(z) non constants, sous les deux conventions de spline.
    cmb_stability: dict[str, Any] = {}
    for name in ("signed_crossing", "oscillatory"):
        for convention in ("natural", "not-a-knot"):
            prof = XZProfile("M2a", profiles[name], convention)
            d_bg = XZBackground(ref, prof)
            t_bg = XZBackground(
                ref, prof, epsabs=1e-10, epsrel=1e-12, quad_limit=500,
                acoustic_zmax=1e8,
            )
            dm_d = float(d_bg.dm(ref.zstar))
            dm_t = float(t_bg.dm(ref.zstar))
            entry: dict[str, Any] = {
                "DM_zstar_rel": float(rel_error(dm_d, dm_t)),
            }
            for mode in ("fixed", "corrected"):
                entry[f"theta_{mode}_abs"] = abs(
                    d_bg.theta_star(mode) - t_bg.theta_star(mode)
                )
                entry[f"chi2_CMB_{mode}_abs"] = abs(
                    chi2(d_bg.cmb_vector(mode), CMB_MU, CMB_ICOV)
                    - chi2(t_bg.cmb_vector(mode), CMB_MU, CMB_ICOV)
                )
            cmb_stability[f"{name}_{convention}"] = entry
    metrics["I6_numerical_stability"]["CMB_default_vs_tight"] = cmb_stability

    # -- I8 : voie indépendante (R3) -------------------------------------
    # Dépendances partagées avec le calcul principal, déclarées : valeurs
    # nodales du profil ; objet H_ref (CAMB) ; constantes physiques.
    probe = np.linspace(0.0, 3.0, 3001)
    h0sq_ox = ref.h0**2 * ref.omega_x0
    independent: dict[str, Any] = {"eds_calibration": eds_calibration()}
    for name in ("signed_crossing", "oscillatory"):
        for convention in ("natural", "not-a-knot"):
            values = profiles[name]
            node_values = np.concatenate(([1.0], np.asarray(values, float)))
            x_ind = manual_spline(NODES["M2a"], node_values, convention)
            p_main = XZProfile("M2a", values, convention)
            bg = XZBackground(ref, p_main)

            def h_ind(z, _x=x_ind):
                zz = np.asarray(z, dtype=float)
                href = np.asarray(ref.hubble(zz), dtype=float)
                return np.sqrt(href * href + h0sq_ox * (_x(zz) - 1.0))

            z_bao = np.unique(BAO_REDSHIFTS)
            dm_main = np.asarray(bg.dm(z_bao), dtype=float)
            dm_ind = np.array([dm_independent(h_ind, float(zz)) for zz in z_bao])
            dm_star_main = float(bg.dm(ref.zstar))
            dm_star_ind = dm_independent(h_ind, ref.zstar)
            dm_star_ind_2n = dm_independent(h_ind, ref.zstar, n=40000)
            theta_fixed_ind = ref.rstar / dm_star_ind
            cmb_ind = np.array([theta_fixed_ind, ref.ombh2, ref.ombh2 + ref.omch2])
            independent[f"{name}_{convention}"] = {
                "X_scipy_vs_manuel_abs_max": float(
                    np.max(np.abs(p_main(probe) - x_ind(probe)))
                ),
                "H_rel_max": float(np.max(rel_error(bg.hubble(probe), h_ind(probe)))),
                "DM_bao_rel_max": float(np.max(rel_error(dm_main, dm_ind))),
                "DM_zstar_rel": float(rel_error(dm_star_main, dm_star_ind)),
                "DM_zstar_richardson_rel": float(
                    rel_error(dm_star_ind, dm_star_ind_2n)
                ),
                "theta_fixed_abs": abs(bg.theta_star("fixed") - theta_fixed_ind),
                "chi2_CMB_fixed_abs": abs(
                    chi2(bg.cmb_vector("fixed"), CMB_MU, CMB_ICOV)
                    - chi2(cmb_ind, CMB_MU, CMB_ICOV)
                ),
            }
    metrics["I8_independent_path"] = independent

    # -- I9 : tests adversariaux (fautes injectées, garde désignée) ------
    # Une faute non détectée par sa garde invalide la garde, pas la faute.
    adv_values = profiles["signed_crossing"]
    adv_nodes = np.concatenate(([1.0], np.asarray(adv_values, float)))
    x_ok = manual_spline(NODES["M2a"], adv_nodes, "natural")
    p_ok = XZProfile("M2a", adv_values, "natural")
    bg_ok = XZBackground(ref, p_ok)

    def h_ok(z):
        zz = np.asarray(z, dtype=float)
        href = np.asarray(ref.hubble(zz), dtype=float)
        return np.sqrt(href * href + h0sq_ox * (x_ok(zz) - 1.0))

    adversarial: dict[str, Any] = {}
    z_grid = np.linspace(0.05, 2.9, 500)

    # F1 — signe inversé dans la correction de H² ; garde : I8-H.
    href_g = np.asarray(ref.hubble(z_grid), dtype=float)
    h_f1 = np.sqrt(np.maximum(href_g**2 - h0sq_ox * (x_ok(z_grid) - 1.0), 1.0))
    dev_f1 = float(np.max(rel_error(h_f1, h_ok(z_grid))))
    wit_f1 = float(np.max(rel_error(bg_ok.hubble(z_grid), h_ok(z_grid))))
    adversarial["F1_signe_H2"] = {
        "garde": "I8_H_rel_max",
        "deviation_faute": dev_f1,
        "temoin_correct": wit_f1,
        "detecte": bool(dev_f1 > 1e-6 and dev_f1 > 1e3 * max(wit_f1, 1e-300)),
        "aveuglement_documente": "l'identité I1 (X=1) est aveugle à cette "
        "faute : la correction s'annule quel que soit son signe.",
    }

    # F2 — facteur de changement de variable omis dans D_M ; garde : I8-DM.
    def dm_f2(z_end):
        u_end = 1.0 / np.sqrt(1.0 + z_end)

        def bad(u):
            u = np.asarray(u, dtype=float)
            zz = 1.0 / (u * u) - 1.0
            return 2.0 * C_KM_S / np.asarray(h_ok(zz), dtype=float)

        return simpson_fixed(bad, u_end, 1.0, 20000)

    dev_f2 = float(rel_error(dm_f2(2.33), dm_independent(h_ok, 2.33)))
    wit_f2 = float(rel_error(float(bg_ok.dm(2.33)), dm_independent(h_ok, 2.33)))
    adversarial["F2_facteur_variable_DM"] = {
        "garde": "I8_DM_bao_rel_max",
        "deviation_faute": dev_f2,
        "temoin_correct": wit_f2,
        "detecte": bool(dev_f2 > 1e-6 and dev_f2 > 1e3 * max(wit_f2, 1e-300)),
    }

    # F3 — nœud déplacé (1/3 -> 0.35) ; garde : I8-X sur points sondes.
    nodes_moved = NODES["M2a"].copy()
    nodes_moved[1] = 0.35
    x_f3 = manual_spline(nodes_moved, adv_nodes, "natural")
    dev_f3 = float(np.max(np.abs(x_f3(probe) - x_ok(probe))))
    wit_f3 = float(np.max(np.abs(p_ok(probe) - x_ok(probe))))
    adversarial["F3_noeud_deplace"] = {
        "garde": "I8_X_scipy_vs_manuel_abs_max",
        "deviation_faute": dev_f3,
        "temoin_correct": wit_f3,
        "detecte": bool(dev_f3 > 1e-6 and dev_f3 > 1e3 * max(wit_f3, 1e-300)),
        "aveuglement_documente": "le test I2 évalué aux nœuds du profil "
        "fautif passerait : il ne garde pas la position des nœuds.",
    }

    # F4 — raccord constant supprimé après z=2.33 ; garde : contrôle I3.
    x_f4 = manual_spline(NODES["M2a"], adv_nodes, "natural", constant_tail=False)
    z_tail = np.linspace(2.33, 3.0, 200)
    dev_f4 = float(np.max(np.abs(x_f4(z_tail) - adv_nodes[-1])))
    wit_f4 = float(np.max(np.abs(x_ok(z_tail) - adv_nodes[-1])))
    adversarial["F4_raccord_supprime"] = {
        "garde": "I3_constant_extension_abs_max",
        "deviation_faute": dev_f4,
        "temoin_correct": wit_f4,
        "detecte": bool(dev_f4 > 1e-6 and wit_f4 == 0.0),
    }

    # F5 — mauvaise valeur de Omega_X,0 (x1.05) ; garde : I8-H.
    h_f5 = np.sqrt(href_g**2 + 1.05 * h0sq_ox * (x_ok(z_grid) - 1.0))
    dev_f5 = float(np.max(rel_error(h_f5, h_ok(z_grid))))
    adversarial["F5_omega_x0_faux"] = {
        "garde": "I8_H_rel_max",
        "deviation_faute": dev_f5,
        "temoin_correct": wit_f1,
        "detecte": bool(dev_f5 > 1e-6 and dev_f5 > 1e3 * max(wit_f1, 1e-300)),
        "aveuglement_documente": "l'identité I1 (X=1) est aveugle à cette "
        "faute : Omega_X,0 multiplie (X-1)=0.",
    }

    adversarial["toutes_fautes_detectees"] = bool(
        all(v["detecte"] for k, v in adversarial.items() if k.startswith("F"))
    )
    metrics["I9_adversarial"] = adversarial
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
