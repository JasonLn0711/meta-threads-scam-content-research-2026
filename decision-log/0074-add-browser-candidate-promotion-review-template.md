# Decision 0074: Add Browser Candidate Promotion Review Template

## Status

Accepted.

## Decision

Add `templates/browser_candidate_promotion_review.md` as the required repo-safe review worksheet for the dedupe-first/full-thread-ready gate.

## Context

Decision 0073 adopted the gate after run `0039` showed that aggressive browser-session search can create strict-valid but duplicate or context-thin candidates.

The gate needed an operational template so future reviewers can consistently record authorization, access, dedupe, source context, reply context, evidence attribution, redaction, validation, and second-review outcomes.

## Consequence

Future browser-session candidate promotion should use the template before any candidate becomes an official selected item or checkpoint record.

The template is not raw evidence storage. Raw candidate evidence remains in the approved controlled store.
