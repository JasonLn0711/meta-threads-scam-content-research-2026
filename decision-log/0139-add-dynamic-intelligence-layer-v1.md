# Decision 0139: Add Dynamic Intelligence Layer v1

Date: 2026-05-05

Status: accepted as synthetic support tooling

## Decision

Add Dynamic Intelligence Layer v1 on top of the concept reasoning layer. The layer:

- builds a metadata-only concept graph with transition, co-occurrence, and evolution edges;
- tracks concept frequency, scam rate, and growth over synthetic rounds;
- detects simple evolution edges using local embedding similarity and keyword drift;
- flags adversarial adaptation candidates using low-feature/high-scam, feature-drop, and concept-mismatch heuristics;
- feeds exploration priorities into query generation, candidate scoring, and contextual bandit context.

## First-Principle Rationale

The research goal is still:

```text
scam-worthy candidates per reviewer hour
```

A static concept inventory is not enough because scam-like strategies can combine, mutate, and hide from known features. This layer makes the synthetic loop ask:

```text
Which concepts are central, growing, mutating, or suspicious enough to deserve exploration budget?
```

That supports signal-family learning and labor-efficient reviewer routing without expanding raw-evidence exposure.

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

All outputs are metadata-only synthetic support artifacts.

## Artifacts

- `docs/69-dynamic-intelligence-layer-v1.md`
- `src/intelligence/graph.py`
- `src/intelligence/temporal.py`
- `src/intelligence/adversarial.py`
- `src/intelligence/yaml_store.py`
- `src/pipeline/runner.py`
- `src/discovery/query_llm.py`
- `src/bandit/contextual_bandit.py`
- `tests/test_dynamic_intelligence_layer.py`

## Generated Local Outputs

The synthetic runner writes ignored metadata-only files:

- `data/concept_graph.yaml`
- `data/concept_time_series.yaml`
- `data/adversarial_patterns.yaml`

## Synthetic Demonstration

Command:

```bash
python3 advanced_run.py --rounds 5 --reset
```

Observed sample result on 2026-05-05:

```text
reward_change=+1.018 scam-worthy_candidates_per_reviewer_hour
```

This is a synthetic smoke-test result only. It demonstrates dynamic feedback and traceable loop mechanics, not real-world discovery performance.

## Decision Implication

Future Reviewer Assist or discovery experiments can use dynamic intelligence as an exploration-priority layer. The safe next use is still labor-savings evaluation under human final judgment, not autonomous detection.
