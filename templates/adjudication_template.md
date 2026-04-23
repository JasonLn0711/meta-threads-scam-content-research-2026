# Adjudication Template

## Item

- `item_id`:
- `collection_batch_id`:
- `schema_version`:
- `adjudicator_id`:
- `adjudication_date`:

## Original Labels

| Reviewer | `scam_label` | `risk_level` | `scam_type` | Confidence | Evidence sufficiency |
|---|---|---|---|---|---|
| Annotator 1 |  |  |  |  |  |
| Annotator 2 |  |  |  |  |  |

## Disagreement Type

Mark all that apply:

- Primary label disagreement
- Risk-level disagreement
- Scam-subtype disagreement
- Signal-tag disagreement
- Evidence-sufficiency disagreement
- Confidence disagreement
- Exclusion/scope disagreement

## Evidence Reviewed

- Post text:
- Reply/comment context:
- OCR text:
- Image/screenshot status:
- Visible links or redirection:
- Missing evidence:

## Final Decision

- `final_label`:
- `final_risk_level`:
- Final `scam_type` values:
- Final `signal_tags`:
- `adjudication_status`: `resolved`

## Rationale

Write a concise evidence-based reason for the final decision. Do not make legal conclusions.

## Guideline Feedback

- Did this disagreement reveal a missing rule or unclear definition?
- Should `docs/06-annotation-guideline-v1.md` be revised?
- Should any schema field or signal tag be revised after the pilot?
