# Track B Candidate Review Template

Use this repo-safe template to record candidate-review outcomes and reviewer-burden measurements for Track B.

Do not include raw post text, raw reply text, raw OCR text, raw URLs, handles, screenshots, contact IDs, controlled-store paths, credentials, browser/session artifacts, stakeholder case IDs, or unnecessary personal data.

This template measures review effort. It does not change Track B caps, authorize new source arms, create legal findings, or support enforcement.

## Review Identity

| Field | Value |
|---|---|
| `track_b_candidate_alias` |  |
| `source_arm` | checkpoint_derived_seed_replay / reviewer_supplied_candidates / approved_browser_session_risk_probe_matrix / reply_comment_funnel_cue_candidates / ocr_image_cue_candidates / hard_negative_probe_arm |
| `reviewer_role_alias` |  |
| `second_reviewer_role_alias` |  |
| `authorization_boundary_confirmed` | yes / no |
| `raw_evidence_excluded_from_git` | yes / no |

## Discovery Outcome

| Field | Value |
|---|---|
| `surfaced_candidate` | yes / no |
| `human_reviewed_candidate` | yes / no |
| `review_worthy_candidate` | yes / no / uncertain |
| `accepted_strict_valid_record` | yes / no / pending |
| `duplicate_status` | not_duplicate / near_duplicate / duplicate_excluded / unknown |
| `evidence_sufficiency_outcome` | sufficient / partial / insufficient / not_reviewable |
| `final_research_label` | scam / non_scam / uncertain / insufficient_evidence / pending |
| `final_risk_level` | high / medium / low / pending |
| `primary_signal_family_group` | repo-safe category only |

## Reviewer Burden Fields

| Field | Value |
|---|---|
| `review_start_time_bucket` |  |
| `review_duration_minutes` |  |
| `full_thread_read_required` | yes / no / partial / not_available |
| `summary_would_have_helped` | yes / no / unclear / not_applicable |
| `schema_fields_auto_fillable` |  |
| `reviewer_hesitation_reason` | reply_context_needed / ocr_unclear / signal_family_ambiguous / hard_negative_possible / duplicate_or_near_duplicate / source_context_thin / schema_field_unclear / evidence_sufficiency_unclear / privacy_or_redaction_boundary / other_repo_safe / none |
| `second_review_reason` | reply_context_needed / ocr_unclear / signal_family_ambiguous / hard_negative_possible / duplicate_or_near_duplicate / source_context_thin / schema_field_unclear / evidence_sufficiency_unclear / privacy_or_redaction_boundary / other_repo_safe / not_required |
| `hard_negative_uncertainty_reason` | anti_scam_warning_possible / ordinary_investment_discussion_possible / financial_education_possible / market_commentary_possible / personal_journaling_possible / legitimate_creator_possible / context_too_thin / not_applicable / other_repo_safe |
| `reviewer_burden_note` | repo-safe note only |

## Manual Schema Burden

| Field | Count Or Notes |
|---|---|
| Schema fields needed for this review |  |
| Schema fields manually filled |  |
| Schema fields that could be auto-filled |  |
| Schema fields needing reviewer interpretation |  |
| Schema fields corrected after first pass |  |

## Second Review And Disagreement

| Field | Value |
|---|---|
| `second_review_required` | yes / no |
| `second_review_completed` | yes / no / not_applicable |
| `reviewer_disagreement` | yes / no / not_applicable |
| `disagreement_category` | label / risk_level / evidence_sufficiency / signal_family / hard_negative_boundary / duplicate_status / other_repo_safe / not_applicable |
| `resolution_status` | resolved / pending / not_applicable |

## Aggregate-Only Reporting Notes

Use this section only for sanitized categories that can be counted later.

- Reviewer task that consumed most time:
- Field most likely to benefit from prefill:
- Signal family easiest to summarize:
- Signal family hardest to summarize:
- Hard-negative hesitation category:
- Suggested Reviewer Assist Layer implication:

