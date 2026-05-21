# Decision 0087: Authorize Aggressive Dedupe-First Browser Candidate Quality Run 0044

## Status

Accepted.

## Decision

Authorize run `0044` as an aggressive but bounded browser-session candidate-quality test.

This is not an official scam expansion and does not authorize automatic creation of official selected items.

## Scope

| Field | Value |
|---|---|
| Run | `0044` |
| Source | approved browser session |
| Goal | candidate quality test and negative/calibration case discovery |
| Candidate review cap | 200 candidates maximum |
| Candidate review target | 180-200 candidates |
| Local selected candidate cap | 180 candidates maximum |
| Local selected candidate target | 150-180 candidates |
| Official item cap | 0 |
| Required gate | dedupe-first plus full-thread/reply-ready |
| Query rule | browser query diversification required |
| Raw output | controlled store only |
| Manual entry creation | no |
| Official checkpoint promotion | no |

## Rationale

CIB approved a more aggressive candidate-quality pass. Negative or non-scam candidates are useful as calibration examples, false-positive pressure, and future hard-negative candidates. They should be recorded as controlled local candidate traces unless a later decision authorizes official item creation.

## Guardrails

- Query terms remain retrieval hints only.
- Dedupe-first review is required before local selection.
- Full-thread/reply-ready status must be attempted or recorded as unavailable.
- Negative, non-scam, uncertain, and insufficient-evidence outcomes are valid controlled results.
- Do not create `manual_entry_0076` or any new official item from run `0044`.
- Do not capture private messages, profile graph, landing pages, redirect chains, credentials, or browser/session artifacts into git.

## Consequence

Run `0044` can execute as a controlled-store-only candidate-quality test. Repo-visible output is limited to aggregate counts, method findings, gate status, and next-step decision implications.
