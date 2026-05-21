# Decision 0097: Authorize Single Confirmed Pointer 0077 Intake

## Status

accepted

## Date

2026-04-26

## Decision

Authorize one narrow stakeholder-confirmed Threads pointer intake for item `0077`.

This decision is limited to one supplied Threads post and its available reply/comment context. It reopens confirmed-pointer intake only for this single item and does not reopen broad collection.

## Scope

| Field | Value |
|---|---|
| Intake type | single confirmed pointer |
| Prospective item | `threads_pilot_v1_0077` |
| Selected path exception | `targeted_confirmed_pointer_tranche`, capped to 1 item |
| Review cap | 1 supplied source pointer |
| Selected item cap | 1 item |
| Required context | top-level post plus available replies/comments |
| Required review | redacted rule extraction, second review, strict validation if manual record is built |

## Rationale

The supplied pointer is asserted by the stakeholder as a scam post. It appears to teach a reusable evidence family around insider/supply-chain authority, major-brand procurement claims, and stock-purchase persuasion.

Because decision 0096 blocked new evidence by default, this decision records the explicit narrow exception before any item `0077` promotion.

## Current Derived Rule Family

Adopt `supply_chain_insider_stock_lure` as a candidate signal family:

```text
Claimed insider, procurement, supplier, or confidential corporate-meeting access is used to justify a specific stock opportunity, often with major-brand authority, exclusive-supplier framing, technical proof, exact price/position cues, or all-in personal buying behavior.
```

This is not a standalone legal fraud determination. It is a scam-risk signal that should be combined with other evidence such as private-channel migration, comment/reply gating, hidden-stock teasing, exact target/price claims, or repeated account behavior.

## Capture Status

Static public metadata inspection recovered top-level post-level signals only. It did not produce reliable full reply/comment capture.

Full rule confirmation from replies/comments remains pending until controlled browser-rendered/session-aware capture succeeds.

## Explicit Non-Authorizations

This decision does not authorize:

- more than item `0077`;
- broad browser-session expansion;
- crawler expansion;
- account/profile graph capture;
- landing-page or redirect-chain capture;
- private-message access;
- embedding or model training;
- production detection;
- legal fraud determinations;
- raw Threads URLs, handles, screenshots, raw text, browser/session artifacts, credentials, or controlled-store paths in git.

## Required Next Step

Open a repo-safe run record for item `0077`, preserve raw evidence only in the controlled store if capture is performed, and keep repo-visible outputs limited to redacted rule-family and validation status.
