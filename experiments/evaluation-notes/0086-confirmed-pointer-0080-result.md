# Confirmed Pointer 0080 Result

## Purpose

Record the repo-safe result for one CIB/project-owner confirmed Threads scam pointer.

This note contains no raw Threads content, full item URL, raw handle, raw stock names, raw stock codes, price values, screenshot, raw reply text, credential, browser artifact, storage-state material, exact controlled-store path, or stakeholder case ID.

## Result

| Field | Value |
|---|---|
| Item ID | `threads_pilot_v1_0080` |
| Source path | single confirmed pointer intake |
| Capture run | `CAPTURE-THREADS-PILOT-V1-0080-FULL-THREAD` |
| Decision link | `0102-authorize-single-confirmed-pointer-0080-intake` |
| Label after second review | `scam` |
| Risk after second review | `high` |
| Evidence family | past-performance profit proof plus no-fee wealth-authority trust funnel |
| Strict validation | pass: `manual_record_0080.json` and 77-record local aggregate, 0 errors, 0 warnings |

## Controlled Full-Thread Capture

The controlled browser run preserved approved browser-rendered raw evidence in the controlled store:

- source pointer;
- browser-rendered body text;
- browser-rendered HTML;
- screenshot;
- visible text blocks;
- manual extracted full-text review artifact.

The accepted capture recorded 6 `[dir='auto']` text blocks, 25 visible text blocks, and 7 hrefs. The `article` selector returned 0, so the preserved evidence relies on body text, visible text blocks, HTML, and screenshot rather than `article` nodes.

No visible replies/comments loaded in the approved capture after scrolling. Treat this as unavailable/absent-at-capture, not as proof that no reply funnel exists.

## Interpretation

This case reinforces a confirmed scam-rule combination:

- prior named stock recommendations are presented as correct;
- positive limit-up or percentage outcomes are used as proof;
- screenshot-style table evidence makes the proof visually concrete;
- followers are claimed to have achieved an extreme luxury outcome;
- the poster uses no-fee, financial-freedom, and friendship-sharing language to lower suspicion.

The key lesson is that a no-fee claim does not reduce risk when it appears inside a stock-picking performance funnel. It can be part of the trust-building mechanism that makes later stock picks, private contact, or group conversion feel safer.

## Rule Boundary

Do not label ordinary performance review, ordinary stock commentary, or transparent financial education as `scam` from this pattern alone.

Escalation requires convergence, especially CIB/stakeholder confirmation or multiple visible signals such as:

- named prior picks;
- limit-up / percentage-gain / profit-table proof;
- screenshot-style proof;
- "followers got rich" or luxury-result claims;
- no-fee / already financially free / just-sharing authority language;
- contact, private-message, group, code, or reply-gated conversion cues if present.

## Validation

Commands run after record build:

```bash
.venv/bin/python scripts/build_manual_collection_record.py data/interim/manual_entry_0080.json --output data/interim/manual_record_0080.json --ack-controlled-details --allow-governance-warnings
python3 scripts/validate_thread_dataset.py data/interim/manual_record_0080.json --strict
python3 scripts/validate_thread_dataset.py data/interim/manual_records_checkpoint_0080.jsonl --strict
```

Results:

- item validation: 1 checked, 0 errors, 0 warnings
- aggregate validation: 77 checked, 0 errors, 0 warnings
- aggregate labels: 34 `scam`, 24 `non_scam`, 16 `uncertain`, 3 `insufficient_evidence`
- aggregate risk: 34 `high`, 9 `medium`, 34 `low`
- manual entry build: 0 governance errors, 0 governance warnings, 0 schema errors, 0 schema warnings
