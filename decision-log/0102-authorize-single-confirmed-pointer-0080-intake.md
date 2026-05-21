# Decision 0102: Authorize Single Confirmed Pointer 0080 Intake

## Status

Accepted.

## Date

2026-04-27

## Decision

Authorize a single controlled full-thread capture and repo-safe rule extraction for item `threads_pilot_v1_0080`.

The source was supplied by the project owner as a CIB-confirmed scam pointer. This decision authorizes only this one supplied pointer and does not reopen browser search, crawler expansion, or broad source discovery.

## Scope

| Field | Value |
|---|---|
| Item | `threads_pilot_v1_0080` |
| Intake type | single confirmed pointer |
| Source type | CIB/project-owner confirmed Threads pointer |
| Capture path | approved browser-rendered/session-aware path |
| Required surfaces | top-level post, available replies/comments, screenshot/image evidence where visible |
| Raw evidence location | controlled store only |
| Repo-visible output | redacted derived fields and rule summary only |

## Explicit Non-Authorizations

This decision does not authorize:

- item `0081` or later;
- broad browser-session expansion;
- crawler/search-query candidate discovery;
- account/profile graph capture;
- private-message access;
- landing-page or redirect-chain capture;
- embedding or model training;
- production detection;
- legal fraud determinations;
- raw Threads URLs, handles, screenshots, raw post text, raw reply text, stock names, stock codes, price values, browser/session artifacts, credentials, or exact controlled-store paths in git.

## Required Handling

- Preserve raw browser-rendered evidence only in the controlled store.
- Record whether replies/comments were visible, unavailable, hidden, deleted, or platform-restricted.
- Use redacted repo-safe fields for manual entry and manual record.
- Run strict validation before including the item in any local aggregate.
- Extract reusable scam-rule families without overgeneralizing ordinary stock discussion.

## Decision Boundary

This decision supports rule learning from one confirmed pointer. It is not a prevalence estimate and does not authorize additional collection.
