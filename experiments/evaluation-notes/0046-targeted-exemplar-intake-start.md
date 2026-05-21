# Targeted Exemplar Intake Start

## Purpose

Record the repo-safe start note for targeted redacted exemplar intake before item `0028`.

This note contains no raw Threads content, item URLs, handles, screenshots, cookies, tokens, browser profiles, HAR files, raw visible text, raw reply text, raw storage paths, source case IDs, or sensitive investigative material.

## Current Gate

| Check | Result |
|---|---|
| Latest checkpoint | `CHK-THREADS-PILOT-V1-0027` |
| API dry-run | blocked; `META_API_PROBE_URL` missing or empty |
| Browser/session search path | mechanically works but has not yielded final high-risk examples |
| Decision before item `0028` | use API/session-aware readiness or targeted redacted exemplars |
| Selected next path | targeted redacted exemplar intake |

## Intake Decision

Status: `open_targeted_exemplar_intake`.

The intake requests 1 to 3 targeted redacted high-risk exemplars or exemplar-like pointers from CIB/stakeholders. The first acceptable exemplar may become local item `0028` only after redaction, build, strict validation, and second review.

## Requested Evidence

Preferred exemplar families:

- reply/comment-driven scam-like examples;
- anti-scam camouflage plus investment/profit funnel;
- link/contact/private-channel migration examples;
- wallet/deposit/payment or credential-risk examples;
- report-worthy high-risk scam-like Threads examples known to CIB/stakeholders.

## Required Before Item 0028

- Receive at least one approved exemplar or pointer.
- Confirm source owner and redaction owner.
- Keep raw/source material outside git.
- Fill only approved redacted local fields.
- Build `manual_record_0028.json`.
- Strict-validate the item and aggregate.
- Complete second review before counting.
