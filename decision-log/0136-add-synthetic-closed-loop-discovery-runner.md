# Decision 0136: Add Synthetic Closed-Loop Discovery Runner

Date: 2026-05-05

Status: accepted as synthetic support tooling

## Decision

Add a synthetic closed-loop discovery runner that connects query generation, mock source discovery, Evidence Layer ingestion, metadata-only candidate creation, rule-based review ranking, simulated reviewer feedback, reward metrics, and epsilon-greedy bandit learning.

## First-Principle Rationale

The core objective is not classification accuracy. The objective is:

```text
high-value candidates per reviewer hour
```

That objective is a feedback-loop problem. A source arm is valuable only if it repeatedly produces review-worthy candidates while consuming little reviewer time. The runner makes that loop explicit and measurable before any real collection or external API integration is considered.

## Scope Boundary

This decision does not authorize:

- external APIs;
- automated Threads or Meta collection;
- production scoring;
- legal fraud determinations;
- AI/system final labels;
- raw evidence in git;
- a web dashboard or database product.

The connector is synthetic-only. Review labels are simulated. The bandit learns query-arm value for reviewer-hour allocation; it does not make final scam decisions.

## Artifacts

- `docs/66-closed-loop-discovery-v1.md`
- `src/discovery/query_generator.py`
- `src/discovery/connector.py`
- `src/candidate/builder.py`
- `src/candidate/scoring.py`
- `src/learning/bandit.py`
- `src/learning/metrics.py`
- `src/learning/runner.py`
- `run.py`
- `data/learning_state/README.md`

## Synthetic Demonstration

Command:

```bash
python3 run.py --rounds 5 --reset
```

Observed sample result on 2026-05-05:

```text
reward_change=+1.420 high_value_candidates_per_reviewer_hour
```

This is a smoke-test result over mock posts only. It demonstrates traceability and loop mechanics, not real-world performance.

## Decision Implication

The next real research move is still Reviewer Assist labor-savings evaluation under human final judgment and metadata-only evidence boundaries. The loop runner can support future capped experiments by making query-arm yield and reviewer-hour cost explicit once governed human-reviewed data exists.
