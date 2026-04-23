# Decision 0010: Add Real Pilot Readiness Review

## Date

2026-04-23

## Decision

Add an integrated real-pilot readiness review before any real 50-item Threads pilot begins.

The readiness review is now the owner-facing final gate that ties together source intake, sampling, authorization, raw storage, redaction, annotation readiness, QA, baseline evaluation, and stop conditions.

## Context

The repo now contains the pieces needed to run a controlled first pilot:

- dataset schema and labeling schema
- annotation guideline
- collection and redaction SOP
- source intake and sampling-frame templates
- authorization request and registers
- pilot go/no-go checklist
- authorized pilot execution plan
- annotator onboarding and QA package
- baseline and pilot decision-analysis protocols

Those pieces are useful, but they are spread across several files. Before handling real Threads evidence, the project needs one integrated review artifact that makes the launch decision easy to inspect and hard to hand-wave.

## Options Considered

1. Rely only on the existing go/no-go checklist.
2. Start the pilot once source authorization is filled.
3. Add a real-pilot readiness review as a final integrated owner gate.

## Rationale

Option 3 is the safest and most useful path. It keeps the project practical without adding software infrastructure, and it prevents a common research failure mode: having many good templates but no single decision record that says whether the pilot is actually ready.

The review also makes it clear that tooling readiness is not the same as data readiness. The synthetic dry run proved the local workflow, not the right to collect or store real Threads evidence.

## Consequences

- Real pilot collection remains blocked until the readiness review is completed.
- The default decision remains `not_ready`.
- `ready_with_limits` is allowed only when all unresolved issues are converted into explicit limits.
- The 500-item expansion remains out of scope until after the 50-item pilot and 100-200 item first usable dataset decision gates.
- No raw Threads evidence, screenshots, credentials, browser exports, or sensitive case material should be committed.

## Follow-Up

Project owner should complete `templates/real_pilot_readiness_review.md` after the source intake, sampling frame, authorization request, go/no-go checklist, and pilot work order are ready.

If the review ends in `go` or `go_with_limits`, execute `docs/29-authorized-pilot-execution-plan.md`.

If the review ends in `no_go`, fix the blocker and update the relevant governance, source, annotation, or evaluation document before retrying.
