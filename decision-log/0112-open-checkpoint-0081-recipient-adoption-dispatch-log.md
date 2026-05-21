# Decision 0112: Open Checkpoint 0081 Recipient Adoption Dispatch Log

## Status

accepted

## Date

2026-04-27

## Decision

Open a repo-safe dispatch log for the checkpoint 0081 recipient adoption request.

This decision follows decision `0111`, which prepared the recipient adoption request. The dispatch log records whether the request is ready, sent through an approved channel, received, or blocked by legal/privacy status.

This decision does not authorize new evidence collection.

## Scope

| Field | Value |
|---|---|
| Checkpoint | `threads_pilot_v1_0081` |
| Dispatch log | `reports/checkpoint-0081-recipient-adoption-dispatch-log.md` |
| Recipient adoption request | `reports/checkpoint-0081-recipient-adoption-request.md` |
| Recipient adoption tracker | `reports/checkpoint-0081-recipient-adoption-tracker.md` |
| Package | `/Users/iKev/Downloads/checkpoint-0081-cib-approved-package.zip` |
| Checksum handoff | `/Users/iKev/Downloads/checkpoint-0081-cib-approved-package.zip.sha256` |
| New evidence collection | no |

## Allowed Dispatch Tracking

The dispatch log may track:

- repo-safe recipient class;
- repo-safe recipient alias or role;
- dispatch status;
- sent date;
- response status;
- whether the adoption tracker has been updated;
- repo-safe evidence location.

The dispatch log should not track personal emails, private contact details, raw Threads evidence, stakeholder case IDs, exact controlled-store paths, or credentials.

## Sharing Gate

| Recipient class | Gate |
|---|---|
| CIB/internal reviewer | ready to dispatch through approved internal/CIB channel |
| Technical/governance reviewer | ready to dispatch through approved internal review channel |
| Broader external recipient | legal/privacy status must be recorded before dispatch |
| Public release | not authorized |

## Non-Authorizations

This decision does not authorize:

- item `0082` or later;
- new confirmed-pointer intake;
- broad browser-session expansion;
- crawler/search-query candidate discovery;
- account/profile graph capture;
- private-message access;
- landing-page or redirect-chain capture;
- embedding or model training;
- production detection;
- legal fraud determinations;
- public release;
- raw evidence in git.

## Next Step

Send the adoption request through an approved channel outside git. After sending, update `reports/checkpoint-0081-recipient-adoption-dispatch-log.md` with repo-safe dispatch status.

When a response arrives, update `reports/checkpoint-0081-recipient-adoption-tracker.md`.
