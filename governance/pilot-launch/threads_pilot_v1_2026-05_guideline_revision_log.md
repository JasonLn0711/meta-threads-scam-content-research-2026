# Guideline Revision Log: Threads Pilot v1

## Revision Log Identity

| Field | Value |
|---|---|
| Dataset or batch ID | `threads_pilot_v1_2026-05` |
| Annotation guideline version | `v1` |
| Log owner | `annotation_lead_01` |
| Date opened | `2026-04-23` |
| Date closed | `2026-04-23` |

## Revision Candidates

| ID | Date | Source | Guideline section | Problem observed | Proposed change | Severity | Decision | Owner |
|---|---|---|---|---|---|---|---|---|
| `GR-001` | `2026-04-23` | `calibration` | primary-label boundary, finance edge cases | Readable finance discussion was being treated as `uncertain` from topic alone. | Clarify that finance discussion without a funnel, guarantee, redirect, fee, or fake authority stays `non_scam`. | `important` | `accepted` | `annotation_lead_01` |
| `GR-002` | `2026-04-23` | `calibration` | evidence sufficiency, screenshot/OCR edge cases | Annotators downgraded decisive OCR cases because destination or profile context was not captured. | Clarify that decisive OCR can still support `sufficient` evidence and that missing destination/profile context belongs in `missing_evidence`. | `important` | `accepted` | `annotation_lead_01` |
| `GR-003` | `2026-04-23` | `calibration` | signal-tag discipline, pseudo-official reward edge cases | Generic verification wording was being tagged as a credential request without an explicit data ask. | Clarify that `credential_or_personal_data_request` requires an explicit request for login, identity, bank, or other personal details. | `important` | `accepted` | `annotation_lead_01` |
| `GR-004` | `2026-04-23` | `calibration` | annotation confidence guidance | Confidence was drifting toward subtype/tag exact-match expectations rather than core-label agreement. | Clarify that confidence should reflect likely agreement on the main label and reason, not exact subtype/tag overlap. | `minor` | `accepted` | `annotation_lead_01` |

## Common Sources

Use one of:

- `calibration`
- `pilot_annotation`
- `second_review`
- `adjudication`
- `dataset_audit`
- `baseline_error_analysis`
- `stakeholder_feedback`

## Severity Guide

| Severity | Meaning |
|---|---|
| `blocker` | Annotation cannot proceed consistently without the change. |
| `important` | The issue affects repeated cases or high-risk decisions. |
| `minor` | Wording cleanup or example improvement. |
| `defer` | Valid issue, but not needed for the current pilot. |

## Revision Decision Rules

Accept a revision when:

- the same disagreement appears more than once
- annotators consistently confuse two labels or signal tags
- a definition causes over-labeling of legitimate content
- a definition causes missing obvious high-risk content
- the current wording creates privacy or overclaiming risk

Defer a revision when:

- the issue depends on evidence not approved for phase 1
- the issue is about rare future modalities such as long video
- the change would add complexity before the 50-item pilot proves it is needed

## Accepted Revision Summary

| Revision ID | Accepted change | File to update | Completed? | Notes |
|---|---|---|---|---|
| `GR-001` | Finance discussion without a conversion step stays `non_scam`. | `docs/06-annotation-guideline-v1.md` | yes | Also reflected in synthetic answer-key rows for `threads-synth-v1-0004`. |
| `GR-002` | Decisive OCR can remain `sufficient` evidence; missing destination/profile context goes in `missing_evidence`. | `docs/06-annotation-guideline-v1.md` | yes | Reinforced in rehearsal watchlist and QA checklist. |
| `GR-003` | Generic verification wording alone does not justify `credential_or_personal_data_request`. | `docs/06-annotation-guideline-v1.md` | yes | Also reflected in synthetic answer-key row for `threads-synth-v1-0005`. |
| `GR-004` | Confidence should track likely agreement on the core label and reason. | `docs/06-annotation-guideline-v1.md` | yes | Reinforced in the controlled rehearsal checklist. |

## Supporting Records

- `../../experiments/evaluation-notes/0012-synthetic-calibration-guideline-revision.md`
- `../../experiments/evaluation-notes/0013-controlled-rehearsal-boundary-watchlist.md`
- `../../templates/manual_collection_rehearsal_checklist.md`
- `../../templates/annotation_qa_checklist.md`

## Post-Revision Checks

After accepted changes:

- update `docs/06-annotation-guideline-v1.md`
- update `docs/04-taxonomy.md` if subtype or signal-tag vocabulary changes
- update `data-contracts/labeling_schema_v1.json` if valid values change
- update templates if new required fields or values are introduced
- record a decision-log entry for material taxonomy or label changes
- rerun calibration if the change affects primary labels or risk levels

Status for this revision set:

- `docs/06-annotation-guideline-v1.md` updated: yes
- vocabulary change requiring taxonomy/schema update: no
- onboarding and QA templates updated: yes
- synthetic calibration answer key aligned: yes
- mandatory taxonomy decision-log entry required: no
- rerun before real items required: only if annotator team changes or the same boundary fails again on real governed rehearsal items
