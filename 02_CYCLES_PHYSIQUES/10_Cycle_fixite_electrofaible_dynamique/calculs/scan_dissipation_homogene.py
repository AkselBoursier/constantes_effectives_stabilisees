"""Scan analytique du toy model homogène dissipatif.

Le script suit un condensat quadratique moyen et un bain relativiste dans une
approximation de domination radiative. Il compare quatre prescriptions pour
Gamma_phi et recherche le plus petit taux satisfaisant des filtres explicites.

Ce calcul ne dérive aucun taux microscopique. Il cartographie le besoin
phénoménologique avant une étude de désintégration ou de thermalisation.
"""
from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np


V0_GEV = 246.22
MH_GEV = 125.25
LAMBDA_H = MH_GEV**2 / (2.0 * V0_GEV**2)
T_EW_GEV = 160.0
T_BBN_GEV = 1.0e-3
T_EQ_GEV = 0.8e-9
GSTAR_EW = 106.75
RHO_RAD_EW = math.pi**2 * GSTAR_EW * T_EW_GEV**4 / 30.0
Q_SIGNIFICANT = 1.0 - 0.99**2

N_MAX = math.log(T_EW_GEV / T_EQ_GEV) + 2.0
N_GRID = np.linspace(0.0, N_MAX, 12_001)
EXP_N = np.exp(N_GRID)


@dataclass(frozen=True)
class Metrics:
    prescription: str
    q_i: float
    gamma_ew: float
    delta_v_i: float
    r_i: float
    max_r_phi_over_r: float
    r_phi_over_r_bbn: float
    r_phi_over_r_eq: float
    delta_v_bbn: float
    entropy_gain_bbn: float
    acceptable: bool


def cumulative_trapezoid(values: np.ndarray, x: np.ndarray) -> np.ndarray:
    """Cumulative trapezoidal integral with a zero at the first point."""
    dx = np.diff(x)
    increments = 0.5 * (values[1:] + values[:-1]) * dx
    return np.concatenate(([0.0], np.cumsum(increments)))


def initial_radiation_ratio(q_i: float) -> float:
    """Initial scalar excess energy divided by radiation at T_EW."""
    delta_v = 0.25 * LAMBDA_H * V0_GEV**4 * (2.0 * q_i - q_i**2)
    return delta_v / RHO_RAD_EW


def scalar_comoving_suppression(
    prescription: str,
    gamma_ew: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray | None]:
    """Return s=P/P_i, Gamma/H and optional analytic U-1 coefficient.

    The third return value is U itself when an analytic expression is used.
    Otherwise it is None and U is obtained by quadrature.
    """
    if prescription == "constant_width":
        integrated_rate = 0.5 * gamma_ew * np.expm1(2.0 * N_GRID)
        s = np.exp(-np.minimum(integrated_rate, 745.0))
        gamma_over_h = np.minimum(gamma_ew * np.exp(2.0 * N_GRID), 1.0e300)
        return s, gamma_over_h, None

    if prescription == "thermal":
        integrated_rate = gamma_ew * np.expm1(N_GRID)
        s = np.exp(-np.minimum(integrated_rate, 745.0))
        gamma_over_h = np.minimum(gamma_ew * EXP_N, 1.0e300)
        return s, gamma_over_h, None

    if prescription == "constant_ratio":
        s = np.exp(-np.minimum(gamma_ew * N_GRID, 745.0))
        gamma_over_h = np.full_like(N_GRID, gamma_ew)
        return s, gamma_over_h, None

    if prescription == "phi2":
        # Gamma proportional to phi^2. The rate self-extinguishes as the
        # condensate decreases. The solution follows from
        # ds/dN = -gamma_EW exp(-N) s^2.
        denominator = 1.0 + gamma_ew * (1.0 - np.exp(-N_GRID))
        s = 1.0 / denominator
        gamma_over_h = gamma_ew * s * np.exp(-N_GRID)
        return s, gamma_over_h, None

    raise ValueError(f"Unknown prescription: {prescription}")


def radiation_comoving_energy(
    prescription: str,
    gamma_ew: float,
    r_i: float,
    s: np.ndarray,
    gamma_over_h: np.ndarray,
) -> np.ndarray:
    """Compute U=rho_r a^4/rho_r,EW with explicit energy transfer."""
    if prescription == "constant_ratio":
        if abs(gamma_ew - 1.0) < 1.0e-10:
            return 1.0 + r_i * N_GRID
        exponent = (1.0 - gamma_ew) * N_GRID
        return 1.0 + gamma_ew * r_i * np.expm1(exponent) / (1.0 - gamma_ew)

    if prescription == "phi2":
        # Exact integral of dU/dN = gamma P exp(N).
        a = 1.0 + gamma_ew
        u = a * EXP_N - gamma_ew
        return 1.0 + (gamma_ew * r_i / a**2) * (
            np.log(u) - gamma_ew / u + gamma_ew
        )

    p = r_i * s
    source = np.nan_to_num(
        gamma_over_h * p * EXP_N,
        nan=0.0,
        posinf=0.0,
        neginf=0.0,
    )
    return 1.0 + cumulative_trapezoid(source, N_GRID)


def first_index_below(values: np.ndarray, threshold: float) -> int:
    indices = np.flatnonzero(values <= threshold)
    return int(indices[0]) if len(indices) else len(values) - 1


def evaluate(prescription: str, q_i: float, gamma_ew: float) -> Metrics:
    if not 0.0 < q_i < 1.0:
        raise ValueError("q_i must lie in the broken branch 0<q_i<1")
    if gamma_ew <= 0.0:
        raise ValueError("gamma_ew must be positive")

    r_i = initial_radiation_ratio(q_i)
    s, gamma_over_h, _ = scalar_comoving_suppression(prescription, gamma_ew)
    p = r_i * s
    u = radiation_comoving_energy(prescription, gamma_ew, r_i, s, gamma_over_h)

    ratio = p * EXP_N / u
    q_envelope = q_i * s * np.exp(-3.0 * N_GRID)
    delta_v = 1.0 - np.sqrt(np.maximum(1.0 - q_envelope, 0.0))
    temperature = T_EW_GEV * np.exp(-N_GRID) * u**0.25

    i_bbn = first_index_below(temperature, T_BBN_GEV)
    i_eq = first_index_below(temperature, T_EQ_GEV)
    entropy_gain_bbn = u[i_bbn] ** 0.75 - 1.0
    delta_v_i = 1.0 - math.sqrt(1.0 - q_i)

    acceptable = bool(
        delta_v_i >= 0.01
        and np.max(ratio[: i_eq + 1]) < 0.1
        and ratio[i_bbn] < 0.01
        and ratio[i_eq] < 0.01
        and delta_v[i_bbn] < 0.01
        and entropy_gain_bbn < 0.1
    )

    return Metrics(
        prescription=prescription,
        q_i=q_i,
        gamma_ew=gamma_ew,
        delta_v_i=delta_v_i,
        r_i=r_i,
        max_r_phi_over_r=float(np.max(ratio[: i_eq + 1])),
        r_phi_over_r_bbn=float(ratio[i_bbn]),
        r_phi_over_r_eq=float(ratio[i_eq]),
        delta_v_bbn=float(delta_v[i_bbn]),
        entropy_gain_bbn=float(entropy_gain_bbn),
        acceptable=acceptable,
    )


def gamma_grid(prescription: str) -> np.ndarray:
    if prescription == "constant_width":
        return np.logspace(-10.0, 0.0, 500)
    if prescription == "thermal":
        return np.logspace(-8.0, 0.0, 500)
    if prescription == "constant_ratio":
        return np.logspace(-2.0, 1.0, 500)
    if prescription == "phi2":
        return np.logspace(4.0, 14.0, 500)
    raise ValueError(prescription)


def minimum_acceptable_gamma(prescription: str, q_i: float) -> Metrics | None:
    for gamma_ew in gamma_grid(prescription):
        metrics = evaluate(prescription, q_i, float(gamma_ew))
        if metrics.acceptable:
            return metrics
    return None


def representative_rows() -> Iterable[Metrics]:
    q_values = [Q_SIGNIFICANT, 0.1, 0.5, 0.9]
    prescriptions = ["constant_width", "thermal", "constant_ratio", "phi2"]
    for prescription in prescriptions:
        for q_i in q_values:
            metrics = minimum_acceptable_gamma(prescription, q_i)
            if metrics is not None:
                yield metrics


def write_summary(rows: Iterable[Metrics], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(Metrics.__dataclass_fields__.keys())
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row.__dict__)


if __name__ == "__main__":
    result_rows = list(representative_rows())
    target = Path(__file__).with_name("resultats_scan_dissipation_homogene_resume.csv")
    write_summary(result_rows, target)
    for row in result_rows:
        print(
            row.prescription,
            f"q={row.q_i:.6g}",
            f"gamma_EW={row.gamma_ew:.6g}",
            f"max_ratio={row.max_r_phi_over_r:.6g}",
            f"DeltaS/S={row.entropy_gain_bbn:.6g}",
        )
