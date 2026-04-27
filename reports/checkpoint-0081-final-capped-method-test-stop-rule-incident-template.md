# Checkpoint 0081 Final Capped Method-Test Stop-Rule Incident Template

## Purpose

Provide a repo-safe incident template for any stop-rule trigger during Track A dry run or Track B method test.

## Template

```yaml
incident_note_id:
date_bucket:
track: track_a_dry_run | track_b_live_method_test
source_arm:
affected_signal_family:
stop_rule_type:
threshold_value:
observed_value:
pause_required: yes | no
pause_scope: full_test | source_arm | candidate_path | reporting_only
stop_rule_owner:
daily_stop_check_owner:
summary:
immediate_action:
resume_condition:
legal_privacy_review_required: yes | no
technical_governance_review_required: yes | no
cib_internal_owner_review_required: yes | no
repo_safe_notes:
```

## Stop Events

| Stop event | Required action |
|---|---|
| Raw evidence leak | immediate stop, incident note, no further intake |
| Hard-negative false-positive cluster | pause affected source arm |
| Duplicate rate > 35% | pause source arm and revise dedupe |
| Reviewer burden > 18 minutes average | pause intake |
| Second-review rate > 55% | pause and revise rubric |
| Disagreement rate > 30% | pause and recalibrate reviewers |
| Insufficient-evidence rate > 40% | pause source method |
| Private-message boundary pressure | stop affected candidate path |
| Legal/privacy uncertainty | no execution |
| Baseline described as enforcement tool | pause reporting and correct wording |
| Source cap pressure | stop at cap; no overflow queue |
| UI or evidence-surface changes | pause and revalidate capture assumptions |

## Daily Stop-Rule Check Fields

```text
date_bucket
surfaced_today
reviewed_today
duplicates_today
insufficient_evidence_today
hard_negative_fp_pressure_today
average_review_time_today
second_review_rate_today
stop_rule_triggered
pause_required
owner_role_alias
```
