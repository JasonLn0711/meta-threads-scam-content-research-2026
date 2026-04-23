# Source Intake Register

## Purpose

Track source candidates before they are approved for collection.

This register is not a place for sensitive source details. Do not include raw evidence, handles, URLs, personal data, stakeholder case IDs, confidential legal analysis, or investigative details.

## Current Status

| Date | Source candidate | Status | Notes |
|---|---|---|---|
| 2026-04-23 | `SRC-SYNTH-2026-04-23` | `approved_synthetic_only` | Synthetic examples for templates, calibration, and dry-run QA. |
| 2026-04-23 | `SRC-REAL-PILOT-APPROVED-2026-04-23` | `approved_for_50_item_pilot` | Approved for bounded 50-item pilot launch prep; exact sensitive source details must be recorded outside git before collection. |
| 2026-04-23 | `SRC-CIB-AUTHORIZED-AUTOMATION-2026-04-23` | `approved_for_50_item_pilot` | CIB-authorized API and automation-assisted source path for the same pilot; run records and controlled storage required. |
| 2026-04-23 | `SRC-UNLIMITED-500-2026-04-23` | `rejected_or_paused` | Unlimited 500-item collection is not a valid source authorization. |
| 2026-04-23 | `SRC-AUTO-LOW-SPEED-NO-SCOPE-2026-04-23` | `rejected_or_paused` | Low-speed automated Threads/Meta collection without legal/platform/stakeholder scope is not accepted. |

## Status Values

| Status | Meaning |
|---|---|
| `candidate` | Proposed but not reviewed. |
| `planning_only` | Can inform planning but cannot provide annotation items. |
| `approved_synthetic_only` | Synthetic or fully redacted non-evidence examples only. |
| `pending_authorization` | May be usable after authorization request is complete. |
| `approved_for_50_item_pilot` | Approved for the first real pilot under stated limits. |
| `approved_for_expansion` | Approved for later 100-200 or 500-item expansion under stated limits. |
| `rejected_or_paused` | Do not collect or use. |

## Candidate Register

| Candidate ID | Source type | Intended use | Authorization status | Privacy risk | Evidence quality | Source skew risk | Decision | Notes |
|---|---|---|---|---|---|---|---|---|
| SRC-SYNTH-2026-04-23 | `researcher_synthetic` | calibration and workflow QA | `approved_synthetic_only` | low | useful for tooling only | high if treated as real data | use only as synthetic | Not real evidence. |
| SRC-REAL-PILOT-APPROVED-2026-04-23 | `stakeholder_provided_case` / `manual_public_example` | 50-item pilot | `approved_with_limits` | medium | useful for pilot | medium | approved for launch prep | Manual-only; exact source, storage, access, retention, and redaction limits required before collection. |
| SRC-CIB-AUTHORIZED-AUTOMATION-2026-04-23 | `api_authorized_sample` / `other_approved` | 50-item pilot and controlled research automation | `approved_with_limits` | medium to high | useful for pilot if run logs and redaction pass | medium to high | approved for launch prep | CIB explicitly authorized API and all research-required automation; raw outputs, credentials, sessions, and logs stay outside git. |
| SRC-UNLIMITED-500-2026-04-23 | unspecified | immediate 500-item collection | `rejected_or_paused` | red | unknown | red | rejected or paused | Use staged expansion plan instead. |
| SRC-AUTO-LOW-SPEED-NO-SCOPE-2026-04-23 | Threads/Meta public surfaces | low-speed automated collection | `rejected_or_paused` | red | unknown | red | rejected or paused | Rate limiting alone does not satisfy authorization, platform, storage, retention, redaction, or audit requirements. |

## Review Requirements

Before a source can move to `approved_for_50_item_pilot`:

- `templates/source_candidate_intake.md` completed
- `templates/data_authorization_request.md` completed if real evidence is involved
- allowed fields recorded
- raw storage outside git confirmed
- redaction, access, retention, and sharing rules recorded
- source appears in `templates/source_sampling_frame_template.csv`
- pilot work order names the source candidate ID
