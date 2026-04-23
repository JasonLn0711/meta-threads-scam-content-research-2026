# Decision 0018: Record CIB API And Automation Authorization

## Identity

- Date: 2026-04-23
- Status: accepted
- Owner: Jason

## Decision

Record the CIB Criminal Investigation Bureau authorization amendment that explicitly approves API access and all automation needed for the Threads scam-content research case, subject to the controlled launch record:

- `governance/pilot-launch/threads_pilot_v1_2026-05_controlled_launch_record.md`

This decision supersedes the earlier manual-only pilot limit for this CIB-authorized research case. It does not erase Decision 0016. Decision 0016 still rejects automation without legal/platform/stakeholder scope; this decision records the scope that was previously missing.

## Context

The project owner reported that CIB approved execution of the research activities needed for the case and specifically required the controlled launch record to note explicit authorization for API access and all automation.

The repo previously allowed only manual or stakeholder-provided collection for the first real pilot. API access, browser automation, scraping/crawling-like collection, redirect expansion, landing-page capture, and profile/account context were not approved by default.

## Options Considered

| Option | Pros | Cons | Decision |
|---|---|---|---|
| Keep the manual-only pilot record unchanged | Preserves conservative first-pilot posture | Contradicts the reported CIB authorization amendment | Rejected |
| Add API and automation authorization without controls | Fastest to write | Reintroduces privacy, source, credential, retention, and audit ambiguity | Rejected |
| Add API and all research-required automation authorization under a controlled launch record | Honors CIB authorization while preserving audit, storage, access, retention, redaction, and checkpoint controls | Requires careful run records and updated governance docs | Accepted |

## Authorized Automation Scope

Within this CIB-authorized research case, automation may include:

- API-based collection and retrieval.
- Browser or workflow automation where needed for approved research collection.
- Screenshot capture.
- OCR extraction.
- Visible-link parsing.
- Redirect-chain and landing-page evidence capture when needed for the approved research question.
- Approved profile/account context capture when needed for the approved research question.
- Deduplication, normalization, redaction support, validation, audit, baseline scoring, review-packet generation, and reporting automation.

Every API or automation run must state purpose, operator, source category, item or batch limit, fields collected, raw output path, redacted output path, credential/session handling, and stop-condition review.

## Constraints

- Raw evidence, credentials, tokens, cookies, browser profiles, HAR files, source URLs, handles, screenshots, and item-level sensitive outputs must stay outside git.
- Repo-visible files may contain only redacted, derived, aggregate, or non-sensitive summaries unless a later decision explicitly approves a specific item-level artifact.
- Automated outputs are research triage artifacts only. They are not legal fraud determinations, public accusations, or production enforcement decisions.
- Larger automated batches still require a work order or decision memo that records source, item count, fields, retention, access, and review gates.
- If automation collects fields outside the run record or cannot be redacted safely, pause the run and update governance before continuing.

## Consequences

- `governance/data-governance.md` is updated to include a CIB-authorized API and automation status.
- The pilot launch packet now includes a controlled launch record with explicit API and automation authorization.
- Scope and budget docs are updated so API/automation is no longer described as categorically unapproved for this CIB-authorized case.
- Decision 0016 remains valid for unscope automation requests and future work without comparable authorization.

## Follow-Up

- Initialize or recreate the local pilot workspace only after confirming the controlled launch record.
- Run item-1 preflight.
- Complete a 1-2 item controlled rehearsal using the intended manual, API, or automation path.
- Pause after the first 10-15 real items for checkpoint review before completing the 50-item pilot.
