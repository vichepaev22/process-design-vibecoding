"""Four offline regressions for preservation and request traceability."""
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1] / "skills/process-design-vibecoding"
MODULE_SPEC = importlib.util.spec_from_file_location("memory_validator", SKILL / "scripts/validate_project_memory.py")
VALIDATOR = importlib.util.module_from_spec(MODULE_SPEC)
MODULE_SPEC.loader.exec_module(VALIDATOR)


class ProjectMemoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        (self.root / "docs").mkdir()
        self.spec = self.root / "docs/PRD.md"
        self.spec.write_text("# Основное ТЗ\nADM-003: notify after confirmed grant\n", encoding="utf-8")
        (self.root / "docs/acceptance.md").write_text("AC-003: confirmation triggers one notification\n", encoding="utf-8")
        (self.root / "docs/plan.md").write_text("TASK-003: implement ADM-003 and check AC-003\n", encoding="utf-8")
        self.change = {
            "id": "CR-003", "summary": "Notify after a confirmed grant",
            "status": "accepted", "delivery": "pending",
            "spec_ref": {"path": "docs/PRD.md", "marker": "ADM-003"},
            "acceptance_ref": {"path": "docs/acceptance.md", "marker": "AC-003"},
            "plan_ref": {"path": "docs/plan.md", "marker": "TASK-003"},
        }

    def validate(self, changes, required=("CR-003",)):
        ledger = self.root / "docs/changes.json"
        ledger.write_text(json.dumps({"changes": changes}), encoding="utf-8")
        return VALIDATOR.validate_changes(self.root, self.spec, ledger, required)

    def test_bootstrap_preserves_existing_prd_and_requires_ambiguous_choice(self):
        before = self.spec.read_bytes()
        command = [sys.executable, str(SKILL / "scripts/bootstrap_project_memory.py"), "--root", str(self.root)]
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.spec.read_bytes(), before)
        self.assertFalse((self.root / "docs/spec.md").exists())
        (self.root / "SPEC.md").write_text("other spec", encoding="utf-8")
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("select the canonical document", result.stderr)
        result = subprocess.run(command + ["--spec", "../outside.md"], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("inside the project", result.stderr)

    def test_auxiliary_only_accepted_change_is_rejected(self):
        (self.root / "docs/admin-plan.md").write_text("ADM-003: implemented in admin", encoding="utf-8")
        self.change["spec_ref"]["path"] = "docs/admin-plan.md"
        self.assertTrue(any("canonical spec" in error for error in self.validate([self.change])))

    def test_missing_request_is_detected_and_proposals_stay_explicit(self):
        proposal = {"id": "CR-004", "summary": "Notification history", "status": "proposed", "delivery": "pending"}
        deferred = {"id": "CR-005", "summary": "Bulk notifications", "status": "deferred", "delivery": "pending"}
        self.assertEqual(self.validate([self.change, proposal, deferred], ("CR-003", "CR-004", "CR-005")), [])
        self.assertIn("missing current-task change: CR-006", self.validate([self.change, proposal], ("CR-006",)))
        proposal["delivery"] = "implemented"
        self.assertTrue(any("unaccepted change" in error for error in self.validate([self.change, proposal])))

    def test_traceable_change_passes_and_verification_requires_evidence(self):
        self.assertEqual(self.validate([self.change]), [])
        self.change["delivery"] = "verified"
        self.assertTrue(any("verification evidence" in error for error in self.validate([self.change])))
        self.change["verification"] = ["Focused notification scenario passed; recorded outcome."]
        self.assertEqual(self.validate([self.change]), [])
        self.change["spec_ref"]["marker"] = "MISSING-REQUIREMENT"
        self.assertTrue(any("marker not found" in error for error in self.validate([self.change])))
        self.change["spec_ref"]["path"] = "../outside.md"
        self.assertTrue(any("inside the project" in error for error in self.validate([self.change])))


if __name__ == "__main__":
    unittest.main()
