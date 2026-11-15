"""Verification suite for the public audit-reporting skill pair."""

from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"
TWO_SKILLS = ("audit-finding-writer", "audit-report-writer")
FORBIDDEN_MARKERS = re.compile(r"\b(TODO|FIXME|TBD|INSERT)\b|\{\{|\}\}|skillfactory:\s*draft")

HANDOFF_FIELDS = (
    "finding_id",
    "title",
    "evidence_status",
    "condition",
    "criteria",
    "cause",
    "cause_status",
    "consequence_realized",
    "consequence_potential",
    "sampling_basis",
    "rating",
    "rating_methodology",
    "accountable_role",
    "target_date",
    "interim_control",
    "closure_evidence",
    "investigation_referral",
    "legal_currency_status",
    "upstream_holds",
)

EVIDENCE_LABELS = (
    "Verified fact",
    "Management representation",
    "Auditor inference",
    "Unverified allegation",
    "Scope limitation",
    "Investigation or protocol referral",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class PublicAuditReportingTests(unittest.TestCase):
    def test_clean_public_provenance_and_no_draft_markers(self):
        for slug in TWO_SKILLS:
            sdir = SKILLS_ROOT / slug
            self.assertTrue((sdir / "SKILL.md").is_file())
            for file in sdir.rglob("*"):
                if file.is_file():
                    text = file.read_text(encoding="utf-8")
                    self.assertIsNone(FORBIDDEN_MARKERS.search(text), f"Draft marker in {file}")
                    self.assertNotIn("inputs/internal-audit-guide", text)
                    self.assertNotIn("ia-audit-", text)

    def test_ui_metadata_and_evals_schema(self):
        for slug in TWO_SKILLS:
            meta = yaml.safe_load((SKILLS_ROOT / slug / "agents" / "ui_metadata.yaml").read_text(encoding="utf-8"))
            self.assertEqual(set(meta.keys()), {"interface"})
            for key in ("display_name", "short_description", "default_prompt"):
                self.assertTrue(isinstance(meta["interface"].get(key), str) and meta["interface"][key].strip())

            payload = json.loads((SKILLS_ROOT / slug / "evals" / "evals.json").read_text(encoding="utf-8"))
            self.assertEqual(set(payload.keys()), {"skill_name", "evals"})
            self.assertEqual(payload["skill_name"], slug)
            for item in payload["evals"]:
                self.assertEqual(set(item.keys()), {"id", "prompt", "expected_output", "files", "expectations"})

    def test_handoff_contract_and_glossary_parity(self):
        ref = (SKILLS_ROOT / "audit-finding-writer" / "references" / "finding-elements-and-guardrails.md").read_text(
            encoding="utf-8"
        )
        for field in HANDOFF_FIELDS:
            self.assertRegex(ref, rf"\b{re.escape(field)}:")

        fw_all = "\n".join(p.read_text(encoding="utf-8") for p in (SKILLS_ROOT / "audit-finding-writer").rglob("*.md"))
        rw_all = "\n".join(p.read_text(encoding="utf-8") for p in (SKILLS_ROOT / "audit-report-writer").rglob("*.md"))
        for label in EVIDENCE_LABELS:
            self.assertIn(label, fw_all)
            self.assertIn(label, rw_all)
        self.assertNotIn("deliberate_act_referral", fw_all)
        self.assertNotIn("11-Part GIAS 15.1", rw_all)

        g1 = SKILLS_ROOT / "audit-finding-writer" / "references" / "vn-banking-terminology.md"
        g2 = SKILLS_ROOT / "audit-report-writer" / "references" / "vn-banking-terminology.md"
        self.assertEqual(sha256(g1), sha256(g2))


if __name__ == "__main__":
    unittest.main()
