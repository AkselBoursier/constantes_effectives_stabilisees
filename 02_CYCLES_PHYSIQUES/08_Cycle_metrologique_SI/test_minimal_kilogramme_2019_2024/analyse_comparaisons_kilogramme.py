from __future__ import annotations

import csv
import math
import statistics
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "donnees_ccm_m_k8_2019_2024.csv"
SUMMARY_OUTPUT = ROOT / "resultats_synthese_comparaisons.csv"
REPRO_OUTPUT = ROOT / "resultats_reproductibilite_laboratoires.csv"


def read_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    with INPUT.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            rows.append(
                {
                    "comparison": row["comparison"],
                    "year": int(row["year"]),
                    "lab": row["lab"],
                    "D_mg": float(row["D_mg"]),
                    "U_mg": float(row["U_mg"]),
                    "included_in_kcrv": row["included_in_kcrv"].lower() == "true",
                    "kcrv_offset_mg": float(row["kcrv_offset_from_previous_definition_mg"]),
                    "uR_mg": float(row["uR_mg"]),
                    "source": row["source"],
                }
            )
    return rows


def participant_standard_uncertainty(row: dict[str, object]) -> float:
    """Reconstruct u_i from the KCDB degree-of-equivalence uncertainty U_i.

    For participants included in the KCRV:
        U_i = 2 * sqrt(u_i^2 - u_R^2)
    For an excluded participant:
        U_i = 2 * sqrt(u_i^2 + u_R^2)
    """
    U = float(row["U_mg"])
    uR = float(row["uR_mg"])
    if bool(row["included_in_kcrv"]):
        return math.sqrt((U / 2.0) ** 2 + uR**2)
    return math.sqrt(max((U / 2.0) ** 2 - uR**2, 0.0))


def write_summary(rows: list[dict[str, object]]) -> None:
    by_year: dict[int, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        by_year[int(row["year"])].append(row)

    fields = [
        "year",
        "participants_total",
        "participants_in_kcrv",
        "kcrv_offset_ug",
        "uR_ug",
        "D_min_ug",
        "D_max_ug",
        "D_range_ug",
        "D_sample_sd_ug",
        "median_abs_D_ug",
        "max_abs_D_ug",
        "within_expanded_U",
    ]

    with SUMMARY_OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for year in sorted(by_year):
            all_rows = by_year[year]
            included = [r for r in all_rows if bool(r["included_in_kcrv"])]
            values = [float(r["D_mg"]) for r in included]
            uncertainties = [float(r["U_mg"]) for r in included]
            writer.writerow(
                {
                    "year": year,
                    "participants_total": len(all_rows),
                    "participants_in_kcrv": len(included),
                    "kcrv_offset_ug": f"{float(included[0]['kcrv_offset_mg']) * 1000:.4f}",
                    "uR_ug": f"{float(included[0]['uR_mg']) * 1000:.4f}",
                    "D_min_ug": f"{min(values) * 1000:.4f}",
                    "D_max_ug": f"{max(values) * 1000:.4f}",
                    "D_range_ug": f"{(max(values) - min(values)) * 1000:.4f}",
                    "D_sample_sd_ug": f"{statistics.stdev(values) * 1000:.4f}",
                    "median_abs_D_ug": f"{statistics.median(abs(v) for v in values) * 1000:.4f}",
                    "max_abs_D_ug": f"{max(abs(v) for v in values) * 1000:.4f}",
                    "within_expanded_U": sum(
                        abs(value) <= uncertainty + 1e-12
                        for value, uncertainty in zip(values, uncertainties)
                    ),
                }
            )


def write_reproducibility(rows: list[dict[str, object]]) -> None:
    by_lab: dict[str, dict[int, dict[str, object]]] = defaultdict(dict)
    for row in rows:
        by_lab[str(row["lab"])][int(row["year"])] = row

    common_labs = sorted(lab for lab, yearly in by_lab.items() if {2019, 2021, 2024} <= set(yearly))
    fields = [
        "lab",
        "offset_2019_ug",
        "offset_2021_ug",
        "offset_2024_ug",
        "range_ug",
        "delta_2024_minus_2019_ug",
        "u_2019_ug",
        "u_2021_ug",
        "u_2024_ug",
    ]

    with REPRO_OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for lab in common_labs:
            yearly = by_lab[lab]
            offsets = {
                year: float(yearly[year]["D_mg"]) + float(yearly[year]["kcrv_offset_mg"])
                for year in (2019, 2021, 2024)
            }
            u_values = {
                year: participant_standard_uncertainty(yearly[year])
                for year in (2019, 2021, 2024)
            }
            writer.writerow(
                {
                    "lab": lab,
                    "offset_2019_ug": f"{offsets[2019] * 1000:.4f}",
                    "offset_2021_ug": f"{offsets[2021] * 1000:.4f}",
                    "offset_2024_ug": f"{offsets[2024] * 1000:.4f}",
                    "range_ug": f"{(max(offsets.values()) - min(offsets.values())) * 1000:.4f}",
                    "delta_2024_minus_2019_ug": f"{(offsets[2024] - offsets[2019]) * 1000:.4f}",
                    "u_2019_ug": f"{u_values[2019] * 1000:.4f}",
                    "u_2021_ug": f"{u_values[2021] * 1000:.4f}",
                    "u_2024_ug": f"{u_values[2024] * 1000:.4f}",
                }
            )


def main() -> None:
    rows = read_rows()
    years = {int(row["year"]) for row in rows}
    if years != {2019, 2021, 2024}:
        raise ValueError(f"Comparaisons attendues absentes ou inattendues : {sorted(years)}")
    write_summary(rows)
    write_reproducibility(rows)
    print(f"Écrit : {SUMMARY_OUTPUT.name}")
    print(f"Écrit : {REPRO_OUTPUT.name}")


if __name__ == "__main__":
    main()
