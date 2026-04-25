# Targeted Exemplar 0028 Result

## Purpose

Record the repo-safe result for the first targeted redacted exemplar after checkpoint `0027`.

This note contains no raw Threads content, full item URL, raw handle, screenshot, raw reply text, credential, browser artifact, storage-state material, raw storage path, or stakeholder case ID.

## Result

| Field | Value |
|---|---|
| Item ID | `threads_pilot_v1_0028` |
| Source path | targeted CIB/stakeholder exemplar intake |
| Intake record | `EXEMPLAR-THREADS-PILOT-V1-0017` |
| Decision link | `0035-record-cib-confirmed-implicit-dm-funnel-rule` |
| Label after second review | `scam` |
| Risk after second review | `high` |
| Evidence family | `implicit_dm_contact_request` |
| Strict validation | pass: `manual_record_0028.json` and 28-record aggregate, 0 errors, 0 warnings |
| Controlled raw capture | complete: run `CAPTURE-THREADS-PILOT-V1-0028-FULL-THREAD` |

## Interpretation

The first accepted targeted exemplar changes the checkpoint interpretation: the prior browser/session search-result runs were useful for boundaries and false-positive pressure, but targeted stakeholder pointers are much higher yield for high-risk calibration.

The key evidence pattern is not a public LINE link, scam URL, or visible handle. The public surface may hide those artifacts and instead ask users to private-message the poster. That means future recall design should treat implicit DM conversion as a review signal when it co-occurs with investment/profit framing or other scam-like evidence.

## Boundary

This item is a calibration exemplar. It does not estimate Threads prevalence and does not authorize broad comment capture, profile review, landing-page crawling, or private-message access.

## Controlled Full-Thread Capture

Run `CAPTURE-THREADS-PILOT-V1-0028-FULL-THREAD` preserved the approved browser-rendered raw evidence in the controlled store:

- source pointer
- browser-rendered body text
- browser-rendered HTML
- screenshot
- visible text blocks
- href list

The accepted capture recorded 54 `[dir='auto']` text blocks, 134 visible text blocks, and 39 hrefs. The `article` selector returned 0, so the preserved raw evidence relies on body text, visible text blocks, HTML, and screenshot rather than `article` nodes.

The capture is limited to content visible to the approved browser session at capture time. Threads displayed that some newly added replies could not be shown, so unavailable or platform-restricted replies are not guaranteed to be preserved.

## Validation

Commands run:

```bash
python3 scripts/validate_thread_dataset.py data/interim/manual_record_0028.json --strict
python3 scripts/validate_thread_dataset.py data/interim/manual_records_checkpoint_0028.jsonl --strict
python3 scripts/audit_thread_dataset.py data/interim/manual_records_checkpoint_0028.jsonl
.venv/bin/python scripts/run_rule_baseline.py data/interim/manual_records_checkpoint_0028.jsonl --variant all --run-name checkpoint-0028-implicit-dm-smoke-v2 --output-dir experiments/baselines/outputs
```

Results:

- item validation: 1 checked, 0 errors, 0 warnings
- aggregate validation: 28 checked, 0 errors, 0 warnings
- aggregate labels: 21 `non_scam`, 5 `uncertain`, 1 `insufficient_evidence`, 1 `scam`
- aggregate risk: 23 `low`, 4 `medium`, 1 `high`
- baseline all-signal smoke after implicit-DM regex patch: 28 items, 22 binary-metric items, 0 false negatives, 6 false positives
