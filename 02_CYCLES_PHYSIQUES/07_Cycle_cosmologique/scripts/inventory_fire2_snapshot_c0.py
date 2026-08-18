#!/usr/bin/env python3
"""Inventory FIRE-2 HDF5 snapshot metadata for C7-GAL-C0.

Read-only utility: it never modifies the input files. It inventories HDF5 groups,
datasets, selected header attributes, required fields, file sizes and SHA-256 hashes.
It supports either a single snapshot HDF5 file or a snapdir containing multiple
HDF5 blocks.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
from typing import Any, Iterable

try:
    import h5py
except ImportError as exc:  # pragma: no cover
    raise SystemExit("h5py is required: python -m pip install h5py") from exc


REQUIRED_FIELDS = {
    "Header": [],
    "PartType0": [
        "Coordinates",
        "Velocities",
        "Masses",
        "Density",
        "InternalEnergy",
        "SmoothingLength",
        "ElectronAbundance",
        "NeutralHydrogenAbundance",
        "StarFormationRate",
    ],
    "PartType1": ["Coordinates", "Velocities", "Masses"],
    "PartType4": ["Coordinates", "Velocities", "Masses"],
}

OPTIONAL_PRIORITY_FIELDS = {
    "PartType0": ["Potential"],
    "PartType1": ["Potential"],
    "PartType4": ["Potential"],
}


def _jsonable(value: Any) -> Any:
    if hasattr(value, "tolist"):
        return value.tolist()
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    try:
        return list(value)
    except TypeError:
        return repr(value)


def sha256_file(path: Path, chunk_size: int = 8 * 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(chunk_size)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def resolve_hdf5_files(path: Path) -> list[Path]:
    if path.is_file():
        if path.suffix.lower() not in {".hdf5", ".h5"}:
            raise SystemExit(f"Not an HDF5 file: {path}")
        return [path.resolve()]
    if path.is_dir():
        files = sorted(
            p.resolve()
            for p in path.iterdir()
            if p.is_file() and p.suffix.lower() in {".hdf5", ".h5"}
        )
        if not files:
            raise SystemExit(f"No HDF5 files found in directory: {path}")
        return files
    raise SystemExit(f"Path does not exist: {path}")


def dataset_inventory(h5: h5py.File) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []

    def visitor(name: str, obj: Any) -> None:
        if isinstance(obj, h5py.Dataset):
            rows.append(
                {
                    "path": name,
                    "shape": list(obj.shape),
                    "dtype": str(obj.dtype),
                    "ndim": int(obj.ndim),
                    "compression": obj.compression,
                    "chunks": list(obj.chunks) if obj.chunks else None,
                }
            )

    h5.visititems(visitor)
    return rows


def header_attributes(h5: h5py.File) -> dict[str, Any]:
    if "Header" not in h5:
        return {}
    return {key: _jsonable(value) for key, value in h5["Header"].attrs.items()}


def field_status(h5: h5py.File) -> dict[str, Any]:
    required: dict[str, dict[str, bool]] = {}
    optional: dict[str, dict[str, bool]] = {}

    for group, fields in REQUIRED_FIELDS.items():
        group_present = group in h5
        required[group] = {"__group_present__": group_present}
        if group_present:
            required[group].update({field: field in h5[group] for field in fields})
        else:
            required[group].update({field: False for field in fields})

    for group, fields in OPTIONAL_PRIORITY_FIELDS.items():
        group_present = group in h5
        optional[group] = {"__group_present__": group_present}
        if group_present:
            optional[group].update({field: field in h5[group] for field in fields})
        else:
            optional[group].update({field: False for field in fields})

    return {"required": required, "optional_priority": optional}


def inspect_block(path: Path, do_hash: bool) -> dict[str, Any]:
    stat = path.stat()
    with h5py.File(path, "r") as h5:
        result = {
            "file": str(path),
            "size_bytes": stat.st_size,
            "size_gib": stat.st_size / (1024**3),
            "header_attributes": header_attributes(h5),
            "fields": field_status(h5),
            "datasets": dataset_inventory(h5),
        }
    if do_hash:
        result["sha256"] = sha256_file(path)
    return result


def aggregate_field_status(blocks: Iterable[dict[str, Any]]) -> dict[str, Any]:
    blocks = list(blocks)
    if not blocks:
        return {}

    aggregate: dict[str, Any] = {"required": {}, "optional_priority": {}}
    for category in ("required", "optional_priority"):
        groups = set()
        for block in blocks:
            groups.update(block["fields"][category].keys())
        for group in sorted(groups):
            keys = set()
            for block in blocks:
                keys.update(block["fields"][category].get(group, {}).keys())
            aggregate[category][group] = {}
            for key in sorted(keys):
                values = [
                    bool(block["fields"][category].get(group, {}).get(key, False))
                    for block in blocks
                ]
                aggregate[category][group][key] = {
                    "present_in_all_blocks": all(values),
                    "present_in_any_block": any(values),
                }
    return aggregate


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Read-only FIRE-2 snapshot HDF5 inventory for C7-GAL-C0."
    )
    parser.add_argument(
        "snapshot",
        type=Path,
        help="Snapshot .hdf5/.h5 file or snapdir containing HDF5 blocks.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Write JSON report to this path; otherwise print to stdout.",
    )
    parser.add_argument(
        "--sha256",
        action="store_true",
        help="Compute SHA-256 for each HDF5 block (streaming; can take time).",
    )
    args = parser.parse_args()

    files = resolve_hdf5_files(args.snapshot)
    blocks = [inspect_block(path, do_hash=args.sha256) for path in files]
    report = {
        "schema": "c7-gal-c0-fire2-inventory-v0.1",
        "input": str(args.snapshot.resolve()),
        "block_count": len(blocks),
        "total_size_bytes": sum(block["size_bytes"] for block in blocks),
        "total_size_gib": sum(block["size_bytes"] for block in blocks) / (1024**3),
        "aggregate_field_status": aggregate_field_status(blocks),
        "blocks": blocks,
    }

    payload = json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload + os.linesep, encoding="utf-8")
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
