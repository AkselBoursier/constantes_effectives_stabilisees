#!/usr/bin/env python3
"""Première reprise computationnelle de la tension N1–N3.

Le mode par défaut reconstruit les planchers oscillatoires, calibre une
vraisemblance gaussienne substitutive sur le résumé publié de DESI, puis teste
la sensibilité à la frontière, au prior et à la paramétrisation du spectre.

Ce mode n'est pas une reproduction des chaînes DESI. Un mode optionnel permet
d'analyser des chaînes Cobaya disponibles localement.
"""
from __future__ import annotations

import argparse
import csv
import glob
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import numpy as np
from scipy.integrate import cumulative_trapezoid, trapezoid
from scipy.optimize import root
from scipy.stats import norm


@dataclass(frozen=True)
class OscillationInputs:
    dm21: float = 7.50e-5
    dm21_sigma: float = 0.12e-5
    dm32_no: float = 2.43e-3
    dm32_no_sigma: float = 0.035e-3
    abs_dm32_io: float = 2.48e-3
    abs_dm32_io_sigma: float = 0.035e-3


@dataclass(frozen=True)
class DesiPublishedSummary:
    bayes_upper_95: float = 0.0642
    posterior_sd: float = 0.020
    feldman_cousins_upper_95: float = 0.053
    w0wa_upper_95: float = 0.163


def masses_from_lightest(
    m_lightest: np.ndarray,
    ordering: str,
    inputs: OscillationInputs,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    ml = np.asarray(m_lightest, dtype=float)
    if ordering == "NO":
        m1 = ml
        m2 = np.sqrt(ml**2 + inputs.dm21)
        # N1 cite Delta m32 pour NO : Delta m31 = Delta m32 + Delta m21.
        m3 = np.sqrt(ml**2 + inputs.dm32_no + inputs.dm21)
        return m1, m2, m3
    if ordering == "IO":
        m3 = ml
        m2 = np.sqrt(ml**2 + inputs.abs_dm32_io)
        m1 = np.sqrt(ml**2 + inputs.abs_dm32_io - inputs.dm21)
        return m1, m2, m3
    raise ValueError("ordering doit valoir 'NO' ou 'IO'")


def sigma_mass(
    m_lightest: np.ndarray,
    ordering: str,
    inputs: OscillationInputs,
) -> np.ndarray:
    return np.sum(
        np.vstack(masses_from_lightest(m_lightest, ordering, inputs)), axis=0
    )


def monte_carlo_floors(
    inputs: OscillationInputs,
    draws: int,
    seed: int,
) -> dict[str, dict[str, float | list[float]]]:
    rng = np.random.default_rng(seed)
    dm21 = rng.normal(inputs.dm21, inputs.dm21_sigma, draws)
    dm32_no = rng.normal(inputs.dm32_no, inputs.dm32_no_sigma, draws)
    dm32_io = rng.normal(inputs.abs_dm32_io, inputs.abs_dm32_io_sigma, draws)

    valid = (dm21 > 0) & (dm32_no + dm21 > 0) & (dm32_io > dm21)
    if valid.mean() < 0.999:
        raise RuntimeError("Trop de tirages non physiques")

    floor_no = np.sqrt(dm21[valid]) + np.sqrt(dm32_no[valid] + dm21[valid])
    floor_io = np.sqrt(dm32_io[valid] - dm21[valid]) + np.sqrt(dm32_io[valid])

    def summarize(x: np.ndarray) -> dict[str, float | list[float]]:
        return {
            "mean_eV": float(np.mean(x)),
            "sd_eV": float(np.std(x, ddof=1)),
            "quantiles_2p5_50_97p5_eV": [
                float(v) for v in np.quantile(x, [0.025, 0.50, 0.975])
            ],
        }

    return {"NO": summarize(floor_no), "IO": summarize(floor_io)}


def truncated_normal_stats(
    mu: float,
    sigma: float,
    lower: float = 0.0,
) -> tuple[float, float, float]:
    a = (lower - mu) / sigma
    z = 1.0 - norm.cdf(a)
    lam = norm.pdf(a) / z
    mean = mu + sigma * lam
    variance = sigma**2 * (1.0 + a * lam - lam**2)
    q95 = mu + sigma * norm.ppf(norm.cdf(a) + 0.95 * z)
    return float(mean), float(math.sqrt(variance)), float(q95)


def calibrate_surrogate(summary: DesiPublishedSummary) -> tuple[float, float]:
    """Calibre N(mu, sigma) avant troncature sur q95 et sd publiés."""

    def residual(x: np.ndarray) -> np.ndarray:
        mu, log_sigma = x
        sigma = math.exp(float(log_sigma))
        _, sd, q95 = truncated_normal_stats(float(mu), sigma, 0.0)
        return np.array([sd - summary.posterior_sd, q95 - summary.bayes_upper_95])

    sol = root(residual, np.array([-0.015, math.log(0.04)]))
    if not sol.success:
        raise RuntimeError(f"Échec de calibration : {sol.message}")
    return float(sol.x[0]), float(math.exp(sol.x[1]))


def trunc_quantile(
    mu: float,
    sigma: float,
    lower: float,
    probability: float,
) -> float:
    a = (lower - mu) / sigma
    return float(
        mu
        + sigma
        * norm.ppf(norm.cdf(a) + probability * (1.0 - norm.cdf(a)))
    )


def prob_above(
    mu: float,
    sigma: float,
    threshold: float,
    lower: float = 0.0,
) -> float:
    if threshold <= lower:
        return 1.0
    numerator = 1.0 - norm.cdf((threshold - mu) / sigma)
    denominator = 1.0 - norm.cdf((lower - mu) / sigma)
    return float(numerator / denominator)


def continuous_quantile(
    x: np.ndarray,
    density: np.ndarray,
    probabilities: Iterable[float],
) -> list[float]:
    cumulative = np.concatenate(([0.0], cumulative_trapezoid(density, x)))
    if cumulative[-1] <= 0:
        raise ValueError("Densité nulle")
    cumulative /= cumulative[-1]
    return [float(np.interp(p, cumulative, x)) for p in probabilities]


def discrete_quantile(
    values: np.ndarray,
    weights: np.ndarray,
    probabilities: Iterable[float],
) -> list[float]:
    order = np.argsort(values)
    values = np.asarray(values, dtype=float)[order]
    weights = np.asarray(weights, dtype=float)[order]
    if np.any(weights < 0) or weights.sum() <= 0:
        raise ValueError("Poids MCMC invalides")
    cumulative = np.cumsum(weights)
    cumulative /= cumulative[-1]
    return [float(np.interp(p, cumulative, values)) for p in probabilities]


def analyze_priors(
    mu: float,
    sigma: float,
    floors: dict[str, dict[str, float | list[float]]],
    inputs: OscillationInputs,
) -> tuple[list[dict[str, float | str]], dict[str, float]]:
    floor_no = float(floors["NO"]["mean_eV"])
    floor_io = float(floors["IO"]["mean_eV"])
    rows: list[dict[str, float | str]] = []

    for label, lower in [
        ("uniforme_Sigma_ge_0", 0.0),
        ("uniforme_Sigma_ge_plancher_NO", floor_no),
        ("uniforme_Sigma_ge_plancher_IO", floor_io),
    ]:
        rows.append(
            {
                "prior": label,
                "lower_eV": lower,
                "median_eV": trunc_quantile(mu, sigma, lower, 0.50),
                "upper95_eV": trunc_quantile(mu, sigma, lower, 0.95),
            }
        )

    ml = np.linspace(0.0, 1.0, 400_001)
    sum_no = sigma_mass(ml, "NO", inputs)
    sum_io = sigma_mass(ml, "IO", inputs)
    like_no = np.exp(-0.5 * ((sum_no - mu) / sigma) ** 2)
    like_io = np.exp(-0.5 * ((sum_io - mu) / sigma) ** 2)
    evidence_no = float(trapezoid(like_no, ml))
    evidence_io = float(trapezoid(like_io, ml))

    for ordering, sums, likelihood in [
        ("NO", sum_no, like_no),
        ("IO", sum_io, like_io),
    ]:
        ml_q50, ml_q95 = continuous_quantile(ml, likelihood, [0.50, 0.95])
        sum_q50, sum_q95 = continuous_quantile(sums, likelihood, [0.50, 0.95])
        rows.append(
            {
                "prior": f"uniforme_m_lightest_0_1eV_{ordering}",
                "lower_eV": 0.0,
                "median_eV": sum_q50,
                "upper95_eV": sum_q95,
                "m_lightest_median_eV": ml_q50,
                "m_lightest_upper95_eV": ml_q95,
            }
        )

    diagnostics = {
        "probability_above_NO_floor_given_uniform_Sigma_ge_0": prob_above(
            mu, sigma, floor_no
        ),
        "probability_above_IO_floor_given_uniform_Sigma_ge_0": prob_above(
            mu, sigma, floor_io
        ),
        "z_NO_floor_from_unbounded_surrogate_mean": (floor_no - mu) / sigma,
        "z_IO_floor_from_unbounded_surrogate_mean": (floor_io - mu) / sigma,
        "bayes_factor_NO_over_IO_uniform_m_lightest_0_1eV": (
            evidence_no / evidence_io
        ),
    }
    return rows, {key: float(value) for key, value in diagnostics.items()}


def write_diagnostic_plot(
    output_dir: Path,
    mu: float,
    sigma: float,
    floor_no: float,
    floor_io: float,
) -> None:
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        return

    x = np.linspace(-0.10, 0.20, 2000)
    unbounded = norm.pdf((x - mu) / sigma) / sigma
    truncated = np.where(x >= 0.0, unbounded, 0.0)
    truncated /= trapezoid(truncated, x)

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.plot(x, unbounded, label="Substitut non borné")
    ax.plot(x, truncated, label="Posterior tronqué Sigma m_nu >= 0")
    ax.axvline(0.0, linestyle="--", label="Frontière cosmologique")
    ax.axvline(floor_no, linestyle=":", label="Plancher oscillatoire NO")
    ax.axvline(floor_io, linestyle="-.", label="Plancher oscillatoire IO")
    ax.set_xlabel("Sigma m_nu [eV]")
    ax.set_ylabel("Densité normalisée")
    ax.set_title("Diagnostic substitutif de la tension N1-N3")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_dir / "diagnostic_tension_n1_n3.svg")
    plt.close(fig)


def read_cobaya_chains(
    paths: list[str],
    parameter: str,
) -> tuple[np.ndarray, np.ndarray]:
    values: list[np.ndarray] = []
    weights: list[np.ndarray] = []
    for path_str in paths:
        path = Path(path_str)
        with path.open("r", encoding="utf-8") as handle:
            first = handle.readline().strip()
        if not first.startswith("#"):
            raise ValueError(f"En-tête absent dans {path}")
        names = first.lstrip("#").split()
        if parameter not in names:
            raise ValueError(f"Paramètre {parameter!r} absent de {path}")
        data = np.loadtxt(path, comments="#")
        weight_name = "weight" if "weight" in names else names[0]
        values.append(data[:, names.index(parameter)])
        weights.append(data[:, names.index(weight_name)])
    return np.concatenate(values), np.concatenate(weights)


def write_outputs(
    output_dir: Path,
    inputs: OscillationInputs,
    summary: DesiPublishedSummary,
    floors: dict[str, dict[str, float | list[float]]],
    mu: float,
    sigma: float,
    rows: list[dict[str, float | str]],
    diagnostics: dict[str, float],
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "status": "surrogate_published_summary_not_official_chain_reproduction",
        "oscillation_inputs": asdict(inputs),
        "desi_published_summary": asdict(summary),
        "oscillation_floors": floors,
        "surrogate_unbounded_gaussian": {"mu_eV": mu, "sigma_eV": sigma},
        "diagnostics": diagnostics,
    }
    (output_dir / "resultats_synthese.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    fieldnames = sorted({key for row in rows for key in row})
    with (output_dir / "sensibilite_priors.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    write_diagnostic_plot(
        output_dir,
        mu,
        sigma,
        float(floors["NO"]["mean_eV"]),
        float(floors["IO"]["mean_eV"]),
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("sorties"))
    parser.add_argument("--draws", type=int, default=500_000)
    parser.add_argument("--seed", type=int, default=20260717)
    parser.add_argument("--chains-glob", help="Motif local des chaînes Cobaya")
    parser.add_argument("--chain-parameter", default="mnu")
    args = parser.parse_args()

    inputs = OscillationInputs()
    summary = DesiPublishedSummary()
    floors = monte_carlo_floors(inputs, args.draws, args.seed)
    mu, sigma = calibrate_surrogate(summary)
    rows, diagnostics = analyze_priors(mu, sigma, floors, inputs)
    write_outputs(args.output_dir, inputs, summary, floors, mu, sigma, rows, diagnostics)

    if args.chains_glob:
        paths = sorted(glob.glob(args.chains_glob))
        if not paths:
            raise FileNotFoundError(f"Aucune chaîne pour {args.chains_glob!r}")
        values, weights = read_cobaya_chains(paths, args.chain_parameter)
        chain_summary = {
            "files": paths,
            "parameter": args.chain_parameter,
            "weighted_mean_eV": float(np.average(values, weights=weights)),
            "weighted_q50_eV": discrete_quantile(values, weights, [0.50])[0],
            "weighted_q95_eV": discrete_quantile(values, weights, [0.95])[0],
        }
        (args.output_dir / "resultats_chaines_officielles.json").write_text(
            json.dumps(chain_summary, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    print(
        json.dumps(
            {"floors": floors, "mu": mu, "sigma": sigma, **diagnostics},
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
