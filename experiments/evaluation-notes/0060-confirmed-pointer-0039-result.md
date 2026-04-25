# Confirmed Pointer 0039 Result

## Purpose

Record the repo-safe result for the next confirmed Threads scam pointer.

This note contains no raw Threads content, full item URL, raw handle, raw contact handle, screenshot, raw reply text, credential, browser artifact, storage-state material, raw storage path, or stakeholder case ID.

## Result

| Field | Value |
|---|---|
| Item ID | `threads_pilot_v1_0039` |
| Source path | confirmed scam pointer intake |
| Capture run | `CAPTURE-THREADS-PILOT-V1-0039-FULL-THREAD` |
| Decision link | `0051-record-lifestyle-trust-market-reassurance-funnel-rule` |
| Label after second review | `scam` |
| Risk after second review | `high` |
| Evidence family | `lifestyle_trust_market_reassurance_funnel` |
| Strict validation | pass: `manual_record_0039.json` and 39-record aggregate, 0 errors, 0 warnings |

## Controlled Full-Thread Capture

The controlled browser run preserved the approved browser-rendered raw evidence in the controlled store:

- source pointer
- browser-rendered body text
- browser-rendered HTML
- screenshot
- visible text blocks
- href list

The accepted capture recorded 50 `[dir='auto']` text blocks, 121 visible text blocks, and 44 hrefs. The `article` selector returned 0, so the preserved raw evidence relies on body text, visible text blocks, HTML, and screenshot rather than `article` nodes.

## Interpretation

This case adds a lifestyle-trust market-reassurance funnel family. The top-level post mixes lifestyle warmth with market panic interpretation, reassurance, and concrete buy/hold/add/low-buy guidance. Selected replies include follower trust and repeated contact/group hijack behavior.

The rule should remain narrow: ordinary lifestyle posts or ordinary market commentary are not scam-like by themselves. The risk signal is the convergence of lifestyle trust, market fear reassurance, trading instruction, and reply-level funnel/hijack context.

## Validation

Commands run after record build:

```bash
python3 scripts/validate_thread_dataset.py data/interim/manual_record_0039.json --strict
python3 scripts/validate_thread_dataset.py data/interim/manual_records_checkpoint_0039.jsonl --strict
python3 scripts/audit_thread_dataset.py data/interim/manual_records_checkpoint_0039.jsonl
.venv/bin/python scripts/run_rule_baseline.py data/interim/manual_records_checkpoint_0039.jsonl --variant all --run-name checkpoint-0039-lifestyle-trust-reassurance-smoke-v2 --output-dir experiments/baselines/outputs
```

Results:

- item validation: 1 checked, 0 errors, 0 warnings
- aggregate validation: 39 checked, 0 errors, 0 warnings
- aggregate labels: 21 `non_scam`, 5 `uncertain`, 12 `scam`, 1 `insufficient_evidence`
- aggregate risk: 23 `low`, 4 `medium`, 12 `high`
- baseline all-signal smoke v2: precision 0.667, recall 1.000, F1 0.800, 6 false positives, 0 false negatives
- item `0039` baseline prediction: `scam_like` / `high`
- item `0039` baseline reasons include `LIFESTYLE_TRUST_MARKET_REASSURANCE_FUNNEL`, `REPLY_IMPERSONATION_CONTACT_HIJACK`, `PRIVATE_REDIRECT`, `CONTACT_HANDLE_PRESENT`, `MARKET_DIRECTION_HERDING_CHORUS`, `INDIVIDUAL_STOCK_ADVICE_REPLY_FUNNEL`, `REPLY_FUNNEL_PATTERN`, and `MULTI_SIGNAL_CONVERGENCE`
- item `0039` total score: 35.5; high guardrail passed
