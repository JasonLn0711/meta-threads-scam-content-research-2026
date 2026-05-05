# Predictions

This directory stores local generated predictive-simulation state for synthetic runs:

- `predicted_variants.jsonl`
- `simulated_posts.jsonl`
- `simulation_scores.jsonl`
- `validation_results.jsonl`

Generated prediction state is ignored by git. It is synthetic-only and must stay
tagged as simulation output. It must not be used as evidence, final labels,
legal determination, enforcement input, or real-world prediction without a later
governed validation decision.

The current implementation uses local deterministic policies only. It does not
authorize real LLM API calls, live Threads collection, automated crawling, or
raw evidence in git.
