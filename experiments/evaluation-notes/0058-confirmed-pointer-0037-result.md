# Confirmed Pointer 0037 Result

## Purpose

Record the repo-safe result for the next confirmed Threads scam pointer.

This note contains no raw Threads content, full item URL, raw handle, raw stock-pick text, screenshot, raw reply text, credential, browser artifact, storage-state material, raw storage path, or stakeholder case ID.

## Result

| Field | Value |
|---|---|
| Item ID | `threads_pilot_v1_0037` |
| Source path | confirmed scam pointer intake |
| Capture run | `CAPTURE-THREADS-PILOT-V1-0037-FULL-THREAD` |
| Decision link | `0049-record-stock-pick-playbook-keyword-funnel-rule` |
| Label after second review | `scam` |
| Risk after second review | `high` |
| Evidence family | `stock_pick_playbook_keyword_funnel` |
| Strict validation | pass: `manual_record_0037.json` and 37-record aggregate, 0 errors, 0 warnings |

## Controlled Full-Thread Capture

The controlled browser run preserved the approved browser-rendered raw evidence in the controlled store:

- source pointer
- browser-rendered body text
- browser-rendered HTML
- screenshot
- visible text blocks
- href list

The accepted capture recorded 18 `[dir='auto']` text blocks, 59 visible text blocks, and 11 hrefs. The `article` selector returned 0, so the preserved raw evidence relies on body text, visible text blocks, HTML, and screenshot rather than `article` nodes.

## Interpretation

This case adds a stock-pick playbook keyword funnel family. The public post creates urgency around a named short-term stock pick with recent-winner comparisons and easy-entry/break-high certainty. The author reply then offers a complete operation playbook through follow/message plus numeric-code action.

The rule should remain narrow: named stock discussion alone is not scam-like. The risk signal is the convergence of named pick, FOMO/strong outcome framing, and a follow/message/code gate for a private playbook.

## Validation

Commands run after record build:

```bash
python3 scripts/validate_thread_dataset.py data/interim/manual_record_0037.json --strict
python3 scripts/validate_thread_dataset.py data/interim/manual_records_checkpoint_0037.jsonl --strict
python3 scripts/audit_thread_dataset.py data/interim/manual_records_checkpoint_0037.jsonl
.venv/bin/python scripts/run_rule_baseline.py data/interim/manual_records_checkpoint_0037.jsonl --variant all --run-name checkpoint-0037-stock-pick-playbook-smoke-v3 --output-dir experiments/baselines/outputs
```

Results:

- item validation: 1 checked, 0 errors, 0 warnings
- aggregate validation: 37 checked, 0 errors, 0 warnings
- aggregate labels: 21 `non_scam`, 5 `uncertain`, 10 `scam`, 1 `insufficient_evidence`
- aggregate risk: 23 `low`, 4 `medium`, 10 `high`
- baseline all-signal smoke v3: precision 0.625, recall 1.000, F1 0.769, 6 false positives, 0 false negatives
- item `0037` baseline prediction: `scam_like` / `high`
- item `0037` baseline reasons include `STOCK_PICK_PLAYBOOK_KEYWORD_FUNNEL`, `COMMENT_CODE_LEAD_MAGNET`, `PRIVATE_REDIRECT`, `PAST_PERFORMANCE_PROFIT_PROOF`, `LOW_EFFORT_HIGH_RETURN`, `TESTIMONIAL_PATTERN`, `REPLY_FUNNEL_PATTERN`, and `MULTI_SIGNAL_CONVERGENCE`
- item `0037` total score: 27.5; high guardrail passed
