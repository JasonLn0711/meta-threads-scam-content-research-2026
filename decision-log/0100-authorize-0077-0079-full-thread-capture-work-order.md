# Decision 0100: Authorize 0077-0079 Full-Thread Capture Work Order

## Status

accepted

## Date

2026-04-26

## Decision

Authorize one bounded controlled full-thread capture work order for existing prospective items `0077-0079`.

This decision does not authorize new source discovery. It only authorizes controlled browser-rendered/session-aware capture attempts for the three already-opened stakeholder-confirmed pointers.

## Scope

| Field | Value |
|---|---|
| Work order | `0049` |
| Items | `0077`, `0078`, `0079` |
| Source type | existing stakeholder-confirmed pointers only |
| Capture cap | 3 supplied source pointers |
| New candidate discovery | no |
| Manual entry build | blocked until capture, redaction, and second review pass |
| Manual record build | blocked until manual entry is accepted |
| Raw evidence location | controlled store only |

## Required Capture Surfaces

Each item needs:

- top-level post capture;
- available replies/comments capture;
- explicit note if replies/comments are unavailable, hidden, deleted, or platform-restricted;
- redacted rule summary;
- second review before any manual entry;
- strict validation if a manual record is built.

## Non-Authorizations

This decision does not authorize:

- item `0080` or later;
- broad browser-session expansion;
- crawler expansion;
- search-query candidate discovery;
- account/profile graph capture;
- landing-page or redirect-chain capture;
- private-message access;
- embedding or model training;
- production detection;
- legal fraud determinations;
- raw Threads URLs, handles, screenshots, raw text, stock names, stock codes, price values, browser/session artifacts, credentials, or controlled-store paths in git.

## Stop Conditions

Stop the work order if:

- controlled browser/session access is not ready;
- capture would require private-message access;
- capture would require account/profile graph review;
- raw evidence cannot be kept out of git;
- replies/comments cannot be captured or explicitly marked unavailable;
- redaction cannot preserve enough evidence for second review.

## Required Next Step

Create the repo-safe work order record and keep item-level status as `capture_pending` until each controlled capture attempt is completed.
