#!/usr/bin/env python3
"""Build deterministic, allowlisted plugin and standalone skill ZIPs (stdlib only)."""
import hashlib
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = Path("skills/process-design-vibecoding")
SKILL_FILES = (
    "SKILL.md", "LOCAL_SUPPLEMENTS.md",
    "references/process-design-methodology.md", "references/discovery-question-bank.md",
    "references/testing-strategy.md", "references/change-management.md",
    "references/quality-gates.md", "references/evaluation-scenarios.md",
    "references/context7-documentation.md",
    "references/project-visualization.md",
    "references/prototype-first.md",
    "assets/spec-template.md", "assets/plan-template.md",
    "assets/acceptance-criteria-template.md", "assets/agents-rules-template.md",
    "assets/change-ledger-template.json",
    "scripts/bootstrap_project_memory.py", "scripts/validate_project_memory.py",
)
PACKAGE_FILES = (
    "plugin.json", "README.md", "LICENSE", "PRIVACY.md", "TERMS.md", "CHANGELOG.md",
    "assets/icon.svg", "docs/INSTALL_CHATGPT.md", "docs/SUBMISSION.md",
    "docs/verification.md", ".agents/plugins/marketplace.json",
)


def checked_source(relative):
    source = ROOT / relative
    if not source.resolve().is_relative_to(ROOT) or source.is_symlink() or not source.is_file():
        raise ValueError(f"Invalid or missing package file: {relative}")
    return source


def write_zip(destination, entries):
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for relative, archive_name in sorted(entries, key=lambda item: item[1]):
            info = zipfile.ZipInfo(archive_name, date_time=(2026, 10, 10, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, checked_source(relative).read_bytes())


def main():
    manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    version = manifest["version"]
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("version must be a numeric semantic version")
    entries = [(Path(name), name) for name in PACKAGE_FILES]
    entries.extend((SKILL / name, (SKILL / name).as_posix()) for name in SKILL_FILES)
    # Validate all inputs before touching prior build output.
    for relative, _ in entries:
        checked_source(relative)
    output = ROOT / "dist"
    if not output.resolve().is_relative_to(ROOT):
        raise ValueError("dist must resolve inside this repository")
    output.mkdir(exist_ok=True)
    plugin = output / f"process-design-vibecoding-plugin-{version}.zip"
    standalone = output / f"process-design-vibecoding-skill-{version}.zip"
    write_zip(plugin, entries)
    write_zip(standalone, [(SKILL / name, f"process-design-vibecoding/{name}") for name in SKILL_FILES]
              + [(Path("LICENSE"), "process-design-vibecoding/LICENSE")])
    sums = []
    for archive in (plugin, standalone):
        digest = hashlib.sha256(archive.read_bytes()).hexdigest()
        sums.append(f"{digest}  {archive.name}")
        print(f"built: {archive.name} ({archive.stat().st_size} bytes)")
    (output / "SHA256SUMS").write_text("\n".join(sums) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
