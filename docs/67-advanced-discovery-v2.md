# Advanced Discovery v2

Status: synthetic implementation layer

Date opened: 2026-05-05

## First Principle

This layer still optimizes:

```text
scam-worthy candidates per reviewer hour
```

It upgrades the previous closed-loop simulation from fixed query arms and keyword features to context-aware query generation, deterministic embeddings, semantic clustering, and a LinUCB-style contextual bandit.

It is not a production detector, crawler, LLM service integration, legal fraud determination system, or automated enforcement tool.

## Loop

```text
history context
-> prompt-shaped query generation
-> synthetic source connector
-> Evidence Layer ingest
-> deterministic embedding
-> local clustering
-> cluster-to-concept reasoning layer
-> dynamic intelligence graph and temporal signals
-> predictive simulation layer
-> metadata-only contextual features
-> LinUCB candidate selection
-> simulated reviewer feedback
-> query, cluster, concept, and reward logs
-> next round context
```

## Modules

```text
src/discovery/query_llm.py       prompt builder plus local structured query generator
src/embedding/encoder.py         deterministic hash-vector encoder
src/embedding/clustering.py      dependency-light KMeans-style clustering
src/concepts/builder.py          metadata-only cluster-to-concept builder
src/concepts/matcher.py          conservative concept matcher and novelty logger
src/intelligence/                graph, temporal, evolution, and adversarial heuristics
src/prediction/                  mutation, simulation, risk scoring, and validation hooks
src/bandit/contextual_bandit.py  LinUCB-style contextual bandit
src/pipeline/runner.py           advanced synthetic loop orchestration and persistence
advanced_run.py                  CLI
```

## LLM Boundary

`query_llm.py` builds the exact prompt shape an approved LLM adapter would receive, but the current implementation uses a deterministic local prompt policy. This keeps the repo runnable without credentials, network calls, or external API use.

A future real LLM adapter requires a new decision record and governance review before it may use external services, secrets, live source data, or controlled evidence.

## Embedding And Clustering Boundary

The encoder is a deterministic local hash-vector encoder. It is useful for loop mechanics and traceability, not for claims about real semantic model quality.

The clustering implementation is intentionally small:

- no sklearn dependency;
- no deep learning runtime;
- deterministic center initialization;
- cluster ids, distances, and counts are logged for auditability.

Candidate features include:

- `cluster_id`;
- `cluster_scam_rate`;
- `embedding_distance`;
- `language`;
- `concept_id`;
- `concept_confidence`;
- `concept_risk_level`;
- `is_novel_concept`;
- `concept_graph_degree`;
- `concept_growth`;
- `evolution_priority`;
- `adversarial_priority`;
- `exploration_priority`;
- `predicted_variant_id`;
- `prediction_evasion_type`;
- `predictive_risk_score`;
- query `expected_signal`;
- exploration/exploitation mode.

No raw text is stored in repo-visible candidate records.

## Contextual Bandit

The bandit uses a simple LinUCB-style score:

```text
score = expected_reward + alpha * uncertainty
```

Context features include cluster scam rate, inverse embedding distance, language, exploration flag, concept confidence, concept risk, novelty flag, dynamic-intelligence priorities, predictive risk, and expected-signal indicators. The bandit is updated from simulated reviewer outcomes using:

```text
reward = scam_count / reviewer_hours
```

For per-candidate updates, a scam decision receives `1 / reviewer_hours`; non-scam and uncertain decisions receive `0`. This is a ranking and resource-allocation policy, not a classifier.

## Logging

Generated local state is ignored by git under `data/learning_state/`:

- `advanced_contextual_bandit_state.json`;
- `advanced_metrics.json`;
- `advanced_rounds.jsonl`.

Logs track:

- query performance;
- cluster performance;
- concept performance;
- reward trends;
- selected metadata-only candidates;
- contextual bandit state.

## Usage

```bash
python3 advanced_run.py --rounds 5 --reset
```

Synthetic sample result on 2026-05-05:

```text
reward_trend=14.913 -> 22.723 -> 8.418 -> 8.963 -> 15.931
reward_change=+1.018 scam-worthy_candidates_per_reviewer_hour
```

This result demonstrates loop mechanics only. It is not real-world performance evidence.

## Boundary Rules

- Do not connect real LLM APIs without a new decision and credential boundary.
- Do not use external source APIs or automated Threads collection.
- Do not store raw content, URLs, handles, screenshots, browser artifacts, or controlled-store paths in git.
- Do not treat clusters, embeddings, or bandit scores as scam labels.
- Do not replace human final judgment.
- Use this layer to test whether context-aware routing can reduce reviewer-hour waste before any governed real experiment is considered.
