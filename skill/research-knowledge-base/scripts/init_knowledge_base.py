#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialize an Obsidian research knowledge base."
    )
    parser.add_argument(
        "--destination",
        required=True,
        type=Path,
        help="Parent directory where the knowledge base will be created.",
    )
    parser.add_argument(
        "--name",
        required=True,
        help="Name of the knowledge-base directory.",
    )
    parser.add_argument(
        "--merge",
        action="store_true",
        help="Copy only missing files into an existing knowledge base.",
    )
    return parser.parse_args()


def validate_name(raw_name: str) -> str:
    name = raw_name.strip()
    if not name:
        raise ValueError("Knowledge-base name must not be blank.")
    if name in {".", ".."} or Path(name).name != name:
        raise ValueError("Knowledge-base name must be a single directory name.")
    return name


def copy_template(
    template_root: Path,
    target: Path,
    merge: bool,
) -> tuple[list[Path], list[Path]]:
    if not template_root.is_dir():
        raise FileNotFoundError(f"Bundled vault template not found: {template_root}")

    if target.exists() and not target.is_dir():
        raise FileExistsError(f"Target exists and is not a directory: {target}")

    if target.is_dir() and any(target.iterdir()) and not merge:
        raise FileExistsError(
            f"Target is not empty: {target}. Re-run with --merge to keep existing files."
        )

    target.mkdir(parents=True, exist_ok=True)
    created: list[Path] = []
    skipped: list[Path] = []

    for source in sorted(template_root.rglob("*")):
        relative = source.relative_to(template_root)
        destination = target / relative
        if source.is_dir():
            if not destination.exists():
                destination.mkdir(parents=True)
                created.append(relative)
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists():
            skipped.append(relative)
            continue
        shutil.copy2(source, destination)
        created.append(relative)

    return created, skipped


def main() -> int:
    args = parse_args()
    try:
        name = validate_name(args.name)
        destination = args.destination.expanduser().resolve()
        template_root = Path(__file__).resolve().parents[1] / "assets" / "vault-template"
        target = destination / name
        created, skipped = copy_template(template_root, target, args.merge)
    except (FileExistsError, FileNotFoundError, OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Knowledge base: {target}")
    for path in created:
        print(f"CREATED {path}")
    for path in skipped:
        print(f"SKIPPED {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
