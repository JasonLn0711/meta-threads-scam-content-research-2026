# Checkpoint 0081 Final Capped Method-Test Candidate Record Template

## Purpose

Provide a repo-safe candidate-review record template for Track A dry run and any later approved Track B execution.

No raw Threads URL, handle, screenshot, raw post text, raw reply text, contact ID, stock name, stock code, price value, credential, browser/session artifact, controlled-store path, stakeholder case ID, or private recipient detail may be entered here.

## Template

```yaml
candidate_id:
track: track_a_dry_run | track_b_live_method_test
candidate_unit: post | thread | account_context | funnel
source_family:
source_arm:
candidate_surface_date_bucket:
candidate_provenance_class:
signal_families_triggered:
signal_combination_strength: weak | moderate | strong
primary_signal_family:
secondary_signal_families:
evidence_surfaces_available:
top_level_post_available: yes | no | unknown
reply_context_available: yes | no | unknown
reply_context_required: yes | no | unknown
ocr_needed: yes | no
ocr_decisive: yes | no | unknown
ocr_quality: none | low | medium | high | unknown
profile_context_used: yes | no
profile_context_boundary:
external_contact_category:
private_channel_migration_visible: yes | no | unknown
dedupe_status: unique | duplicate | near_duplicate | unknown
duplicate_cluster_id:
near_duplicate_reason:
evidence_completeness_score: 0 | 1 | 2 | 3
primary_reviewer_role:
review_time_minutes:
initial_label: scam | non_scam | uncertain | insufficient_evidence
initial_risk: high | medium | low
second_review_required: yes | no
second_review_reason:
second_reviewer_role:
reviewer_disagreement_type:
final_label: scam | non_scam | uncertain | insufficient_evidence
final_risk: high | medium | low
hard_negative_flag: yes | no
hard_negative_type:
uncertain_reason:
insufficient_evidence_reason:
false_positive_pressure: low | medium | high
false_negative_pressure: low | medium | high
stop_rule_triggered: yes | no
stop_rule_type:
repo_safe_notes:
```

## Evidence Completeness Score

| Score | Meaning |
|---:|---|
| 0 | Too thin to evaluate. |
| 1 | One surface available, no funnel context. |
| 2 | Main surface plus at least one supporting context surface. |
| 3 | Full-thread or decisive evidence-surface context available under approved boundary. |

## Mandatory Second Review Triggers

- high-risk initial label;
- anti-scam language plus possible funnel cue;
- teacher/advisor framing without contact or proof;
- profit-proof without conversion path;
- public contact information without investment funnel;
- profile-context pattern as main evidence;
- OCR-dependent candidate;
- investment vocabulary only;
- ordinary group/community discussion;
- hard-negative flag;
- reviewer uncertainty.
