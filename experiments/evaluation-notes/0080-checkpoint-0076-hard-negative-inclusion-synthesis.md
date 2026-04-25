# Checkpoint 0076 Hard-Negative Inclusion Synthesis

## Purpose

Record the repo-safe inclusion result for local item `0076`.

This synthesis contains no raw Threads content, full URLs, raw handles, screenshots, raw reply text, credentials, browser artifacts, storage-state material, raw storage paths, contact IDs, stock names, stock codes, price values, or stakeholder case IDs.

## Scope

| Field | Value |
|---|---|
| Local aggregate | `data/interim/manual_records_checkpoint_0076.jsonl` |
| Records | 76 |
| Latest item | `threads_pilot_v1_0076` |
| Item role | hard-negative calibration |
| Label / risk | `non_scam` / `low` |
| Checkpoint status | local inclusion accepted; broader checkpoint report update pending |

## Validation

Commands run:

```text
.venv/bin/python scripts/validate_thread_dataset.py data/interim/manual_records_checkpoint_0076.jsonl --strict
.venv/bin/python scripts/audit_thread_dataset.py data/interim/manual_records_checkpoint_0076.jsonl
.venv/bin/python scripts/run_rule_baseline.py data/interim/manual_records_checkpoint_0076.jsonl --variant all --run-name checkpoint-0076-hard-negative-smoke-v1 --output-dir experiments/baselines/outputs
```

Results:

| Check | Result |
|---|---:|
| Strict validation errors | 0 |
| Strict validation warnings | 0 |
| Audit schema errors | 0 |
| Audit schema warnings | 0 |
| Baseline precision | 0.708 |
| Baseline recall | 1.000 |
| Baseline false positives | 7 |
| Baseline false negatives | 0 |

## Aggregate Counts

| Label | Count |
|---|---:|
| `scam` | 17 |
| `non_scam` | 24 |
| `uncertain` | 29 |
| `insufficient_evidence` | 6 |

| Risk | Count |
|---|---:|
| `high` | 17 |
| `medium` | 13 |
| `low` | 46 |

Source mix:

| Source type | Count |
|---|---:|
| `manual_public` | 58 |
| `stakeholder_provided` | 18 |

## Delta From Local 0075 Aggregate

| Metric | 0075 | 0076 | Delta |
|---|---:|---:|---:|
| Total records | 75 | 76 | +1 |
| `scam` | 17 | 17 | 0 |
| `non_scam` | 23 | 24 | +1 |
| `uncertain` | 29 | 29 | 0 |
| `insufficient_evidence` | 6 | 6 | 0 |
| `high` risk | 17 | 17 | 0 |
| `medium` risk | 13 | 13 | 0 |
| `low` risk | 45 | 46 | +1 |

## Interpretation

Item `0076` does not add scam/high-risk evidence. It adds a hard-negative boundary for anti-scam warning and victim-prevention content.

This is useful because the candidate contains scam-method and private-channel vocabulary in a warning context. The rule system needs this kind of negative case so high-recall triage does not become blind keyword matching.

## Audit Notes

The 76-record audit still flags:

- `uncertain` share above the pilot warning threshold;
- source skew toward `manual_public`;
- collection-method skew toward `manual_capture`.

These are expected from runs `0039`, `0043`, and `0044`; they are not caused by item `0076`.

## Decision Implication

The next checkpoint can include local item `0076` as `non_scam` / `low`.

Do not treat this as browser-session scam expansion. The next high-risk rule-learning path should still prioritize confirmed pointers or a separately authorized source path.
