# Confirmed Non-Scam Warning 0042 Result

## Purpose

Record the repo-safe result for a confirmed non-scam Threads pointer that warns potential victims.

This note contains no raw Threads content, full item URL, raw handle, screenshot, raw reply text, credential, browser artifact, storage-state material, raw storage path, or stakeholder case ID.

## Result

| Field | Value |
|---|---|
| Item ID | `threads_pilot_v1_0042` |
| Source path | confirmed non-scam warning pointer intake |
| Capture run | `CAPTURE-THREADS-PILOT-V1-0042-FULL-THREAD` |
| Decision link | `0054-record-anti-scam-warning-hard-negative-boundary` |
| Label after second review | `non_scam` |
| Risk after second review | `low` |
| Evidence family | anti-scam warning hard negative |
| Strict validation | pass: `manual_record_0042.json` and 42-record aggregate, 0 errors, 0 warnings |

## Controlled Full-Thread Capture

The controlled browser run preserved the approved browser-rendered raw evidence in the controlled store:

- source pointer
- browser-rendered body text
- browser-rendered HTML
- screenshot
- visible text blocks
- href list

The accepted capture recorded 48 `[dir='auto']` text blocks, 115 visible text blocks, and 30 hrefs. The `article` selector returned 0, so the preserved raw evidence relies on body text, visible text blocks, HTML, and screenshot rather than `article` nodes.

## Interpretation

This case should be used as a hard negative. It mentions scam mechanics and investment-risk vocabulary, but the direction of persuasion is victim prevention: do not join suspicious groups, do not trust stock-call teachers, do not chase promised returns, and remain cautious.

The boundary should remain narrow: anti-scam warnings are `non_scam` only when they do not introduce a new private group, paid service, affiliate path, replacement teacher, account-opening step, or investment method controlled by the author.

## Validation

Commands run after record build:

```bash
python3 scripts/validate_thread_dataset.py data/interim/manual_record_0042.json --strict
python3 scripts/validate_thread_dataset.py data/interim/manual_records_checkpoint_0042.jsonl --strict
python3 scripts/audit_thread_dataset.py data/interim/manual_records_checkpoint_0042.jsonl
.venv/bin/python scripts/run_rule_baseline.py data/interim/manual_records_checkpoint_0042.jsonl --variant all --run-name checkpoint-0042-anti-scam-warning-hard-negative-smoke-v1 --output-dir experiments/baselines/outputs
```

Results:

- item validation: 1 checked, 0 errors, 0 warnings
- aggregate validation: 42 checked, 0 errors, 0 warnings
- aggregate labels: 22 `non_scam`, 5 `uncertain`, 14 `scam`, 1 `insufficient_evidence`
- aggregate risk: 24 `low`, 4 `medium`, 14 `high`
- baseline all-signal smoke v1: precision 0.700, recall 1.000, F1 0.824, 6 false positives, 0 false negatives
- item `0042` baseline prediction: `not_scam_like` / `low`
- item `0042` baseline reasons: none
- item `0042` total score: 0.0
