# Learning State

This directory stores local closed-loop discovery state:

- `bandit_state.json`
- `metrics.json`
- `rounds.jsonl`
- `advanced_contextual_bandit_state.json`
- `advanced_metrics.json`
- `advanced_rounds.jsonl`

Generated state is ignored by git. It may contain run metadata and controlled-store references, so keep repo-visible reports aggregate or redacted.

Advanced metrics may include query, cluster, concept, dynamic-intelligence, prediction-priority, self-play-priority, and adaptive-policy summaries. The current implementation is synthetic-only and does not authorize real Threads collection, real LLM calls, actionable scam content generation, final scam determinations, enforcement, or production detection.
