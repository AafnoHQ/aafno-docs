"""Regression tests for mandatory documentation QA failures."""
from pathlib import Path, PurePosixPath
import tempfile
import unittest

import specification_qa as qa


class SpecificationTests(unittest.TestCase):
    def setUp(self):
        self.path = qa.CONCEPTS / "example.md"
        self.active = {"G01-001": ("Example", "Construct a clause.")}
        sections = dict.fromkeys(range(1, 16), "Example section content.")
        sections[1] = (
            "- Catalogue ID: **G01-001**\n- English title: Example.\n- Concept type: Syntax.\n"
            "- Catalogue learning outcome: Construct a clause.\n- Specification status: Draft.\n"
            "- Validation status: Pending.\n- CEFR assignment: Unassigned."
        )
        sections[2] = "- LO1: Identify the clause.\n- LO2: Construct a clause."
        sections[6] = (
            "| Devanagari | Romanisation | English | Context and analysis to review |\n"
            "| --- | --- | --- | --- |\n| म जान्छु। | Ma jaanchhu. | I go. | Routine. |"
        )
        sections[11] = "\n".join(f"| {depth} | LO1, LO2 |" for depth in qa.DEPTH)
        self.text = "\n".join(f"## {n}. {heading}\n\n{sections[n]}\n"
                              for n, heading in enumerate(qa.HEADINGS, 1))

    def check(self, text, expected=None):
        errors = []
        qa.specification(self.path, text, self.active, errors)
        if expected:
            self.assertTrue(any(expected in msg for msg in errors), errors)
        else:
            self.assertEqual(errors, [])

    def test_valid(self):
        self.check(self.text)

    def test_missing_section(self):
        self.check(self.text.replace("## 12. Activity types", ""), "15 numbered")

    def test_unknown_id(self):
        self.check(self.text.replace("G01-001", "G01-999"), "unknown or inactive")

    def test_duplicate_spec(self):
        entries, errors = {}, []
        qa.add_spec(entries, "G01-001", self.path, "", errors)
        qa.add_spec(entries, "G01-001", self.path, "", errors)
        self.assertIn("duplicate canonical", errors[0])

    def test_duplicate_outcome(self):
        self.check(self.text.replace("LO2: Construct", "LO1: Construct"), "must exist and be unique")

    def test_omitted_outcome(self):
        self.check(self.text.replace("LO1, LO2", "LO1"), "omits LO2")

    def test_undefined_outcome(self):
        self.check(self.text.replace("LO1, LO2", "LO1, LO2, LO3"), "undefined outcome LO3")

    def test_missing_representation(self):
        self.check(self.text.replace("Ma jaanchhu.", ""), "empty or malformed")


class RepositoryTests(unittest.TestCase):
    def test_broken_link_and_anchor(self):
        errors = []
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            files = {PurePosixPath("index.md"): "# Home\n[x](missing.md)\n[y](#absent)"}
            qa.check_links(root, files, errors)
        self.assertEqual(len(errors), 2)
        self.assertIn("broken link", errors[0])
        self.assertIn("unresolved anchor", errors[1])

    def test_stale_tracker(self):
        errors = []
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "tracker.md"
            file.write_text("18 authored", encoding="utf-8")
            qa.check_tracker(file, "19 authored", errors)
        self.assertIn("stale tracker", errors[0])

    def test_unapproved_eligibility(self):
        errors = []
        qa.status("G01-001", "- Specification status: Draft\n- CEFR assignment: Unassigned\n"
                  "- Validation status: Pending.", {"publication": "Eligible"}, errors)
        self.assertTrue(any("publication requires" in item for item in errors))
        self.assertTrue(any("draft conflicts" in item for item in errors))

    def test_same_count_different_inventory(self):
        original = {f"G{i:02}-001" for i in range(1, 32)}
        active = original - {"G01-001"} | {"G01-002"}
        manifest = {"expected_active": len(active), "expected_original": len(original),
                    "active_sha256": qa.fingerprint(original), "original_sha256": qa.fingerprint(original),
                    "baseline": "test"}
        errors = []
        qa.check_inventory(active, original, manifest, errors)
        self.assertTrue(any("active ID set differs" in item for item in errors))
