"""Small LinUCB-style contextual bandit with standard-library matrix math."""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


FEATURE_NAMES = [
    "bias",
    "cluster_scam_rate",
    "embedding_distance_inverse",
    "language_zh_hant",
    "language_en",
    "is_exploration",
    "concept_confidence",
    "concept_risk_high",
    "concept_risk_medium",
    "is_novel_concept",
    "concept_graph_degree",
    "concept_growth",
    "evolution_priority",
    "adversarial_priority",
    "exploration_priority",
    "predictive_risk_score",
    "is_predictive_query",
    "selfplay_reward_signal",
    "is_selfplay_query",
    "signal_guaranteed_return",
    "signal_off_platform_contact",
    "signal_authority_impersonation",
    "signal_urgency",
    "signal_hard_negative_warning",
]


@dataclass
class ContextualBandit:
    alpha: float = 0.8
    feature_names: list[str] = field(default_factory=lambda: list(FEATURE_NAMES))
    a_matrix: list[list[float]] | None = None
    b_vector: list[float] | None = None
    updates: int = 0

    def __post_init__(self) -> None:
        dim = len(self.feature_names)
        if self.a_matrix is None:
            self.a_matrix = [[1.0 if row == col else 0.0 for col in range(dim)] for row in range(dim)]
        if self.b_vector is None:
            self.b_vector = [0.0] * dim

    def select(self, context_list: list[dict[str, Any]]) -> dict[str, Any]:
        """Return the context with the highest LinUCB score."""
        if not context_list:
            raise ValueError("select requires at least one context")
        scored = [(self.score(context), context) for context in context_list]
        score, selected = max(scored, key=lambda item: (item[0]["ucb_score"], item[1].get("candidate_id", "")))
        result = dict(selected)
        result["bandit_score"] = score
        return result

    def score(self, context: dict[str, Any]) -> dict[str, float]:
        x = context_to_vector(context, self.feature_names)
        inverse = _invert_matrix(self.a_matrix or [])
        theta = _matrix_vector_multiply(inverse, self.b_vector or [])
        mean = _dot(theta, x)
        uncertainty = math.sqrt(max(0.0, _dot(x, _matrix_vector_multiply(inverse, x))))
        return {
            "mean_reward": round(mean, 6),
            "uncertainty": round(uncertainty, 6),
            "ucb_score": round(mean + (self.alpha * uncertainty), 6),
        }

    def update(self, context: dict[str, Any], reward: float) -> None:
        """Update the linear model with one observed context reward."""
        x = context_to_vector(context, self.feature_names)
        for row in range(len(x)):
            for col in range(len(x)):
                self.a_matrix[row][col] += x[row] * x[col]
            self.b_vector[row] += float(reward) * x[row]
        self.updates += 1

    def to_state(self) -> dict[str, Any]:
        return {
            "schema_version": "contextual_bandit_v1",
            "policy": "linucb",
            "alpha": self.alpha,
            "feature_names": self.feature_names,
            "a_matrix": self.a_matrix,
            "b_vector": self.b_vector,
            "updates": self.updates,
        }

    @classmethod
    def from_state(cls, state: dict[str, Any] | None, *, alpha: float = 0.8) -> "ContextualBandit":
        if not state:
            return cls(alpha=alpha)
        state = _migrate_state_features(state)
        return cls(
            alpha=float(state.get("alpha", alpha)),
            feature_names=list(state.get("feature_names", FEATURE_NAMES)),
            a_matrix=state.get("a_matrix"),
            b_vector=state.get("b_vector"),
            updates=int(state.get("updates", 0)),
        )

    @classmethod
    def load(cls, path: Path, *, alpha: float = 0.8, reset: bool = False) -> "ContextualBandit":
        if reset or not path.exists():
            return cls(alpha=alpha)
        return cls.from_state(json.loads(path.read_text(encoding="utf-8")), alpha=alpha)

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_state(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def context_to_vector(context: dict[str, Any], feature_names: list[str] | None = None) -> list[float]:
    feature_names = feature_names or FEATURE_NAMES
    signal = str(context.get("expected_signal", ""))
    language = str(context.get("language", ""))
    distance = float(context.get("embedding_distance", 1.0) or 1.0)
    values = {
        "bias": 1.0,
        "cluster_scam_rate": float(context.get("cluster_scam_rate", 0.0) or 0.0),
        "embedding_distance_inverse": 1.0 / (1.0 + max(0.0, distance)),
        "language_zh_hant": 1.0 if language == "zh-Hant" else 0.0,
        "language_en": 1.0 if language == "en" else 0.0,
        "is_exploration": 1.0 if bool(context.get("exploration")) else 0.0,
        "concept_confidence": float(context.get("concept_confidence", 0.0) or 0.0),
        "concept_risk_high": 1.0 if context.get("concept_risk_level") == "high" else 0.0,
        "concept_risk_medium": 1.0 if context.get("concept_risk_level") == "medium" else 0.0,
        "is_novel_concept": 1.0 if bool(context.get("is_novel_concept")) else 0.0,
        "concept_graph_degree": float(context.get("concept_graph_degree", 0.0) or 0.0),
        "concept_growth": float(context.get("concept_growth", 0.0) or 0.0),
        "evolution_priority": float(context.get("evolution_priority", 0.0) or 0.0),
        "adversarial_priority": float(context.get("adversarial_priority", 0.0) or 0.0),
        "exploration_priority": float(context.get("exploration_priority", 0.0) or 0.0),
        "predictive_risk_score": float(context.get("predictive_risk_score", 0.0) or 0.0),
        "is_predictive_query": 1.0 if bool(context.get("predicted_variant_id")) else 0.0,
        "selfplay_reward_signal": float(context.get("selfplay_reward_signal", 0.0) or 0.0),
        "is_selfplay_query": 1.0 if bool(context.get("selfplay_variant_id")) else 0.0,
        "signal_guaranteed_return": 1.0 if signal == "guaranteed_return" else 0.0,
        "signal_off_platform_contact": 1.0 if signal == "off_platform_contact" else 0.0,
        "signal_authority_impersonation": 1.0 if signal == "authority_impersonation" else 0.0,
        "signal_urgency": 1.0 if signal == "urgency" else 0.0,
        "signal_hard_negative_warning": 1.0 if signal == "hard_negative_warning" else 0.0,
    }
    return [float(values[name]) for name in feature_names]


def _migrate_state_features(state: dict[str, Any]) -> dict[str, Any]:
    old_names = list(state.get("feature_names", FEATURE_NAMES))
    if old_names == FEATURE_NAMES:
        return state

    old_a = state.get("a_matrix") or []
    old_b = state.get("b_vector") or []
    new_size = len(FEATURE_NAMES)
    new_a = [[1.0 if row == col else 0.0 for col in range(new_size)] for row in range(new_size)]
    new_b = [0.0] * new_size
    index_by_name = {name: index for index, name in enumerate(FEATURE_NAMES)}

    for old_row, row_name in enumerate(old_names):
        if row_name not in index_by_name:
            continue
        new_row = index_by_name[row_name]
        if old_row < len(old_b):
            new_b[new_row] = float(old_b[old_row])
        for old_col, col_name in enumerate(old_names):
            if col_name not in index_by_name:
                continue
            new_col = index_by_name[col_name]
            if old_row < len(old_a) and old_col < len(old_a[old_row]):
                new_a[new_row][new_col] = float(old_a[old_row][old_col])

    migrated = dict(state)
    migrated["feature_names"] = list(FEATURE_NAMES)
    migrated["a_matrix"] = new_a
    migrated["b_vector"] = new_b
    return migrated


def _dot(left: list[float], right: list[float]) -> float:
    return sum(a * b for a, b in zip(left, right))


def _matrix_vector_multiply(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return [_dot(row, vector) for row in matrix]


def _invert_matrix(matrix: list[list[float]]) -> list[list[float]]:
    n = len(matrix)
    augmented = [
        [float(matrix[row][col]) for col in range(n)] + [1.0 if row == col else 0.0 for col in range(n)]
        for row in range(n)
    ]

    for col in range(n):
        pivot_row = max(range(col, n), key=lambda row: abs(augmented[row][col]))
        if abs(augmented[pivot_row][col]) < 1e-12:
            raise ValueError("matrix is not invertible")
        if pivot_row != col:
            augmented[col], augmented[pivot_row] = augmented[pivot_row], augmented[col]
        pivot = augmented[col][col]
        augmented[col] = [value / pivot for value in augmented[col]]
        for row in range(n):
            if row == col:
                continue
            factor = augmented[row][col]
            augmented[row] = [value - factor * base for value, base in zip(augmented[row], augmented[col])]

    return [row[n:] for row in augmented]
