#!/usr/bin/env python3
"""Optional document structure and change traceability check; not proof of behavior."""
import argparse
import json
import re
from pathlib import Path


EXPECTED = {
    "docs/spec.md": {"Context and problem", "Requirements and domain rules", "Acceptance criteria", "Assumptions and open questions"},
    "docs/plan.md": {"Objective and scope", "Vertical slices", "Verification commands", "Progress and remaining work"},
    "docs/acceptance.md": {"Scenarios", "Coverage and limitations"},
    "docs/decisions.md": {"Decision records"},
}
STATUSES = {"proposed", "accepted", "deferred", "rejected"}
DELIVERY = {"pending", "implemented", "verified"}


def project_path(root, value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("document path must be a nonempty string")
    path = Path(value)
    if path.is_absolute() or not (root / path).resolve().is_relative_to(root):
        raise ValueError("document path must resolve inside the project")
    return (root / path).resolve()


def validate_changes(root, spec, ledger_path, required_ids=()):
    failures = []
    try:
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        return [f"cannot read change ledger: {error}"]
    if not isinstance(ledger, dict) or not isinstance(ledger.get("changes"), list):
        return ["change ledger must contain a changes array"]
    ids = set()
    for index, change in enumerate(ledger["changes"], start=1):
        prefix = f"change {index}"
        if not isinstance(change, dict):
            failures.append(f"{prefix}: must be an object")
            continue
        change_id = change.get("id")
        if not isinstance(change_id, str) or not change_id.strip():
            failures.append(f"{prefix}: missing id")
        elif change_id in ids:
            failures.append(f"{prefix}: duplicate id {change_id}")
        else:
            ids.add(change_id)
            prefix = change_id
        summary = change.get("summary")
        if not isinstance(summary, str) or not summary.strip():
            failures.append(f"{prefix}: missing summary")
        status = change.get("status")
        delivery = change.get("delivery", "pending")
        if not isinstance(status, str) or status not in STATUSES:
            failures.append(f"{prefix}: invalid status")
        if not isinstance(delivery, str) or delivery not in DELIVERY:
            failures.append(f"{prefix}: invalid delivery state")
        if status != "accepted":
            if delivery != "pending":
                failures.append(f"{prefix}: unaccepted change must remain pending")
            continue
        for key in ("spec_ref", "acceptance_ref", "plan_ref"):
            reference = change.get(key)
            if not isinstance(reference, dict):
                failures.append(f"{prefix}: missing {key}")
                continue
            try:
                target = project_path(root, reference.get("path"))
            except ValueError as error:
                failures.append(f"{prefix}: {key}: {error}")
                continue
            if key == "spec_ref" and target != spec.resolve():
                failures.append(f"{prefix}: accepted changes must reference the canonical spec")
            marker = reference.get("marker")
            if not isinstance(marker, str) or not marker.strip():
                failures.append(f"{prefix}: {key}: missing marker")
                continue
            try:
                content = target.read_text(encoding="utf-8")
            except (OSError, UnicodeError):
                failures.append(f"{prefix}: {key}: cannot read {reference.get('path')}")
                continue
            if marker not in content:
                failures.append(f"{prefix}: {key}: marker not found: {marker}")
        if delivery == "verified":
            evidence = change.get("verification")
            if not isinstance(evidence, list) or not evidence or not all(isinstance(item, str) and item.strip() for item in evidence):
                failures.append(f"{prefix}: verified requires recorded verification evidence")
    for change_id in required_ids:
        if change_id not in ids:
            failures.append(f"missing current-task change: {change_id}")
    return failures


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--spec", help="Canonical spec path; custom formats skip default spec headings")
    parser.add_argument("--changes", help="Optional project-relative JSON change ledger")
    parser.add_argument("--require-change", action="append", default=[], help="Material current-task request ID; repeat as needed")
    args = parser.parse_args()
    root = args.root.expanduser().resolve(strict=True)
    if args.require_change and not args.changes:
        parser.error("--require-change needs --changes")
    try:
        spec = project_path(root, args.spec or "docs/spec.md")
        ledger = project_path(root, args.changes) if args.changes else None
    except ValueError as error:
        parser.error(str(error))
    failures = []
    if not spec.is_file():
        failures.append("canonical spec is missing")
    for relative, required in EXPECTED.items():
        if relative == "docs/spec.md" and args.spec:
            continue
        try:
            file = project_path(root, relative)
        except ValueError as error:
            failures.append(f"{relative}: {error}")
            continue
        if not file.is_file():
            failures.append(f"missing: {relative}")
            continue
        try:
            content = file.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            failures.append(f"cannot read {relative}: {error}")
            continue
        headings = set(re.findall(r"^## (.+?)\s*$", content, re.MULTILINE))
        missing = required - headings
        if missing:
            failures.append(f"{relative}: missing sections: {', '.join(sorted(missing))}")
    if ledger:
        failures.extend(validate_changes(root, spec, ledger, args.require_change))
    for failure in failures:
        print(failure)
    print("Structure/traceability only: manually reconcile request meaning and actual verification outcomes.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
