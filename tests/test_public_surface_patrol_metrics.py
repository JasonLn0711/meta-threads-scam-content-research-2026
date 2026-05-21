from __future__ import annotations

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from engine.common import write_yaml
from scripts.evaluate_public_surface_patrol_records import build_summary


SCHEMA = {
    "forbidden_keys": [
        "post_text",
        "reply_texts",
        "ocr_text",
        "raw_text",
        "screenshot",
        "screenshot_path",
        "url",
        "urls",
        "handle",
        "token",
    ],
    "forbidden_string_patterns": ["https?://", "www\\.", "@[A-Za-z0-9_]{2,}"],
}


def patrol_record(candidate_id: str, query_ref: str, review_worthy: bool) -> dict:
    return {
        "schema_version": "discovery_candidate_v1",
        "discovery_candidate_id": candidate_id,
        "discovery_round_id": "round-test",
        "source_arm_id": "controlled_browser_run_scoped",
        "source_access_mode": "controlled_browser_run_scoped",
        "source_access_submode": "public_surface_human_reproducible_patrol_v0",
        "query_strategy_id": "query-plan-1",
        "query_signal_family_hints": ["guarantee_or_profit_cue"],
        "surface_type_hints": ["top_level_post"],
        "context_needed": "metadata_only_candidate_triage",
        "human_reproducibility_trace": {
            "route_type": "public_search",
            "query_text_or_query_ref": query_ref,
            "entry_point": "threads_public_search",
            "capture_time": "2026-05-06T00:00:00+08:00",
            "scroll_depth_bucket": "01_10",
            "surface_position_bucket": "visible_window",
            "public_surface_check": True,
            "raw_artifact_ref": "artifact-hash-only",
        },
        "evidence_availability_flags": {
            "has_post_metadata": True,
            "has_reply_metadata": False,
            "has_image_metadata": False,
            "has_ocr_metadata": False,
            "has_link_or_contact_metadata": False,
            "raw_evidence_excluded_from_git": True,
        },
        "dedupe": {"dedupe_key_ref": "dedupe-hash", "near_duplicate_status": "new_candidate"},
        "priority": {
            "priority_score": 0.5,
            "priority_reason_codes": ["guarantee_or_profit_cue"],
            "hard_negative_reason_codes": [],
        },
        "review": {
            "review_status": "reviewed",
            "human_final_label_or_not_reviewable": "scam" if review_worthy else "non_scam",
            "review_worthy": review_worthy,
            "review_time_seconds": 30,
            "second_review_required": False,
        },
    }


class PublicSurfacePatrolMetricsTests(unittest.TestCase):
    def test_build_summary_computes_review_worthy_rate_by_query(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_yaml(root / "candidate-1.yaml", patrol_record("candidate-1", "query-a", True))
            write_yaml(root / "candidate-2.yaml", patrol_record("candidate-2", "query-a", False))
            write_yaml(root / "candidate-3.yaml", patrol_record("candidate-3", "query-b", True))

            summary = build_summary(sorted(root.glob("*.yaml")), SCHEMA)

        self.assertEqual(summary["valid_record_count"], 3)
        self.assertEqual(summary["invalid_record_count"], 0)
        self.assertEqual(summary["review_worthy_count"], 2)
        self.assertEqual(summary["review_worthy_rate"], 0.666667)
        self.assertEqual(summary["human_reproducible_route_rate"], 1.0)
        self.assertEqual(
            {row["query_text_or_query_ref"]: row["review_worthy_rate"] for row in summary["by_query"]},
            {"query-a": 0.5, "query-b": 1.0},
        )

    def test_summary_rejects_raw_url_and_screenshot_path(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            unsafe = patrol_record("candidate-1", "query-a", True)
            unsafe["search_url"] = "https://www.threads.net/search?q=example"
            unsafe["screenshot_local_path"] = "evidence/screenshots/candidate.png"
            write_yaml(root / "unsafe.yaml", unsafe)

            summary = build_summary([root / "unsafe.yaml"], SCHEMA)

        self.assertEqual(summary["valid_record_count"], 0)
        self.assertEqual(summary["invalid_record_count"], 1)
        self.assertEqual(summary["raw_evidence_leakage_incidents"], 1)
        self.assertIn("forbidden raw/sensitive field", summary["errors"][0])


if __name__ == "__main__":
    unittest.main()
