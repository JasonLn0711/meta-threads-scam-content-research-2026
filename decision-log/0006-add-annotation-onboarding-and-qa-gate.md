# Decision 0006: Add Annotation Onboarding And QA Gate

## Identity

- Date: 2026-04-23
- Status: accepted
- Owner: Jason

## Decision

Add a formal annotator onboarding and annotation QA gate before the first real 50-item pilot can produce baseline-ready labels.

This gate requires annotator onboarding, calibration review, in-pass QA after the first 10-15 rows, second-review routing, adjudication, and guideline revision logging.

## Context

The repo already has a v1 annotation guideline, calibration protocol, adjudication template, and pilot runbook. The missing layer was quality control during actual annotation:

- annotator readiness could be assumed rather than checked
- the first 10-15 pilot rows might reveal label drift too late
- guideline revision needs could be scattered across notes
- baseline work could start before label quality is understood

## Options Considered

| Option | Pros | Cons | Decision |
|---|---|---|---|
| Rely on the full annotation guideline only | Less process | New annotators may miss operational rules and edge-case boundaries | Rejected |
| Add heavy annotation management tooling | More control | Overbuilt for a 50-item pilot | Rejected |
| Add lightweight onboarding and QA docs/templates | Practical and reviewable | Adds a small checklist burden | Accepted |

## Rationale

The first pilot is small enough that a few inconsistent labels can distort all early conclusions. A lightweight QA gate protects:

- `scam` versus `uncertain` boundaries
- `uncertain` versus `insufficient_evidence` boundaries
- OCR-only and reply-only evidence handling
- false positives on legitimate finance, recruitment, giveaway, health, and marketing content
- baseline metrics from weak or unreviewed labels

## Consequences

The annotation workflow should now use:

- `docs/30-annotator-onboarding-quickstart.md`
- `docs/31-annotation-quality-control-plan.md`
- `templates/annotator_onboarding_checklist.md`
- `templates/annotation_qa_checklist.md`
- `templates/guideline_revision_log_template.md`

Do not treat a pilot dataset as baseline-ready until QA and second-review routing have been completed.

## Next Review

Review this decision after the 5-item calibration and again after the first 10-15 real pilot rows, if the pilot is authorized.

