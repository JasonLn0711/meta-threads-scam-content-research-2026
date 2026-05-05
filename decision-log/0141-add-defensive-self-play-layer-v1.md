# Decision 0141: Add Defensive Self-Play Layer v1

Date: 2026-05-05

Status: accepted as synthetic support tooling

## Decision

Add Defensive Self-Play Layer v1. The layer:

- generates abstract, non-actionable adversarial variants from existing concepts;
- generates safe synthetic self-play data;
- runs a concept-aware detector over simulated data;
- computes adversary and detector rewards;
- updates local self-play state across rounds;
- stores generated logs under ignored `data/selfplay/`;
- feeds hard-to-detect self-play priorities into query generation, candidate features, and contextual bandit context.

## First-Principle Rationale

The goal remains:

```text
scam-worthy candidates per reviewer hour
```

Static discovery reacts to known language. Dynamic intelligence explains observed change. Predictive simulation creates plausible variants. Defensive self-play stress-tests whether the detection scaffold remains useful when those variants become harder and more subtle.

This improves robustness without changing the repo into a production detector or an adversary playbook.

## Scope Boundary

This decision does not authorize:

- actionable scam content generation;
- real LLM/API calls;
- automated Threads or Meta collection;
- crawler expansion;
- raw evidence in git;
- final scam determinations;
- legal fraud determinations;
- enforcement recommendations;
- public warnings or automated takedowns.

The adversary simulator uses deterministic local templates and must output abstract patterns only.

## Artifacts

- `docs/71-defensive-self-play-layer-v1.md`
- `data/selfplay/README.md`
- `selfplay_run.py`
- `src/selfplay/adversary.py`
- `src/selfplay/simulation.py`
- `src/selfplay/detector.py`
- `src/selfplay/judge.py`
- `src/selfplay/runner.py`
- `src/selfplay/logging.py`
- `src/discovery/query_llm.py`
- `src/bandit/contextual_bandit.py`
- `src/pipeline/runner.py`
- `tests/test_selfplay_layer.py`

## Generated Local Outputs

The self-play runner writes ignored synthetic files:

- `data/selfplay/variants.jsonl`
- `data/selfplay/simulated_data.jsonl`
- `data/selfplay/detection_results.jsonl`
- `data/selfplay/rewards.jsonl`
- `data/selfplay/selfplay_state.json`

## Synthetic Demonstration

Command:

```bash
python3 selfplay_run.py --rounds 5 --reset
```

The demonstration output should be read as a smoke test for learning mechanics only. It is not real-world discovery performance evidence.

Observed sample result on 2026-05-05:

```text
detector_reward_change=+0.311
detection_confidence_trend=0.566 -> 0.574 -> 0.582 -> 0.589 -> 0.595
```

## Decision Implication

Future discovery experiments can use self-play priorities as exploration seeds for robustness testing. Any real validation must remain governed, human-reviewed, aggregate, and metadata-safe.
