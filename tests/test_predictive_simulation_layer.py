from __future__ import annotations

import unittest

from src.discovery.query_llm import generate_queries
from src.prediction.mutation import mutate_concept
from src.prediction.scoring import score_simulation
from src.prediction.simulation import generate_simulated_posts
from src.prediction.validation import track_prediction_validation


class PredictiveSimulationLayerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.concept = {
            "concept_id": "concept_a",
            "concept_name": "Mentor-led authority investment lure",
            "description": "Teacher persona invites guided trading.",
            "attack_pattern": "Claim expertise -> guide action -> move private.",
            "psychological_hook": "authority plus trust",
            "risk_level": "high",
            "dominant_signal": "authority_impersonation",
            "keywords": ["老師", "助理", "帶單"],
            "metrics": {"scam_rate": 0.8, "sample_count": 4},
        }

    def test_mutate_concept_returns_plausible_tagged_variants(self) -> None:
        variants = mutate_concept(self.concept, count=2)

        self.assertEqual(len(variants), 2)
        self.assertTrue(all(variant["variant_id"].startswith("variant_") for variant in variants))
        self.assertTrue(all(variant["simulated_only"] for variant in variants))
        self.assertTrue(all("example_text" in variant for variant in variants))
        self.assertTrue(all(0.0 <= variant["evasion_strength"] <= 1.0 for variant in variants))

    def test_generate_simulated_posts_tags_outputs(self) -> None:
        variants = mutate_concept(self.concept, count=1)
        posts = generate_simulated_posts(variants)

        self.assertEqual(len(posts), 1)
        self.assertTrue(posts[0]["simulated"])
        self.assertEqual(posts[0]["candidate_type"], "simulated")
        self.assertEqual(posts[0]["source"], "predictive_layer")

    def test_score_simulation_uses_similarity_match_and_novelty(self) -> None:
        variant = mutate_concept(self.concept, count=1)[0]
        post = generate_simulated_posts([variant])[0]
        score = score_simulation(post, self.concept)

        self.assertEqual(score["variant_id"], variant["variant_id"])
        self.assertGreaterEqual(score["risk_score"], 0.0)
        self.assertLessEqual(score["risk_score"], 1.0)
        self.assertIn("embedding_similarity", score)
        self.assertIn("novelty_score", score)

    def test_validation_tracks_later_observation_without_raw_claims(self) -> None:
        variant = mutate_concept(self.concept, count=1)[0]
        variant["origin_round"] = 1
        validation = track_prediction_validation(
            [variant],
            [{"candidate_id": "cand_1", "round": 3, "text": variant["example_text"]}],
            current_round=3,
        )

        result = validation["results"][0]
        self.assertTrue(result["observed"])
        self.assertEqual(result["time_lag_rounds"], 2)
        self.assertIn("synthetic observation only", result["validation_note"])

    def test_query_generator_uses_predicted_variants(self) -> None:
        variant = mutate_concept(self.concept, count=1)[0]
        variant["risk_score"] = 0.82
        queries = generate_queries({"predicted_variants": [variant]}, count=2)

        self.assertTrue(any(query["mode"] == "predictive_explore" for query in queries))
        predictive = next(query for query in queries if query["mode"] == "predictive_explore")
        self.assertEqual(predictive["variant_id"], variant["variant_id"])


if __name__ == "__main__":
    unittest.main()
