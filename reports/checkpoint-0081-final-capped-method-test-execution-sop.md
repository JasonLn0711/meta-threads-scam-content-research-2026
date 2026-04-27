# Checkpoint 0081 Final Capped Method-Test Execution SOP

## Purpose

Define the day-by-day SOP for the proposed capped investment-scam discovery method test.

This SOP is not executable until final authorization approves Track A and/or Track B.

## Tracks

| Track | Scope | Execution status |
|---|---|---|
| Track A | zero-new-evidence dry run using existing repo-safe checkpoint materials | requires final authorization |
| Track B | capped live candidate-discovery method test | requires final authorization plus legal/privacy clearance |

## Day 0: Gate Confirmation

Before any authorized activity begins:

- confirm approved track scope;
- confirm reviewer role aliases;
- confirm legal/privacy status;
- confirm controlled-store boundary;
- confirm source-arm caps;
- confirm stop-rule owner;
- confirm daily stop-rule check owner;
- confirm strict validation command;
- confirm aggregate reporting template;
- confirm no raw evidence will enter git.

## Track A SOP

Track A uses existing repo-safe checkpoint materials only.

Steps:

1. Select a small repo-safe checkpoint slice.
2. Fill the candidate-review record template without raw evidence.
3. Run dedupe-status simulation.
4. Fill evidence-completeness fields from existing repo-safe summaries only.
5. Perform primary reviewer workflow rehearsal.
6. Trigger second review where the template requires it.
7. Run hard-negative check.
8. Fill daily stop-rule check fields.
9. Run aggregate report template.
10. Record SOP gaps without opening new collection.

Track A stop conditions:

- template cannot be completed without raw evidence;
- reviewer role ownership is unclear;
- stop-rule owner is missing;
- aggregate report cannot separate Track A from Track B;
- baseline output is mistaken for enforcement recommendation.

## Track B SOP

Track B may proceed only after explicit final authorization.

### Day 1-14: Intake And Review Window

For each approved source arm:

1. Surface candidates within source-arm cap.
2. Create repo-safe candidate note.
3. Perform dedupe check.
4. Perform evidence-completeness check.
5. Perform primary human review.
6. Trigger second review when required.
7. Assign label and risk.
8. Run hard-negative check.
9. Record reviewer time.
10. Run daily stop-rule check.

No overflow queue is allowed. Stop at approved caps.

### Day 15-17: Validation And Aggregation

1. Build accepted strict-valid records.
2. Run strict validation.
3. Resolve validation errors or exclude invalid records.
4. Produce aggregate-only report.
5. Record stop-rule incidents.
6. Produce go/no-go analysis.

### Day 18: Debrief

1. Reviewer debrief.
2. Technical/governance review.
3. Legal/privacy boundary review.
4. Decide whether to close, revise, or propose a next tranche.

## Daily Stop-Rule Check

Daily fields:

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

If a stop threshold is crossed, pause the affected path immediately.

## Always Prohibited

- private-message access;
- raw URL in git;
- handle in git;
- screenshot in git;
- raw post/reply text in git;
- account graph capture;
- landing-page or redirect-chain capture;
- enforcement recommendation;
- public release;
- legal fraud conclusion;
- model training.
