# Confirmed Pointer 0031 Result

## Purpose

Record the repo-safe result for the fourth confirmed Threads scam pointer.

This note contains no raw Threads content, full item URL, raw handle, screenshot, raw reply text, credential, browser artifact, storage-state material, raw storage path, or stakeholder case ID.

## Result

| Field | Value |
|---|---|
| Item ID | `threads_pilot_v1_0031` |
| Source path | confirmed scam pointer intake |
| Capture run | `CAPTURE-THREADS-PILOT-V1-0031-FULL-THREAD` |
| Decision link | `0040-record-past-performance-profit-proof-rule` |
| Label after second review | `scam` |
| Risk after second review | `high` |
| Evidence family | `past_performance_profit_proof` |
| Strict validation | pass: `manual_record_0031.json` and 31-record aggregate, 0 errors, 0 warnings |

## Controlled Full-Thread Capture

The controlled browser run preserved the approved browser-rendered raw evidence in the controlled store:

- source pointer
- browser-rendered body text
- browser-rendered HTML
- screenshot
- visible text blocks
- href list

The accepted capture recorded 6 `[dir='auto']` text blocks, 25 visible text blocks, and 7 hrefs. The `article` selector returned 0, so the preserved raw evidence relies on body text, visible text blocks, HTML, and screenshot rather than `article` nodes.

## Interpretation

This case adds a distinct rule-library family from items `0028`, `0029`, and `0030`. Item `0028` involved implicit DM conversion. Item `0029` involved a high-fee course or membership funnel. Item `0030` involved a comment-code lead magnet. Item `0031` involves past-performance profit proof: a stock-pick post uses alleged recommendation accuracy, limit-up or percentage-gain proof, and wealth-result/free-sharing framing to establish authority.

The rule should remain narrow: ordinary stock performance review or investment journaling is not automatically scam-like. The high-risk signal is the combination of investment/profit framing, named stock-pick proof, wealth-result claims, and guru-style credibility framing.

## Validation

Commands run:

```bash
python3 scripts/validate_thread_dataset.py data/interim/manual_record_0031.json --strict
python3 scripts/validate_thread_dataset.py data/interim/manual_records_checkpoint_0031.jsonl --strict
python3 scripts/audit_thread_dataset.py data/interim/manual_records_checkpoint_0031.jsonl
.venv/bin/python scripts/run_rule_baseline.py data/interim/manual_records_checkpoint_0031.jsonl --variant all --run-name checkpoint-0031-past-performance-smoke-v2 --output-dir experiments/baselines/outputs
```

Results:

- item validation: 1 checked, 0 errors, 0 warnings
- aggregate validation: 31 checked, 0 errors, 0 warnings
- aggregate labels: 21 `non_scam`, 5 `uncertain`, 4 `scam`, 1 `insufficient_evidence`
- aggregate risk: 23 `low`, 4 `medium`, 4 `high`
- baseline all-signal smoke: 31 items, 25 binary-metric items, 0 false negatives, 6 false positives
- item `0031` baseline prediction: `scam_like` / `high`
- item `0031` baseline reasons include `PAST_PERFORMANCE_PROFIT_PROOF`
