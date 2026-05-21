from __future__ import annotations

import json
import unittest

from src.concepts.builder import generate_concept
from src.concepts.matcher import match_concept


class ConceptReasoningLayerTests(unittest.TestCase):
    def test_generate_concept_is_metadata_only(self) -> None:
        sample = "合成樣本：投資老師保證收益，私訊加入 LINE 群"
        concept = generate_concept(
            {
                "cluster_id": "C12",
                "samples": [sample],
                "keywords": ["投資老師", "保證", "line", "私訊"],
                "scam_rate": 0.8,
            }
        )

        self.assertEqual(concept["schema_version"], "concept_v1")
        self.assertTrue(concept["concept_id"].startswith("concept_"))
        self.assertEqual(concept["risk_level"], "high")
        self.assertFalse(concept["raw_samples_included"])
        self.assertNotIn(sample, json.dumps(concept, ensure_ascii=False))

    def test_match_concept_returns_conservative_structured_match(self) -> None:
        concept = generate_concept(
            {
                "cluster_id": "C12",
                "samples": ["合成樣本：保證收益 私訊 LINE 群"],
                "keywords": ["保證", "收益", "line", "私訊"],
                "scam_rate": 0.7,
            }
        )
        result = match_concept("合成樣本：保證收益，請私訊加入 LINE 群", [concept])

        self.assertEqual(result["matched_concept"], concept["concept_id"])
        self.assertGreaterEqual(result["confidence"], 0.52)
        self.assertFalse(result["is_novel"])
        self.assertFalse(result["raw_post_included"])
        self.assertLessEqual(len(result["reasoning"]), 80)

    def test_match_concept_marks_unknown_pool_when_no_concepts_exist(self) -> None:
        result = match_concept("合成樣本：新的陌生投資敘事", [])

        self.assertIsNone(result["matched_concept"])
        self.assertEqual(result["confidence"], 0.0)
        self.assertTrue(result["is_novel"])
        self.assertFalse(result["raw_post_included"])


if __name__ == "__main__":
    unittest.main()
