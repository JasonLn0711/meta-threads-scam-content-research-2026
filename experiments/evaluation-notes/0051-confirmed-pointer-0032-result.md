# Confirmed Pointer 0032 Result

## Purpose

Record the repo-safe result for the fifth confirmed Threads scam pointer.

This note contains no raw Threads content, full item URL, raw handle, screenshot, raw reply text, raw external link, credential, browser artifact, storage-state material, raw storage path, or stakeholder case ID.

## Result

| Field | Value |
|---|---|
| Item ID | `threads_pilot_v1_0032` |
| Source path | confirmed scam pointer intake |
| Capture run | `CAPTURE-THREADS-PILOT-V1-0032-FULL-THREAD` |
| Decision link | `0041-record-stock-rescue-group-funnel-rule` |
| Label after second review | `scam` |
| Risk after second review | `high` |
| Evidence family | `stock_rescue_group_funnel` |
| Strict validation | pass: `manual_record_0032.json` and 32-record aggregate, 0 errors, 0 warnings |

## Controlled Full-Thread Capture

The controlled browser run preserved the approved browser-rendered raw evidence in the controlled store:

- source pointer
- browser-rendered body text
- browser-rendered HTML
- screenshot
- visible text blocks
- href list

The accepted capture recorded 10 `[dir='auto']` text blocks, 32 visible text blocks, and 8 hrefs. The `article` selector returned 0, so the preserved raw evidence relies on body text, visible text blocks, HTML, and screenshot rather than `article` nodes.

## Interpretation

This case adds a distinct rule-library family from items `0028` through `0031`. Item `0032` involves a stock-rescue group funnel: free community access, trapped-stock help, synchronized operation, private stock consultation, and a LINE/OpenChat or shortener-based group path.

The rule should remain narrow: ordinary investment groups, education communities, or short links are not automatically scam-like. The high-risk signal is the combination of investment-help framing, off-platform group migration, private stock consultation, and free guru/community language.

## Validation

Commands run:

```bash
python3 scripts/validate_thread_dataset.py data/interim/manual_record_0032.json --strict
python3 scripts/validate_thread_dataset.py data/interim/manual_records_checkpoint_0032.jsonl --strict
python3 scripts/audit_thread_dataset.py data/interim/manual_records_checkpoint_0032.jsonl
.venv/bin/python scripts/run_rule_baseline.py data/interim/manual_records_checkpoint_0032.jsonl --variant all --run-name checkpoint-0032-stock-rescue-group-smoke-v1 --output-dir experiments/baselines/outputs
```

Results:

- item validation: 1 checked, 0 errors, 0 warnings
- aggregate validation: 32 checked, 0 errors, 0 warnings
- aggregate labels: 21 `non_scam`, 5 `uncertain`, 5 `scam`, 1 `insufficient_evidence`
- aggregate risk: 23 `low`, 4 `medium`, 5 `high`
- baseline all-signal smoke: 32 items, 26 binary-metric items, 0 false negatives, 6 false positives
- item `0032` baseline prediction: `scam_like` / `high`
- item `0032` baseline reasons include `STOCK_RESCUE_GROUP_FUNNEL`
