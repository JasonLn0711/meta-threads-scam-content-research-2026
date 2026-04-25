# Confirmed Pointer 0030 Result

## Purpose

Record the repo-safe result for the third confirmed Threads scam pointer.

This note contains no raw Threads content, full item URL, raw handle, screenshot, raw reply text, credential, browser artifact, storage-state material, raw storage path, or stakeholder case ID.

## Result

| Field | Value |
|---|---|
| Item ID | `threads_pilot_v1_0030` |
| Source path | confirmed scam pointer intake |
| Capture run | `CAPTURE-THREADS-PILOT-V1-0030-FULL-THREAD` |
| Decision link | `0039-record-comment-code-lead-magnet-rule` |
| Label after second review | `scam` |
| Risk after second review | `high` |
| Evidence family | `comment_code_lead_magnet` |
| Strict validation | pass: `manual_record_0030.json` and 30-record aggregate, 0 errors, 0 warnings |

## Controlled Full-Thread Capture

The controlled browser run preserved the approved browser-rendered raw evidence in the controlled store:

- source pointer
- browser-rendered body text
- browser-rendered HTML
- screenshot
- visible text blocks
- href list

The accepted capture recorded 60 `[dir='auto']` text blocks, 133 visible text blocks, and 48 hrefs. The `article` selector returned 0, so the preserved raw evidence relies on body text, visible text blocks, HTML, and screenshot rather than `article` nodes.

## Interpretation

This case adds a distinct rule-library family from items `0028` and `0029`. Item `0028` involved implicit DM conversion. Item `0029` involved a high-fee course or membership funnel. Item `0030` involves finance/authority hype paired with an author's reply that uses a code/keyword/free-receive instruction as the conversion signal.

The rule should remain narrow: ordinary stock commentary, public-figure references, or engagement prompts are not automatically scam-like. The high-risk signal is the combination of investment/profit framing, fake authority or public-figure bait, target-price or strong-upside language, and a reply-level code/keyword lead magnet.

## Validation

Commands run:

```bash
python3 scripts/validate_thread_dataset.py data/interim/manual_record_0030.json --strict
python3 scripts/validate_thread_dataset.py data/interim/manual_records_checkpoint_0030.jsonl --strict
python3 scripts/audit_thread_dataset.py data/interim/manual_records_checkpoint_0030.jsonl
.venv/bin/python scripts/run_rule_baseline.py data/interim/manual_records_checkpoint_0030.jsonl --variant all --run-name checkpoint-0030-comment-code-smoke-v2 --output-dir experiments/baselines/outputs
```

Results:

- item validation: 1 checked, 0 errors, 0 warnings
- aggregate validation: 30 checked, 0 errors, 0 warnings
- aggregate labels: 21 `non_scam`, 5 `uncertain`, 3 `scam`, 1 `insufficient_evidence`
- aggregate risk: 23 `low`, 4 `medium`, 3 `high`
- baseline all-signal smoke: 30 items, 24 binary-metric items, 0 false negatives, 6 false positives
- item `0030` baseline prediction: `scam_like` / `high`
- item `0030` baseline reasons include `COMMENT_CODE_LEAD_MAGNET`
