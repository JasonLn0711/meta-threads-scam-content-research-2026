# Decision 0137: Add Advanced Discovery v2

Date: 2026-05-05

Status: accepted as synthetic support tooling

## Decision

Add Advanced Discovery v2 as a synthetic support layer that upgrades the closed-loop discovery simulation with:

- prompt-shaped query generation;
- deterministic local embeddings;
- dependency-light semantic clustering;
- metadata-only candidate context features;
- LinUCB-style contextual bandit selection;
- query, cluster, and reward trend logging.

## First-Principle Rationale

The scarce resource is reviewer time. The project should learn which language patterns, semantic neighborhoods, and query strategies produce scam-worthy candidates per reviewer hour.

Fixed query arms are useful for a first loop, but they are too coarse for the real research question. Advanced Discovery v2 moves the simulation closer to:

```text
reward = f(query context, semantic cluster, reviewer burden)
```

without introducing external APIs, heavy ML dependencies, or raw evidence exposure.

## Scope Boundary

This decision does not authorize:

- real LLM API calls;
- external API credentials;
- automated Threads or Meta collection;
- live source crawling;
- raw evidence in git;
- final scam determinations;
- legal fraud determinations;
- enforcement recommendations;
- production detection.

`query_llm.py` builds a prompt and returns structured queries through a deterministic local policy only. The embedding model is a local hash-vector encoder for traceable simulation, not a real semantic model claim.

## Artifacts

- `docs/67-advanced-discovery-v2.md`
- `advanced_run.py`
- `src/discovery/query_llm.py`
- `src/embedding/encoder.py`
- `src/embedding/clustering.py`
- `src/bandit/contextual_bandit.py`
- `src/pipeline/runner.py`
- `tests/test_advanced_discovery_v2.py`

## Synthetic Demonstration

Command:

```bash
python3 advanced_run.py --rounds 5 --reset
```

Observed sample result on 2026-05-05:

```text
reward_change=+1.018 scam-worthy_candidates_per_reviewer_hour
```

This is a synthetic smoke-test result only. It demonstrates traceability and loop mechanics, not real-world discovery performance.

## Decision Implication

Future Reviewer Assist or discovery experiments can use this layer to reason about context-aware reviewer-hour allocation. Any movement from local synthetic simulation to real LLMs, real embeddings, external APIs, or governed live evidence requires a new decision record and governance review.
