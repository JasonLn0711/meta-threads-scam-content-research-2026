# Confirmed Pointer 0040 Result

## Purpose

Record the repo-safe result for the next confirmed Threads scam pointer.

This note contains no raw Threads content, full item URL, raw handle, raw stock names, raw price/target values, raw code, screenshot, raw reply text, credential, browser artifact, storage-state material, raw storage path, or stakeholder case ID.

## Result

| Field | Value |
|---|---|
| Item ID | `threads_pilot_v1_0040` |
| Source path | confirmed scam pointer intake |
| Capture run | `CAPTURE-THREADS-PILOT-V1-0040-FULL-THREAD` |
| Decision link | `0052-record-dark-horse-stock-target-price-dm-funnel-rule` |
| Label after second review | `scam` |
| Risk after second review | `high` |
| Evidence family | `dark_horse_stock_target_price_dm_funnel` |
| Strict validation | pass: `manual_record_0040.json` and 40-record aggregate, 0 errors, 0 warnings |

## Controlled Full-Thread Capture

The controlled browser run preserved the approved browser-rendered raw evidence in the controlled store:

- source pointer
- browser-rendered body text
- browser-rendered HTML
- screenshot
- visible text blocks
- href list

The accepted capture recorded 27 `[dir='auto']` text blocks, 89 visible text blocks, and 23 hrefs. The `article` selector returned 0, so the preserved raw evidence relies on body text, visible text blocks, HTML, and screenshot rather than `article` nodes.

## Interpretation

This case adds a dark-horse stock target-price DM-funnel family. The top-level post and selected reply context combine a public stock-command list, hidden-stock teaser, low-current/high-target-price framing, technology or major-brand catalyst authority, urgency, and follow/message/code/private-share action gating.

The rule should remain narrow: ordinary stock watchlists, ordinary target-price discussion, or ordinary catalyst commentary are not scam-like by themselves. The risk signal is the convergence of hidden-stock lure, high target-price promise, catalyst authority, urgency, and private/action-gated delivery.

## Validation

Commands run after record build:

```bash
python3 scripts/validate_thread_dataset.py data/interim/manual_record_0040.json --strict
python3 scripts/validate_thread_dataset.py data/interim/manual_records_checkpoint_0040.jsonl --strict
python3 scripts/audit_thread_dataset.py data/interim/manual_records_checkpoint_0040.jsonl
.venv/bin/python scripts/run_rule_baseline.py data/interim/manual_records_checkpoint_0040.jsonl --variant all --run-name checkpoint-0040-dark-horse-target-dm-smoke-v1 --output-dir experiments/baselines/outputs
```

Results:

- item validation: 1 checked, 0 errors, 0 warnings
- aggregate validation: 40 checked, 0 errors, 0 warnings
- aggregate labels: 21 `non_scam`, 5 `uncertain`, 13 `scam`, 1 `insufficient_evidence`
- aggregate risk: 23 `low`, 4 `medium`, 13 `high`
- baseline all-signal smoke v1: precision 0.684, recall 1.000, F1 0.812, 6 false positives, 0 false negatives
- item `0040` baseline prediction: `scam_like` / `high`
- item `0040` baseline reasons include `DARK_HORSE_STOCK_TARGET_PRICE_DM_FUNNEL`, `COMMENT_CODE_LEAD_MAGNET`, `PRIVATE_REDIRECT`, `LOW_EFFORT_HIGH_RETURN`, `REPLY_FUNNEL_PATTERN`, and `MULTI_SIGNAL_CONVERGENCE`
- item `0040` total score: 24.0; high guardrail passed
