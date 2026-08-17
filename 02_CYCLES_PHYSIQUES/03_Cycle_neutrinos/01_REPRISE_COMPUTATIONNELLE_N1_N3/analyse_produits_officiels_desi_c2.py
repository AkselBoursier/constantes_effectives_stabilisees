#!/usr/bin/env python3
"""C2 — ingestion contrôlée des produits officiels DESI DR2.

Le programme ne remplace jamais une chaîne absente par un substitut. Il distingue
les quantiles empiriques calculés depuis les poids, les limites officielles de
``chain.margestats``, les diagnostics Cobaya, les corrélations dérivées et les
produits ponctuels ``iminuit`` effectivement présents sous le même nom de modèle
et la même combinaison de données.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Sequence

import numpy as np


CORRELATION_CANDIDATES: dict[str, tuple[str, ...]] = {
    "H0": ("H0",),
    "Omega_m": ("omegam", "Omega_m", "OmegaM"),
    "w0": ("w0", "w"),
    "wa": ("wa",),
    "logA": ("logA", "logAs", "ln10As"),
    "A_s": ("As", "A_s"),
    "tau": ("tau",),
}


@dataclass(frozen=True)
class ChainSummary:
    model: str
    scope: str
    chain: str
    parameter: str
    rows: int
    weight_sum: float
    effective_sample_size: float
    weighted_mean_eV: float
    weighted_sd_eV: float
    weighted_q50_eV: float
    weighted_q95_eV: float
    minimum_eV: float
    maximum_eV: float


def sha256_file(path: Path, block_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while block := handle.read(block_size):
            digest.update(block)
    return digest.hexdigest()


def relative_to_repo(path: Path) -> str:
    resolved = path.resolve()
    root = Path.cwd().resolve()
    try:
        return resolved.relative_to(root).as_posix()
    except ValueError as exc:
        raise ValueError(
            f"Le chemin doit rester sous la racine du dépôt : {resolved}"
        ) from exc


def git_head() -> str | None:
    completed = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        return None
    return completed.stdout.strip() or None


def weighted_quantile(
    values: np.ndarray,
    weights: np.ndarray,
    probabilities: Sequence[float],
) -> list[float]:
    values = np.asarray(values, dtype=float)
    weights = np.asarray(weights, dtype=float)
    if values.ndim != 1 or weights.ndim != 1 or values.size != weights.size:
        raise ValueError("Valeurs et poids doivent être deux vecteurs de même taille")
    if values.size == 0 or np.any(~np.isfinite(values)):
        raise ValueError("Échantillon vide ou non fini")
    if np.any(~np.isfinite(weights)) or np.any(weights < 0) or weights.sum() <= 0:
        raise ValueError("Poids invalides")
    order = np.argsort(values)
    sorted_values = values[order]
    sorted_weights = weights[order]
    cumulative = np.cumsum(sorted_weights) - 0.5 * sorted_weights
    cumulative /= sorted_weights.sum()
    return [
        float(np.interp(probability, cumulative, sorted_values))
        for probability in probabilities
    ]


def first_header(path: Path) -> list[str]:
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if not stripped:
                continue
            if not stripped.startswith("#"):
                raise ValueError(f"En-tête Cobaya absent dans {path}")
            return stripped.lstrip("#").split()
    raise ValueError(f"Fichier vide : {path}")


def choose_column(
    names: Sequence[str],
    candidates: Sequence[str],
    kind: str,
    *,
    required: bool = True,
) -> str | None:
    lower_map = {name.lower(): name for name in names}
    for candidate in candidates:
        if candidate.lower() in lower_map:
            return lower_map[candidate.lower()]
    normalized = {re.sub(r"[^a-z0-9]", "", name.lower()): name for name in names}
    for candidate in candidates:
        key = re.sub(r"[^a-z0-9]", "", candidate.lower())
        if key in normalized:
            return normalized[key]
    if required:
        raise ValueError(
            f"Colonne {kind} absente. Candidats={list(candidates)}, "
            f"colonnes={list(names)}"
        )
    return None


def read_chain(
    path: Path,
    parameter_candidates: Sequence[str],
) -> tuple[list[str], np.ndarray, np.ndarray, np.ndarray, str]:
    names = first_header(path)
    weight_name = choose_column(names, ["weight", "weights"], "poids")
    parameter_name = choose_column(names, parameter_candidates, "masse")
    data = np.loadtxt(path, comments="#", ndmin=2)
    if data.shape[1] != len(names):
        raise ValueError(
            f"Nombre de colonnes incohérent dans {path}: "
            f"{data.shape[1]} != {len(names)}"
        )
    values = data[:, names.index(parameter_name)]
    weights = data[:, names.index(weight_name)]
    if np.any(~np.isfinite(values)):
        raise ValueError(f"Valeurs de masse non finies dans {path}")
    if np.any(~np.isfinite(weights)) or np.any(weights < 0) or weights.sum() <= 0:
        raise ValueError(f"Poids invalides dans {path}")
    return names, data, values, weights, parameter_name


def effective_sample_size(weights: np.ndarray) -> float:
    weights = np.asarray(weights, dtype=float)
    denominator = np.square(weights).sum()
    if denominator <= 0:
        raise ValueError("Somme des carrés des poids nulle")
    return float(weights.sum() ** 2 / denominator)


def summarize_arrays(
    model: str,
    scope: str,
    chain: str,
    parameter: str,
    values: np.ndarray,
    weights: np.ndarray,
) -> ChainSummary:
    mean = float(np.average(values, weights=weights))
    variance = float(np.average(np.square(values - mean), weights=weights))
    q50, q95 = weighted_quantile(values, weights, [0.50, 0.95])
    return ChainSummary(
        model=model,
        scope=scope,
        chain=chain,
        parameter=parameter,
        rows=int(values.size),
        weight_sum=float(weights.sum()),
        effective_sample_size=effective_sample_size(weights),
        weighted_mean_eV=mean,
        weighted_sd_eV=math.sqrt(max(variance, 0.0)),
        weighted_q50_eV=q50,
        weighted_q95_eV=q95,
        minimum_eV=float(values.min()),
        maximum_eV=float(values.max()),
    )


def weighted_correlation(
    x: np.ndarray,
    y: np.ndarray,
    weights: np.ndarray,
) -> float | None:
    mean_x = float(np.average(x, weights=weights))
    mean_y = float(np.average(y, weights=weights))
    centered_x = x - mean_x
    centered_y = y - mean_y
    variance_x = float(np.average(np.square(centered_x), weights=weights))
    variance_y = float(np.average(np.square(centered_y), weights=weights))
    if variance_x <= 0 or variance_y <= 0:
        return None
    covariance = float(np.average(centered_x * centered_y, weights=weights))
    return covariance / math.sqrt(variance_x * variance_y)


def parse_scalar(value: str) -> bool | int | float | str:
    stripped = value.strip()
    if stripped.lower() in {"true", "false"}:
        return stripped.lower() == "true"
    try:
        return int(stripped)
    except ValueError:
        pass
    try:
        return float(stripped)
    except ValueError:
        return stripped


def parse_checkpoint(path: Path) -> dict[str, Any]:
    wanted = {"converged", "Rminus1_last", "burn_in", "mpi_size"}
    result: dict[str, Any] = {"path": relative_to_repo(path), "exists": path.is_file()}
    if not path.is_file():
        return result
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"\s*([A-Za-z0-9_]+)\s*:\s*(.*?)\s*$", line)
        if match and match.group(1) in wanted:
            result[match.group(1)] = parse_scalar(match.group(2))
    return result


def parse_progress(path: Path) -> dict[str, Any]:
    result: dict[str, Any] = {"path": relative_to_repo(path), "exists": path.is_file()}
    if not path.is_file():
        return result
    lines = [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not lines:
        result["empty"] = True
        return result
    comments = [line.lstrip("#").strip() for line in lines if line.startswith("#")]
    data_lines = [line for line in lines if not line.startswith("#")]
    if comments:
        result["header"] = comments[-1].split()
    if data_lines:
        result["last_row_raw"] = data_lines[-1]
        values = data_lines[-1].split()
        result["last_row_values"] = values
        header = result.get("header")
        if isinstance(header, list) and len(header) == len(values):
            result["last_row"] = dict(zip(header, values))
    return result


def parse_margestats(path: Path, parameter: str) -> dict[str, Any]:
    result: dict[str, Any] = {"path": relative_to_repo(path), "exists": path.is_file()}
    if not path.is_file():
        return result
    parameter_pattern = re.compile(rf"^\s*{re.escape(parameter)}\s+(.*)$", re.IGNORECASE)
    for line in path.read_text(encoding="utf-8").splitlines():
        match = parameter_pattern.match(line)
        if not match:
            continue
        limits = [float(value) for value in re.findall(r"<\s*([0-9.eE+-]+)", line)]
        result["raw_line"] = line.strip()
        result["upper_limits_eV"] = limits
        if limits:
            result["upper68_eV"] = limits[0]
        if len(limits) >= 2:
            result["upper95_eV"] = limits[1]
        return result
    result["parameter_line_found"] = False
    return result


def resolve_model_directory(data_root: Path, relative_directory: str) -> Path:
    direct = data_root / Path(relative_directory)
    if direct.is_dir():
        return direct
    tail = Path(relative_directory)
    candidates = [
        data_root / tail.name,
        data_root / "cobaya" / tail.parent.name / tail.name,
        data_root / tail.parent.name / tail.name,
    ]
    for candidate in candidates:
        if candidate.is_dir():
            return candidate
    return direct


def inspect_iminuit(data_root: Path, model: str, dataset: str) -> dict[str, Any]:
    directory = data_root / "iminuit" / model / dataset
    result: dict[str, Any] = {
        "model": model,
        "dataset": dataset,
        "resolved_directory": relative_to_repo(directory),
        "exact_directory_exists": directory.is_dir(),
        "files": [],
        "status": "exact_product_not_available",
        "guardrail": "Aucun modèle voisin n'est substitué au modèle demandé.",
    }
    if not directory.is_dir():
        return result
    files = sorted(path for path in directory.rglob("bestfit.*") if path.is_file())
    result["files"] = [relative_to_repo(path) for path in files]
    result["status"] = "point_products_available" if files else "directory_without_bestfit_files"
    result["profile_status"] = "not_reconstructed_point_products_only"
    return result


def inspect_model(
    model: str,
    specification: dict[str, Any],
    data_root: Path | None,
    compute_hashes: bool,
    parameter_candidates: Sequence[str],
) -> dict[str, Any]:
    availability = specification.get("availability")
    result: dict[str, Any] = {
        "model": model,
        "definition": specification.get("definition"),
        "availability": availability,
        "relative_directory": specification.get("relative_directory"),
        "files": [],
        "metadata_files": [],
        "status": "not_inspected_no_data_root",
    }
    if availability and str(availability).startswith("not_present"):
        result["status"] = "not_available_in_verified_distribution"
        result["archive_observation"] = specification.get("archive_observation")
        return result
    if data_root is None:
        return result
    relative_directory = specification.get("relative_directory")
    if not relative_directory:
        result["status"] = "manifest_missing_relative_directory"
        return result

    model_directory = resolve_model_directory(data_root, relative_directory)
    result["resolved_directory"] = relative_to_repo(model_directory)
    expected_chain_files = specification.get("chain_files", [])
    expected_metadata_files = specification.get("metadata_files", [])
    result["expected_chain_count"] = len(expected_chain_files)
    result["expected_chain_bytes"] = sum(item["size_bytes"] for item in expected_chain_files)

    chain_paths: list[Path] = []
    missing: list[str] = []
    mismatched_sizes: list[dict[str, Any]] = []
    checksums: list[dict[str, Any]] = []

    def inspect_file(item: dict[str, Any], category: str) -> dict[str, Any]:
        path = model_directory / item["name"]
        record: dict[str, Any] = {
            "name": item["name"],
            "category": category,
            "path": relative_to_repo(path),
            "expected_size_bytes": item.get("size_bytes"),
            "exists": path.is_file(),
        }
        if path.is_file():
            actual_size = path.stat().st_size
            record["actual_size_bytes"] = actual_size
            expected_size = item.get("size_bytes")
            record["size_matches"] = expected_size is None or actual_size == expected_size
            if expected_size is not None and actual_size != expected_size:
                mismatched_sizes.append(record.copy())
            if compute_hashes:
                digest = sha256_file(path)
                record["sha256"] = digest
                checksums.append({"path": record["path"], "sha256": digest})
        else:
            missing.append(item["name"])
        return record

    for item in expected_chain_files:
        record = inspect_file(item, "chain")
        result["files"].append(record)
        if record["exists"]:
            chain_paths.append(model_directory / item["name"])
    for item in expected_metadata_files:
        result["metadata_files"].append(inspect_file(item, "metadata"))

    result["missing_files"] = missing
    result["size_mismatches"] = mismatched_sizes
    result["checksums"] = checksums
    if missing:
        result["status"] = "incomplete_missing_files"
        return result
    if mismatched_sizes:
        result["status"] = "incomplete_size_mismatch"
        return result

    per_chain: list[dict[str, Any]] = []
    all_values: list[np.ndarray] = []
    all_weights: list[np.ndarray] = []
    correlation_values: dict[str, list[np.ndarray]] = {
        alias: [] for alias in CORRELATION_CANDIDATES
    }
    selected_parameter: str | None = None
    selected_columns: dict[str, str] = {}

    for path in chain_paths:
        names, data, values, weights, parameter = read_chain(path, parameter_candidates)
        if selected_parameter is None:
            selected_parameter = parameter
        elif selected_parameter != parameter:
            raise ValueError(
                f"Nom de paramètre incohérent pour {model}: "
                f"{selected_parameter!r} puis {parameter!r}"
            )
        per_chain.append(
            summarize_arrays(
                model,
                "single_chain",
                path.name,
                parameter,
                values,
                weights,
            ).__dict__
        )
        all_values.append(values)
        all_weights.append(weights)
        for alias, candidates in CORRELATION_CANDIDATES.items():
            column = choose_column(names, candidates, alias, required=False)
            if column is None:
                continue
            if alias in selected_columns and selected_columns[alias] != column:
                raise ValueError(
                    f"Colonne incohérente pour {alias} dans {model}: "
                    f"{selected_columns[alias]!r} puis {column!r}"
                )
            selected_columns[alias] = column
            correlation_values[alias].append(data[:, names.index(column)])

    values = np.concatenate(all_values)
    weights = np.concatenate(all_weights)
    combined = summarize_arrays(
        model,
        "combined",
        "all",
        selected_parameter or "",
        values,
        weights,
    )
    correlations: list[dict[str, Any]] = []
    for alias, arrays in correlation_values.items():
        if len(arrays) != len(chain_paths):
            continue
        other = np.concatenate(arrays)
        correlations.append(
            {
                "model": model,
                "mass_parameter": selected_parameter,
                "parameter": alias,
                "source_column": selected_columns[alias],
                "weighted_pearson_r": weighted_correlation(values, other, weights),
            }
        )

    margestats = parse_margestats(model_directory / "chain.margestats", selected_parameter or "mnu")
    checkpoint = parse_checkpoint(model_directory / "chain.checkpoint")
    progress = parse_progress(model_directory / "chain.progress")
    dataset = Path(relative_directory).name
    iminuit = inspect_iminuit(data_root, model, dataset)

    official_upper95 = margestats.get("upper95_eV")
    comparison: dict[str, Any] = {
        "empirical_weighted_q95_eV": combined.weighted_q95_eV,
        "official_margestats_upper95_eV": official_upper95,
    }
    if isinstance(official_upper95, (int, float)):
        difference = combined.weighted_q95_eV - float(official_upper95)
        comparison["difference_eV"] = difference
        comparison["relative_difference_percent"] = (
            difference / float(official_upper95) * 100.0 if official_upper95 else None
        )

    result.update(
        {
            "status": "chains_ingested",
            "parameter": selected_parameter,
            "columns": first_header(chain_paths[0]),
            "per_chain_summaries": per_chain,
            "combined_summary": combined.__dict__,
            "margestats": margestats,
            "checkpoint": checkpoint,
            "progress": progress,
            "correlations": correlations,
            "iminuit": iminuit,
            "quantile_comparison": comparison,
        }
    )
    return result


def write_csv(path: Path, rows: Sequence[dict[str, Any]], fields: Sequence[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(fields), extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def write_outputs(payload: dict[str, Any], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "resultats_c2.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (output_dir / "manifest_local_desi_dr2_c2.json").write_text(
        json.dumps(
            {
                "instruction_version": "C2 post-consolidation v0.1",
                "executed_at_utc": payload["executed_at_utc"],
                "git_commit": payload["git_commit"],
                "data_root": payload["data_root"],
                "distribution": payload["distribution"],
                "models": [
                    {
                        "model": result["model"],
                        "status": result["status"],
                        "availability": result.get("availability"),
                        "resolved_directory": result.get("resolved_directory"),
                        "files": result.get("files", []),
                        "metadata_files": result.get("metadata_files", []),
                        "missing_files": result.get("missing_files", []),
                    }
                    for result in payload["models"]
                ],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    combined_rows: list[dict[str, Any]] = []
    chain_rows: list[dict[str, Any]] = []
    diagnostic_rows: list[dict[str, Any]] = []
    correlation_rows: list[dict[str, Any]] = []
    maxima_rows: list[dict[str, Any]] = []
    inventory_rows: list[dict[str, Any]] = []
    checksum_lines: list[str] = []

    for result in payload["models"]:
        model = result["model"]
        for record in result.get("files", []) + result.get("metadata_files", []):
            inventory_rows.append({"model": model, "status": result["status"], **record})
            if record.get("sha256"):
                checksum_lines.append(f"{record['sha256']}  {record['path']}")
        combined = result.get("combined_summary")
        if combined:
            comparison = result.get("quantile_comparison", {})
            combined_rows.append(
                {
                    **combined,
                    "official_margestats_upper95_eV": comparison.get(
                        "official_margestats_upper95_eV"
                    ),
                    "difference_eV": comparison.get("difference_eV"),
                    "relative_difference_percent": comparison.get(
                        "relative_difference_percent"
                    ),
                    "result_status": "reproduced_from_samples_with_statistical_convention_difference",
                }
            )
        chain_rows.extend(result.get("per_chain_summaries", []))
        checkpoint = result.get("checkpoint", {})
        diagnostic_rows.append(
            {
                "model": model,
                "status": result["status"],
                "converged": checkpoint.get("converged"),
                "Rminus1_last": checkpoint.get("Rminus1_last"),
                "burn_in": checkpoint.get("burn_in"),
                "mpi_size": checkpoint.get("mpi_size"),
                "progress_last_row_raw": result.get("progress", {}).get("last_row_raw"),
            }
        )
        correlation_rows.extend(result.get("correlations", []))
        iminuit = result.get("iminuit", {})
        maxima_rows.append(
            {
                "model": model,
                "dataset": iminuit.get("dataset"),
                "status": iminuit.get("status", "not_applicable"),
                "exact_directory_exists": iminuit.get("exact_directory_exists"),
                "files": ";".join(iminuit.get("files", [])),
                "profile_status": iminuit.get("profile_status"),
            }
        )

    write_csv(
        output_dir / "quantiles_c2.csv",
        combined_rows,
        [
            "model",
            "parameter",
            "rows",
            "weight_sum",
            "effective_sample_size",
            "weighted_mean_eV",
            "weighted_sd_eV",
            "weighted_q50_eV",
            "weighted_q95_eV",
            "official_margestats_upper95_eV",
            "difference_eV",
            "relative_difference_percent",
            "minimum_eV",
            "maximum_eV",
            "result_status",
        ],
    )
    write_csv(
        output_dir / "quantiles_par_chaine_c2.csv",
        chain_rows,
        list(ChainSummary.__dataclass_fields__),
    )
    write_csv(
        output_dir / "diagnostics_convergence_c2.csv",
        diagnostic_rows,
        [
            "model",
            "status",
            "converged",
            "Rminus1_last",
            "burn_in",
            "mpi_size",
            "progress_last_row_raw",
        ],
    )
    write_csv(
        output_dir / "correlations_c2.csv",
        correlation_rows,
        ["model", "mass_parameter", "parameter", "source_column", "weighted_pearson_r"],
    )
    write_csv(
        output_dir / "maxima_iminuit_c2.csv",
        maxima_rows,
        [
            "model",
            "dataset",
            "status",
            "exact_directory_exists",
            "files",
            "profile_status",
        ],
    )
    write_csv(
        output_dir / "inventaire_produits_desi_dr2_c2.csv",
        inventory_rows,
        [
            "model",
            "status",
            "category",
            "name",
            "path",
            "expected_size_bytes",
            "actual_size_bytes",
            "size_matches",
            "exists",
            "sha256",
        ],
    )
    (output_dir / "checksums_desi_dr2_c2.sha256").write_text(
        "\n".join(sorted(checksum_lines)) + ("\n" if checksum_lines else ""),
        encoding="utf-8",
    )
    write_markdown_report(payload, output_dir / "C2_Resultats_ingestion_locale_DESI_DR2_v0_2.md")


def format_number(value: Any, digits: int = 6) -> str:
    if value is None or value == "":
        return "non disponible"
    if isinstance(value, bool):
        return "oui" if value else "non"
    if isinstance(value, (int, float)):
        return f"{value:.{digits}g}"
    return str(value)


def write_markdown_report(payload: dict[str, Any], path: Path) -> None:
    lines = [
        "# C2 — Résultats de l’ingestion locale DESI DR2 v0.2",
        "",
        "## Statut",
        "",
        f"- exécution UTC : `{payload['executed_at_utc']}` ;",
        f"- commit de départ : `{payload['git_commit'] or 'non disponible'}` ;",
        f"- racine relative : `{payload['data_root'] or 'non fournie'}` ;",
        "- données brutes : hors Git ;",
        "- portée : reproduction depuis les chaînes distribuées, sans nouvel ajustement cosmologique.",
        "",
        "## Quantiles et convergence",
        "",
        "| Modèle | Statut | q95 empirique (eV) | limite officielle `margestats` (eV) | écart (eV) | R−1 final |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for result in payload["models"]:
        combined = result.get("combined_summary", {})
        comparison = result.get("quantile_comparison", {})
        checkpoint = result.get("checkpoint", {})
        lines.append(
            "| {model} | {status} | {q95} | {official} | {difference} | {rminus1} |".format(
                model=f"`{result['model']}`",
                status=result["status"],
                q95=format_number(combined.get("weighted_q95_eV")),
                official=format_number(comparison.get("official_margestats_upper95_eV")),
                difference=format_number(comparison.get("difference_eV")),
                rminus1=format_number(checkpoint.get("Rminus1_last")),
            )
        )
    lines.extend(
        [
            "",
            "Les quantiles empiriques utilisent directement les poids des échantillons. "
            "Les limites de `chain.margestats` restent séparées, car GetDist peut appliquer "
            "une convention de densité, de lissage ou d’interpolation différente.",
            "",
            "## Produits `iminuit`",
            "",
            "| Modèle | Produit exact même modèle/même jeu | Profil |",
            "|---|---|---|",
        ]
    )
    for result in payload["models"]:
        iminuit = result.get("iminuit", {})
        lines.append(
            f"| `{result['model']}` | {iminuit.get('status', 'non applicable')} | "
            f"{iminuit.get('profile_status', 'non reconstruit')} |"
        )
    lines.extend(
        [
            "",
            "Un fichier ponctuel `bestfit.*` n’est pas qualifié de profil. Aucun modèle voisin "
            "n’est substitué au modèle demandé.",
            "",
            "## Limites",
            "",
            "- `base_mnu_binary_3` n’est qualifié qu’au niveau de la distribution inspectée ;",
            "- l’absence dans cette archive ne vaut pas absence de toute distribution officielle ;",
            "- aucune conclusion de nouvelle physique n’est tirée avant séparation du support, "
            "des priors, du modèle d’expansion et des likelihoods.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def self_test(workdir: Path) -> dict[str, Any]:
    workdir.mkdir(parents=True, exist_ok=True)
    names = ["weight", "minuslogpost", "mnu", "omegam", "H0", "w", "wa"]
    chain_paths: list[Path] = []
    for number, offset in [(1, 0.0), (2, 0.01)]:
        path = workdir / f"chain.{number}.txt"
        values = np.array(
            [
                [1.0, 5.0, 0.05 + offset, 0.30, 67.0, -1.0, 0.0],
                [2.0, 4.0, 0.07 + offset, 0.31, 68.0, -0.9, -0.1],
                [1.0, 4.5, 0.09 + offset, 0.32, 69.0, -0.8, -0.2],
            ]
        )
        np.savetxt(path, values, header=" ".join(names))
        chain_paths.append(path)
    summaries = []
    all_values = []
    all_weights = []
    for path in chain_paths:
        _, _, values, weights, parameter = read_chain(path, ["mnu"])
        summaries.append(
            summarize_arrays("synthetic", "single_chain", path.name, parameter, values, weights)
        )
        all_values.append(values)
        all_weights.append(weights)
    combined = summarize_arrays(
        "synthetic",
        "combined",
        "all",
        "mnu",
        np.concatenate(all_values),
        np.concatenate(all_weights),
    )
    if combined.rows != 6 or not (0.05 <= combined.weighted_q50_eV <= 0.10):
        raise AssertionError("Échec du test synthétique")
    return {
        "status": "self_test_passed",
        "combined": combined.__dict__,
        "per_chain": [summary.__dict__ for summary in summaries],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--data-root", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("sorties_c2"))
    parser.add_argument("--models", nargs="*", default=None)
    parser.add_argument(
        "--parameter-candidates",
        nargs="+",
        default=["mnu", "sum_mnu", "Sigma_mnu", "omeganu"],
    )
    parser.add_argument("--hash-files", action="store_true")
    parser.add_argument("--allow-missing", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        test_payload = self_test(args.output_dir / "self_test")
        print(json.dumps(test_payload, ensure_ascii=False, indent=2))
        if args.data_root is None:
            return 0

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    selected_models = args.models or list(manifest["models"])
    unknown = sorted(set(selected_models) - set(manifest["models"]))
    if unknown:
        raise KeyError(f"Modèles absents du manifeste : {unknown}")

    data_root = args.data_root
    if data_root is not None:
        relative_to_repo(data_root)
    results = [
        inspect_model(
            model,
            manifest["models"][model],
            data_root,
            args.hash_files,
            args.parameter_candidates,
        )
        for model in selected_models
    ]
    ingested = [result for result in results if result["status"] == "chains_ingested"]
    incomplete = [
        result
        for result in results
        if result["status"] not in {"chains_ingested", "not_available_in_verified_distribution"}
    ]
    unavailable = [
        result for result in results if result["status"] == "not_available_in_verified_distribution"
    ]
    if len(ingested) == len(results):
        overall_status = "official_chains_ingested"
    elif ingested and unavailable and not incomplete:
        overall_status = "verified_distribution_partially_ingested_with_documented_absence"
    else:
        overall_status = "official_chains_not_fully_ingested"

    payload = {
        "status": overall_status,
        "executed_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": git_head(),
        "manifest": relative_to_repo(args.manifest),
        "data_root": relative_to_repo(data_root) if data_root else None,
        "distribution": manifest.get("local_distribution_observation"),
        "models": results,
        "guardrails": [
            "Aucun substitut C1 n'est utilisé lorsqu'une chaîne officielle manque.",
            "Aucun modèle iminuit voisin n'est substitué au modèle exact demandé.",
            "Un maximum ponctuel n'est pas qualifié de profil de vraisemblance.",
        ],
    }
    write_outputs(payload, args.output_dir)
    print(json.dumps(payload, ensure_ascii=False, indent=2))

    blocking = incomplete or (unavailable and not args.allow_missing)
    return 2 if blocking else 0


if __name__ == "__main__":
    raise SystemExit(main())
