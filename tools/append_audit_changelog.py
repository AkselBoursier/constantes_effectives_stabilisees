from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def fail(message: str) -> None:
    raise SystemExit(f"REFUS: {message}")


def resolve_target(repo_root: Path, relative_path: str) -> Path:
    target = (repo_root / relative_path).resolve()
    try:
        target.relative_to(repo_root)
    except ValueError:
        fail("la cible sort du depot")
    if target.suffix.lower() != ".md":
        fail("la cible doit etre un fichier Markdown")
    if "data_external" in target.relative_to(repo_root).parts:
        fail("la cible est dans data_external")
    return target


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def find_git(explicit: str | None) -> str:
    if explicit:
        return explicit
    detected = shutil.which("git")
    if detected:
        return detected
    standard_windows_path = Path(r"C:\Program Files\Git\cmd\git.exe")
    if standard_windows_path.is_file():
        return str(standard_windows_path)
    fail("git est introuvable; utiliser --git-executable")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Append controle d'une entree de changelog Markdown."
    )
    parser.add_argument("target", help="chemin de la cible relatif au depot")
    parser.add_argument("addition", type=Path, help="bloc Markdown a ajouter")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--git-executable")
    parser.add_argument("--expected-sha256", required=True)
    parser.add_argument("--required-tail", required=True)
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    git_executable = find_git(args.git_executable)
    target = resolve_target(repo_root, args.target)
    addition = args.addition.resolve()

    if not target.is_file():
        fail("la cible n'existe pas")
    if not addition.is_file():
        fail("le bloc d'ajout n'existe pas")

    old = target.read_bytes()
    expected_sha = args.expected_sha256.lower()
    if sha256(old) != expected_sha:
        fail("le SHA-256 courant est different du SHA attendu")

    marker = args.required_tail.encode("utf-8")
    if not old.endswith(marker):
        fail("le marqueur de fin attendu est absent")

    block = addition.read_bytes()
    if not block:
        fail("le bloc d'ajout est vide")

    old_ended_with_newline = old.endswith((b"\n", b"\r"))
    separator = b"" if old_ended_with_newline else b"\n"
    new = old + separator + block
    if not new.startswith(old):
        fail("le nouveau contenu ne preserve pas le prefixe")

    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            dir=target.parent,
            prefix=f".{target.name}.",
            suffix=".tmp",
            delete=False,
        ) as temporary:
            temporary_path = Path(temporary.name)
            temporary.write(new)
            temporary.flush()
            os.fsync(temporary.fileno())

        if temporary_path.read_bytes()[: len(old)] != old:
            fail("la verification du prefixe temporaire a echoue")

        os.replace(temporary_path, target)
        temporary_path = None

        readback = target.read_bytes()
        if readback != new or readback[: len(old)] != old:
            fail("le read-back n'est pas append-only")
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)

    check = subprocess.run(
        [
            git_executable,
            "-C",
            str(repo_root),
            "diff",
            "--check",
            "--",
            args.target,
        ],
        text=True,
        capture_output=True,
    )
    if check.returncode != 0:
        sys.stderr.write(check.stdout)
        sys.stderr.write(check.stderr)
        fail("git diff --check a echoue")

    print(f"APPEND_OK target={args.target}")
    print(f"OLD_SHA256={expected_sha}")
    print(f"NEW_SHA256={sha256(new)}")
    print(f"OLD_BYTES={len(old)}")
    print(f"ADDED_BYTES={len(new) - len(old)}")
    print(f"EOF_NEWLINE_ADDED={not old_ended_with_newline}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())