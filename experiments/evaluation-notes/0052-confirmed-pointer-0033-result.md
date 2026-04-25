# Confirmed Pointer 0033 Result

## Purpose

Record the repo-safe result for the sixth confirmed Threads scam pointer.

This note contains no raw Threads content, full item URL, raw handle, screenshot, raw reply text, credential, browser artifact, storage-state material, raw storage path, or stakeholder case ID.

## Result

| Field | Value |
|---|---|
| Item ID | `threads_pilot_v1_0033` |
| Source path | confirmed scam pointer intake |
| Capture run | `CAPTURE-THREADS-PILOT-V1-0033-FULL-THREAD` |
| Decision link | `0042-record-individual-stock-advice-reply-funnel-rule` |
| Label after second review | `scam` |
| Risk after second review | `high` |
| Evidence family | `individual_stock_advice_reply_funnel` |
| Strict validation | pass: `manual_record_0033.json` and 33-record aggregate, 0 errors, 0 warnings |

## Controlled Full-Thread Capture

The controlled browser run preserved the approved browser-rendered raw evidence in the controlled store:

- source pointer
- browser-rendered body text
- browser-rendered HTML
- screenshot
- visible text blocks
- href list

The accepted capture recorded 54 `[dir='auto']` text blocks, 139 visible text blocks, and 40 hrefs. The `article` selector returned 0, so the preserved raw evidence relies on body text, visible text blocks, HTML, and screenshot rather than `article` nodes.

## Interpretation

This case adds a distinct reply-level rule-library family. The top-level post uses prediction accuracy and market-timing authority. The reply thread then shows repeated individualized stock questions and short author answers, plus group-join context. This makes the comment layer part of the funnel, not just incidental discussion.

The rule should remain narrow: ordinary stock Q&A is not automatically scam-like. The high-risk signal is the combination of prediction-proof, profit framing, repeated individualized reply advice, and group/private-channel context.

## Validation

Commands run:

```bash
python3 scripts/validate_thread_dataset.py data/interim/manual_record_0033.json --strict
python3 scripts/validate_thread_dataset.py data/interim/manual_records_checkpoint_0033.jsonl --strict
python3 scripts/audit_thread_dataset.py data/interim/manual_records_checkpoint_0033.jsonl
.venv/bin/python scripts/run_rule_baseline.py data/interim/manual_records_checkpoint_0033.jsonl --variant all --run-name checkpoint-0033-individual-advice-smoke-v2 --output-dir experiments/baselines/outputs
```

Results:

- item validation: 1 checked, 0 errors, 0 warnings
- aggregate validation: 33 checked, 0 errors, 0 warnings
- aggregate labels: 21 `non_scam`, 5 `uncertain`, 6 `scam`, 1 `insufficient_evidence`
- aggregate risk: 23 `low`, 4 `medium`, 6 `high`
- baseline all-signal smoke: 33 items, 27 binary-metric items, 0 false negatives, 6 false positives
- item `0033` baseline prediction: `scam_like` / `high`
- item `0033` baseline reasons include `INDIVIDUAL_STOCK_ADVICE_REPLY_FUNNEL`
