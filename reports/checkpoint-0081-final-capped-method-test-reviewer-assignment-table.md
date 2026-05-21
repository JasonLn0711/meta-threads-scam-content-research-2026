# Checkpoint 0081 Final Capped Method-Test Reviewer Assignment Table

## Purpose

Define repo-safe reviewer role aliases required before any Track A or Track B execution can begin.

This table intentionally avoids real names, email addresses, account IDs, or private contact details.

## Required Roles

| Role alias | Required for Track A | Required for Track B | Responsibility | Assigned? |
|---|---:|---:|---|---|
| `track_a_primary_reviewer_role` | yes | no | Primary dry-run review and initial label/risk rehearsal. | assigned for Track A |
| `track_a_second_reviewer_role` | yes | no | Second-review trigger rehearsal for hard negatives, high-risk patterns, and uncertainty. | assigned for Track A |
| `track_a_technical_governance_owner` | yes | no | Method integrity, template usability, metrics shape, stop-rule rehearsal, and QA. | assigned for Track A |
| `legal_privacy_owner` | no | yes | Legal/privacy status, evidence-surface permissions, retention, redaction, and sharing boundary. | pending for Track B |
| `controlled_store_custodian` | no | yes | Raw/sensitive evidence boundary and controlled-store handling. | pending for Track B |
| `track_a_stop_rule_owner` | yes | no | Pause decisions and incident notes during Track A dry run. | assigned for Track A |
| `track_a_daily_stop_check_owner` | yes | no | Daily stop-rule check completion during Track A dry run. | assigned for Track A |
| `track_a_validation_owner` | yes | no | Strict-validation handoff check and validation-command readiness for Track A outputs. | assigned for Track A |
| `track_a_reporting_owner` | yes | no | Aggregate-only Track A report and non-authorization wording. | assigned for Track A |
| `track_a_cib_internal_owner` | yes | no | Confirms Track A remains zero-new-evidence and does not imply Track B start. | assigned for Track A |
| `track_b_primary_reviewer_role` | no | yes | Primary candidate review and initial label/risk assignment for Track B. | pending for Track B |
| `track_b_second_reviewer_role` | no | yes | Second review for required triggers, disagreement, hard negatives, and high-risk candidates in Track B. | pending for Track B |
| `track_b_technical_governance_owner` | no | yes | Method integrity, schema, metrics, stop rules, and QA for Track B. | pending for Track B |
| `track_b_stop_rule_owner` | no | yes | Pause decisions and incident notes during Track B. | pending for Track B |
| `track_b_daily_stop_check_owner` | no | yes | Daily stop-rule check completion during Track B. | pending for Track B |
| `track_b_validation_owner` | no | yes | Strict validation command and validation-result recording for Track B. | pending for Track B |
| `track_b_reporting_owner` | no | yes | Aggregate-only Track B report creation and non-authorization wording. | pending for Track B |
| `track_b_cib_internal_owner` | no | yes | Operational need, reviewer capacity, and approval scope for Track B. | pending for Track B |

## Assignment Rule

Execution cannot begin until required role aliases for the approved track are assigned.

Track B cannot begin without `legal_privacy_owner` and `controlled_store_custodian`.

Track A role aliases are repo-safe functional aliases for zero-new-evidence dry-run execution. They do not identify private people, accounts, email addresses, or external contacts.

## Separation Rule

Technical/governance approval does not imply legal/privacy approval. Legal/privacy approval does not imply operational readiness. CIB/internal owner approval does not override stop rules.
