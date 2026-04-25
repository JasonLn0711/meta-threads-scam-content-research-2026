# Decision 0028: Select Scoped Evidence-Path Study

## Date

2026-04-25

## Decision

Select a scoped evidence-path study before any further item 0017 attempt.

The next run should not collect a new item yet. It should prepare a narrow run design that evaluates whether item 0017 can become reviewable through the smallest evidence-scope change:

1. domain-only visible-link or redirect-category evidence, and
2. narrow reply-context feasibility review.

Screenshots/OCR, landing-page capture, broad profile review, broad comment capture, and full redirect-chain crawling remain out of scope until a later run record explicitly authorizes them.

## Context

Text-only visible search-result methods failed across run 0010 and run 0011. Run 0011 also showed that query echo and interface/search text can masquerade as candidate content unless explicitly filtered.

The project needs to decide whether the problem is:

- candidate retrieval,
- candidate extraction,
- evidence field scope, or
- source-path suitability.

The evidence-path study should answer that question before another collection attempt.

## Options Considered

| Option | Decision |
|---|---|
| Stop item 0017 extension entirely | Deferred; too early to stop before one scoped evidence-path study. |
| Continue text-only visible search-result diagnostics | Rejected; repeated low-yield path. |
| Add broad replies/comments | Rejected; too privacy-heavy for the next step. |
| Add screenshots/OCR | Rejected for now; higher privacy/storage burden and OCR quality risk. |
| Add landing-page or redirect-chain crawling | Rejected for now; scope can expand quickly. |
| Add domain-only visible-link/redirect-category evidence plus narrow reply-context feasibility review | Accepted as the smallest next evidence-path study. |

## Rationale

Domain-only link or redirect-category evidence may identify funnel behavior without storing full raw URLs. A narrow reply-context feasibility review may determine whether search-result text lacks the context needed for a research label.

This study remains proportionate because it does not authorize broad collection, screenshots/OCR, landing-page capture, profile review, raw URL retention, or item 0018 advancement.

## Consequences

- Item 0017 remains unaccepted.
- Item 0018 remains blocked.
- A new run record is required before any further item 0017 attempt.
- The new run must state exact field limits, raw-storage limits, stop conditions, and redaction rules.
- Raw candidate text, full URLs, handles, screenshots, cookies, session material, and raw API responses stay outside git.

## Follow-Up

Open run 0012 as an evidence-path design run. It should:

1. define the domain-only link/redirect-category field boundary;
2. define what "narrow reply-context feasibility" means and what remains prohibited;
3. prohibit screenshots/OCR, landing pages, profile review, broad comments, and full redirect-chain capture;
4. run no collection until the run record is reviewed;
5. keep item 0018 blocked.
