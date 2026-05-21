"""Small epsilon-greedy bandit for query-arm selection."""

from __future__ import annotations

import json
import random
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from src.discovery.query_generator import known_query_ids


@dataclass
class Bandit:
    arms: dict[str, dict[str, float | int]] = field(default_factory=dict)
    epsilon: float = 0.2
    seed: int = 20260505

    def __post_init__(self) -> None:
        for query_id in known_query_ids():
            self.arms.setdefault(query_id, {"trials": 0, "average_reward": 0.0, "last_reward": 0.0})
        self._rng = random.Random(self.seed + sum(int(arm.get("trials", 0)) for arm in self.arms.values()))

    def update(self, query_id: str, reward: float) -> None:
        arm = self.arms.setdefault(query_id, {"trials": 0, "average_reward": 0.0, "last_reward": 0.0})
        trials = int(arm.get("trials", 0)) + 1
        previous_average = float(arm.get("average_reward", 0.0))
        average_reward = previous_average + ((float(reward) - previous_average) / trials)
        arm["trials"] = trials
        arm["average_reward"] = round(average_reward, 6)
        arm["last_reward"] = round(float(reward), 6)

    def select_queries(self, count: int = 3) -> list[str]:
        query_ids = known_query_ids()
        selected: list[str] = []

        untried = [query_id for query_id in query_ids if int(self.arms[query_id].get("trials", 0)) == 0]
        for query_id in untried[:count]:
            selected.append(query_id)

        while len(selected) < count:
            available = [query_id for query_id in query_ids if query_id not in selected]
            if not available:
                break
            if self._rng.random() < self.epsilon:
                selected.append(self._rng.choice(available))
                continue
            selected.append(
                max(
                    available,
                    key=lambda query_id: (
                        float(self.arms[query_id].get("average_reward", 0.0)),
                        -query_ids.index(query_id),
                    ),
                )
            )
        return selected

    def to_state(self) -> dict[str, Any]:
        return {
            "schema_version": "bandit_state_v1",
            "policy": "epsilon_greedy",
            "epsilon": self.epsilon,
            "seed": self.seed,
            "arms": self.arms,
        }

    @classmethod
    def from_state(cls, state: dict[str, Any] | None, *, epsilon: float = 0.2, seed: int = 20260505) -> "Bandit":
        if not state:
            return cls(epsilon=epsilon, seed=seed)
        return cls(
            arms=dict(state.get("arms", {})),
            epsilon=float(state.get("epsilon", epsilon)),
            seed=int(state.get("seed", seed)),
        )

    @classmethod
    def load(cls, path: Path, *, epsilon: float = 0.2, seed: int = 20260505, reset: bool = False) -> "Bandit":
        if reset or not path.exists():
            return cls(epsilon=epsilon, seed=seed)
        return cls.from_state(json.loads(path.read_text(encoding="utf-8")), epsilon=epsilon, seed=seed)

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_state(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
