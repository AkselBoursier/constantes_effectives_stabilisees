#!/usr/bin/env python3
"""
Exploratory scan for the minimal Z2-symmetric scalar-Higgs portal model.

The scan is deliberately limited. It assumes:
- the Higgs follows its post-crossover minimum adiabatically;
- 0 < q_i = lambda_Hphi * phi_i^2 / mu_H^2 < 1;
- the portal contribution dominates the late scalar mass;
- once H ~ m_eff, the coherent scalar condensate oscillates quadratically;
- the condensate is stable and receives no dissipative depletion;
- after oscillation onset, rho_phi scales as a^-3.

This is not a global cosmological fit. It is a falsification-oriented
test of whether a stable coherent condensate can both produce an initially
meaningful shift of the weak scale and remain cosmologically subdominant.
"""

from __future__ import annotations

import argparse
import csv
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

# Reference inputs (GeV units)
V0 = 246.22
M_H = 125.25
LAMBDA_H = M_H**2 / (2.0 * V0**2)
MU_H = math.sqrt(LAMBDA_H) * V0
M_PL = 1.2209e19
M_PL_REDUCED = 2.435e18

T_EW = 160.0
T_BBN = 1.0e-3
T_EQ = 0.8e-9
G_BBN = 10.75
GS_BBN = 10.75
GS_EQ = 3.91


def g_star(temperature: float) -> float:
    if temperature > 100.0:
        return 106.75
    if temperature > 1.0:
        return 75.0
    if temperature > 0.2:
        return 61.75
    if temperature > 1.0e-3:
        return 17.25
    if temperature > 1.0e-4:
        return 10.75
    return 3.36


def g_star_s(temperature: float) -> float:
    if temperature > 100.0:
        return 106.75
    if temperature > 1.0:
        return 75.0
    if temperature > 0.2:
        return 61.75
    if temperature > 1.0e-3:
        return 17.25
    if temperature > 1.0e-4:
        return 10.75
    return 3.91


def hubble_radiation(temperature: float, g_value: float | None = None) -> float:
    g_value = g_star(temperature) if g_value is None else g_value
    return 1.66 * math.sqrt(g_value) * temperature**2 / M_PL


def radiation_density(temperature: float, g_value: float | None = None) -> float:
    g_value = g_star(temperature) if g_value is None else g_value
    return (math.pi**2 / 30.0) * g_value * temperature**4


def oscillation_temperature(m_eff: float) -> float:
    """Solve H(T_osc)=m_eff with a coarse piecewise g*(T), capped at T_EW."""
    if m_eff <= 0.0:
        return 0.0
    temperature = min(T_EW, math.sqrt(m_eff * M_PL / 10.0))
    for _ in range(30):
        candidate = math.sqrt(
            m_eff * M_PL / (1.66 * math.sqrt(g_star(max(temperature, 1.0e-12))))
        )
        temperature = 0.5 * temperature + 0.5 * min(T_EW, candidate)
    return min(T_EW, temperature)


def delta_vacuum_energy(q_value: float) -> float:
    """
    Excess post-crossover potential energy relative to q=0 after minimizing H:
      Delta V = lambda_H v0^4 (2 q - q^2) / 4.
    """
    return LAMBDA_H * V0**4 * (2.0 * q_value - q_value**2) / 4.0


@dataclass(frozen=True)
class ScanPoint:
    lambda_portal: float
    q_initial: float
    phi_initial: float
    m_eff: float
    t_osc: float
    r_osc: float
    q_bbn: float
    delta_v_bbn: float
    r_eq: float
    initial_delta_v: float
    sub_planckian: bool
    no_preoscillation_domination: bool
    bbn_safe: bool
    relic_safe: bool
    meaningful_initial_shift: bool

    @property
    def passes_without_relic(self) -> bool:
        return (
            self.sub_planckian
            and self.no_preoscillation_domination
            and self.bbn_safe
            and self.meaningful_initial_shift
        )

    @property
    def passes_all(self) -> bool:
        return self.passes_without_relic and self.relic_safe


def evaluate(lambda_portal: float, q_initial: float) -> ScanPoint:
    if not (0.0 < q_initial < 1.0):
        raise ValueError("q_initial must satisfy 0 < q_initial < 1")
    if lambda_portal <= 0.0:
        raise ValueError("lambda_portal must be positive")

    phi_initial = MU_H * math.sqrt(q_initial / lambda_portal)
    m_eff = math.sqrt(lambda_portal * V0**2 * (1.0 - q_initial))
    t_osc = oscillation_temperature(m_eff)

    r_osc = delta_vacuum_energy(q_initial) / radiation_density(t_osc)

    if t_osc > T_BBN:
        a_osc_over_a_bbn = (
            (T_BBN / t_osc) * (GS_BBN / g_star_s(t_osc)) ** (1.0 / 3.0)
        )
        q_bbn = q_initial * a_osc_over_a_bbn**3
    else:
        q_bbn = q_initial

    delta_v_bbn = abs(math.sqrt(max(1.0 - q_bbn, 0.0)) - 1.0)

    if t_osc > T_EQ:
        a_eq_over_a_osc = (
            (t_osc / T_EQ) * (g_star_s(t_osc) / GS_EQ) ** (1.0 / 3.0)
        )
        r_eq = r_osc * a_eq_over_a_osc
    else:
        r_eq = r_osc

    initial_delta_v = abs(math.sqrt(1.0 - q_initial) - 1.0)

    return ScanPoint(
        lambda_portal=lambda_portal,
        q_initial=q_initial,
        phi_initial=phi_initial,
        m_eff=m_eff,
        t_osc=t_osc,
        r_osc=r_osc,
        q_bbn=q_bbn,
        delta_v_bbn=delta_v_bbn,
        r_eq=r_eq,
        initial_delta_v=initial_delta_v,
        sub_planckian=phi_initial < M_PL_REDUCED,
        no_preoscillation_domination=r_osc < 1.0,
        bbn_safe=delta_v_bbn < 0.01,
        relic_safe=r_eq < 1.0,
        meaningful_initial_shift=initial_delta_v > 0.01,
    )


def logspace(start_exp: float, stop_exp: float, count: int) -> list[float]:
    if count < 2:
        return [10.0**start_exp]
    step = (stop_exp - start_exp) / (count - 1)
    return [10.0 ** (start_exp + i * step) for i in range(count)]


def geometric_space(start: float, stop: float, count: int) -> list[float]:
    return [math.exp(value) for value in [
        math.log(start) + i * (math.log(stop) - math.log(start)) / (count - 1)
        for i in range(count)
    ]]


def scan(
    lambda_values: Iterable[float],
    q_values: Iterable[float],
) -> list[ScanPoint]:
    return [evaluate(lam, q) for lam in lambda_values for q in q_values]


def write_csv(points: list[ScanPoint], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(ScanPoint.__dataclass_fields__.keys()) + [
        "passes_without_relic",
        "passes_all",
    ]
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for point in points:
            row = {name: getattr(point, name) for name in ScanPoint.__dataclass_fields__}
            row["passes_without_relic"] = point.passes_without_relic
            row["passes_all"] = point.passes_all
            writer.writerow(row)


def summarize(points: list[ScanPoint]) -> dict[str, float | int]:
    relic_points = [
        point
        for point in points
        if point.sub_planckian
        and point.no_preoscillation_domination
        and point.bbn_safe
        and point.relic_safe
    ]
    max_relic_shift = max(
        (point.initial_delta_v for point in relic_points),
        default=float("nan"),
    )
    max_relic_q = max((point.q_initial for point in relic_points), default=float("nan"))
    return {
        "points": len(points),
        "sub_planckian": sum(point.sub_planckian for point in points),
        "no_preoscillation_domination": sum(
            point.no_preoscillation_domination for point in points
        ),
        "bbn_safe": sum(point.bbn_safe for point in points),
        "relic_safe": sum(point.relic_safe for point in points),
        "meaningful_initial_shift": sum(
            point.meaningful_initial_shift for point in points
        ),
        "passes_without_relic": sum(point.passes_without_relic for point in points),
        "passes_all": sum(point.passes_all for point in points),
        "max_relic_safe_q": max_relic_q,
        "max_relic_safe_initial_delta_v": max_relic_shift,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", type=Path, default=Path("scan_portail_higgs.csv"))
    parser.add_argument("--lambda-min-exp", type=float, default=-40.0)
    parser.add_argument("--lambda-max-exp", type=float, default=-8.0)
    parser.add_argument("--lambda-count", type=int, default=129)
    parser.add_argument("--q-min", type=float, default=1.0e-12)
    parser.add_argument("--q-max", type=float, default=0.9)
    parser.add_argument("--q-count", type=int, default=161)
    args = parser.parse_args()

    points = scan(
        logspace(args.lambda_min_exp, args.lambda_max_exp, args.lambda_count),
        geometric_space(args.q_min, args.q_max, args.q_count),
    )
    write_csv(points, args.csv)
    summary = summarize(points)

    for key, value in summary.items():
        if isinstance(value, float):
            print(f"{key}: {value:.8e}")
        else:
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()
