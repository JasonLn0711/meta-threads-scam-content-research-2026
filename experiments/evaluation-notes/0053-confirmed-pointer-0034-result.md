# Confirmed Pointer 0034 Result

## Purpose

Record the repo-safe result for the seventh confirmed Threads scam pointer.

This note contains no raw Threads content, full item URL, raw handle, screenshot, raw reply text, credential, browser artifact, storage-state material, raw storage path, or stakeholder case ID.

## Result

| Field | Value |
|---|---|
| Item ID | `threads_pilot_v1_0034` |
| Source path | confirmed scam pointer intake |
| Capture run | `CAPTURE-THREADS-PILOT-V1-0034-FULL-THREAD` |
| Decision link | `0043-record-market-direction-herding-chorus-rule` |
| Label after second review | `scam` |
| Risk after second review | `high` |
| Evidence family | `market_direction_herding_chorus` |
| Strict validation | pass: `manual_record_0034.json` and 34-record aggregate, 0 errors, 0 warnings |

## Controlled Full-Thread Capture

The controlled browser run preserved the approved browser-rendered raw evidence in the controlled store:

- source pointer
- top-level poster identity/profile context
- browser-rendered body text
- browser-rendered HTML
- screenshot
- visible text blocks
- href list

The accepted capture recorded 58 `[dir='auto']` text blocks, 128 visible text blocks, and 50 hrefs. The `article` selector returned 0, so the preserved raw evidence relies on body text, visible text blocks, HTML, and screenshot rather than `article` nodes.

Repo-safe records represent poster identity only through `poster_threads_id_ref`, `poster_profile_context_status`, `poster_profile_signals`, and redacted notes. Raw poster ID, profile URL, profile photo, follower/following graph, and broad profile history are not stored in git.

## Interpretation

This case adds a distinct social-pressure rule-library family. The top-level post uses strong full-position/no-retreat/bullish direction framing and dismisses bearish voices. The reply thread then shows a chorus of users saying they bought, added, held, refilled, or followed along.

The rule should remain narrow: ordinary bullish or bearish opinions are not automatically scam-like. The high-risk signal is the combination of a strong market-direction call, follower action-taking comments, and surrounding investment persuasion context.

## Validation

Commands run:

```bash
python3 scripts/validate_thread_dataset.py data/interim/manual_record_0034.json --strict
python3 scripts/validate_thread_dataset.py data/interim/manual_records_checkpoint_0034.jsonl --strict
python3 scripts/audit_thread_dataset.py data/interim/manual_records_checkpoint_0034.jsonl
.venv/bin/python scripts/run_rule_baseline.py data/interim/manual_records_checkpoint_0034.jsonl --variant all --run-name checkpoint-0034-herding-chorus-smoke-v2 --output-dir experiments/baselines/outputs
```

Results:

- item validation: 1 checked, 0 errors, 0 warnings
- aggregate validation: 34 checked, 0 errors, 0 warnings
- aggregate labels: 21 `non_scam`, 5 `uncertain`, 7 `scam`, 1 `insufficient_evidence`
- aggregate risk: 23 `low`, 4 `medium`, 7 `high`
- baseline all-signal smoke v2: precision 0.538, recall 1.000, F1 0.700, 6 false positives, 0 false negatives
- item `0034` baseline prediction: `scam_like` / `high`
- item `0034` baseline reasons include `MARKET_DIRECTION_HERDING_CHORUS` and `REPLY_FUNNEL_PATTERN`
- item `0034` total score: 9.5; high guardrail passed
