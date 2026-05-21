# Decision 0157: Record Breeze Guard 26 As Deferred Candidate Baseline

## Date

2026-05-21

## Decision

Record Breeze Guard 26 as a deferred candidate for a later Taiwan-localized safety-classifier baseline or guardrail comparison.

This decision does not authorize current Phase 1 classifier-assisted review, LLM-assisted explanation, production scoring, or automated adjudication. The active baseline remains the transparent rule system over approved, redacted, governed evidence fields.

## Context

Breeze Guard 26 is relevant because it is designed around Taiwanese Mandarin safety risks and uses an official category vocabulary that overlaps with this repo's interests:

- `scam`
- `fin_malpractice`
- `health_misinfo`
- `gender_bias`
- `group_hate`
- `pol_manipulation`

The overlap is strongest for scam-like Threads content, unlawful-financial or investment-lure content, and health-miracle or health-misinformation lures. It is weaker for categories that are important to general content safety but not core to this repo's scam-triage objective.

## Options Considered

1. Add Breeze Guard 26 immediately to the Phase 1 launch.
2. Ignore it until after the pilot.
3. Record it now as a deferred candidate with explicit boundaries.

## Rationale

Option 3 captures the useful research signal without changing the current launch scope.

Breeze Guard 26 may become useful after labels and redaction workflows are stable, but using it too early would blur the repo's current learning target: whether preserved Threads text, OCR, replies, and visible redirection evidence can support human-review-oriented triage through transparent baselines.

The model should be treated as a prompt-level text safety signal. It cannot verify identity, money movement, professional license status, link backends, account relationships, legal fraud facts, or medical truth.

## Consequences

- `docs/50-breeze-guard-26-candidate-baseline.md` records the model facts, category mapping, fit, preconditions, and claim boundaries.
- `docs/08-baseline-strategy.md` includes Breeze Guard 26 only as a deferred classifier candidate.
- `docs/09-phase-1-experiment-plan.md` routes any model-assisted or classifier-assisted test through a later decision record.
- `docs/11-budget-fit-analysis.md` keeps Breeze Guard 26 outside the current funded Phase 1 mainline.
- `experiments/baselines/README.md` blocks a Breeze Guard experiment log until explicit authorization exists.

## Follow-Up

Revisit only after:

- governed real evidence exists
- redaction has passed review
- labels are stable enough for a meaningful comparison
- the pilot decision memo supports a later classifier-assisted experiment
- a new decision record authorizes the exact inference mode, data boundary, cost, and run-record requirements
