# Confirmed Pointer 0036 Result

## Purpose

Record the repo-safe result for the next confirmed Threads scam pointer.

This note contains no raw Threads content, full item URL, raw handle, raw contact handle, screenshot, raw reply text, credential, browser artifact, storage-state material, raw storage path, or stakeholder case ID.

## Result

| Field | Value |
|---|---|
| Item ID | `threads_pilot_v1_0036` |
| Source path | confirmed scam pointer intake |
| Capture run | `CAPTURE-THREADS-PILOT-V1-0036-FULL-THREAD` |
| Decision link | `0048-record-reply-impersonation-contact-hijack-rule` |
| Label after second review | `scam` |
| Risk after second review | `high` |
| Evidence family | `reply_impersonation_contact_hijack` |
| Strict validation | pass: `manual_record_0036.json` and 36-record aggregate, 0 errors, 0 warnings |

## Controlled Full-Thread Capture

The controlled browser run preserved the approved browser-rendered raw evidence in the controlled store:

- source pointer
- browser-rendered body text
- browser-rendered HTML
- screenshot
- visible text blocks
- href list

The accepted capture recorded 58 `[dir='auto']` text blocks, 144 visible text blocks, and 49 hrefs. The `article` selector returned 0, so the preserved raw evidence relies on body text, visible text blocks, HTML, and screenshot rather than `article` nodes.

## Interpretation

This case adds a reply-layer impersonation/contact-hijack rule-library family. The top-level post builds trust around humble stock-sharing and no-benefit framing, while selected replies repeatedly redirect readers to contact/group paths for daily lists or holdings viewpoints and use official-contact or anti-scam camouflage.

The rule should preserve attribution uncertainty: the evidence can show thread-level scam risk even if the suspicious contact replies may be impersonation/hijack rather than the top-level poster's own reply.

## Validation

Commands run after record build:

```bash
python3 scripts/validate_thread_dataset.py data/interim/manual_record_0036.json --strict
python3 scripts/validate_thread_dataset.py data/interim/manual_records_checkpoint_0036.jsonl --strict
python3 scripts/audit_thread_dataset.py data/interim/manual_records_checkpoint_0036.jsonl
.venv/bin/python scripts/run_rule_baseline.py data/interim/manual_records_checkpoint_0036.jsonl --variant all --run-name checkpoint-0036-reply-impersonation-hijack-smoke-v2 --output-dir experiments/baselines/outputs
```

Results:

- item validation: 1 checked, 0 errors, 0 warnings
- aggregate validation: 36 checked, 0 errors, 0 warnings
- aggregate labels: 21 `non_scam`, 5 `uncertain`, 9 `scam`, 1 `insufficient_evidence`
- aggregate risk: 23 `low`, 4 `medium`, 9 `high`
- baseline all-signal smoke v2: precision 0.600, recall 1.000, F1 0.750, 6 false positives, 0 false negatives
- item `0036` baseline prediction: `scam_like` / `high`
- item `0036` baseline reasons include `REPLY_IMPERSONATION_CONTACT_HIJACK`, `PRIVATE_REDIRECT`, `CONTACT_HANDLE_PRESENT`, `PSEUDO_OFFICIAL_LANGUAGE`, `REPLY_FUNNEL_PATTERN`, and `MULTI_SIGNAL_CONVERGENCE`
- item `0036` total score: 30.5; high guardrail passed
