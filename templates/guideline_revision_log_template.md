# Guideline Revision Log

## Revision Log Identity

| Field | Value |
|---|---|
| Dataset or batch ID |  |
| Annotation guideline version | `v1` |
| Log owner |  |
| Date opened |  |
| Date closed |  |

## Revision Candidates

| ID | Date | Source | Guideline section | Problem observed | Proposed change | Severity | Decision | Owner |
|---|---|---|---|---|---|---|---|---|
| GR-001 |  | calibration / pilot / adjudication / audit |  |  |  | blocker / important / minor / defer | accepted / rejected / deferred / pending |  |

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
|  |  | `docs/06-annotation-guideline-v1.md` |  |  |

## Post-Revision Checks

After accepted changes:

- update `docs/06-annotation-guideline-v1.md`
- update `docs/04-taxonomy.md` if subtype or signal-tag vocabulary changes
- update `data-contracts/labeling_schema_v1.json` if valid values change
- update templates if new required fields or values are introduced
- record a decision-log entry for material taxonomy or label changes
- rerun calibration if the change affects primary labels or risk levels

