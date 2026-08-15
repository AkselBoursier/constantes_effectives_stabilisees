#!/usr/bin/env python3
"""Detecteur d'ecarts entre regles declarees et regles suivies.

Principe directeur : une regle non instrumentee n'est pas une regle mais une
resolution. Ce script ne juge pas la conformite ; il rend l'absence visible en
tant que donnee. Il repond, pour chaque regle instrumentee, a une seule
question : "quel evenement aurait du declencher cette regle, et l'a-t-il fait ?"

Deux familles de regles (point 3 du plan) :

- regles de gouvernement (P28, P29, ...) : testees par audit d'ecart, ici ;
- regles de verdict (P27, ...) : testees par cas adversariaux, hors de ce
  script ; ce script ne fait que signaler une regle de verdict qui ne declare
  pas son mecanisme d'epreuve.

Meta-regle (point 5) : toute regle nommee du corpus doit declarer
  (a) l'incident date qui la motive ;
  (b) l'evenement observable qui compterait comme sa violation ;
  (c) le mecanisme qui detecte cet ecart.
Une regle sans ces trois elements est une "formulation exploratoire" (P28
amendee), sans autorite normative : le script la signale.

Severites :
- ERROR : un mecanisme declare est brise (ex. la regle pretend etre detectee
  par un fichier ou un registre absent) ;
- WARNING : une regle est declaree mais non instrumentee (ecart probable non
  observable) ;
- le script ne bloque jamais sur une difference d'interpretation : il signale.

Le script est sans dependance externe et ne modifie rien.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

EXCLUDED_PARTS = {
    ".git",
    ".github",
    "node_modules",
    "__pycache__",
}

# Les sources historiques et archives ne sont pas tenues a la regle courante :
# on ne requalifie pas retroactivement (regle temporelle du corpus).
SOURCE_OR_ARCHIVE_PARTS = {
    "00_Sources_docx",
    "00_Sources_docx_Genealogie_cartes",
    "90_Critiques_ constantes_effectives_stabilisees",
    "91_TRAVAUX_ANTERIEURS",
    "92_ARCHIVES_CONVERSATIONNELLES",
}

RULE_RE = re.compile(r"\b(P2[3-9]|P3[0-9])\b")
VERSIONED_MAP_RE = re.compile(r"^Carte_consolidee_(v[\w.]+?)(?:_([\w]+))?\.md$")
DATE_RE = re.compile(
    r"\b(20[0-9]{2}-[01][0-9]-[0-3][0-9]"
    r"|[0-3]?[0-9]\s+(janvier|fevrier|février|mars|avril|mai|juin|juillet"
    r"|aout|août|septembre|octobre|novembre|decembre|décembre)\s+20[0-9]{2})\b"
)
ISSUE_REF_RE = re.compile(r"#\d+|issues?/\d+|Registre_court_arbitrages")


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


@dataclass
class RuleOccurrence:
    name: str
    path: Path
    line: int
    has_date: bool = False
    has_instantiation_context: bool = False


def iter_markdown(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.md"):
        if any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        files.append(path)
    return sorted(files)


def is_source_or_archive(path: Path) -> bool:
    return any(part in SOURCE_OR_ARCHIVE_PARTS for part in path.parts)


# --- Meta-regle (point 5) : regles nommees -------------------------------


def collect_rule_occurrences(root: Path, files: list[Path]) -> dict[str, list[RuleOccurrence]]:
    """Repere chaque mention d'une regle nommee et note si elle est datee."""
    occurrences: dict[str, list[RuleOccurrence]] = {}
    for path in files:
        if is_source_or_archive(path):
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for number, line in enumerate(lines, start=1):
            for match in RULE_RE.finditer(line):
                name = match.group(1)
                occ = RuleOccurrence(name=name, path=path, line=number)
                # Fenetre de contexte : la ligne et les deux suivantes.
                window = " ".join(lines[number - 1 : number + 2])
                occ.has_date = bool(DATE_RE.search(window))
                occ.has_instantiation_context = bool(
                    ISSUE_REF_RE.search(window) or DATE_RE.search(window)
                )
                occurrences.setdefault(name, []).append(occ)
    return occurrences


def check_rules_instantiated(
    root: Path, occurrences: dict[str, list[RuleOccurrence]]
) -> list[Finding]:
    """Signale une regle nommee qui n'a nulle part de date d'instauration.

    Une regle active dont aucune occurrence n'est datee ni reliee a une issue
    ou au registre est une regle dont l'ecart n'est pas observable : c'est une
    resolution, pas une regle instrumentee.
    """
    findings: list[Finding] = []
    for name, occs in sorted(occurrences.items()):
        if any(occ.has_instantiation_context for occ in occs):
            continue
        first = occs[0]
        findings.append(
            Finding(
                "WARNING",
                first.path,
                first.line,
                f"regle {name} mentionnee {len(occs)} fois sans date d'instauration "
                "ni reference d'issue/registre : ecart non observable (meta-regle)",
            )
        )
    return findings


# --- P28 : remplacement de couches versionnees -----------------------------


def check_versioned_maps_replacement(root: Path, files: list[Path]) -> list[Finding]:
    """Une carte consolidee versionnee doit nommer la version qu'elle remplace.

    P28 impose qu'une nouvelle couche remplace ou simplifie une couche
    existante. L'accumulation de versions sans remplacement declare est le
    symptome historique que ce controle rend visible.
    """
    findings: list[Finding] = []
    maps: dict[str, list[Path]] = {}
    for path in files:
        match = VERSIONED_MAP_RE.match(path.name)
        if match and not is_source_or_archive(path):
            maps.setdefault("Carte_consolidee", []).append(path)

    for family, paths in maps.items():
        versions = sorted(paths, key=lambda p: p.name)
        for path in versions:
            try:
                head = "\n".join(path.read_text(encoding="utf-8").splitlines()[:30])
            except UnicodeDecodeError:
                continue
            names_others = [p.name for p in versions if p != path]
            declares = any(other.split(".md")[0] in head for other in names_others) or bool(
                re.search(r"remplace|conserve la v|etat anterieur|supersede", head, re.I)
            )
            if not declares:
                findings.append(
                    Finding(
                        "WARNING",
                        path,
                        1,
                        f"{family} versionnee sans declaration explicite de la version "
                        "remplacee/conservee (accumulation possible, cf. P28)",
                    )
                )
    return findings


# --- P29 / tracabilite : Decision_* reliee a une issue ou au registre ------


def check_decisions_traced(root: Path, files: list[Path]) -> list[Finding]:
    """Un document Decision_* doit referenceer une issue ou le registre.

    P29 exige que les arbitrages soient consignes. Une decision isolee, sans
    lien vers une issue ou le registre des arbitrages, est une decision dont la
    genealogie n'est pas reconstructible.
    """
    findings: list[Finding] = []
    for path in files:
        if not path.name.startswith("Decision_") or is_source_or_archive(path):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if not ISSUE_REF_RE.search(text):
            findings.append(
                Finding(
                    "WARNING",
                    path,
                    1,
                    "document Decision_* sans reference a une issue (#n) ni au "
                    "registre des arbitrages : genealogie non reconstructible (P29)",
                )
            )
    return findings


# --- Meta-regle : declaration des trois elements ---------------------------


def check_rule_mechanism_declared(root: Path) -> list[Finding]:
    """Verifie que le registre de regles existe et declare les mecanismes.

    Le registre des regles (audit/regles_actives.md) est la piece qui rend
    l'ecart observable : chaque regle y declare incident date, evenement de
    violation et mecanisme de detection. Son absence est un ERROR car le
    detecteur perd alors sa cible.
    """
    register = root / "audit" / "regles_actives.md"
    if not register.exists():
        return [
            Finding(
                "ERROR",
                register,
                1,
                "registre des regles actives absent : les regles nommees ne declarent "
                "ni incident date, ni violation observable, ni mecanisme de detection",
            )
        ]

    try:
        text = register.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return [Finding("ERROR", register, 1, "registre des regles illisible en UTF-8")]

    findings: list[Finding] = []
    # Chaque regle declaree (### Pxx) doit porter les trois champs.
    sections = re.split(r"\n(?=###\s)", text)
    for section in sections:
        title = section.splitlines()[0] if section.strip() else ""
        if not section.lstrip().startswith("###"):
            continue
        for label, needle in (
            ("incident date", "incident"),
            ("violation observable", "violation"),
            ("mecanisme de detection", "canisme"),
        ):
            if needle not in section.lower():
                findings.append(
                    Finding(
                        "WARNING",
                        register,
                        1,
                        f"regle '{title.strip('# ').strip()}' sans champ '{label}' "
                        "(meta-regle : formulation exploratoire tant que non complet)",
                    )
                )
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

    findings: list[Finding] = []
    occurrences = collect_rule_occurrences(root, files)
    findings.extend(check_rules_instantiated(root, occurrences))
    findings.extend(check_versioned_maps_replacement(root, files))
    findings.extend(check_decisions_traced(root, files))
    findings.extend(check_rule_mechanism_declared(root))

    for finding in findings:
        print(finding.render(root))

    errors = sum(f.severity == "ERROR" for f in findings)
    warnings = sum(f.severity == "WARNING" for f in findings)
    print(
        f"Audit des ecarts de regles : {len(files)} fichiers, "
        f"{len(occurrences)} regle(s) nommee(s), "
        f"{errors} erreur(s), {warnings} ecart(s) signale(s)."
    )

    if errors:
        return 1
    if args.strict and warnings:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
