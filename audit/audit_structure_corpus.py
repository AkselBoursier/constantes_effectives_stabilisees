#!/usr/bin/env python3
"""Audit structurel leger du corpus Markdown.

Controle :
- marqueurs de conflit Git ;
- blocs de code Markdown non fermes ;
- titres sans contenu avant le titre suivant ou la fin du fichier ;
- liens relatifs vers des fichiers absents ;
- references a quelques versions obsoletes dans les documents actifs.

Le script ne valide pas le contenu scientifique et ne remplace pas la lecture
humaine. Il est sans dependance externe.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


EXCLUDED_PARTS = {
    ".git",
    ".github",
    "node_modules",
    "__pycache__",
}

SOURCE_OR_ARCHIVE_PARTS = {
    "00_Sources_docx",
    "90_Critiques_ constantes_effectives_stabilisees",
}

CONFLICT_MARKERS = ("<<<<<<<", "=======", ">>>>>>>")

OBSOLETE_ACTIVE_REFERENCES = {
    "Matrice_temporelle_v0_1.md": "Matrice_temporelle_v0_2.md",
    "Reecriture_positive_vocabulaire_v0_1.md": "Reecriture_positive_vocabulaire_v0_3.md",
    "Workflow_GitHub_v0_1.md": "Workflow_GitHub_v0_2.md",
    "Plan_livrable_theorique_v0_1.md": "Plan_livrable_papier_A_v0_1.md ou les plans A1/A2",
}

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+\S")
FENCE_RE = re.compile(r"^\s*```")


@dataclass(frozen=True)
class Finding:
    severity: str
    path: Path
    line: int
    message: str

    def render(self, root: Path) -> str:
        try:
            relative = self.path.relative_to(root)
        except ValueError:
            relative = self.path
        return f"{self.severity}: {relative}:{self.line}: {self.message}"


def iter_markdown(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.md"):
        if any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        files.append(path)
    return sorted(files)


def is_historical_or_source(path: Path) -> bool:
    return any(part in SOURCE_OR_ARCHIVE_PARTS for part in path.parts)


def check_conflicts(path: Path, lines: list[str]) -> list[Finding]:
    findings: list[Finding] = []
    for number, line in enumerate(lines, start=1):
        stripped = line.lstrip()
        if any(stripped.startswith(marker) for marker in CONFLICT_MARKERS):
            findings.append(
                Finding("ERROR", path, number, "marqueur de conflit Git")
            )
    return findings


def check_fences(path: Path, lines: list[str]) -> list[Finding]:
    fence_lines = [
        number
        for number, line in enumerate(lines, start=1)
        if FENCE_RE.match(line)
    ]
    if len(fence_lines) % 2 == 0:
        return []
    return [
        Finding(
            "ERROR",
            path,
            fence_lines[-1],
            "nombre impair de blocs ``` ; bloc probablement non ferme",
        )
    ]


def check_empty_headings(path: Path, lines: list[str]) -> list[Finding]:
    findings: list[Finding] = []
    headings = [
        index for index, line in enumerate(lines) if HEADING_RE.match(line)
    ]
    for position, index in enumerate(headings):
        next_index = headings[position + 1] if position + 1 < len(headings) else len(lines)
        body = lines[index + 1 : next_index]
        meaningful = [
            line.strip()
            for line in body
            if line.strip() and not line.strip().startswith("<!--")
        ]
        if not meaningful:
            findings.append(
                Finding(
                    "WARNING",
                    path,
                    index + 1,
                    "titre sans contenu avant le titre suivant ou la fin du fichier",
                )
            )
    return findings


def normalize_link_target(raw: str) -> str | None:
    target = raw.strip()
    if not target:
        return None

    # Markdown autorise parfois un titre apres l'URL : (path "titre").
    if " " in target and not target.startswith("<"):
        target = target.split(" ", 1)[0]

    target = target.strip("<>")
    if target.startswith(("http://", "https://", "mailto:", "tel:", "#")):
        return None

    target = target.split("#", 1)[0].split("?", 1)[0]
    if not target:
        return None

    return unquote(target)


def check_links(path: Path, lines: list[str], root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for number, line in enumerate(lines, start=1):
        for match in LINK_RE.finditer(line):
            target = normalize_link_target(match.group(1))
            if target is None:
                continue

            candidate = (path.parent / target).resolve()
            try:
                candidate.relative_to(root.resolve())
            except ValueError:
                findings.append(
                    Finding(
                        "WARNING",
                        path,
                        number,
                        f"lien sortant du depot : {target}",
                    )
                )
                continue

            if not candidate.exists():
                findings.append(
                    Finding(
                        "ERROR",
                        path,
                        number,
                        f"lien relatif absent : {target}",
                    )
                )
    return findings


def check_obsolete_references(path: Path, lines: list[str]) -> list[Finding]:
    if is_historical_or_source(path):
        return []

    findings: list[Finding] = []
    for number, line in enumerate(lines, start=1):
        for obsolete, replacement in OBSOLETE_ACTIVE_REFERENCES.items():
            if obsolete in line:
                findings.append(
                    Finding(
                        "WARNING",
                        path,
                        number,
                        f"reference potentiellement obsolete : {obsolete} -> {replacement}",
                    )
                )
    return findings


def audit_file(path: Path, root: Path) -> list[Finding]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return [Finding("ERROR", path, 1, "fichier non lisible en UTF-8")]

    lines = text.splitlines()
    findings: list[Finding] = []
    findings.extend(check_conflicts(path, lines))
    findings.extend(check_fences(path, lines))
    findings.extend(check_empty_headings(path, lines))
    findings.extend(check_links(path, lines, root))
    findings.extend(check_obsolete_references(path, lines))
    return findings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="racine du depot (defaut : parent du dossier audit)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="faire echouer aussi sur les avertissements",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    if not root.exists():
        print(f"ERROR: racine absente : {root}", file=sys.stderr)
        return 2

    files = iter_markdown(root)
    findings = [finding for path in files for finding in audit_file(path, root)]

    for finding in findings:
        print(finding.render(root))

    errors = sum(finding.severity == "ERROR" for finding in findings)
    warnings = sum(finding.severity == "WARNING" for finding in findings)

    print(
        f"Audit structurel : {len(files)} fichiers Markdown, "
        f"{errors} erreur(s), {warnings} avertissement(s)."
    )

    if errors:
        return 1
    if args.strict and warnings:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
