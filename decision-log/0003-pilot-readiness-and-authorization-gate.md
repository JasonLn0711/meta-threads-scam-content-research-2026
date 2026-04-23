# Decision 0003: Add Pilot Readiness And Authorization Gate

## Identity

- Date: 2026-04-23
- Status: accepted
- Owner: Jason

## Decision

Before collecting or annotating any real Threads examples, require a pilot readiness gate covering data authorization, collection/redaction rules, annotator calibration, annotation operations, and baseline readiness.

The project may continue using synthetic examples for tooling and calibration practice, but real examples require an explicit authorization record.

## Context

The repo now contains the phase-1 research scaffold: schema, annotation guide, collection/redaction SOP, validation and audit scripts, baseline scripts, calibration scripts, and synthetic samples.

The next research risk is not technical capability. It is starting the real pilot without clear source approval, redaction rules, or annotator calibration.

## Options Considered

| Option | Pros | Cons | Decision |
|---|---|---|---|
| Start collecting immediately | Fastest path to examples | Risks unclear authorization and inconsistent labels | Rejected |
| Wait for full institutional data process before any pilot prep | Maximally cautious | Slows down harmless synthetic calibration and planning | Rejected |
| Add a go/no-go gate before real examples | Keeps momentum while protecting governance and quality | Adds a small process step | Accepted |

## Rationale

The first real dataset will shape the project. If it is collected under unclear authority or annotated inconsistently, later baselines will be difficult to defend.

A go/no-go checklist keeps the project practical:

- it does not add production infrastructure
- it does not authorize automation
- it makes stakeholder decisions explicit
- it protects raw evidence from entering git
- it requires calibration before the 50-item pilot

## Consequences

- Use `docs/25-stakeholder-pilot-kickoff.md` to request stakeholder approval.
- Use `docs/26-pilot-go-no-go-checklist.md` before real collection.
- Use `templates/data_authorization_request.md` for the approval record.
- Do not collect real examples until the gate is satisfied.
- If the gate fails, revise the relevant governance, redaction, annotation, or workflow docs before proceeding.

## Next Review

Review this decision after the 5-item calibration and before the 50-item pilot begins.
