# Decision 0101: Authorize Existing Ambiguous And Medium-Risk Second Review

## Status

accepted

## Date

2026-04-26

## Decision

Authorize a bounded second-review queue for existing checkpoint 0076 records with any of:

- `uncertain` label;
- `insufficient_evidence` label;
- `medium` risk.

This decision is review-only. It does not authorize new evidence collection.

## Scope

| Field | Value |
|---|---|
| Dataset | `manual_records_checkpoint_0076.jsonl` |
| Review queue | `data/interim/review_queue_checkpoint_0076_uncertain_insufficient_medium.csv` |
| Queue size | 35 records |
| Source | existing redacted records only |
| New capture | no |
| New crawler/browser search | no |
| Manual record rebuild | only after explicit adjudication result |

## Rationale

Checkpoint 0076 contains many unresolved or medium-risk records. Before adding new evidence, reviewers should decide whether existing redacted evidence can resolve any of these cases into `scam`, `non_scam`, or a better-supported `uncertain`/`insufficient_evidence` status.

CIB policy favors avoiding false negatives, but the repo still needs evidence-based adjudication. Medium-risk and uncertain cases are the right place to improve recall without expanding collection.

## Review Questions

For each queued item:

1. Does existing redacted evidence support `scam` / `high`?
2. Does existing redacted evidence support `non_scam` / `low`?
3. Should it remain `uncertain` because the evidence is mixed?
4. Should it remain `insufficient_evidence` because decisive context is missing?
5. Is controlled full-thread/reply capture required before any label change?

## Non-Authorizations

This decision does not authorize:

- item `0080` or later;
- new source discovery;
- browser/crawler expansion;
- account/profile graph capture;
- landing-page or redirect-chain capture;
- private-message access;
- embedding or model training;
- production detection;
- legal fraud determinations;
- raw Threads URLs, handles, screenshots, raw text, stock names, stock codes, price values, credentials, browser/session artifacts, or controlled-store paths in git.

## Required Next Step

Create the work order and use the review queue for item-by-item second review.

Do not rewrite labels or rebuild aggregate records until the adjudication outcome is recorded.
