# Evidence-Path Study Decision

## Purpose

Record the repo-safe decision from the item 0017 evidence-path study.

This note contains no raw Threads content, item URLs, handles, screenshots, cookies, tokens, browser profiles, HAR files, raw visible text, raw storage paths, credential values, or sensitive investigative material.

## Decision

```text
open_scoped_evidence_path_design_run_0012
```

## Selected Evidence Path

| Evidence path | Status | Rationale |
|---|---|---|
| Domain-only visible-link or redirect-category evidence | selected for scoped study | May reveal funnel behavior without raw URL retention. |
| Narrow reply-context feasibility review | selected for scoped study | May determine whether search-result text lacks needed context. |
| Screenshot/OCR | not selected | Higher privacy/storage burden; requires later explicit scope. |
| Landing-page capture | not selected | Higher scope-expansion risk. |
| Broad profile or comment review | not selected | Too privacy-heavy for next step. |
| Full redirect-chain capture | not selected | Too expansive for next step. |

## Guardrails For Run 0012

- No item 0018.
- No accepted item 0017 until a new scoped run record is opened and reviewed.
- No screenshots/OCR.
- No landing pages.
- No broad profile review.
- No broad comments.
- No full raw URL retention in git.
- No cookies, tokens, browser profiles, HAR files, or raw API responses in git.

## Next Required Action

Open run 0012 as an evidence-path design run. It should specify field boundaries before any collection attempt.
