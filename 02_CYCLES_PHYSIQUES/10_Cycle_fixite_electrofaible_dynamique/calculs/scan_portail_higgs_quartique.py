"""Scan analytique exploratoire du régime quartique du portail scalaire-Higgs.

Le modèle suit un condensat phi dont l'auto-interaction quartique domine d'abord,
puis qui passe au régime quadratique induit par le Higgs. Le but est de tester
si la dilution de type rayonnement évite la surabondance trouvée dans le cas
quadratique minimal.

Ce script n'est pas un solveur de Boltzmann ni un ajustement cosmologique global.
"""

from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np


V0_GEV = 246.22
MH_GEV = 125.25
LAMBDA_H = MH_GEV**2 / (2.0 * V0_GEV**2)
MU_H2_GEV2 = LAMBDA_H * V0_GEV**2
MPL_REDUCED_GEV = 2.435e18
T_EW_GEV = 160.0
T_EQ_GEV = 0.8e-9
GSTAR_EW = 106.75
RHO_RAD_EW = math.pi**2 * GSTAR_EW * T_EW_GEV**4 / 30.0


@dataclass(frozen=True)
class Point:
    lambda_hphi: float
    lambda_phi: float
    q_i: float
    phi_i_over_mpl: float
    q_transition: float
    t_transition_gev: float
    r_ew: float
    r_eq: float
    significant: bool
    acceptable: bool


def evaluate(lambda_hphi: float, lambda_phi: float, q_i: float) -> Point:
    phi_i = math.sqrt(q_i * MU_H2_GEV2 / lambda_hphi)
    phi_i_over_mpl = phi_i / MPL_REDUCED_GEV

    # Transition quartique -> quadratique définie par
    # lambda_phi phi^2 ~ m_eff^2, avec m_eff^2 = lambda_hphi v^2.
    q_transition = lambda_hphi**2 / (lambda_phi * LAMBDA_H)
    quartic_initially = q_i > q_transition

    # Dans le régime quartique, phi ∝ a^-1 et q ∝ a^-2.
    if quartic_initially and q_transition > 0.0:
        t_transition_gev = T_EW_GEV * math.sqrt(q_transition / q_i)
    else:
        t_transition_gev = T_EW_GEV

    # Excès énergétique au crossover : auto-interaction quartique + déplacement
    # du minimum du Higgs. Approximation au niveau arbre.
    delta_v_higgs = 0.25 * LAMBDA_H * V0_GEV**4 * (2.0 * q_i - q_i**2)
    rho_quartic = 0.25 * lambda_phi * phi_i**4
    r_ew = (delta_v_higgs + rho_quartic) / RHO_RAD_EW

    # Tant que le régime quartique domine, rho_phi/rho_rad reste approximativement
    # constant. Après la transition quadratique, il croît comme a ∝ 1/T.
    if t_transition_gev <= T_EQ_GEV:
        r_eq = r_ew
    else:
        r_eq = r_ew * (t_transition_gev / T_EQ_GEV)

    delta_v_fraction = 1.0 - math.sqrt(1.0 - q_i)
    significant = delta_v_fraction > 0.01
    acceptable = (
        phi_i_over_mpl < 1.0
        and quartic_initially
        and r_ew < 1.0
        and r_eq < 1.0
        and significant
    )

    return Point(
        lambda_hphi=lambda_hphi,
        lambda_phi=lambda_phi,
        q_i=q_i,
        phi_i_over_mpl=phi_i_over_mpl,
        q_transition=q_transition,
        t_transition_gev=t_transition_gev,
        r_ew=r_ew,
        r_eq=r_eq,
        significant=significant,
        acceptable=acceptable,
    )


def run_scan() -> tuple[list[Point], dict[str, float]]:
    lambda_hphi_values = np.logspace(-40, -8, 97)
    lambda_phi_values = np.logspace(-40, 4, 133)
    q_values = np.logspace(-12, math.log10(0.9), 161)

    points: list[Point] = []
    best_significant: Point | None = None
    acceptable_count = 0

    for lambda_hphi in lambda_hphi_values:
        for lambda_phi in lambda_phi_values:
            for q_i in q_values:
                point = evaluate(float(lambda_hphi), float(lambda_phi), float(q_i))
                if point.acceptable:
                    acceptable_count += 1
                if point.significant and point.phi_i_over_mpl < 1.0:
                    if best_significant is None or point.r_eq < best_significant.r_eq:
                        best_significant = point
                points.append(point)

    summary = {
        "total_points": float(len(points)),
        "acceptable_points": float(acceptable_count),
        "best_significant_r_eq": float(best_significant.r_eq if best_significant else math.nan),
        "best_significant_lambda_hphi": float(best_significant.lambda_hphi if best_significant else math.nan),
        "best_significant_lambda_phi": float(best_significant.lambda_phi if best_significant else math.nan),
        "best_significant_q_i": float(best_significant.q_i if best_significant else math.nan),
        "best_significant_t_transition_gev": float(best_significant.t_transition_gev if best_significant else math.nan),
        "best_significant_r_ew": float(best_significant.r_ew if best_significant else math.nan),
    }
    return points, summary


def write_summary(summary: dict[str, float], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["metric", "value"])
        for key, value in summary.items():
            writer.writerow([key, f"{value:.12g}"])


if __name__ == "__main__":
    _, summary = run_scan()
    target = Path(__file__).with_name("resultats_scan_portail_higgs_quartique_resume.csv")
    write_summary(summary, target)
    for key, value in summary.items():
        print(f"{key}: {value:.12g}")
