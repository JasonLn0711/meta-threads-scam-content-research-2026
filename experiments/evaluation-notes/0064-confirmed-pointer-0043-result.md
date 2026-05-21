# Confirmed Pointer 0043 Result

## Purpose

Record the repo-safe result for the next confirmed Threads scam pointer.

This note contains no raw Threads content, full item URL, raw handle, raw stock names, raw stock codes, raw price values, screenshot, raw reply text, credential, browser artifact, storage-state material, raw storage path, or stakeholder case ID.

## Result

| Field | Value |
|---|---|
| Item ID | `threads_pilot_v1_0043` |
| Source path | confirmed scam pointer intake |
| Capture run | `CAPTURE-THREADS-PILOT-V1-0043-FULL-THREAD` |
| Decision link | `0055-record-coded-animal-stock-limit-up-group-funnel-rule` |
| Label after second review | `scam` |
| Risk after second review | `high` |
| Evidence family | `coded_animal_stock_limit_up_group_funnel` |
| Strict validation | pass: `manual_record_0043.json` and 43-record aggregate, 0 errors, 0 warnings |

## Controlled Full-Thread Capture

The controlled browser run preserved the approved browser-rendered raw evidence in the controlled store:

- source pointer
- browser-rendered body text
- browser-rendered HTML
- screenshot
- visible text blocks
- href list

The accepted capture recorded 22 `[dir='auto']` text blocks, 71 visible text blocks, and 13 hrefs. The `article` selector returned 0, so the preserved raw evidence relies on body text, visible text blocks, HTML, and screenshot rather than `article` nodes.

## Interpretation

This case adds a coded-animal stock limit-up group-funnel family. The public post combines a mass stock-command list, claimed call accuracy, wealth-result proof, and free-sharing framing with an obscured animal-coded low-price target, near-term limit-up/exit timing, prepared-data language, and group/message/`+1` action gating.

The rule should remain narrow: animal nicknames, market metaphors, or ordinary stock watchlists are not scam-like by themselves. The risk signal is the convergence of coded/obscured stock lure, near-term outcome certainty, and group/private-message conversion.

## Validation

Commands run after record build:

```bash
python3 scripts/validate_thread_dataset.py data/interim/manual_record_0043.json --strict
python3 scripts/validate_thread_dataset.py data/interim/manual_records_checkpoint_0043.jsonl --strict
python3 scripts/audit_thread_dataset.py data/interim/manual_records_checkpoint_0043.jsonl
.venv/bin/python scripts/run_rule_baseline.py data/interim/manual_records_checkpoint_0043.jsonl --variant all --run-name checkpoint-0043-coded-animal-stock-group-smoke-v1 --output-dir experiments/baselines/outputs
```

Results:

- item validation: 1 checked, 0 errors, 0 warnings
- aggregate validation: 43 checked, 0 errors, 0 warnings
- aggregate labels: 22 `non_scam`, 5 `uncertain`, 15 `scam`, 1 `insufficient_evidence`
- aggregate risk: 24 `low`, 4 `medium`, 15 `high`
- baseline all-signal smoke v1: precision 0.714, recall 1.000, F1 0.833, 6 false positives, 0 false negatives
- item `0043` baseline prediction: `scam_like` / `high`
- item `0043` baseline reasons include `CODED_ANIMAL_STOCK_LIMIT_UP_GROUP_FUNNEL`, `PAST_PERFORMANCE_PROFIT_PROOF`, `STOCK_RESCUE_GROUP_FUNNEL`, `MARKET_DIRECTION_HERDING_CHORUS`, `PRIVATE_REDIRECT`, `IMPLICIT_DM_CONTACT_REQUEST`, `COMMENT_CODE_LEAD_MAGNET`, `REPLY_FUNNEL_PATTERN`, and `MULTI_SIGNAL_CONVERGENCE`
- item `0043` total score: 44.5; high guardrail passed
