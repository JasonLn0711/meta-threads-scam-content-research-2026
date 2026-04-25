# Confirmed Pointer 0038 Result

## Purpose

Record the repo-safe result for the next confirmed Threads scam pointer.

This note contains no raw Threads content, full item URL, raw handle, raw stock-pick text, screenshot, raw reply text, credential, browser artifact, storage-state material, raw storage path, or stakeholder case ID.

## Result

| Field | Value |
|---|---|
| Item ID | `threads_pilot_v1_0038` |
| Source path | confirmed scam pointer intake |
| Capture run | `CAPTURE-THREADS-PILOT-V1-0038-FULL-THREAD` |
| Decision link | `0050-record-trapped-position-dm-playbook-reply-rule` |
| Label after second review | `scam` |
| Risk after second review | `high` |
| Evidence family | `trapped_position_dm_playbook_reply` |
| Strict validation | pass: `manual_record_0038.json` and 38-record aggregate, 0 errors, 0 warnings |

## Controlled Full-Thread Capture

The controlled browser run preserved the approved browser-rendered raw evidence in the controlled store:

- source pointer
- browser-rendered body text
- browser-rendered HTML
- screenshot
- visible text blocks
- href list

The accepted capture recorded 25 `[dir='auto']` text blocks, 78 visible text blocks, and 16 hrefs. The `article` selector returned 0, so the preserved raw evidence relies on body text, visible text blocks, HTML, and screenshot rather than `article` nodes.

## Interpretation

This case adds a trapped-position DM playbook reply family. The public post and pinned reply reinforce the existing stock-pick playbook funnel, while one visible reply shows a commenter with a trapped-position/loss concern and an author response moving the guidance into private message with a detailed operation playbook.

The rule should remain narrow: not every loss question or stock-help reply is scam-like. The high-risk point is the conversion of loss anxiety into private playbook guidance inside a broader short-term stock-pick funnel.

## Validation

Commands run after record build:

```bash
python3 scripts/validate_thread_dataset.py data/interim/manual_record_0038.json --strict
python3 scripts/validate_thread_dataset.py data/interim/manual_records_checkpoint_0038.jsonl --strict
python3 scripts/audit_thread_dataset.py data/interim/manual_records_checkpoint_0038.jsonl
.venv/bin/python scripts/run_rule_baseline.py data/interim/manual_records_checkpoint_0038.jsonl --variant all --run-name checkpoint-0038-trapped-position-playbook-smoke-v1 --output-dir experiments/baselines/outputs
```

Results:

- item validation: 1 checked, 0 errors, 0 warnings
- aggregate validation: 38 checked, 0 errors, 0 warnings
- aggregate labels: 21 `non_scam`, 5 `uncertain`, 11 `scam`, 1 `insufficient_evidence`
- aggregate risk: 23 `low`, 4 `medium`, 11 `high`
- baseline all-signal smoke v1: precision 0.647, recall 1.000, F1 0.786, 6 false positives, 0 false negatives
- item `0038` baseline prediction: `scam_like` / `high`
- item `0038` baseline reasons include `TRAPPED_POSITION_DM_PLAYBOOK_REPLY`, `STOCK_PICK_PLAYBOOK_KEYWORD_FUNNEL`, `COMMENT_CODE_LEAD_MAGNET`, `PRIVATE_REDIRECT`, `PAST_PERFORMANCE_PROFIT_PROOF`, `INDIVIDUAL_STOCK_ADVICE_REPLY_FUNNEL`, `TESTIMONIAL_PATTERN`, `REPLY_FUNNEL_PATTERN`, and `MULTI_SIGNAL_CONVERGENCE`
- item `0038` total score: 36.5; high guardrail passed
