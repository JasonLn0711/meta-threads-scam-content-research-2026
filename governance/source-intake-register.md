# Source Intake Register

## Purpose

Track source candidates before they are approved for collection.

This register is not a place for sensitive source details. Do not include raw evidence, handles, URLs, personal data, stakeholder case IDs, confidential legal analysis, or investigative details.

## Current Status

| Date | Source candidate | Status | Notes |
|---|---|---|---|
| 2026-04-23 | `SRC-SYNTH-2026-04-23` | `approved_synthetic_only` | Synthetic examples for templates, calibration, and dry-run QA. |
| 2026-04-23 | `SRC-REAL-PILOT-TBD` | `pending` | No real Threads source has been approved. |
| 2026-04-23 | `SRC-UNLIMITED-500-2026-04-23` | `rejected_or_paused` | Unlimited 500-item collection is not a valid source authorization. |

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
| SRC-REAL-PILOT-TBD |  | 50-item pilot | `pending_authorization` |  |  |  | pending | Complete `templates/source_candidate_intake.md`. |
| SRC-UNLIMITED-500-2026-04-23 | unspecified | immediate 500-item collection | `rejected_or_paused` | red | unknown | red | rejected or paused | Use staged expansion plan instead. |

## Review Requirements

Before a source can move to `approved_for_50_item_pilot`:

- `templates/source_candidate_intake.md` completed
- `templates/data_authorization_request.md` completed if real evidence is involved
- allowed fields recorded
- raw storage outside git confirmed
- redaction, access, retention, and sharing rules recorded
- source appears in `templates/source_sampling_frame_template.csv`
- pilot work order names the source candidate ID

