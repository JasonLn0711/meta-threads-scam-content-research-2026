# Decision 0121: Record Final Gate Review Response For Track A Now And Track B Conditional

## Status

accepted

## Date

2026-04-27

## Decision

Record the final gate reviewer response for the checkpoint `0081` capped investment-scam discovery method test.

Recommended status:

```text
approve_track_a_now_track_b_after_conditions
```

This means:

- Track A zero-new-evidence dry run is approved to start once the Track A start checklist is complete.
- Track B capped live method test is approved only after the Track B condition checklist is fully satisfied.
- No further abstract review package should be opened unless a required condition changes.
- Decision `0118` and decision `0120` should not be polished again for wording-only reasons.

## Reviewer Response

```text
Checkpoint reviewed:
threads_pilot_v1_0081

Package reviewed:
checkpoint-0081-final-capped-investment-scam-discovery-method-test-execution-authorization

Recommended status:
approve_track_a_and_track_b_execution_with_conditions

Track A zero-new-evidence dry run:
approved

Track B capped live method test:
approved with hard execution conditions
```

## Track A Scope

Track A may use existing repo-safe checkpoint `0081` materials only.

Track A does not authorize:

- new candidates;
- browser session use;
- new evidence collection;
- raw evidence expansion;
- item `0082`;
- model training;
- enforcement use;
- public release.

Track A tests:

- SOP usability;
- candidate-review record fields;
- reviewer-time recording;
- second-review triggers;
- hard-negative triggers;
- stop-rule incident template usability;
- aggregate report template usability;
- strict-validation handoff;
- repo-safe output boundaries.

## Track B Scope

Track B remains blocked until all hard conditions are marked complete in:

```text
reports/checkpoint-0081-track-b-capped-live-method-test-condition-checklist.md
```

Track B is a capped live candidate-discovery method test, not item `0082` and not checkpoint continuation by habit.

If authorized to begin, Track B must stay inside:

| Cap | Value |
|---|---:|
| Surfaced candidates | 300 |
| Human-reviewed candidates | 150 |
| Accepted strict-valid records | 75 |
| Intake window | 14 calendar days |

Source-arm caps:

| Source arm | Surfaced candidate cap |
|---|---:|
| Checkpoint-derived seed replay | 30 |
| Reviewer-supplied candidates | 30 |
| Approved browser-session risk-probe matrix | 110 |
| Reply/comment funnel cue candidates | 60 |
| OCR/image-cue candidates | 20 |
| Hard-negative probe arm | 50 |

No overflow queue is allowed.

## Required Next Artifacts

Open and maintain:

```text
reports/checkpoint-0081-track-a-zero-new-evidence-dry-run-start-checklist.md
reports/checkpoint-0081-track-b-capped-live-method-test-condition-checklist.md
```

Track A may begin only after its checklist is complete.

Track B may begin only after its condition checklist is fully green.

## Track B Hard Conditions

Track B cannot begin unless all of the following are recorded:

- legal/privacy reviewer has no veto;
- CIB/internal owner accepts the capped method-test boundary;
- technical/governance owner assigns or confirms the stop-rule owner;
- controlled-store custodian is assigned;
- reviewer role aliases are assigned;
- source-arm caps are locked;
- surfaced-candidate cap is locked;
- human-review cap is locked;
- accepted-record cap is locked;
- intake window is locked;
- daily stop-rule checklist is ready;
- strict validation command is ready;
- aggregate-only report template is ready;
- raw evidence exclusion scan/check is ready.

## Hard-Negative Requirement

Track B must preserve the hard-negative probe arm.

The method test is not valid unless it measures false-positive pressure against:

- genuine anti-scam warnings;
- ordinary investment discussion;
- financial education;
- general market commentary;
- personal investment journaling;
- legitimate finance creator content;
- public contact information without funnel behavior;
- educational chart or screenshot content;
- news discussion;
- risk warning content.

## Stop Rules

Track B must stop or pause if any of the following occur:

| Stop event | Required action |
|---|---|
| Raw evidence leak | Immediate stop, incident note, no further intake. |
| Raw URL, handle, screenshot, or raw text enters git | Immediate stop and cleanup review. |
| Hard-negative false-positive pressure > 20% | Pause affected source arm. |
| Duplicate rate > 35% | Pause affected source arm and revise dedupe. |
| Insufficient-evidence rate > 40% | Pause affected source method. |
| Average reviewer time > 18 minutes | Pause intake. |
| Second-review rate > 55% | Pause and revise rubric. |
| Reviewer disagreement rate > 30% | Pause and recalibrate reviewers. |
| Private-message boundary pressure appears | Stop affected candidate path. |
| Legal/privacy uncertainty appears | No execution for affected path. |
| Baseline used as enforcement recommendation | Pause reporting and correct wording. |
| Source cap exceeded | Stop at cap; no overflow queue. |
| Candidate cap exceeded | Stop at cap; no overflow queue. |

## Non-Authorizations

This decision does not authorize:

- item `0082`;
- open-ended collection;
- broad crawler/browser expansion;
- private-message access;
- account/profile graph capture;
- landing-page or redirect-chain capture;
- embedding/model training;
- production detector claims;
- legal fraud determinations;
- public warning lists;
- automated enforcement;
- public release;
- raw evidence in git.

## Rationale

The repo has already moved through checkpoint synthesis, recipient adoption, readiness analysis, method charter, capped decision draft, decision-review package, and final authorization package preparation.

Continuing to create abstract review artifacts would no longer advance the first-principle goal:

```text
find a scalable, stable, and reviewable method for discovering Threads investment-scam candidates at volume.
```

The next value is controlled execution planning:

- run Track A as a zero-new-evidence workflow dry run after its checklist passes;
- run Track B only after hard conditions pass;
- measure yield, reviewer burden, duplicate load, insufficient evidence, hard-negative false-positive pressure, and stop-rule behavior;
- do not move to model training or production claims after Track B without a later decision.

## Consequences

- The active state moves from final-gate package preparation to controlled execution planning.
- Track A is approved but still gated by its start checklist.
- Track B is conditionally approved but still blocked by hard conditions.
- No new package is needed unless a required condition changes.
- Future reporting should focus on Track A dry-run result and Track B condition status, not additional abstract readiness review.
