# Confirmed Pointer 0041 Result

## Purpose

Record the repo-safe result for the next confirmed Threads scam pointer.

This note contains no raw Threads content, full item URL, raw handle, raw stock names, raw stock codes, raw price values, screenshot, raw reply text, credential, browser artifact, storage-state material, raw storage path, or stakeholder case ID.

## Result

| Field | Value |
|---|---|
| Item ID | `threads_pilot_v1_0041` |
| Source path | confirmed scam pointer intake |
| Capture run | `CAPTURE-THREADS-PILOT-V1-0041-FULL-THREAD` |
| Decision link | `0053-record-mass-stock-command-list-group-funnel-rule` |
| Label after second review | `scam` |
| Risk after second review | `high` |
| Evidence family | `mass_stock_command_list_group_funnel` |
| Strict validation | pass: `manual_record_0041.json` and 41-record aggregate, 0 errors, 0 warnings |

## Controlled Full-Thread Capture

The controlled browser run preserved the approved browser-rendered raw evidence in the controlled store:

- source pointer
- browser-rendered body text
- browser-rendered HTML
- screenshot
- visible text blocks
- href list

The accepted capture recorded 11 `[dir='auto']` text blocks, 75 visible text blocks, and 7 hrefs. The `article` selector returned 0, so the preserved raw evidence relies on body text, visible text blocks, HTML, and screenshot rather than `article` nodes.

## Interpretation

This case adds a mass stock-command list group-funnel family. The post combines a large list of stock-specific entry/exit or strong-outcome instructions with claimed call accuracy, free sharing, and a daily signal/group or quota conversion path.

The rule should remain narrow: ordinary stock watchlists, ordinary target-price discussion, or ordinary market notes are not scam-like by themselves. The risk signal is the convergence of mass command-list behavior, claimed accuracy, strong-outcome framing, and group/quota/action-gated delivery.

## Validation

Commands run after record build:

```bash
python3 scripts/validate_thread_dataset.py data/interim/manual_record_0041.json --strict
python3 scripts/validate_thread_dataset.py data/interim/manual_records_checkpoint_0041.jsonl --strict
python3 scripts/audit_thread_dataset.py data/interim/manual_records_checkpoint_0041.jsonl
.venv/bin/python scripts/run_rule_baseline.py data/interim/manual_records_checkpoint_0041.jsonl --variant all --run-name checkpoint-0041-mass-stock-command-group-smoke-v1 --output-dir experiments/baselines/outputs
```

Results:

- item validation: 1 checked, 0 errors, 0 warnings
- aggregate validation: 41 checked, 0 errors, 0 warnings
- aggregate labels: 21 `non_scam`, 5 `uncertain`, 14 `scam`, 1 `insufficient_evidence`
- aggregate risk: 23 `low`, 4 `medium`, 14 `high`
- baseline all-signal smoke v1: precision 0.700, recall 1.000, F1 0.824, 6 false positives, 0 false negatives
- item `0041` baseline prediction: `scam_like` / `high`
- item `0041` baseline reasons include `MASS_STOCK_COMMAND_LIST_GROUP_FUNNEL`, `PRIVATE_REDIRECT`, and `REPLY_FUNNEL_PATTERN`
- item `0041` total score: 9.5; high guardrail passed
