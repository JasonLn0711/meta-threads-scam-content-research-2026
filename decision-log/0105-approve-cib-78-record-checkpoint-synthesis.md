# Decision 0105: Approve CIB 78-Record Checkpoint Synthesis

## Status

accepted

## Date

2026-04-27

## Decision

CIB approval is recorded for moving the current 78-record local adjudicated aggregate into a repo-safe research checkpoint synthesis.

The checkpoint should be described as:

```text
CIB-approved 78-record research checkpoint
```

It must not be described as a legal fraud determination, production detector, prevalence estimate, or authorization for new collection.

## Scope

| Field | Value |
|---|---|
| Checkpoint | `threads_pilot_v1_0081` |
| Dataset file | `data/interim/manual_records_checkpoint_0081.jsonl` |
| Records | 78 |
| Latest included item | `threads_pilot_v1_0081` |
| Approval source | CIB approval as recorded by project owner |
| Synthesis artifact | `experiments/evaluation-notes/0089-checkpoint-0081-cib-approved-synthesis.md` |
| New evidence collection | no |
| Browser/crawler expansion | no |

## Rationale

The 78-record aggregate now combines:

- the previously approved checkpoint base;
- local hard-negative calibration;
- completed second review of existing ambiguous, insufficient, and medium-risk records;
- two CIB/project-owner confirmed pointer captures with strict-valid local records.

CIB has approved turning this local adjudicated state into a checkpoint synthesis, so the repo should stop treating it merely as an internal queue state.

## Required Handling

- Keep the synthesis repo-safe and aggregate-level.
- Include validation, audit, and baseline-smoke provenance.
- Keep raw Threads URLs, handles, screenshots, raw post text, raw reply text, contact IDs, stock names, stock codes, price values, credentials, browser/session artifacts, and exact controlled-store paths out of git.
- Preserve duplicate and evidence-sufficiency caveats.
- Preserve the distinction between scam-like research labels and legal fraud determinations.

## Non-Authorizations

This decision does not authorize:

- item `0082` or later;
- new source discovery;
- broad browser-session expansion;
- crawler/search-query candidate discovery;
- account/profile graph capture;
- private-message access;
- landing-page or redirect-chain capture;
- embedding or model training;
- production detection;
- legal fraud determinations;
- raw evidence in git.

## Next Step

Create the 78-record checkpoint synthesis and update the run index so reviewers can find the current CIB-approved research checkpoint.
