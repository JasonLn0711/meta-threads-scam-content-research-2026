# Confirmed Pointer 0035 Result

## Purpose

Record the repo-safe result for the next confirmed Threads scam pointer.

This note contains no raw Threads content, full item URL, raw handle, screenshot, raw reply text, credential, browser artifact, storage-state material, raw storage path, or stakeholder case ID.

## Result

| Field | Value |
|---|---|
| Item ID | `threads_pilot_v1_0035` |
| Source path | confirmed scam pointer intake |
| Capture run | `CAPTURE-THREADS-PILOT-V1-0035-FULL-THREAD` |
| Decision link | `0046-record-institutional-flow-authority-lure-rule` |
| Label after second review | `scam` |
| Risk after second review | `high` |
| Evidence family | `institutional_flow_authority_lure` |
| Strict validation | pass: `manual_record_0035.json` and 35-record aggregate, 0 errors, 0 warnings |

## Controlled Full-Thread Capture

The controlled browser run preserved the approved browser-rendered raw evidence in the controlled store:

- source pointer
- browser-rendered body text
- browser-rendered HTML
- screenshot
- visible text blocks
- href list

The accepted capture recorded 58 `[dir='auto']` text blocks, 128 visible text blocks, and 51 hrefs. The `article` selector returned 0, so the preserved raw evidence relies on body text, visible text blocks, HTML, and screenshot rather than `article` nodes.

## Interpretation

This case adds an institutional-flow authority rule-library family. The item combines past stock-pick performance proof, institutional/foreign-investor/futures/spot flow framing, macro-event/weekend-risk reassurance, full-position/do-long instruction, and replies showing readers feel reassured or follow the direction.

The rule should remain narrow: ordinary macro analysis or institutional-flow commentary is not automatically scam-like. The high-risk signal is the combination of external market authority cues with strong trading action and follower reassurance/action comments.

## Validation

Commands run after record build:

```bash
python3 scripts/validate_thread_dataset.py data/interim/manual_record_0035.json --strict
python3 scripts/validate_thread_dataset.py data/interim/manual_records_checkpoint_0035.jsonl --strict
python3 scripts/audit_thread_dataset.py data/interim/manual_records_checkpoint_0035.jsonl
.venv/bin/python scripts/run_rule_baseline.py data/interim/manual_records_checkpoint_0035.jsonl --variant all --run-name checkpoint-0035-institutional-flow-authority-smoke-v2 --output-dir experiments/baselines/outputs
```

Results:

- item validation: 1 checked, 0 errors, 0 warnings
- aggregate validation: 35 checked, 0 errors, 0 warnings
- aggregate labels: 21 `non_scam`, 5 `uncertain`, 8 `scam`, 1 `insufficient_evidence`
- aggregate risk: 23 `low`, 4 `medium`, 8 `high`
- baseline all-signal smoke v2: precision 0.571, recall 1.000, F1 0.727, 6 false positives, 0 false negatives
- item `0035` baseline prediction: `scam_like` / `high`
- item `0035` baseline reasons include `INSTITUTIONAL_FLOW_AUTHORITY_LURE`, `MARKET_DIRECTION_HERDING_CHORUS`, `LOW_EFFORT_HIGH_RETURN`, and `REPLY_FUNNEL_PATTERN`
- item `0035` total score: 16.0; high guardrail passed
