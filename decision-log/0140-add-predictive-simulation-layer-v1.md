# Decision 0140: Add Predictive Simulation Layer v1

Date: 2026-05-05

Status: accepted as synthetic support tooling

## Decision

Add Predictive Simulation Layer v1. The layer:

- mutates known concepts into plausible subtle variants;
- generates tagged simulated posts;
- scores simulations by embedding similarity, concept matching, novelty, and evasion strength;
- stores prediction logs locally under ignored `data/predictions/`;
- feeds high-risk predicted variants into query generation, candidate features, and contextual bandit context;
- records validation hooks for later observation and time-lag tracking.

## First-Principle Rationale

The goal remains:

```text
scam-worthy candidates per reviewer hour
```

Dynamic intelligence explains what has happened. Predictive simulation asks what subtle variant is worth looking for next. This is a way to spend exploration budget before obvious keywords appear, while preserving human review and governance boundaries.

## Scope Boundary

This decision does not authorize:

- real LLM/API calls;
- automated Threads or Meta collection;
- crawler expansion;
- real-world predictive claims;
- raw evidence in git;
- final scam determinations;
- legal fraud determinations;
- enforcement recommendations;
- public warnings or automated takedowns.

The mutation engine builds LLM prompt shapes but uses deterministic local policies only. Simulated posts are research seeds, not evidence.

## Artifacts

- `docs/70-predictive-simulation-layer-v1.md`
- `data/predictions/README.md`
- `src/prediction/mutation.py`
- `src/prediction/simulation.py`
- `src/prediction/scoring.py`
- `src/prediction/validation.py`
- `src/prediction/logging.py`
- `src/pipeline/runner.py`
- `src/discovery/query_llm.py`
- `src/bandit/contextual_bandit.py`
- `tests/test_predictive_simulation_layer.py`

## Generated Local Outputs

The synthetic runner writes ignored metadata-only or synthetic-tagged files:

- `data/predictions/predicted_variants.jsonl`
- `data/predictions/simulated_posts.jsonl`
- `data/predictions/simulation_scores.jsonl`
- `data/predictions/validation_results.jsonl`

## Synthetic Demonstration

Command:

```bash
python3 advanced_run.py --rounds 5 --reset
```

Observed sample result on 2026-05-05:

```text
reward_change=+1.018 scam-worthy_candidates_per_reviewer_hour
```

This is a synthetic smoke-test result only. It demonstrates predictive feedback and traceable loop mechanics, not real-world discovery performance.

## Decision Implication

Future Reviewer Assist or discovery experiments can use predictive variants as exploration seeds. Any real validation must be governed, aggregate, and human-reviewed.
