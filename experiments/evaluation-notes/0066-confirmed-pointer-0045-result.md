# Confirmed Pointer 0045 Result

## Purpose

Record the repo-safe result for the next confirmed Threads scam pointer.

This note contains no raw Threads content, full item URL, raw handle, raw stock names, raw stock codes, brand names, price values, visible contact ID, screenshot, raw reply text, credential, browser artifact, storage-state material, raw storage path, or stakeholder case ID.

## Result

| Field | Value |
|---|---|
| Item ID | `threads_pilot_v1_0045` |
| Source path | confirmed scam pointer intake |
| Capture run | `CAPTURE-THREADS-PILOT-V1-0045-FULL-THREAD` |
| Decision link | `0057-record-brand-patent-extreme-roi-contact-funnel-rule` |
| Label after second review | `scam` |
| Risk after second review | `high` |
| Evidence family | `brand_patent_extreme_roi_contact_funnel` |
| Strict validation | pass: `manual_record_0045.json` and 45-record aggregate, 0 errors, 0 warnings |

## Controlled Full-Thread Capture

The controlled browser run preserved the approved browser-rendered raw evidence in the controlled store:

- source pointer
- browser-rendered body text
- browser-rendered HTML
- screenshot
- visible text blocks
- href list

The accepted capture recorded 21 `[dir='auto']` text blocks, 69 visible text blocks, and 15 hrefs. The `article` selector returned 0, so the preserved raw evidence relies on body text, visible text blocks, HTML, and screenshot rather than `article` nodes.

## Interpretation

This case adds a brand/patent extreme-ROI contact-funnel family. The public thread combines mass stock-specific buy/target instructions, loss-rescue language, extreme ROI framing, major-brand/patent/catalyst authority packaging, visible contact routing, and author reply reinforcement for private follow-up.

The rule should remain narrow: ordinary company-news catalysts, analyst target prices, or technology-sector commentary are not scam-like by themselves. The risk signal is the convergence of brand/patent authority, extreme small-stake-to-large-return framing, and contact/action-gated delivery.

## Validation

Commands run after record build:

```bash
python3 scripts/validate_thread_dataset.py data/interim/manual_record_0045.json --strict
python3 scripts/validate_thread_dataset.py data/interim/manual_records_checkpoint_0045.jsonl --strict
python3 scripts/audit_thread_dataset.py data/interim/manual_records_checkpoint_0045.jsonl
.venv/bin/python scripts/run_rule_baseline.py data/interim/manual_records_checkpoint_0045.jsonl --variant all --run-name checkpoint-0045-brand-patent-extreme-roi-smoke-v2 --output-dir experiments/baselines/outputs
```

Results:

- item validation: 1 checked, 0 errors, 0 warnings
- aggregate validation: 45 checked, 0 errors, 0 warnings
- aggregate labels: 22 `non_scam`, 5 `uncertain`, 17 `scam`, 1 `insufficient_evidence`
- aggregate risk: 24 `low`, 4 `medium`, 17 `high`
- baseline all-signal smoke v2: precision 0.739, recall 1.000, F1 0.850, 6 false positives, 0 false negatives
- item `0045` baseline prediction: `scam_like` / `high`
- item `0045` baseline reasons include `BRAND_PATENT_EXTREME_ROI_CONTACT_FUNNEL`, `PRIVATE_REDIRECT`, `IMPLICIT_DM_CONTACT_REQUEST`, `CONTACT_HANDLE_PRESENT`, `MENTOR_COPYTRADE_LANGUAGE`, `REPLY_FUNNEL_PATTERN`, and `MULTI_SIGNAL_CONVERGENCE`
- item `0045` total score: 24.0; high guardrail passed
