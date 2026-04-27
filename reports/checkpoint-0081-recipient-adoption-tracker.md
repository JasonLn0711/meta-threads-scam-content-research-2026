# Checkpoint 0081 Recipient Adoption Tracker

## Purpose

Track whether allowed recipient classes have accepted checkpoint 0081 for the stated research uses after final handoff.

This tracker is repo-safe. It contains no raw Threads URLs, handles, screenshots, raw post text, raw reply text, contact IDs, stock names, stock codes, price values, credentials, browser/session artifacts, exact controlled-store paths, stakeholder case IDs, personal emails, or private recipient contact details.

## Current Package

| Field | Value |
|---|---|
| Checkpoint | `threads_pilot_v1_0081` |
| Package status | recipient adoption tracking opened; ready for allowed checkpoint use |
| Package directory | `/Users/iKev/Downloads/checkpoint-0081-cib-approved-package` |
| ZIP path | `/Users/iKev/Downloads/checkpoint-0081-cib-approved-package.zip` |
| ZIP SHA-256 | external handoff checksum generated after ZIP rebuild in `/Users/iKev/Downloads/checkpoint-0081-cib-approved-package.zip.sha256` |
| Current handoff decision | `decision-log/0109-record-checkpoint-0081-final-handoff.md` |
| Current tracking decision | `decision-log/0110-open-checkpoint-0081-recipient-adoption-tracking.md` |

## Recipient Classes

| Recipient class | Allowed current use | Current gate |
|---|---|---|
| CIB/internal reviewer | Evidence-system review, annotation-rule calibration, governance review, and future research decision planning | Allowed within checkpoint 0081 research package boundary |
| Technical/governance reviewer | Validation, schema, package, and implementation-readiness review | Allowed within checkpoint 0081 research package boundary |
| Broader external recipient | External review or sharing outside the current internal/CIB boundary | Legal/privacy status must be recorded first |
| Public release | Public posting, open publication, or unrestricted distribution | Not authorized |

## Adoption Record

| Recipient class | Recipient alias or role | Status | Accepted use | Conditions or limits | Date | Evidence location |
|---|---|---|---|---|---|---|
| CIB/internal reviewer |  | pending |  |  |  |  |
| technical/governance reviewer |  | pending |  |  |  |  |
| broader external recipient |  | blocked_until_legal_privacy |  | Legal/privacy status must be recorded before sharing. |  |  |
| public release |  | not_authorized |  | Public release is outside checkpoint 0081 handoff scope. |  |  |

Allowed statuses:

- `pending`
- `received`
- `accepted_for_checkpoint_use`
- `accepted_with_conditions`
- `revision_requested`
- `new_capped_evidence_decision_requested`
- `blocked_until_legal_privacy`
- `not_authorized`

## What Counts As Adoption

Adoption means a named role or repo-safe recipient alias accepts checkpoint 0081 for one or more allowed research uses:

- evidence-system review;
- annotation-rule calibration;
- governance review;
- report/package handoff;
- planning future research decisions.

Adoption does not mean:

- legal fraud determination;
- production detector approval;
- broad external release approval;
- authorization for item `0082` or later;
- authorization for new crawler, browser-session, confirmed-pointer, account/profile, private-message, landing-page, redirect-chain, embedding, or model-training work.

## If A Recipient Requests Changes

Record only repo-safe change requests here. Do not add raw evidence, sensitive recipient details, or controlled-store paths.

| Request | Required repo-safe action | New decision needed? |
|---|---|---|
| Editorial/package correction | Patch relevant report/package docs, rebuild ZIP/checksum, update package QA | Usually no, unless scope changes |
| Legal/privacy review before broader sharing | Record legal/privacy status and constraints | Yes |
| New evidence or item collection | Create a new capped decision before any collection | Yes |
| Model training or production detector work | Create a separate scope decision and risk review | Yes |

## Next Action

When the first allowed recipient response arrives, update the `Adoption Record` table with a repo-safe role or alias, accepted use, conditions, date, and evidence location.

Do not start item `0082` or any new evidence collection from this tracker alone.
