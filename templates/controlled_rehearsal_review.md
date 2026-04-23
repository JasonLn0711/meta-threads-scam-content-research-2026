# Controlled Rehearsal Review

Use this template after the first 1-2 controlled real rehearsal items. Keep this file free of raw Threads content, screenshots, source URLs, handles, case IDs, credentials, browser exports, raw storage paths, access-list details, API tokens, automation logs, and other sensitive investigative material.

This review is the repo-safe bridge between the 1-2 item rehearsal and the first 10-15 item checkpoint. It is not the checkpoint itself and it does not authorize expansion beyond the approved launch path.

## Review Identity

| Field | Value |
|---|---|
| Rehearsal review ID |  |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Collection batch ID | `threads_pilot_v1_2026-05` |
| Rehearsal work order ID | `CRWO-THREADS-PILOT-V1-2026-04-23` |
| Review date |  |
| Reviewed item count |  |
| Review owner |  |
| Governance reviewer |  |
| Annotation lead |  |
| Research engineer |  |
| Controlled launch details confirmed outside git? | yes / no |
| Before-item-1 preflight result |  |
| Collection path used | manual / stakeholder_provided / api_authorized / automation_assisted / mixed |
| Separate API or automation run record confirmed if needed? | yes / no / n/a |

## Research Framing

| Question | Value |
|---|---|
| Research question | Can the team convert approved evidence into redacted, schema-valid local records without governance, redaction, or annotation-boundary failure? |
| Hypothesis | A 1-2 item controlled rehearsal is enough to catch the first operational failures before the first 10-15 item checkpoint. |
| Main decision after this review | `pass_ready_for_calibration_or_first_10_15` / `pass_with_limits` / pause outcome |

## Data Slice

| Slice summary | Count | Notes |
|---|---:|---|
| approved rehearsal items attempted |  |  |
| schema-valid local records built |  |  |
| items excluded before record build |  |  |
| text-only items |  |  |
| text plus image or screenshot-style items |  |  |
| OCR-relevant items |  |  |
| reply/comment-context items |  |  |
| visible link or redirect-signal items |  |  |

## Method

Record the local steps used without copying item-level evidence.

| Step | Completed? | Notes |
|---|---|---|
| local workspace initialized | yes / no |  |
| before-item-1 preflight passed with `ERROR: 0` | yes / no |  |
| rehearsal record build command run | yes / no |  |
| strict validation run | yes / no |  |
| local collection log reviewed | yes / no |  |
| manual rehearsal checklist reviewed | yes / no |  |
| boundary watchlist reviewed | yes / no |  |
| annotation lead reviewed calibration status | yes / no |  |

## Cost And Burden

| Cost area | Value | Notes |
|---|---|---|
| collector time |  |  |
| governance review time |  |  |
| annotation lead review time |  |  |
| research engineer time |  |  |
| redaction burden | low / medium / high |  |
| unclear field count |  |  |

## Result Summary

| Check | Result | Notes |
|---|---|---|
| raw evidence stayed outside git | yes / no |  |
| strict validation passed | yes / no |  |
| schema warnings | 0 / nonzero |  |
| governance errors | 0 / nonzero |  |
| redaction issues found | none / limited / blocking |  |
| unapproved context needed | none / limited / blocking |  |
| repeated boundary-watch failure | none / one item / repeated |  |
| collection burden acceptable for checkpoint start | yes / no |  |
| calibration rerun needed before first 10-15 | yes / no | only if annotator team changed or the same boundary fails again |

## Boundary Review

| Boundary question | Outcome | Notes |
|---|---|---|
| Finance discussion without a funnel stayed `non_scam` rather than escalating from topic alone | pass / fail / not_observed |  |
| Decisive OCR remained `sufficient` when missing context was only uncaptured destination or profile detail | pass / fail / not_observed |  |
| Generic verification wording was not treated as a credential-request tag without an explicit data ask | pass / fail / not_observed |  |
| Confidence tracked likely agreement on the core label and reason rather than exact subtype or tag overlap | pass / fail / not_observed |  |

## Failure Modes And Follow-Up

| Failure or concern | Severity | Required action | Owner | Required before continuing? |
|---|---|---|---|---|
|  | blocker / important / minor |  |  | yes / no |

## Decision

Choose one:

- `pass_ready_for_calibration_or_first_10_15`
- `pass_with_limits`
- `pause_for_redaction_fix`
- `pause_for_schema_or_guideline_fix`
- `pause_for_authorization_review`
- `stop_source_for_pilot`

Decision:

```text

```

## Decision Rationale

Summarize the reason for the rehearsal decision in 3-6 bullets.

- 

## Next Action

| Next action | Owner | Required before the first 10-15 item checkpoint? |
|---|---|---|
|  |  | yes / no |

## Recording Boundary

- Commit only non-sensitive aggregate findings.
- Keep local rehearsal inputs, local records, collection logs, screenshots, URLs, handles, run records, and item-level notes outside git unless explicitly sanitized and approved.
- If the decision is `pass_ready_for_calibration_or_first_10_15`, rerun calibration only if the annotator team changed; otherwise proceed to `docs/38-first-pilot-checkpoint-protocol.md`.
- If the decision is `pass_with_limits`, record the exact limit before the first 10-15 item checkpoint starts.
- If the decision is any pause or stop, update the relevant guideline, schema, SOP, authorization, or launch artifact before collecting more items.
