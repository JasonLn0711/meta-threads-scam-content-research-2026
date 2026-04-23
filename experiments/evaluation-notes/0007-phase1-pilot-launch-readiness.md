# Phase 1 Pilot Launch Readiness

## Objective

Test whether the repo is operationally ready to launch governed Phase 1 evidence work without expanding scope.

This is an operational readiness note, not a model experiment. It does not authorize collection, scraping, browser automation, live ingestion, production scoring, or legal fraud determinations.

## Current Status

As of `2026-04-23`:

- repo structure, governance posture, schema, annotation guidance, baseline tooling, calibration tooling, and synthesis tooling exist
- local workspace initializer exists
- pilot preflight verifier exists
- manual collection assistant exists for manually supplied local fields
- first 10-15 item checkpoint protocol exists
- item-level controlled pilot artifacts, if present, live only in the outside-git controlled store; no raw or controlled Threads evidence is committed here
- controlled launch details are no longer the named blocker for the approved path; controlled rehearsal, redaction review, and checkpoint discipline are the next blockers

The latest repo-only preflight observed during planning produced `0 ERROR`, with expected warnings for missing local workspace, missing controlled-details acknowledgement, and dirty worktree.

## Dependencies

Readiness depends on:

- completed controlled launch record outside git
- exact source/source category, raw storage, access list, retention/deletion rule, redaction, screenshot, OCR, URL/link, and handle/contact policies
- approved collector, annotator, reviewer, adjudicator, and research engineer IDs
- initialized ignored local workspace
- item-1 preflight with `ERROR: 0`
- 1-2 item manual collection rehearsal
- 5-item annotator calibration
- first 10-15 item checkpoint before 50-item completion

## Expected Outputs

Repo-safe outputs:

- updated controlled launch template
- local workspace and preflight instructions
- manual rehearsal checklist
- annotator calibration packet template
- first checkpoint review template
- Phase 1 runbook
- non-sensitive launch decision note

Local-only outputs after human launch signoff:

- `data/interim/threads_pilot_v1_collection_log.csv`
- `data/interim/threads_pilot_v1_annotations.csv`
- `data/interim/manual_record_0001.json`
- `data/processed/calibration_agreement.md`
- `data/processed/calibration_disagreements.csv`
- `data/processed/threads_pilot_v1_checkpoint_audit.md`

Do not commit local-only outputs if they contain item-level real evidence.

## Risk Notes

| Risk | Readiness control |
|---|---|
| Controlled details fabricated or stored in git | Filled controlled record stays outside git; repo only references its existence. |
| Collection begins before storage/access/retention/redaction are complete | `--ack-controlled-details` is required and human signoff is explicit. |
| Manual collection drifts into unapproved context | Rehearsal checklist and assistant governance checks catch profile, landing-page, redirect, and automation pressure. |
| Annotation begins before labels are stable | 5-item calibration and disagreement review are required. |
| Team jumps to 50 too early | First 10-15 item checkpoint is a hard gate. |
| Baseline outputs overclaim value | Baseline and synthesis remain local, aggregate, and post-QA only. |

## Readiness Criteria

Launch is ready for the first 10-15 items only when:

- controlled launch record is complete outside git
- local workspace is initialized
- item-1 preflight has `ERROR: 0`
- rehearsal passes strict validation and redaction review
- calibration has no dangerous unresolved label drift
- all participants know that raw evidence and sensitive details stay out of git

Readiness for 50 items requires the additional first checkpoint decision `continue_to_50` or `continue_with_limits`.

## Failure To Launch Safely

Launch fails safely if any of these occur:

- controlled launch details are incomplete
- exact raw storage/access/retention/redaction policy is missing
- raw evidence, screenshots, URLs, handles, credentials, browser data, or sensitive case material enters git
- preflight reports any `ERROR`
- rehearsal requires unapproved profile/account/landing-page/redirect-chain context
- calibration shows repeated primary-label drift
- checkpoint review does not explicitly permit continuation beyond 10-15 items

Failure to launch safely means the repo remains available for synthetic dry runs, guideline updates, and governance repair only.
