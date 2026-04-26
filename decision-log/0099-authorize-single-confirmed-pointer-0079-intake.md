# Decision 0099: Authorize Single Confirmed Pointer 0079 Intake

## Status

accepted

## Date

2026-04-26

## Decision

Authorize one narrow stakeholder-confirmed Threads pointer intake for item `0079`.

This decision is limited to one supplied Threads post and its available reply/comment context. It reopens confirmed-pointer intake only for this single item and does not reopen broad collection.

## Scope

| Field | Value |
|---|---|
| Intake type | single confirmed pointer |
| Prospective item | `threads_pilot_v1_0079` |
| Selected path exception | `targeted_confirmed_pointer_tranche`, capped to 1 item |
| Review cap | 1 supplied source pointer |
| Selected item cap | 1 item |
| Required context | top-level post plus available replies/comments |
| Required review | redacted rule extraction, second review, strict validation if manual record is built |

## Rationale

The supplied pointer is asserted by the stakeholder as a scam post. Static public metadata exposed top-level post signals around prior stock-pick performance proof, a hidden next-stock code, catalyst/technical claims, and a public keyword/comment gate.

Because decision 0096 blocked new evidence by default, this decision records the explicit narrow exception before any item `0079` promotion.

## Current Derived Rule Family

Apply the existing candidate signal family `hidden_stock_code_past_performance_lure` with an explicit co-signal:

- `comment_code_lead_magnet`

Repo-safe rule statement:

```text
Past buy/sell or stock-pick performance proof is used to establish trading authority, then the post teases an unnamed next stock, hidden code, or "number" as a high-value opportunity and asks readers to comment a keyword/phrase so the poster can share details individually.
```

This is not a standalone legal fraud determination. It is a scam-risk signal that should be combined with other evidence such as private-channel migration, visible contact handles, external links, repeated account behavior, or individualized stock advice in replies.

## Capture Status

Static public metadata inspection recovered top-level post-level signals only. It did not produce reliable full reply/comment capture.

Full rule confirmation from replies/comments remains pending until controlled browser-rendered/session-aware capture succeeds.

## Explicit Non-Authorizations

This decision does not authorize:

- more than item `0079`;
- broad browser-session expansion;
- crawler expansion;
- account/profile graph capture;
- landing-page or redirect-chain capture;
- private-message access;
- embedding or model training;
- production detection;
- legal fraud determinations;
- raw Threads URLs, handles, screenshots, raw text, stock names, stock codes, price values, browser/session artifacts, credentials, or controlled-store paths in git.

## Required Next Step

Open a repo-safe run record for item `0079`, preserve raw evidence only in the controlled store if capture is performed, and keep repo-visible outputs limited to redacted rule-family and validation status.
