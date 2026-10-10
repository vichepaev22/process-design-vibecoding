#!/usr/bin/env python3
"""Local optional helper derived from SKILL.md (2026-10-05); never overwrite files."""
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--spec", type=Path, help="Existing canonical specification, relative to the project")
    parser.add_argument("--with-agents-template", action="store_true")
    args = parser.parse_args()
    root = args.root.expanduser().resolve(strict=True)
    if not root.is_dir():
        parser.error("--root must be an existing project directory")
    if args.with_agents_template and (root / "AGENTS.md").exists():
        parser.error("existing AGENTS.md must be preserved and adapted manually")
    candidates = [name for name in ("docs/spec.md", "docs/PRD.md", "PRD.md", "SPEC.md") if (root / name).is_file()]
    if args.spec is None and len(candidates) > 1:
        parser.error("multiple specifications found; select the canonical document with --spec")
    relative_spec = args.spec or Path(candidates[0] if candidates else "docs/spec.md")
    if relative_spec.is_absolute() or not (root / relative_spec).resolve().is_relative_to(root):
        parser.error("--spec must resolve inside the project")
    assets = Path(__file__).resolve().parent.parent / "assets"
    documents = {
        relative_spec.as_posix(): (assets / "spec-template.md").read_text(encoding="utf-8"),
        "docs/plan.md": (assets / "plan-template.md").read_text(encoding="utf-8"),
        "docs/acceptance.md": (assets / "acceptance-criteria-template.md").read_text(encoding="utf-8"),
        "docs/decisions.md": "# Decisions\n\n## Decision records\n\nRecord context, decision, reasons, consequences and linked requirements.\n",
    }
    if args.with_agents_template:
        documents["AGENTS.md"] = (assets / "agents-rules-template.md").read_text(encoding="utf-8")
    for relative, content in documents.items():
        destination = root / relative
        if not destination.resolve().is_relative_to(root):
            parser.error(f"destination resolves outside the project: {relative}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        try:
            with destination.open("x", encoding="utf-8", newline="\n") as output:
                output.write(content)
            print(f"created: {relative}")
        except FileExistsError:
            print(f"preserved: {relative}")
    print("Templates need project-specific content; this is not proof of readiness.")


if __name__ == "__main__":
    main()
