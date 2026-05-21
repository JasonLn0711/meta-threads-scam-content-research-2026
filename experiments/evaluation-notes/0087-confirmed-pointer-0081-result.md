# Confirmed Pointer 0081 Result

## Purpose

Record the repo-safe result for one CIB/project-owner confirmed Threads scam pointer.

This note contains no raw Threads content, full item URL, raw handle, raw contact ID, screenshot, raw reply text, credential, browser artifact, storage-state material, exact controlled-store path, or stakeholder case ID.

## Result

| Field | Value |
|---|---|
| Item ID | `threads_pilot_v1_0081` |
| Source path | single confirmed pointer intake |
| Capture run | `CAPTURE-THREADS-PILOT-V1-0081-FULL-THREAD` |
| Decision link | `0104-authorize-single-confirmed-pointer-0081-intake` |
| Label after second review | `scam` |
| Risk after second review | `high` |
| Evidence family | top-level trust-building plus reply-level contact-hijack/private-group funnel |
| Strict validation | pass: `manual_record_0081.json` and 78-record local aggregate, 0 errors, 0 warnings |

## Controlled Full-Thread Capture

The controlled browser run preserved approved browser-rendered raw evidence in the controlled store:

- source pointer;
- browser-rendered body text;
- browser-rendered HTML;
- screenshot;
- visible text blocks;
- controlled full-text/reply review artifact.

The accepted capture recorded 34 `[dir='auto']` text blocks, 90 visible text blocks, and 25 hrefs. The `article` selector returned 0, so the preserved evidence relies on body text, visible text blocks, HTML, and screenshot rather than `article` nodes.

Reply/comment status is `partial_visible`: multiple visible replies were captured, but the UI also indicated hidden replies / view-all affordance. Do not treat the visible capture as the complete platform reply set.

## Interpretation

This case reinforces that scam evidence can be split across the post and replies:

- the top-level post builds trust through humility, non-analyst/no-benefit disclaimers, ordinary-person identity, claimed stock-experience influence, follower profit/joy, and loss-recovery framing;
- the reply layer then contains messaging/contact paths, private-group cues, daily watchlists, holdings viewpoints, free-group language, and social proof that a user was added to a group;
- anti-scam wording in replies can function as camouflage when the same reply publishes the supposed safe contact route.

The rule lesson is not that every humble investment post is scam-like. The risk comes from convergence: trust-building top-level text plus reply-level contact hijack, private-channel redirect, group conversion, or holdings/watchlist funnel cues.

## Rule Boundary

Do not label ordinary investment reflection, ordinary anti-scam warnings, or ordinary community comments as `scam` from this pattern alone.

Escalation requires convergence, especially CIB/stakeholder confirmation or multiple visible signals such as:

- top-level investment authority / trust softening;
- claimed follower profit, follower recognition, or loss-recovery benefit;
- inability-to-reply or message-volume pressure;
- reply-level contact IDs or messaging migration;
- daily watchlist, holdings viewpoint, stock-rescue, or group-entry offers;
- anti-scam camouflage paired with a "safe" contact route;
- fake social proof that the user was already added to a group.

## Validation

Commands run after record build:

```bash
.venv/bin/python scripts/build_manual_collection_record.py data/interim/manual_entry_0081.json --output data/interim/manual_record_0081.json --ack-controlled-details --allow-governance-warnings
python3 scripts/validate_thread_dataset.py data/interim/manual_record_0081.json --strict
python3 scripts/validate_thread_dataset.py data/interim/manual_records_checkpoint_0081.jsonl --strict
```

Results:

- manual entry build: 0 governance errors, 0 governance warnings, 0 schema errors, 0 schema warnings
- item validation: 1 checked, 0 errors, 0 warnings
- aggregate validation: 78 checked, 0 errors, 0 warnings
- aggregate labels: 35 `scam`, 24 `non_scam`, 16 `uncertain`, 3 `insufficient_evidence`
- aggregate risk: 35 `high`, 9 `medium`, 34 `low`

These aggregate counts are an intermediate local snapshot before the final checkpoint 0081 second-review synthesis. The canonical checkpoint 0081 counts are recorded in `experiments/evaluation-notes/0089-checkpoint-0081-cib-approved-synthesis.md` and `reports/checkpoint-0081-approved-package-index.md`.
