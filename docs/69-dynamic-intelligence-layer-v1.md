# Dynamic Intelligence Layer v1

Status: synthetic implementation layer

Date opened: 2026-05-05

## First Principle

Scam-like strategies are dynamic. They combine, mutate, and adapt to the review signals used against them.

This layer models relationships, time movement, evolution, and adversarial adaptation so the synthetic discovery loop can prioritize exploration by expected reviewer-hour value, not by static keyword confidence.

It is not a production detector, crawler, enforcement system, legal fraud determination system, or real-world predictive claim.

## Flow

```text
concepts and metadata-only candidates
-> concept graph
-> temporal concept tracking
-> evolution edges
-> adversarial adaptation findings
-> exploration priorities
-> predictive simulation seeds
-> query generation, scoring, and bandit context
```

## Modules

```text
src/intelligence/graph.py       concept graph plus evolution edges
src/intelligence/temporal.py    concept frequency, scam-rate, and growth tracking
src/intelligence/adversarial.py low-feature/high-scam and mismatch heuristics
src/intelligence/yaml_store.py  tiny deterministic YAML writer
src/pipeline/runner.py          integration with advanced synthetic rounds
```

## Concept Graph

`build_concept_graph(concepts, candidates)` creates metadata-only nodes and edges.

Edges include:

- `transition`: sequential movement between primary concepts in candidate order;
- `co_occurrence`: multiple concept matches on the same metadata-only candidate;
- `evolution`: semantic proximity plus keyword drift between concepts.

Generated output is local and ignored:

```text
data/concept_graph.yaml
```

## Temporal Tracking

`track_concept_over_time(concepts, timestamps)` computes:

- frequency;
- reviewed count;
- scam count;
- scam rate;
- growth.

The synthetic runner uses round buckets such as `round_0002`. A governed real experiment would need an explicit decision before using real timestamps or controlled evidence.

Generated output is local and ignored:

```text
data/concept_time_series.yaml
```

## Evolution Detection

`detect_evolution(concepts)` uses:

- deterministic local hash embeddings over concept metadata;
- cosine similarity;
- keyword drift.

It outputs reviewable evolution edges with short reasons. These edges are hypotheses for exploration, not proof of a real adversarial mutation.

## Adversarial Detection

`detect_adversarial_patterns(candidates)` flags:

- `low_feature_high_scam`: high-value simulated review outcome with weak explicit feature surface;
- `feature_drop_anomaly`: feature strength drops inside a concept while scam outcomes remain present;
- `concept_mismatch`: high-value outcome with novelty routing or signal mismatch.

Generated output is local and ignored:

```text
data/adversarial_patterns.yaml
```

## Integration

Dynamic intelligence feeds the next round through:

- `exploration_priorities` in query generation;
- `concept_graph_degree`, `concept_growth`, `evolution_priority`, `adversarial_priority`, and `exploration_priority` in candidate features;
- the same fields in contextual bandit vectors.

The purpose is to spend more reviewer attention on concepts that appear central, growing, mutating, or adversarially suspicious.

Predictive Simulation Layer v1 uses these priorities to mutate concepts, generate synthetic posts, score future variants, and send high-risk variants back into query generation.

## Usage

```bash
python3 advanced_run.py --rounds 5 --reset
```

Synthetic sample result on 2026-05-05:

```text
reward_trend=14.913 -> 22.723 -> 8.418 -> 8.963 -> 15.931
reward_change=+1.018 scam-worthy_candidates_per_reviewer_hour
```

This demonstrates loop mechanics only. It is not real-world performance evidence.

## Boundary Rules

- Do not treat graph edges as real-world attack paths without governed evidence.
- Do not treat growth or adversarial flags as labels.
- Do not connect real LLM APIs, source APIs, or live Threads collection without a new decision and governance review.
- Keep all dynamic intelligence outputs metadata-only.
- Preserve human final judgment and uncertainty labels.
