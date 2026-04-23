# Governance

This folder records data handling, authorization, privacy, platform, and evidence-boundary decisions for the Threads scam-content research project.

## Current Status

As of `2026-04-23`:

- synthetic examples are approved for templates, calibration, and tooling dry runs
- no real Threads evidence has been approved for collection
- no automated collection, scraping, crawling, browser automation, bulk export, landing-page crawling, or redirect expansion is approved
- raw evidence must not be committed to git

## Current Governance Records

| File | Purpose |
|---|---|
| `data-governance.md` | Main data-handling policy and collection boundary. |
| `source-intake-register.md` | Candidate source review before authorization and collection. |
| `pilot-authorization-register.md` | Register of pilot source approvals, pending requests, and decisions. |

## Required Before Real Pilot Data

Before the 50-item pilot begins:

1. Complete `templates/data_authorization_request.md`.
2. Complete `templates/source_candidate_intake.md`.
3. Record the candidate in `source-intake-register.md`.
4. Build `templates/source_sampling_frame_template.csv`.
5. Record the decision in `pilot-authorization-register.md`.
6. Complete `docs/26-pilot-go-no-go-checklist.md`.
7. Complete `templates/real_pilot_readiness_review.md` using `docs/35-real-pilot-readiness-review.md`.
8. Complete `templates/pilot_batch_work_order.md`.
9. Confirm raw evidence storage outside git.
10. Confirm redaction, access, retention, and sharing rules.

If any item is unresolved, the project remains synthetic-only.
