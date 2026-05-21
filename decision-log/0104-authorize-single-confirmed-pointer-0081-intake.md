# Decision 0104: Authorize Single Confirmed Pointer 0081 Intake

## Status

Accepted.

## Date

2026-04-27

## Decision

Authorize a single controlled full-thread/reply capture and repo-safe rule extraction for item `threads_pilot_v1_0081`.

The source was supplied by the project owner as a CIB-confirmed scam pointer. This decision authorizes only this one supplied pointer and does not reopen browser search, crawler expansion, or broad source discovery.

## Scope

| Field | Value |
|---|---|
| Item | `threads_pilot_v1_0081` |
| Intake type | single confirmed pointer |
| Source type | CIB/project-owner confirmed Threads pointer |
| Capture path | approved browser-rendered/session-aware path |
| Required surfaces | top-level post plus visible replies/comments |
| Full-text/reply artifact | required in controlled store |
| Raw evidence location | controlled store only |
| Repo-visible output | redacted derived fields and rule summary only |

## Explicit Non-Authorizations

This decision does not authorize:

- item `0082` or later;
- broad browser-session expansion;
- crawler/search-query candidate discovery;
- account/profile graph capture;
- private-message access;
- landing-page or redirect-chain capture;
- embedding or model training;
- production detection;
- legal fraud determinations;
- raw Threads URLs, handles, screenshots, raw post text, raw reply text, contact IDs, browser/session artifacts, credentials, or exact controlled-store paths in git.

## Required Handling

- Preserve raw browser-rendered evidence only in the controlled store.
- Preserve complete visible top-level post text and visible reply/comment text in controlled-store `extracted_full_text_review.json`.
- Record whether reply/comment capture was complete, partial, unavailable, hidden, or platform-restricted.
- Use redacted repo-safe fields for manual entry and manual record.
- Run strict validation before including the item in any local aggregate.
- Extract reusable scam-rule families without overgeneralizing ordinary stock discussion or ordinary anti-scam warnings.

## Decision Boundary

This decision supports rule learning from one confirmed pointer. It is not a prevalence estimate and does not authorize additional collection.
