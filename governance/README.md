# Governance

This folder records data handling, authorization, privacy, platform, and evidence-boundary decisions for the Threads scam-content research project.

## Current Status

As of `2026-04-23`:

- synthetic examples are approved for templates, calibration, and tooling dry runs
- the first real 50-item Threads pilot is approved for bounded launch preparation under `go_with_limits`
- no real Threads evidence has been collected or committed
- exact source, storage, access, retention, and redaction limits must be written into the controlled launch record before the first item
- no automated collection, scraping, crawling, browser automation, bulk export, landing-page crawling, or redirect expansion is approved
- low-speed automated Threads/Meta collection is not accepted without the same recorded legal/platform/stakeholder scope required for any automation
- raw evidence must not be committed to git

## Current Governance Records

| File | Purpose |
|---|---|
| `data-governance.md` | Main data-handling policy and collection boundary. |
| `source-intake-register.md` | Candidate source review before authorization and collection. |
| `pilot-authorization-register.md` | Register of pilot source approvals, pending requests, and decisions. |
| `pilot-launch/` | Non-sensitive launch records for the approved 50-item pilot. |

## Required Before Real Pilot Data

Before the first real item is collected:

1. Complete the controlled launch record with exact source, storage, access, retention, and redaction limits outside git using `templates/controlled_launch_details_template.md` as the blank structure.
2. Confirm raw evidence storage outside git.
3. Confirm redaction, access, retention, and sharing rules.
4. Confirm collector, annotator, reviewer, adjudicator, and research engineer IDs.
5. Create local-only files under ignored `data/interim/`.
6. Start with the first 10-15 item checkpoint before completing all 50 items.

If any item is unresolved, the project remains synthetic-only.
