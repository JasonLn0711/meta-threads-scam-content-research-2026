# Concept Reasoning Layer v1

Status: synthetic implementation layer

Date opened: 2026-05-05

## First Principle

Clusters are statistical neighborhoods. Concepts are reviewer-facing behavioral hypotheses.

This layer transforms a cluster such as `C12` into a short, auditable concept such as "private-channel migration lure" or "mentor-led authority investment lure," then uses conservative concept matching to help rank candidates by expected reviewer-hour value.

It is not a final scam detector, legal fraud determination system, external LLM integration, crawler, or production enforcement tool.

## Flow

```text
cluster samples and keywords
-> metadata-only concept generation
-> concept store
-> new post concept matching
-> candidate concept features
-> novelty pool when no conservative match exists
-> query, scoring, and bandit context feedback
```

## Modules

```text
src/concepts/builder.py   cluster-to-concept prompt shape and local concept policy
src/concepts/matcher.py   concept matching, novelty detection, and reasoning logs
src/pipeline/runner.py    integration into advanced synthetic discovery rounds
data/concepts/README.md   generated-state boundary
```

## Concept Builder

`generate_concept(cluster_data)` accepts metadata and synthetic samples:

- `cluster_id`;
- representative sample text for local synthetic analysis only;
- extracted keywords;
- historical `scam_rate`.

It writes concept records through `store_concept()` under ignored `data/concepts/`. Repo-facing concept records do not include raw samples. They include sample hashes, concept name, short description, attack pattern, psychological hook, risk level, derived cluster id, prompt hash, and local backend id.

The current backend is `local_concept_policy_v1`. It builds the prompt an approved LLM adapter would receive, but it does not call an external LLM.

## Concept Matcher

`match_concept(post, concepts)` returns:

- `matched_concept`;
- `confidence`;
- short `reasoning`;
- `is_novel`;
- `risk_level`;
- `post_hash`.

Matching is intentionally conservative. Weak matches become `is_novel: true` and are logged to the ignored new-cluster pool for later clustering. The matcher stores no raw post text in git-facing logs.

## Candidate Integration

Advanced synthetic candidates now include:

- `cluster_id`;
- `concept_id`;
- `concept_name`;
- `concept_confidence`;
- `concept_risk_level`;
- `is_novel_concept`;
- short concept-match reasoning.

Concept confidence and risk affect scoring. Concept confidence, risk, and novelty are also part of the contextual bandit vector.

The dynamic intelligence and predictive simulation layers extend these candidate features with concept graph degree, concept growth, evolution priority, adversarial priority, exploration priority, predicted variant id, evasion type, and predictive risk score.

## Feedback

Concept performance is persisted in ignored `data/learning_state/advanced_metrics.json` and fed back into query generation through `top_concepts`.

This lets the synthetic loop test the research question:

```text
Which behavioral concepts produce more scam-worthy candidates per reviewer hour?
```

## Logging

Generated concept-layer logs are ignored by git:

- `data/concepts/concept_*.json`;
- `data/concepts/concept_evolution.jsonl`;
- `data/concepts/match_results.jsonl`;
- `data/concepts/reasoning_trace.jsonl`;
- `data/concepts/new_cluster_pool.jsonl`.

These logs are metadata-only and synthetic-only. Raw posts, URLs, handles, screenshots, browser artifacts, and controlled-store paths must not be committed.

## Usage

The concept layer runs inside:

```bash
python3 advanced_run.py --rounds 5 --reset
```

Synthetic sample result on 2026-05-05:

```text
reward_trend=14.913 -> 22.723 -> 8.418 -> 8.963 -> 15.931
reward_change=+1.018 scam-worthy_candidates_per_reviewer_hour
```

This demonstrates loop mechanics only. It is not real-world discovery evidence.

## Boundary Rules

- Do not connect real LLM APIs without a new decision and governance review.
- Do not use this layer for final scam labels.
- Do not infer guilt, legal fraud, platform violations, or enforcement actions.
- Prefer conservative matching over broad over-claiming.
- Treat novelty as a future clustering signal, not proof of scam behavior.
- Keep reasoning short, auditable, and evidence-referenced.
