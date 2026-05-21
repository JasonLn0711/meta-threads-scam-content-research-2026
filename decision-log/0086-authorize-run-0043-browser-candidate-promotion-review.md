# Decision 0086: Authorize Run 0043 Browser Candidate Promotion Review

## Status

Accepted.

## Decision

Authorize a formal browser-candidate promotion review for the 24 quality-review candidates from run `0043`.

This decision does not automatically promote any candidate into `manual_entry_0076`. It opens the review gate required before any one candidate can be promoted.

## Scope

| Field | Value |
|---|---|
| Source run | `0043` |
| Review candidate count | 24 |
| Source path | approved browser session |
| Candidate reference type | controlled-store local candidate hash/reference |
| Review template | `templates/browser_candidate_promotion_review.md` |
| Required gate | `docs/53-dedupe-first-full-thread-ready-gate.md` |
| Query rule | `docs/54-browser-query-diversification-rule.md` |
| Official item cap for this decision | 1 candidate maximum, only if every promotion gate passes |
| Intended first item if promoted | `manual_entry_0076` |
| Raw output in git | no |

## Required Promotion Conditions

A run `0043` candidate may become `manual_entry_0076` only if all are true:

- authorization gate passes;
- approved browser/session-aware access gate passes;
- query-diversification gate passes;
- dedupe gate passes;
- source-context gate passes;
- reply-context gate passes or replies are explicitly unavailable;
- evidence attribution gate passes;
- redaction gate passes;
- second-review gate passes;
- strict validation passes with 0 errors and 0 warnings.

## Rationale

Run `0043` was intentionally a candidate-quality method test, not an official expansion. It produced enough candidate signal to justify formal review, but candidate discovery is still not labeling.

This decision creates the missing governance step between `quality_review_candidate` and `manual_entry_0076`.

## Consequences

- A controlled-store promotion review packet can be built for the 24 run `0043` quality-review candidates.
- The repo may record only repo-safe aggregate promotion review status.
- No candidate may be promoted if it relies on search terms alone, page-level context not tied to the item, duplicate content, or incomplete source/reply context.
- Negative or non-scam outcomes are valid review results and can be retained as controlled local candidate traces.
