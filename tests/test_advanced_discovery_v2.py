from __future__ import annotations

import unittest

from src.bandit.contextual_bandit import ContextualBandit
from src.discovery.query_llm import generate_queries
from src.embedding.clustering import assign_cluster, fit_clusters
from src.embedding.encoder import detect_language, encode
from src.pipeline.runner import build_candidate_features, score_advanced_candidate


class AdvancedDiscoveryV2Tests(unittest.TestCase):
    def test_llm_query_generator_returns_structured_explore_and_exploit_queries(self) -> None:
        queries = generate_queries(
            {
                "high_signal_features": ["guaranteed_return", "off_platform_contact"],
                "language_distribution": {"zh-Hant": 1.0},
            },
            count=6,
        )
        self.assertEqual(len(queries), 6)
        self.assertTrue(all("llm_prompt_hash" in query for query in queries))
        self.assertTrue(any(not query["exploration"] for query in queries))
        self.assertTrue(any(query["exploration"] for query in queries))

    def test_embedding_and_clustering_are_deterministic(self) -> None:
        text = "合成樣本：保證收益 投資老師 加 LINE 群"
        self.assertEqual(encode(text), encode(text))
        self.assertEqual(detect_language(text), "zh-Hant")

        embeddings = [
            encode("保證收益 投資老師 加群"),
            encode("穩賺 明牌 私訊"),
            encode("一般投資心得 風險提醒"),
        ]
        model = fit_clusters(embeddings, cluster_count=2)
        assignment = assign_cluster(embeddings[0], model)
        self.assertIn(assignment["cluster_id"], {"C00", "C01"})
        self.assertIn("embedding_distance", assignment)

    def test_advanced_features_include_required_context(self) -> None:
        item = {
            "raw_text": "合成樣本：保證收益 投資老師 加 LINE 群",
            "expected_signal": "guaranteed_return",
            "exploration": False,
        }
        features = build_candidate_features(
            item,
            cluster={"cluster_id": "C00", "embedding_distance": 0.25},
            cluster_scam_rate=0.75,
            concept_match={
                "matched_concept": "concept_test",
                "matched_concept_name": "Guaranteed-return investment lure",
                "dominant_signal": "guaranteed_return",
                "confidence": 0.72,
                "reasoning": "Matches guaranteed-return investment framing.",
                "is_novel": False,
                "risk_level": "high",
            },
        )
        self.assertEqual(features["cluster_id"], "C00")
        self.assertEqual(features["cluster_scam_rate"], 0.75)
        self.assertEqual(features["embedding_distance"], 0.25)
        self.assertEqual(features["language"], "zh-Hant")
        self.assertEqual(features["concept_id"], "concept_test")
        self.assertEqual(features["concept_confidence"], 0.72)
        self.assertFalse(features["is_novel_concept"])
        self.assertGreater(score_advanced_candidate(features), 0.5)

    def test_contextual_bandit_updates_toward_rewarded_context(self) -> None:
        bandit = ContextualBandit(alpha=0.1)
        good = {
            "candidate_id": "good",
            "cluster_scam_rate": 0.8,
            "embedding_distance": 0.1,
            "language": "zh-Hant",
            "concept_confidence": 0.8,
            "concept_risk_level": "high",
            "is_novel_concept": False,
            "expected_signal": "guaranteed_return",
            "exploration": False,
        }
        weak = {
            "candidate_id": "weak",
            "cluster_scam_rate": 0.0,
            "embedding_distance": 1.2,
            "language": "zh-Hant",
            "concept_confidence": 0.0,
            "concept_risk_level": "unknown",
            "is_novel_concept": True,
            "expected_signal": "hard_negative_warning",
            "exploration": True,
        }

        for _ in range(3):
            bandit.update(good, reward=20.0)
            bandit.update(weak, reward=0.0)

        selected = bandit.select([weak, good])
        self.assertEqual(selected["candidate_id"], "good")
        self.assertGreater(selected["bandit_score"]["ucb_score"], 0.0)


if __name__ == "__main__":
    unittest.main()
