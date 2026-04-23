# Governance

This folder records data handling, authorization, privacy, platform, and evidence-boundary decisions for the Threads scam-content research project.

## Current Status

As of `2026-04-23`:

- synthetic examples are approved for templates, calibration, and tooling dry runs
- the integrated synthetic launch rehearsal has been completed and recorded as tooling evidence only
- the first real 50-item Threads pilot is approved for bounded launch preparation under `go_with_limits`
- CIB-authorized API access and all research-required automation are approved under the controlled launch record and Decision 0018
- item-level controlled pilot artifacts, if present, live only in the outside-git controlled store; no raw or controlled Threads evidence is committed to this repo
- exact source, storage, access, retention, and redaction limits are governed by the outside-git controlled launch record
- unscope automation remains rejected; every API or automation run needs source, field, storage, access, retention, redaction, credential, and audit controls
- raw evidence must not be committed to git

## Current Governance Records

| File | Purpose |
|---|---|
| `data-governance.md` | Main data-handling policy and collection boundary. |
| `source-intake-register.md` | Candidate source review before authorization and collection. |
| `pilot-authorization-register.md` | Register of pilot source approvals, pending requests, and decisions. |
| `pilot-launch/` | Non-sensitive launch records for the approved 50-item pilot. |
| `../decision-log/0017-record-integrated-synthetic-launch-rehearsal.md` | Decision record for the synthetic-only launch rehearsal and remaining real-collection gate. |
| `../decision-log/0018-record-cib-api-and-automation-authorization.md` | Decision record for CIB-authorized API access and automation. |
| `../experiments/evaluation-notes/0008-phase1-synthetic-launch-rehearsal.md` | Synthetic-only integrated rehearsal results. |

## Required Before Controlled Pilot Data Continues

Before controlled pilot data work continues or expands beyond the approved run path:

1. Confirm the controlled launch record with exact source, storage, access, retention, redaction, API credential, automation log, and run-record limits.
2. Confirm raw evidence storage outside git.
3. Confirm redaction, access, retention, automation-run, and sharing rules.
4. Confirm collector, annotator, reviewer, adjudicator, and research engineer IDs.
5. Create local-only files under ignored `data/interim/`.
6. Start with the first 10-15 item checkpoint before completing all 50 items.

If any item is unresolved, pause controlled evidence work and return to synthetic-only tooling or governance repair.

The synthetic rehearsal does not satisfy these requirements. It confirms repo tooling behavior only. Controlled-store files must not be renamed, indexed, or summarized as examples if they are real controlled pilot artifacts.
