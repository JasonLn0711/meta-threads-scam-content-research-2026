from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from src.discovery.query_llm import generate_queries
from src.intelligence.adversarial import detect_adversarial_patterns
from src.intelligence.graph import build_concept_graph, detect_evolution
from src.intelligence.temporal import track_concept_over_time


class DynamicIntelligenceLayerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.concepts = [
            {
                "concept_id": "concept_a",
                "concept_name": "Mentor-led authority investment lure",
                "description": "Teacher persona invites guided trading.",
                "attack_pattern": "Claim expertise -> guide action -> move private.",
                "psychological_hook": "authority plus trust",
                "risk_level": "high",
                "dominant_signal": "authority_impersonation",
                "derived_from_cluster": "C01",
                "keywords": ["老師", "助理", "帶單"],
                "metrics": {"scam_rate": 0.8, "sample_count": 4},
            },
            {
                "concept_id": "concept_b",
                "concept_name": "Private-channel migration lure",
                "description": "Moves public readers into private chat.",
                "attack_pattern": "Tease value -> request DM -> continue off-platform.",
                "psychological_hook": "exclusivity plus access",
                "risk_level": "medium",
                "dominant_signal": "off_platform_contact",
                "derived_from_cluster": "C02",
                "keywords": ["line", "私訊", "群組"],
                "metrics": {"scam_rate": 0.5, "sample_count": 3},
            },
        ]

    def test_concept_graph_detects_transition_and_co_occurrence(self) -> None:
        candidates = [
            {
                "candidate_id": "cand_1",
                "created_at": "2026-05-05T01:00:00+00:00",
                "features": {"concept_id": "concept_a", "related_concept_ids": ["concept_b"]},
            },
            {
                "candidate_id": "cand_2",
                "created_at": "2026-05-05T01:01:00+00:00",
                "features": {"concept_id": "concept_b"},
            },
        ]
        with tempfile.TemporaryDirectory() as directory:
            graph = build_concept_graph(self.concepts, candidates, output_path=Path(directory) / "graph.yaml")

        edge_types = {edge["type"] for edge in graph["edges"]}
        self.assertIn("transition", edge_types)
        self.assertIn("co_occurrence", edge_types)
        self.assertFalse(graph["raw_content_included"])

    def test_temporal_tracking_computes_growth_and_scam_rate(self) -> None:
        events = [
            {"concept_id": "concept_a", "period": "round_0001", "decision": "scam"},
            {"concept_id": "concept_a", "period": "round_0002", "decision": "scam"},
            {"concept_id": "concept_a", "period": "round_0002", "decision": "non_scam"},
        ]
        with tempfile.TemporaryDirectory() as directory:
            series = track_concept_over_time(self.concepts, events, output_path=Path(directory) / "time.yaml")

        rows = series["concepts"][0]["time_series"]
        self.assertEqual(rows[0]["frequency"], 1)
        self.assertEqual(rows[1]["frequency"], 2)
        self.assertEqual(rows[1]["scam_rate"], 0.5)
        self.assertGreater(rows[1]["growth"], 0)

    def test_evolution_detection_uses_similarity_and_keyword_drift(self) -> None:
        related = [
            self.concepts[0],
            {
                **self.concepts[0],
                "concept_id": "concept_c",
                "keywords": ["專家", "社群", "穩定收益"],
            },
        ]
        edges = detect_evolution(related)

        self.assertTrue(any(edge["type"] == "evolution" for edge in edges))
        self.assertTrue(all("embedding_similarity" in edge for edge in edges))

    def test_adversarial_detection_flags_low_feature_high_scam(self) -> None:
        candidates = [
            {
                "candidate_id": "cand_1",
                "review_decision": "scam",
                "features": {
                    "concept_id": "concept_a",
                    "concept_confidence": 0.1,
                    "is_novel_concept": True,
                    "guaranteed_return": False,
                    "off_platform_contact": False,
                    "impersonation": False,
                    "urgency": False,
                },
            }
        ]
        with tempfile.TemporaryDirectory() as directory:
            result = detect_adversarial_patterns(candidates, output_path=Path(directory) / "adversarial.yaml")

        self.assertEqual(result["summary"]["finding_count"], 2)
        self.assertIn("low_feature_high_scam", result["summary"]["types"])

    def test_query_generator_uses_dynamic_exploration_priorities(self) -> None:
        queries = generate_queries(
            {
                "exploration_priorities": [
                    {
                        "concept_id": "concept_a",
                        "concept_name": "Mentor-led authority investment lure",
                        "dominant_signal": "authority_impersonation",
                        "exploration_priority": 0.9,
                    }
                ]
            },
            count=3,
        )

        self.assertTrue(any(query["mode"] == "dynamic_explore" for query in queries))


if __name__ == "__main__":
    unittest.main()
