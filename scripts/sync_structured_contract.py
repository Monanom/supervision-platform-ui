#!/usr/bin/env python3
"""Sync the generated Sketch contract into every distributed supervision skill copy."""

from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
GENERIC = WORKSPACE / "Supervision-Platform-AI-Skill"
LOCAL_SKILL = WORKSPACE / "skills/supervision-platform-ui"


def copy_file(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def copy_docs(destination: Path) -> None:
    source_dir = ROOT / "knowledge/component-parameters"
    destination.mkdir(parents=True, exist_ok=True)
    for source in sorted(source_dir.glob("*.md")):
        copy_file(source, destination / source.name)


def main() -> int:
    contract = ROOT / "data/sketch-component-contract.json"
    conflicts = ROOT / "data/sketch-contract-conflicts.json"
    if not contract.exists() or not conflicts.exists():
        raise SystemExit("Run scripts/extract_sketch_contract.py before syncing.")

    kb_skill = ROOT / "codex-skills/supervision-page-builder/references"
    copy_file(contract, kb_skill / "data/sketch-component-contract.json")
    copy_file(conflicts, kb_skill / "data/sketch-contract-conflicts.json")
    copy_docs(kb_skill / "component-contract")

    copy_file(contract, LOCAL_SKILL / "references/data/sketch-component-contract.json")
    copy_file(conflicts, LOCAL_SKILL / "references/data/sketch-contract-conflicts.json")
    copy_docs(LOCAL_SKILL / "references/component-contract")

    if GENERIC.exists():
        copy_file(ROOT / "scripts/extract_sketch_contract.py", GENERIC / "scripts/extract_sketch_contract.py")
        copy_file(ROOT / "data/sketch-contract/component-map.json", GENERIC / "data/sketch-contract/component-map.json")
        copy_file(ROOT / "data/sketch-contract/manual-overrides.json", GENERIC / "data/sketch-contract/manual-overrides.json")
        copy_file(contract, GENERIC / "data/sketch-component-contract.json")
        copy_file(conflicts, GENERIC / "data/sketch-contract-conflicts.json")
        copy_docs(GENERIC / "rules/component-parameters")
        copy_file(ROOT / "data/design-token.json", GENERIC / "data/design-token.json")

        install_refs = GENERIC / "install/codex-skills/supervision-platform-ai-skill/references"
        copy_file(contract, install_refs / "data/sketch-component-contract.json")
        copy_file(conflicts, install_refs / "data/sketch-contract-conflicts.json")
        copy_file(ROOT / "data/design-token.json", install_refs / "data/design-token.json")
        copy_docs(install_refs / "component-contract")

    print("Structured Sketch contract synchronized to all available distribution copies.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
