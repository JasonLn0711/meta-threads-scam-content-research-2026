from __future__ import annotations

import unittest

from src.policy.deployment import run_deployment_loop
from src.policy.evaluation import evaluate_policy
from src.policy.feedback import collect_feedback
from src.policy.policy import policy
from src.policy.training import train_policy, update_policy


class AdaptivePolicyLayerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.context = {
            "schema_version": "adaptive_policy_context_v1",
            "context_id": "ctx_1",
            "source": "unit_test",
            "queries": [
                {
                    "query_id": "q_1",
                    "query_string": "metadata-only query seed",
                    "strategy": "selfplay_platform_reference_drop",
                    "expected_signal": "off_platform_contact",
                    "selfplay_reward_signal": 0.6,
                    "exploration_priority": 0.5,
                }
            ],
            "candidates": [
                {
                    "candidate_id": "cand_1",
                    "score": 0.72,
                    "features": {
                        "concept_confidence": 0.68,
                        "predictive_risk_score": 0.4,
                        "selfplay_reward_signal": 0.35,
                    },
                    "raw_content_included": False,
                }
            ],
            "raw_source_included": False,
        }

    def test_policy_shadow_mode_has_no_workflow_impact(self) -> None:
        action = policy(self.context, mode="shadow")

        self.assertEqual(action["mode"], "shadow")
        self.assertEqual(action["deployment_effect"], "record_only_no_workflow_impact")
        self.assertEqual(action["query_selection"][0]["policy_action"], "record_only")
        self.assertTrue(action["guardrails"]["human_final_judgment_required"])

    def test_policy_partial_mode_only_routes_metadata_for_human_review(self) -> None:
        action = policy(self.context, mode="partial")

        self.assertEqual(action["mode"], "partial")
        self.assertTrue(action["candidate_prioritization"][0]["human_final_decision_required"])
        self.assertFalse(action["candidate_prioritization"][0]["raw_content_included"])

    def test_collect_feedback_computes_reviewer_hour_reward(self) -> None:
        action = policy(self.context, mode="assist")
        feedback = collect_feedback(
            action,
            human_labels=[
                {"decision": "scam", "review_minutes": 2.0},
                {"decision": "non_scam", "review_minutes": 1.5},
            ],
            delayed_outcomes=[{"observed": True, "time_lag_rounds": 2}],
        )

        self.assertEqual(feedback["human_feedback"]["scam_count"], 1)
        self.assertGreater(feedback["human_feedback"]["reward_per_reviewer_hour"], 0.0)
        self.assertGreaterEqual(feedback["reward"], 0.0)
        self.assertLessEqual(feedback["reward"], 1.0)

    def test_train_policy_updates_weights_with_bounds(self) -> None:
        action = policy(self.context, mode="assist")
        logs = [
            {
                "action": action,
                "outcome": {"reward": 0.8},
                "reward": 0.8,
            }
        ]
        trained = train_policy(logs, learning_rate=0.2, max_weight_delta=0.03)

        self.assertEqual(trained["policy_version"], 2)
        self.assertLessEqual(trained["largest_weight_delta"], 0.03)
        self.assertAlmostEqual(sum(trained["weights"].values()), 1.0, places=5)

    def test_update_policy_records_safe_update_summary(self) -> None:
        action = policy(self.context, mode="assist")
        historical = [{"action": action, "outcome": {"reward": 0.9}, "reward": 0.9}]
        recent = [{"action": action, "outcome": {"reward": 0.2}, "reward": 0.2}]
        updated = update_policy(recent, historical_logs=historical, persist=False)

        self.assertIn("safe_update", updated)
        self.assertEqual(updated["safe_update"]["overfit_guard"], "reduced_rate_on_reward_drop")

    def test_evaluate_policy_reports_core_metrics(self) -> None:
        action = policy(self.context, mode="shadow")
        feedback = collect_feedback(
            action,
            human_labels=[{"decision": "scam", "review_minutes": 3.0}],
            delayed_outcomes=[{"observed": True, "time_lag_rounds": 1}],
        )
        report = evaluate_policy([{"action": action, "outcome": feedback}])

        self.assertEqual(report["decision_count"], 1)
        self.assertGreater(report["reward_per_reviewer_hour"], 0.0)
        self.assertEqual(report["detection_latency_rounds"], 1.0)
        self.assertIn("robustness", report)

    def test_run_deployment_loop_returns_records_and_report(self) -> None:
        run = run_deployment_loop([self.context], mode="shadow", log=False)

        self.assertEqual(run["decision_count"], 1)
        self.assertEqual(run["records"][0]["action"]["mode"], "shadow")
        self.assertIn("reward_per_reviewer_hour", run["evaluation"])


if __name__ == "__main__":
    unittest.main()
