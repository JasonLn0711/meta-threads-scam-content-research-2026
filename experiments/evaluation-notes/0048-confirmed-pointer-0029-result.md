# Confirmed Pointer 0029 Result

## Purpose

Record the repo-safe result for the second confirmed Threads scam pointer.

This note contains no raw Threads content, full item URL, raw handle, screenshot, raw reply text, credential, browser artifact, storage-state material, raw storage path, or stakeholder case ID.

## Result

| Field | Value |
|---|---|
| Item ID | `threads_pilot_v1_0029` |
| Source path | confirmed scam pointer intake |
| Capture run | `CAPTURE-THREADS-PILOT-V1-0029-FULL-THREAD` |
| Decision link | `0036-adopt-confirmed-scam-pointer-intake-method` |
| Label after second review | `scam` |
| Risk after second review | `high` |
| Evidence family | `high_fee_course_or_membership_funnel` |
| Strict validation | pass: `manual_record_0029.json` and 29-record aggregate, 0 errors, 0 warnings |

## Controlled Full-Thread Capture

The controlled browser run preserved the approved browser-rendered raw evidence in the controlled store:

- source pointer
- browser-rendered body text
- browser-rendered HTML
- screenshot
- visible text blocks
- href list

The accepted capture recorded 42 `[dir='auto']` text blocks, 100 visible text blocks, and 24 hrefs. The `article` selector returned 0, so the preserved raw evidence relies on body text, visible text blocks, HTML, and screenshot rather than `article` nodes.

## Interpretation

This case adds a distinct rule-library family from item `0028`. Item `0028` involved implicit DM conversion. Item `0029` involves a trading or financial-education brand narrative plus high-fee course/membership funnel and reply-context guarantee/profit disputes.

The rule should remain narrow: paid education is not automatically scam-like. The high-risk signal is the combination of financial outcome framing, fee/funnel structure, and selected reply context exposing guarantee/profit or legitimacy disputes.

## Validation

Commands run:

```bash
python3 scripts/validate_thread_dataset.py data/interim/manual_record_0029.json --strict
python3 scripts/validate_thread_dataset.py data/interim/manual_records_checkpoint_0029.jsonl --strict
python3 scripts/audit_thread_dataset.py data/interim/manual_records_checkpoint_0029.jsonl
.venv/bin/python scripts/run_rule_baseline.py data/interim/manual_records_checkpoint_0029.jsonl --variant all --run-name checkpoint-0029-confirmed-pointer-smoke-v2 --output-dir experiments/baselines/outputs
```

Results:

- item validation: 1 checked, 0 errors, 0 warnings
- aggregate validation: 29 checked, 0 errors, 0 warnings
- aggregate labels: 21 `non_scam`, 5 `uncertain`, 2 `scam`, 1 `insufficient_evidence`
- aggregate risk: 23 `low`, 4 `medium`, 2 `high`
- baseline all-signal smoke: 29 items, 23 binary-metric items, 0 false negatives, 6 false positives
- item `0029` baseline reasons include `HIGH_FEE_COURSE_FUNNEL`
