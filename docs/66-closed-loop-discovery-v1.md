# Closed-Loop Discovery v1

Status: synthetic implementation layer

Date opened: 2026-05-05

## First Principle

This layer does not optimize classification accuracy. It optimizes:

```text
high-value candidates per reviewer hour
```

The loop tests which query strategies produce review-worthy candidates with the least reviewer time. It is a research workflow simulator, not a production detector, crawler, enforcement tool, or legal fraud determination system.

## Loop

```text
query generator
-> synthetic source connector
-> evidence ingestion
-> metadata-only candidate builder
-> rule-based review ranking
-> simulated reviewer feedback
-> reward metrics
-> epsilon-greedy bandit update
-> next query generator pass
```

## Modules

```text
src/discovery/query_generator.py  static templates plus bandit-weighted query objects
src/discovery/connector.py        synthetic mock source connector
src/evidence/ingestion.py         controlled-store ingest reused from Evidence Layer v1
src/candidate/builder.py          metadata-only candidate builder and feature extraction
src/candidate/scoring.py          rule-based ranking score and top-K selection
src/learning/metrics.py           simulated review and reward calculation
src/learning/bandit.py            epsilon-greedy query-arm learning
src/learning/runner.py            one-round orchestration and persistence
run.py                            CLI
```

## Reward

The reward is computed as:

```text
scam_count / reviewer_hours
```

The simulated reviewer returns `scam`, `non_scam`, or `uncertain` plus `review_minutes`. In real use, this must be replaced by human review outcomes. The bandit updates query arms from the observed reward, not from model confidence.

## Persistence

Local state is saved under ignored `data/learning_state/`:

- `bandit_state.json`
- `metrics.json`
- `rounds.jsonl`

Selected metadata-only candidates are written as ignored JSONL files under `data/candidate_intake/closed_loop_round_*.jsonl`. Raw synthetic evidence is stored through the Evidence Layer under ignored `data/evidence_store/`, with audit entries under ignored `data/audit_logs/`.

## Usage

```bash
python3 run.py --rounds 5 --reset
```

The CLI prints round-level logs and a reward trend.

## Boundary

- The connector is synthetic-only.
- No external APIs are called.
- Candidate records do not include raw content.
- Scores rank candidates for review; they are not labels.
- The bandit learns query-arm value for reviewer-hour allocation; it does not make final scam decisions.
