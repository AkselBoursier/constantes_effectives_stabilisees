#!/usr/bin/env python3
"""C2 — ingestion contrôlée des produits officiels DESI DR2.

Le programme ne remplace jamais une chaîne absente par le substitut de C1.
Sans fichiers locaux, il produit uniquement un diagnostic d'accessibilité et
retourne un statut explicite. Avec les chaînes extraites localement, il vérifie
leur taille, calcule les sommes SHA-256, lit les poids Cobaya et publie des
quantiles pondérés par modèle.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import numpy as np


@dataclass(frozen=True)
class ChainSummary:
    model: str
    parameter: str
    files: list[str]
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


def choose_column(names: Sequence[str], candidates: Sequence[str], kind: str) -> str:
    lower_map = {name.lower(): name for name in names}
    for candidate in candidates:
        if candidate.lower() in lower_map:
            return lower_map[candidate.lower()]
    normalized = {re.sub(r"[^a-z0-9]", "", name.lower()): name for name in names}
    for candidate in candidates:
        key = re.sub(r"[^a-z0-9]", "", candidate.lower())
        if key in normalized:
            return normalized[key]
    raise ValueError(
        f"Colonne {kind} absente. Candidats={list(candidates)}, colonnes={list(names)}"
    )


def read_chain(
    path: Path,
    parameter_candidates: Sequence[str],
) -> tuple[np.ndarray, np.ndarray, str]:
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
    return values, weights, parameter_name


def effective_sample_size(weights: np.ndarray) -> float:
    weights = np.asarray(weights, dtype=float)
    return float(weights.sum() ** 2 / np.square(weights).sum())


def summarize_model(
    model: str,
    chain_paths: Sequence[Path],
    parameter_candidates: Sequence[str],
) -> ChainSummary:
    all_values: list[np.ndarray] = []
    all_weights: list[np.ndarray] = []
    selected_parameter: str | None = None
    for path in chain_paths:
        values, weights, parameter = read_chain(path, parameter_candidates)
        if selected_parameter is None:
            selected_parameter = parameter
        elif selected_parameter != parameter:
            raise ValueError(
                f"Nom de paramètre incohérent pour {model}: "
                f"{selected_parameter!r} puis {parameter!r}"
            )
        all_values.append(values)
        all_weights.append(weights)
    values = np.concatenate(all_values)
    weights = np.concatenate(all_weights)
    mean = float(np.average(values, weights=weights))
    variance = float(np.average(np.square(values - mean), weights=weights))
    q50, q95 = weighted_quantile(values, weights, [0.50, 0.95])
    return ChainSummary(
        model=model,
        parameter=selected_parameter or "",
        files=[str(path) for path in chain_paths],
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


def resolve_model_directory(data_root: Path, relative_directory: str) -> Path:
    direct = data_root / relative_directory
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


def inspect_model(
    model: str,
    specification: dict,
    data_root: Path | None,
    compute_hashes: bool,
    parameter_candidates: Sequence[str],
) -> dict:
    expected_files = specification.get("chain_files", [])
    result: dict = {
        "model": model,
        "definition": specification.get("definition"),
        "relative_directory": specification.get("relative_directory"),
        "expected_chain_count": len(expected_files),
        "expected_chain_bytes": sum(item["size_bytes"] for item in expected_files),
        "files": [],
        "status": "not_inspected_no_data_root",
    }
    if data_root is None:
        return result

    model_directory = resolve_model_directory(
        data_root, specification["relative_directory"]
    )
    result["resolved_directory"] = str(model_directory)
    chain_paths: list[Path] = []
    missing: list[str] = []
    mismatched_sizes: list[dict] = []

    for item in expected_files:
        path = model_directory / item["name"]
        record = {
            "name": item["name"],
            "expected_size_bytes": item["size_bytes"],
            "exists": path.is_file(),
        }
        if path.is_file():
            actual_size = path.stat().st_size
            record["actual_size_bytes"] = actual_size
            record["size_matches"] = actual_size == item["size_bytes"]
            if actual_size != item["size_bytes"]:
                mismatched_sizes.append(record.copy())
            if compute_hashes:
                record["sha256"] = sha256_file(path)
            chain_paths.append(path)
        else:
            missing.append(item["name"])
        result["files"].append(record)

    result["missing_files"] = missing
    result["size_mismatches"] = mismatched_sizes
    if missing:
        result["status"] = "incomplete_missing_chain_files"
        return result
    if mismatched_sizes:
        result["status"] = "incomplete_size_mismatch"
        return result

    summary = summarize_model(model, chain_paths, parameter_candidates)
    result["status"] = "chains_ingested"
    result["summary"] = summary.__dict__
    return result


def write_csv(results: Sequence[dict], output_path: Path) -> None:
    fields = [
        "model",
        "status",
        "parameter",
        "rows",
        "weight_sum",
        "effective_sample_size",
        "weighted_mean_eV",
        "weighted_sd_eV",
        "weighted_q50_eV",
        "weighted_q95_eV",
        "minimum_eV",
        "maximum_eV",
    ]
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for result in results:
            summary = result.get("summary", {})
            writer.writerow(
                {
                    "model": result["model"],
                    "status": result["status"],
                    **{field: summary.get(field, "") for field in fields[2:]},
                }
            )


def self_test(workdir: Path) -> None:
    workdir.mkdir(parents=True, exist_ok=True)
    names = ["weight", "minuslogpost", "mnu", "omegam"]
    for number, offset in [(1, 0.0), (2, 0.01)]:
        path = workdir / f"chain.{number}.txt"
        values = np.array(
            [
                [1.0, 5.0, 0.05 + offset, 0.30],
                [2.0, 4.0, 0.07 + offset, 0.31],
                [1.0, 4.5, 0.09 + offset, 0.32],
            ]
        )
        np.savetxt(path, values, header=" ".join(names))
    summary = summarize_model(
        "synthetic", sorted(workdir.glob("chain.*.txt")), ["mnu"]
    )
    if summary.rows != 6 or not (0.05 <= summary.weighted_q50_eV <= 0.10):
        raise AssertionError("Échec du test synthétique")


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
        self_test(args.output_dir / "self_test")

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    selected_models = args.models or list(manifest["models"])
    unknown = sorted(set(selected_models) - set(manifest["models"]))
    if unknown:
        raise KeyError(f"Modèles absents du manifeste : {unknown}")

    results = [
        inspect_model(
            model,
            manifest["models"][model],
            args.data_root,
            args.hash_files,
            args.parameter_candidates,
        )
        for model in selected_models
    ]

    args.output_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "status": (
            "official_chains_ingested"
            if all(result["status"] == "chains_ingested" for result in results)
            else "official_metadata_only_chains_not_fully_ingested"
        ),
        "manifest": str(args.manifest),
        "data_root": str(args.data_root) if args.data_root else None,
        "models": results,
        "guardrail": (
            "Aucun substitut C1 n'est utilisé lorsqu'une chaîne officielle manque."
        ),
    }
    (args.output_dir / "resultats_c2.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_csv(results, args.output_dir / "quantiles_c2.csv")

    incomplete = [result for result in results if result["status"] != "chains_ingested"]
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if incomplete and not args.allow_missing:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
