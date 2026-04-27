# Checkpoint 0081 Track A Zero-New-Evidence Dry Run Start Checklist

## Purpose

Confirm whether Track A can start under decision `0121`.

Track A is a zero-new-evidence dry run. It uses existing repo-safe checkpoint `0081` materials only to test SOP, templates, reviewer workflow, stop-rule logging, strict-validation handoff, and aggregate reporting.

This checklist does not authorize Track B and does not authorize new evidence collection.

## Current Status

| Field | Value |
|---|---|
| Authorization decision | `decision-log/0121-record-final-gate-review-response-track-a-now-track-b-conditional.md` |
| Track | `track_a_zero_new_evidence_dry_run` |
| Execution status | `approved_pending_start_checklist_completion` |
| New evidence collection authorized | no |
| Browser/session use authorized | no |
| Item `0082` authorized | no |
| Raw evidence expansion authorized | no |
| Model training authorized | no |
| Enforcement use authorized | no |

## Start Checklist

| Gate | Required state | Current status | Repo-safe evidence |
|---|---|---|---|
| Existing repo-safe materials only | confirmed | pass | Checkpoint `0081` repo-safe reports and summaries only. |
| No new candidates | confirmed | pass | Track A scope prohibits candidate discovery. |
| No browser session | confirmed | pass | Track A scope prohibits browser/session use. |
| No raw evidence expansion | confirmed | pass | Track A scope prohibits raw evidence expansion. |
| Candidate record template ready | ready | pass | `reports/checkpoint-0081-final-capped-method-test-candidate-record-template.md` |
| Aggregate report template ready | ready | pass | `reports/checkpoint-0081-final-capped-method-test-aggregate-report-template.md` |
| Stop-rule incident template ready | ready | pass | `reports/checkpoint-0081-final-capped-method-test-stop-rule-incident-template.md` |
| Controlled-store boundary understood | confirmed for dry-run use | pass | `reports/checkpoint-0081-final-capped-method-test-controlled-store-boundary.md` |
| Reviewer role aliases assigned | required before start | pending | `reports/checkpoint-0081-final-capped-method-test-reviewer-assignment-table.md` currently records assignment fields. |
| Stop-rule owner assigned | required before start | pending | Role alias must be recorded before starting. |
| Daily stop-check owner assigned | required before start | pending | Role alias must be recorded before starting. |
| Validation owner assigned | required before start | pending | Role alias must be recorded before starting. |
| Strict validation command ready | command shape ready | pending_output_target | Use `python3 scripts/validate_thread_dataset.py <track_a_output>.json --strict` after a repo-safe Track A output file exists. |
| Repo-safe output path selected | required before start | pending | Suggested output: `reports/checkpoint-0081-track-a-zero-new-evidence-dry-run-report.md`. |

## Minimum Start Condition

Track A may start only after these pending fields are resolved:

- reviewer role aliases assigned;
- stop-rule owner assigned;
- daily stop-check owner assigned;
- validation owner assigned;
- Track A output path selected.

## Track A Dry-Run Slice

Use a small repo-safe checkpoint slice from existing checkpoint `0081` summaries.

The slice should include at minimum:

- one `scam` / `high` pattern summary;
- one `non_scam` / `low` hard-negative summary;
- one `uncertain` or `insufficient_evidence` summary;
- one item requiring second-review trigger rehearsal;
- one item that tests hard-negative protection.

Do not copy raw Threads URLs, handles, screenshots, raw post text, raw reply text, contact IDs, stock identifiers, credentials, browser/session artifacts, exact controlled-store paths, stakeholder case IDs, or private recipient details into the Track A output.

## Track A Success Criteria

Track A succeeds if:

- candidate record fields can be filled from repo-safe summaries;
- reviewer time can be recorded;
- second-review triggers can be applied;
- hard-negative flags can be applied;
- stop-rule daily check can be completed;
- aggregate-only report can be produced;
- strict-validation handoff is clear;
- no raw evidence enters git;
- no baseline output is described as enforcement, legal fraud determination, or production detection.

## Track A Stop Conditions

Pause Track A if:

- a template cannot be completed without raw evidence;
- reviewer role ownership is unclear;
- stop-rule ownership is missing;
- aggregate reporting cannot separate Track A from Track B;
- raw evidence would need to enter git;
- baseline output is treated as an enforcement recommendation.

## Next Action

Resolve the pending start fields, then run Track A and create:

```text
reports/checkpoint-0081-track-a-zero-new-evidence-dry-run-report.md
```

Track B remains blocked by:

```text
reports/checkpoint-0081-track-b-capped-live-method-test-condition-checklist.md
```
