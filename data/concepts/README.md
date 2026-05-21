# Concepts

This directory stores local generated concept-layer state for synthetic runs:

- `concept_*.json`
- `concept_evolution.jsonl`
- `match_results.jsonl`
- `reasoning_trace.jsonl`
- `new_cluster_pool.jsonl`

Generated concept state is ignored by git. Concept records must remain metadata-only:
no raw post text, URLs, handles, screenshots, browser artifacts, or controlled-store
paths.

The current implementation is local and synthetic-only. It does not authorize real
LLM API calls, live Threads collection, final scam determinations, or production
detection.

`python3 advanced_run.py --rounds N --reset` clears generated concept state before
the synthetic run while preserving this README.
