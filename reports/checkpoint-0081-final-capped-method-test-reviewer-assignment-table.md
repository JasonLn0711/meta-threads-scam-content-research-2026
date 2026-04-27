# Checkpoint 0081 Final Capped Method-Test Reviewer Assignment Table

## Purpose

Define repo-safe reviewer role aliases required before any Track A or Track B execution can begin.

This table intentionally avoids real names, email addresses, account IDs, or private contact details.

## Required Roles

| Role alias | Required for Track A | Required for Track B | Responsibility | Assigned? |
|---|---:|---:|---|---|
| `primary_reviewer_role` | yes | yes | Primary candidate review and initial label/risk assignment. | pending |
| `second_reviewer_role` | yes | yes | Second review for required triggers, disagreement, hard negatives, and high-risk candidates. | pending |
| `technical_governance_owner` | yes | yes | Method integrity, schema, metrics, stop rules, and QA. | pending |
| `legal_privacy_owner` | no | yes | Legal/privacy status, evidence-surface permissions, retention, redaction, and sharing boundary. | pending |
| `controlled_store_custodian` | no | yes | Raw/sensitive evidence boundary and controlled-store handling. | pending |
| `stop_rule_owner` | yes | yes | Pause decisions and incident notes. | pending |
| `daily_stop_check_owner` | yes | yes | Daily stop-rule check completion. | pending |
| `validation_owner` | yes | yes | Strict validation command and validation-result recording. | pending |
| `reporting_owner` | yes | yes | Aggregate-only report creation and non-authorization wording. | pending |
| `cib_internal_owner` | yes | yes | Operational need, reviewer capacity, and approval scope. | pending |

## Assignment Rule

Execution cannot begin until required role aliases for the approved track are assigned.

Track B cannot begin without `legal_privacy_owner` and `controlled_store_custodian`.

## Separation Rule

Technical/governance approval does not imply legal/privacy approval. Legal/privacy approval does not imply operational readiness. CIB/internal owner approval does not override stop rules.
