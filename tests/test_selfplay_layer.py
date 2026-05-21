from __future__ import annotations

import unittest

from src.discovery.query_llm import generate_queries
from src.selfplay.adversary import DISALLOWED_TERMS, generate_variant
from src.selfplay.detector import detect
from src.selfplay.judge import compute_rewards
from src.selfplay.runner import run_selfplay_round
from src.selfplay.simulation import generate_simulated_data


class DefensiveSelfPlayLayerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.concept = {
            "concept_id": "concept_a",
            "concept_name": "Mentor-led authority investment lure",
            "description": "Teacher persona invites guided trading.",
            "attack_pattern": "Claim expertise -> guide action -> move private.",
            "psychological_hook": "authority plus trust",
            "risk_level": "high",
            "dominant_signal": "authority_impersonation",
            "keywords": ["teacher", "assistant", "guided"],
            "metrics": {"scam_rate": 0.8, "sample_count": 4},
        }

    def test_generate_variant_is_abstract_and_non_actionable(self) -> None:
        variant = generate_variant(self.concept, difficulty=0.45)

        self.assertTrue(variant["variant_id"].startswith("selfplay_variant_"))
        self.assertTrue(variant["non_actionable"])
        self.assertFalse(variant["actionable_content_included"])
        self.assertEqual(variant["abstraction_level"], "high")
        lowered = variant["abstract_example"].lower()
        self.assertFalse(any(term in lowered for term in DISALLOWED_TERMS))

    def test_generate_simulated_data_tags_safe_output(self) -> None:
        variant = generate_variant(self.concept)
        simulated = generate_simulated_data(variant)

        self.assertEqual(simulated["candidate_type"], "selfplay_simulated")
        self.assertEqual(simulated["source"], "defensive_selfplay")
        self.assertTrue(simulated["simulated"])
        self.assertFalse(simulated["actionable_content_included"])
        self.assertIn("Abstract defensive simulation", simulated["text"])

    def test_detect_returns_confidence_match_and_novelty_fields(self) -> None:
        variant = generate_variant(self.concept, difficulty=0.3)
        simulated = generate_simulated_data(variant)
        detection = detect(simulated, [self.concept], detector_state={"robustness": 0.55, "threshold": 0.58})

        self.assertEqual(detection["variant_id"], variant["variant_id"])
        self.assertGreaterEqual(detection["confidence"], 0.0)
        self.assertLessEqual(detection["confidence"], 1.0)
        self.assertIn("matched_concept", detection)
        self.assertIn("novelty", detection)

    def test_compute_rewards_bounds_adversary_and_detector_rewards(self) -> None:
        variant = generate_variant(self.concept)
        simulated = generate_simulated_data(variant)
        detection = detect(simulated, [self.concept], detector_state={"robustness": 0.45})
        rewards = compute_rewards(variant, detection)

        self.assertAlmostEqual(rewards["adversary_reward"], 1.0 - detection["confidence"], places=6)
        self.assertGreaterEqual(rewards["detector_reward"], 0.0)
        self.assertLessEqual(rewards["detector_reward"], 1.0)

    def test_selfplay_round_updates_priorities_and_state(self) -> None:
        state = {
            "adversary": {"difficulty": 0.32},
            "detector": {"robustness": 0.34, "threshold": 0.58},
            "rounds": [],
            "reward_progression": [],
            "selfplay_priorities": [],
        }
        record = run_selfplay_round(
            round_number=1,
            concepts=[self.concept],
            state=state,
            variants_per_round=1,
            log=False,
        )

        self.assertEqual(record["summary"]["variant_count"], 1)
        self.assertEqual(len(record["state_after_round"]["selfplay_priorities"]), 1)
        self.assertGreater(record["state_after_round"]["detector"]["robustness"], state["detector"]["robustness"])

    def test_query_generator_uses_selfplay_priorities(self) -> None:
        priority = {
            "variant_id": "selfplay_variant_x",
            "origin_concept_id": self.concept["concept_id"],
            "origin_dominant_signal": "authority_impersonation",
            "evasion_characteristic": "authority_signal_drop",
            "search_query": "peer market notes cautious investment discussion",
            "selfplay_reward_signal": 0.62,
            "detector_confidence": 0.38,
            "exploration_priority": 0.71,
        }
        queries = generate_queries({"selfplay_priorities": [priority]}, count=1)

        self.assertEqual(queries[0]["mode"], "selfplay_explore")
        self.assertEqual(queries[0]["selfplay_variant_id"], "selfplay_variant_x")


if __name__ == "__main__":
    unittest.main()
