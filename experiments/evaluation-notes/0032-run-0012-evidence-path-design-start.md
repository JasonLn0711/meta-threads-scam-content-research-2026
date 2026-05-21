# Run 0012 Evidence-Path Design Start

## Purpose

Record the repo-safe start condition for run 0012, a design-only evidence-path run after item 0017 text-only methods failed.

This note contains no raw Threads content, item URLs, handles, screenshots, cookies, tokens, browser profiles, HAR files, raw visible text, raw storage paths, credential values, or sensitive investigative material.

## Start Condition

| Check | Result |
|---|---|
| Prior accepted checkpoint | 16 accepted records |
| Item 0017 | excluded local trace only |
| Item 0018 | blocked |
| Prior method result | text-only visible search-result methods failed |
| Selected evidence path | domain-only link/redirect category plus narrow reply-context feasibility |
| Collection in run 0012 | none; design-only |

## Design Decision

```text
design_only_no_collection_until_run_0012_reviewed
```

## Field Boundaries

| Area | Boundary |
|---|---|
| Domain-only link evidence | Allowed only as normalized domain category or redacted domain-only reference in a later run. |
| Redirect category | Allowed only as category without landing-page or redirect-chain capture. |
| Narrow reply context | Feasibility only; no broad replies/comments and no handles in git. |
| Screenshots/OCR | Not allowed in this design. |
| Landing pages | Not allowed in this design. |
| Profile review | Not allowed in this design. |
| Item 0018 | Blocked. |

## Next Required Action

Review run 0012 design. If accepted, open a separate execution run record for at most one item 0017 attempt. Do not collect from this design note.

## Design Review Result

| Check | Result |
|---|---|
| Design reviewed | yes |
| Field boundaries sufficient | yes |
| Collection authorized by run 0012 | no |
| Next run record required | yes; run 0013 |
| Item 0018 | blocked |

## Decision After Review

```text
open_run_0013_scoped_execution_record_only
```
