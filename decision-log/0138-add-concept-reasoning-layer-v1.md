# Decision 0138: Add Concept Reasoning Layer v1

Date: 2026-05-05

Status: accepted as synthetic support tooling

## Decision

Add Concept Reasoning Layer v1 on top of Advanced Discovery v2. The layer:

- transforms synthetic clusters into metadata-only behavioral concepts;
- matches new synthetic posts to known concepts conservatively;
- routes novel posts to an ignored new-cluster pool;
- adds concept id, confidence, risk, and novelty features to candidate records;
- feeds concept performance into query generation, scoring, and contextual bandit context.

## First-Principle Rationale

The project is not trying to maximize classification accuracy. It is trying to maximize:

```text
scam-worthy candidates per reviewer hour
```

Clusters identify statistical neighborhoods, but reviewers and research decisions need behavioral concepts. A concept layer makes the loop ask a better question:

```text
Which scam-like behavior pattern produces the highest review-worthy yield per reviewer hour?
```

This supports signal-family learning and reviewer-assist evaluation without expanding raw evidence exposure.

## Scope Boundary

This decision does not authorize:

- real LLM API calls;
- automated Threads or Meta collection;
- crawler expansion;
- raw evidence in git;
- final scam determinations;
- legal fraud determinations;
- enforcement recommendations;
- production detection;
- public warnings or automated takedowns.

The current modules build LLM prompt shapes and use deterministic local policies only. Any future real LLM adapter requires a new decision record, governance review, credential boundary, and controlled evidence plan.

## Artifacts

- `docs/68-concept-reasoning-layer-v1.md`
- `data/concepts/README.md`
- `src/concepts/builder.py`
- `src/concepts/matcher.py`
- `src/pipeline/runner.py`
- `tests/test_concept_reasoning_layer.py`

## Synthetic Demonstration

Command:

```bash
python3 advanced_run.py --rounds 5 --reset
```

Observed sample result on 2026-05-05:

```text
reward_change=+1.018 scam-worthy_candidates_per_reviewer_hour
```

This is a synthetic smoke-test result only. It demonstrates concept feedback and traceable loop mechanics, not real-world discovery performance.

## Decision Implication

Future Reviewer Assist or discovery experiments can use concepts as the bridge between embeddings/clusters and human-readable scam-like behavior hypotheses. The safe next use is labor-savings evaluation: shorter review, clearer signal explanation, conservative novelty routing, and better reviewer-hour allocation under human final judgment.
