from __future__ import annotations

import unittest
from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory

from engine.common import CandidateValidationError, candidate_paths, validate_candidate
from engine.discrepancy.detect import detect_discrepancies
from engine.embedding.clustering import cluster_embedding_candidates
from engine.feature_discovery.propose import (
    build_review_queue,
    generate_feature_candidates,
    promote_accepted_features,
)
from engine.feature_discovery.auto_generate import auto_generate_feature_candidates
from engine.exploration.generate import generate_exploration_plan
from engine.exploration.batch import build_exploration_batch
from engine.exploration.convert_intake import (
    build_candidate_record_from_intake_entry,
    build_intake_conversion_report,
)
from engine.exploration.intake import build_candidate_intake, validate_candidate_intake
from engine.sparse.clustering import cluster_sparse_candidates
from engine.sparse.contrast import assign_contrast_lane, build_contrast_aware_scores
from engine.sparse.svs import build_latest_ranking


SPARSE_SCHEMA = {
    "schema_version": "sparse_features_v1",
    "cognitive_load": {
        "base": 1.0,
        "needs_thread_weight": 0.75,
        "second_review_weight": 0.5,
        "dense_feature_threshold": 4,
        "dense_feature_penalty_per_feature": 0.15,
    },
    "features": {
        "誘導聯絡": {"weight": 1.2},
        "保證收益": {"weight": 1.4},
        "社群導流": {"weight": 1.2},
        "情緒操控": {"weight": 1.0},
        "成果展示": {"weight": 1.1},
        "reply_funnel": {"weight": 1.1},
        "needs_thread": {"weight": 0.8},
    },
}

SCHEMA = {
    "required_top_level": ["schema_version", "candidate_id", "batch_id", "sparse_vector", "embedding", "review"],
    "properties": {"review": {"allowed_decisions": ["scam", "non_scam", "uncertain"]}},
    "forbidden_keys": ["post_text", "reply_texts", "ocr_text", "url", "handle", "token"],
    "forbidden_string_patterns": ["https?://", "www\\.", "@[A-Za-z0-9_]{2,}"],
}


def candidate(
    item_id: str,
    features: dict[str, int],
    vector: list[float],
    decision: str = "scam",
    review_time: int = 100,
    second_review: bool = False,
) -> dict:
    all_features = {name: 0 for name in SPARSE_SCHEMA["features"]}
    all_features.update(features)
    return {
        "schema_version": "candidate_record_v2",
        "candidate_id": item_id,
        "batch_id": "batch-test",
        "sparse_vector": {
            "schema_version": "sparse_features_v1",
            "features": all_features,
        },
        "embedding": {
            "model": "synthetic-vector-v1" if vector else "none",
            "dim": len(vector),
            "vector": vector,
        },
        "review": {
            "decision": decision,
            "confidence": 0.75,
            "review_time_seconds": review_time,
            "second_review_required": second_review,
        },
    }


class V2ResearchOperatingSystemTests(unittest.TestCase):
    def test_candidate_validation_rejects_raw_fields_and_urls(self) -> None:
        valid = candidate("cand-1", {"誘導聯絡": 1}, [1.0, 0.0])
        validate_candidate(valid, SCHEMA, SPARSE_SCHEMA)

        raw_field = deepcopy(valid)
        raw_field["post_text"] = "not allowed"
        with self.assertRaises(CandidateValidationError):
            validate_candidate(raw_field, SCHEMA, SPARSE_SCHEMA)

        raw_url = deepcopy(valid)
        raw_url["candidate_id"] = "https://example.invalid/raw"
        with self.assertRaises(CandidateValidationError):
            validate_candidate(raw_url, SCHEMA, SPARSE_SCHEMA)

    def test_candidate_paths_include_nested_batch_records(self) -> None:
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            nested = root / "batch_0004" / "candidate.yaml"
            nested.parent.mkdir(parents=True)
            nested.write_text("schema_version: candidate_record_v2\n", encoding="utf-8")
            self.assertEqual(candidate_paths(root), [nested])

    def test_sparse_svs_and_clustering(self) -> None:
        candidates = [
            candidate("cand-1", {"誘導聯絡": 1, "社群導流": 1, "reply_funnel": 1}, [1.0, 0.0]),
            candidate("cand-2", {"誘導聯絡": 1, "社群導流": 1, "reply_funnel": 1}, [0.0, 1.0], "uncertain"),
            candidate("cand-3", {"保證收益": 1}, [1.0, 0.0]),
        ]
        clusters = cluster_sparse_candidates(candidates, SPARSE_SCHEMA, threshold=0.45)
        self.assertTrue(any(set(cluster["candidate_ids"]) == {"cand-1", "cand-2"} for cluster in clusters["clusters"]))

        ranking = build_latest_ranking(candidates, SPARSE_SCHEMA)
        self.assertEqual(ranking["decision_layer"], "sparse_primary")
        self.assertTrue(ranking["ranked_signals"])

    def test_contrast_aware_scoring_routes_by_sparse_context(self) -> None:
        candidates = [
            candidate(
                "cand-strong",
                {"保證收益": 1, "誘導聯絡": 1, "reply_funnel": 1},
                [],
                "scam",
                35,
                False,
            ),
            candidate(
                "cand-context",
                {"成果展示": 1, "needs_thread": 1, "誘導聯絡": 1},
                [],
                "uncertain",
                60,
                True,
            ),
            candidate("cand-holdout", {"成果展示": 1}, [], "non_scam", 30, False),
        ]

        self.assertEqual(assign_contrast_lane(candidates[0]), "strong_source_priority")
        self.assertEqual(assign_contrast_lane(candidates[1]), "result_display_context_review")
        self.assertEqual(assign_contrast_lane(candidates[2]), "result_display_contrast_holdout")

        scores = build_contrast_aware_scores(candidates, SPARSE_SCHEMA)
        lanes = {row["lane"]: row for row in scores["lane_scores"]}
        self.assertEqual(scores["decision_layer"], "sparse_primary_reviewer_routing")
        self.assertTrue(scores["not_a_classifier"])
        self.assertGreater(lanes["strong_source_priority"]["svs"], lanes["result_display_context_review"]["svs"])
        self.assertEqual(lanes["result_display_context_review"]["uncertainty_rate"], 1.0)
        self.assertFalse(scores["guardrails"]["embedding_used_for_decision"])

    def test_embedding_clusters_skip_missing_vectors(self) -> None:
        candidates = [
            candidate("cand-1", {"誘導聯絡": 1}, [1.0, 0.0]),
            candidate("cand-2", {"保證收益": 1}, [0.99, 0.01]),
            candidate("cand-3", {"情緒操控": 1}, [], "non_scam"),
        ]
        clusters = cluster_embedding_candidates(candidates, threshold=0.85)
        self.assertTrue(clusters["discovery_only"])
        self.assertIn("cand-3", clusters["skipped_missing_embedding"])
        self.assertFalse(clusters["labels_or_decisions_included"])

    def test_discrepancy_detection_finds_both_required_cases(self) -> None:
        candidates = [
            candidate("cand-1", {"誘導聯絡": 1, "社群導流": 1}, [1.0, 0.0]),
            candidate("cand-2", {"保證收益": 1, "成果展示": 1}, [0.99, 0.01]),
            candidate("cand-3", {"誘導聯絡": 1, "社群導流": 1}, [0.0, 1.0], "uncertain", 140, True),
        ]
        sparse_clusters = cluster_sparse_candidates(candidates, SPARSE_SCHEMA, threshold=0.45)
        report = detect_discrepancies(candidates, sparse_clusters, 0.85, 0.25)
        case_types = {case["type"] for case in report["cases"]}
        self.assertIn("missed_pattern", case_types)
        self.assertIn("over_generalization", case_types)

    def test_feature_discovery_requires_acceptance_before_promotion(self) -> None:
        discrepancy_report = {
            "cases": [
                {"case_id": "disc-0001", "type": "missed_pattern"},
                {"case_id": "disc-0002", "type": "over_generalization"},
            ]
        }
        feature_candidates = generate_feature_candidates(discrepancy_report)
        queue = build_review_queue(feature_candidates)
        pending_schema = promote_accepted_features(SPARSE_SCHEMA, feature_candidates, queue)
        self.assertEqual(set(pending_schema["features"]), set(SPARSE_SCHEMA["features"]))

        queue["items"][0]["decision"] = "accepted"
        queue["items"][1]["decision"] = "rejected"
        promoted_schema = promote_accepted_features(SPARSE_SCHEMA, feature_candidates, queue)
        self.assertIn("emergent_embedding_close_sparse_gap", promoted_schema["features"])
        self.assertNotIn("emergent_sparse_cluster_split_signal", promoted_schema["features"])

    def test_auto_generate_filters_to_missed_pattern_groups_of_three(self) -> None:
        candidates = [
            candidate("cand-1", {"誘導聯絡": 1, "reply_funnel": 1}, [1.0, 0.0]),
            candidate("cand-2", {"誘導聯絡": 1, "社群導流": 1}, [0.99, 0.01]),
            candidate("cand-3", {"誘導聯絡": 1, "needs_thread": 1}, [0.98, 0.02], "uncertain", 180, True),
            candidate("cand-4", {"情緒操控": 1}, [0.0, 1.0], "non_scam"),
        ]
        report = {
            "cases": [
                {"case_id": "disc-0001", "type": "missed_pattern", "candidate_ids": ["cand-1", "cand-2"]},
                {"case_id": "disc-0002", "type": "over_generalization", "candidate_ids": ["cand-1", "cand-2", "cand-3"]},
                {"case_id": "disc-0003", "type": "missed_pattern", "candidate_ids": ["cand-1", "cand-2", "cand-3"]},
            ]
        }
        generated = auto_generate_feature_candidates(report, candidates, min_group_size=3)
        self.assertEqual(generated["summary"]["valid_group_count"], 1)
        self.assertEqual(generated["summary"]["skipped_case_count"], 2)
        self.assertTrue(generated["features"])
        self.assertFalse(generated["guardrails"]["features_auto_promoted"])

    def test_exploration_generates_low_coverage_and_outlier_stubs(self) -> None:
        ranking = {
            "ranked_signals": [
                {"signal_id": "保證收益", "reviewed_count": 1, "yield_rate": 1.0, "svs": 0.01},
                {"signal_id": "情緒操控", "reviewed_count": 1, "yield_rate": 0.0, "svs": 0.0},
            ]
        }
        discrepancy = {"cases": []}
        embedding = {
            "clusters": [
                {"cluster_id": "embedding-cluster-0001", "candidate_ids": ["cand-1"]},
                {"cluster_id": "embedding-cluster-0002", "candidate_ids": ["cand-2", "cand-3"]},
            ],
            "nearest_neighbors": [
                {"candidate_id": "cand-1", "neighbors": [{"candidate_id": "cand-2", "cosine_similarity": 0.01}]}
            ],
            "skipped_missing_embedding": ["cand-4"],
        }
        tasks, stubs = generate_exploration_plan(ranking, discrepancy, embedding, stubs_per_task=5)
        self.assertEqual(tasks["summary"]["low_coverage_task_count"], 1)
        self.assertEqual(tasks["summary"]["embedding_outlier_task_count"], 2)
        self.assertEqual(stubs["summary"]["stub_count"], tasks["summary"]["task_count"] * 5)
        self.assertFalse(tasks["guardrails"]["external_systems_accessed"])

    def test_build_exploration_batch_selects_tasks_and_stubs(self) -> None:
        tasks_payload = {
            "tasks": [
                {"task_id": "EXP_0001", "signal_hint": "成果展示"},
                {"task_id": "EXP_0002", "signal_hint": "保證收益"},
                {"task_id": "EXP_0003", "signal_hint": "review_stable_funnel_anchor"},
            ]
        }
        stubs_payload = {
            "candidate_stubs": [
                {"candidate_stub_id": "STUB_0001", "task_id": "EXP_0001", "signal_hint": "成果展示"},
                {"candidate_stub_id": "STUB_0002", "task_id": "EXP_0002", "signal_hint": "保證收益"},
                {"candidate_stub_id": "STUB_0003", "task_id": "EXP_0003", "signal_hint": "review_stable_funnel_anchor"},
            ]
        }
        batch, stub_batch = build_exploration_batch(
            tasks_payload,
            stubs_payload,
            batch_id="batch-test",
            selected_task_ids=["EXP_0001", "EXP_0002"],
        )
        self.assertEqual(batch["candidate_stub_count"], 2)
        self.assertEqual(stub_batch["summary"]["target_signal_hints"], ["保證收益", "成果展示"])
        self.assertFalse(batch["guardrails"]["this_file_authorizes_collection"])

    def test_candidate_intake_builds_pending_entries_without_fabrication(self) -> None:
        batch_plan = {
            "batch_id": "batch-test",
            "before_metrics": {"discrepancy_case_count": 0},
        }
        stub_batch = {
            "batch_id": "batch-test",
            "selected_task_ids": ["EXP_0001"],
            "summary": {"stub_count": 1, "target_signal_hints": ["成果展示"]},
            "candidate_stubs": [
                {
                    "candidate_stub_id": "STUB_0001",
                    "task_id": "EXP_0001",
                    "signal_hint": "成果展示",
                    "expected_behavior": "result_display_anchor",
                }
            ],
        }
        intake = build_candidate_intake(stub_batch, batch_plan)
        self.assertEqual(intake["candidate_count"], 1)
        self.assertEqual(intake["intake_entries"][0]["fill_status"], "pending_manual_review")
        self.assertEqual(intake["intake_entries"][0]["review_metadata_to_fill"]["decision"], "pending")
        self.assertFalse(intake["guardrails"]["candidate_records_fabricated"])
        self.assertEqual(validate_candidate_intake(intake, expected_count=1), [])

    def test_candidate_intake_conversion_blocks_pending_entries(self) -> None:
        intake = {
            "schema_version": "candidate_intake_batch_v1",
            "batch_id": "batch-test",
            "intake_entries": [
                {
                    "intake_id": "INTAKE_0001",
                    "candidate_stub_id": "STUB_0001",
                    "fill_status": "pending_manual_review",
                    "sparse_feature_observations": {name: "pending" for name in SPARSE_SCHEMA["features"]},
                    "review_metadata_to_fill": {
                        "decision": "pending",
                        "confidence": "pending",
                        "review_time_seconds": "pending",
                        "second_review_required": "pending",
                    },
                    "candidate_record_output_target": "data/candidates/batch_test/cand-1.yaml",
                    "completion_gate": {
                        "raw_threads_content_excluded": "pending",
                        "pii_excluded": "pending",
                        "only_structured_metadata": "pending",
                        "human_review_completed": "pending",
                    },
                }
            ],
        }
        report = build_intake_conversion_report(intake, SCHEMA, SPARSE_SCHEMA, repo_root=Path.cwd())
        self.assertEqual(report["summary"]["converted_count"], 0)
        self.assertEqual(report["summary"]["blocked_count"], 1)
        self.assertFalse(report["guardrails"]["candidate_records_written"])
        self.assertIn("fill_status must be completed", report["blocked_entries"][0]["blockers"])

    def test_candidate_intake_conversion_builds_valid_completed_record(self) -> None:
        entry = {
            "intake_id": "INTAKE_0001",
            "candidate_stub_id": "STUB_0001",
            "task_id": "EXP_0001",
            "signal_hint": "保證收益",
            "expected_behavior": "guarantee_or_certainty_anchor",
            "fill_status": "completed",
            "sparse_feature_observations": {name: 0 for name in SPARSE_SCHEMA["features"]},
            "review_metadata_to_fill": {
                "decision": "uncertain",
                "confidence": 0.6,
                "review_time_seconds": 88,
                "second_review_required": False,
            },
            "structured_hints_to_fill": {
                "common_behaviors": ["保證收益"],
                "structural_patterns": ["承諾收益+CTA"],
                "reviewer_signals": ["metadata signal"],
                "hard_negative_contrast": "無收益承諾",
                "metadata_only_note": "metadata_only",
            },
            "candidate_record_output_target": "data/candidates/batch_test/cand-1.yaml",
            "completion_gate": {
                "raw_threads_content_excluded": True,
                "pii_excluded": True,
                "only_structured_metadata": True,
                "human_review_completed": True,
            },
        }
        entry["sparse_feature_observations"]["保證收益"] = 1
        intake = {"schema_version": "candidate_intake_batch_v1", "batch_id": "batch-test", "intake_entries": [entry]}

        record, blockers = build_candidate_record_from_intake_entry(entry, intake, SCHEMA, SPARSE_SCHEMA)
        self.assertEqual(blockers, [])
        validate_candidate(record, SCHEMA, SPARSE_SCHEMA)
        self.assertEqual(record["embedding"], {"model": "none", "dim": 0, "vector": []})
        self.assertEqual(record["structured_hints"]["common_behaviors"], ["保證收益"])

        report = build_intake_conversion_report(intake, SCHEMA, SPARSE_SCHEMA, repo_root=Path.cwd())
        self.assertEqual(report["status"], "ready")
        self.assertEqual(report["summary"]["converted_count"], 1)
        self.assertEqual(report["summary"]["written_count"], 0)
        self.assertFalse(report["converted_records"][0]["written"])


if __name__ == "__main__":
    unittest.main()
