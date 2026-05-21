# Reviewer Assist Labor-Savings Worksheet

Use this worksheet for a repo-safe assisted-review entry.

Do not include raw post text, raw reply text, raw OCR text, raw URLs, handles, screenshots, browser/session artifacts, credentials, controlled-store locators, stakeholder case IDs, or unnecessary personal data.

## Candidate Header

| Field | Value |
|---|---|
| `candidate_alias` |  |
| `slice_id` |  |
| `source_lane` | strong_source_priority / result_display_clean_holdout / result_display_low_context_transition / result_display_thread_required / other_governed_slice |
| `condition` | manual_baseline / assisted_review |
| `reviewer_role_alias` |  |
| `raw_evidence_excluded_from_git` | yes / no |
| `human_decision_required` | yes |

## Assisted Outputs

| Output | Draft present | Accepted | Corrected | Rejected | Correction category |
|---|---|---|---|---|---|
| Candidate summary | yes / no / n/a | yes / no / n/a | yes / no / n/a | yes / no / n/a |  |
| Signal-family suggestions | yes / no / n/a | yes / no / n/a | yes / no / n/a | yes / no / n/a |  |
| Schema prefill | yes / no / n/a | yes / no / n/a | yes / no / n/a | yes / no / n/a |  |
| Hard-negative warning | yes / no / n/a | yes / no / n/a | yes / no / n/a | yes / no / n/a |  |
| Priority explanation | yes / no / n/a | yes / no / n/a | yes / no / n/a | yes / no / n/a |  |
| Missing-evidence note | yes / no / n/a | yes / no / n/a | yes / no / n/a | yes / no / n/a |  |
| Second-review suggestion | yes / no / n/a | yes / no / n/a | yes / no / n/a | yes / no / n/a |  |

## Human Review Outcome

| Field | Value |
|---|---|
| `final_research_label` | scam / non_scam / uncertain / insufficient_evidence / not_reviewable |
| `final_risk_level` | high / medium / low / not_applicable |
| `review_worthy_candidate` | yes / no / uncertain |
| `evidence_sufficiency_outcome` | sufficient / partial / insufficient / not_reviewable |
| `duplicate_status` | not_duplicate / near_duplicate / duplicate_excluded / unknown |
| `second_review_required` | yes / no |
| `second_review_reason` | reply_context_needed / ocr_unclear / signal_family_ambiguous / hard_negative_possible / duplicate_or_near_duplicate / source_context_thin / schema_field_unclear / evidence_sufficiency_unclear / privacy_or_redaction_boundary / other_repo_safe / not_required |

## Labor Measurement

| Field | Value |
|---|---|
| `review_duration_seconds` |  |
| `full_thread_read_required` | yes / no / partial / not_available |
| `summary_usefulness_rating` | 1 / 2 / 3 / 4 / 5 / not_applicable |
| `manual_fields_needed` |  |
| `manual_fields_filled` |  |
| `prefilled_fields_accepted` |  |
| `prefilled_fields_corrected` |  |
| `prefilled_fields_rejected` |  |
| `reviewer_hesitation_reason` | none / reply_context_needed / ocr_unclear / signal_family_ambiguous / hard_negative_possible / duplicate_or_near_duplicate / source_context_thin / schema_field_unclear / evidence_sufficiency_unclear / privacy_or_redaction_boundary / other_repo_safe |

## Repo-Safe Notes

- Most useful assist output:
- Most harmful or noisy assist output:
- Missing evidence category:
- Hard-negative concern:
- Priority-routing concern:
- Aggregate-only lesson:
