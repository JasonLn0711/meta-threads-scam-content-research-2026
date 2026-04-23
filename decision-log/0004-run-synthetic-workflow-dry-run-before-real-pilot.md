# Decision 0004: Run Synthetic Workflow Dry Run Before Real Pilot

## Identity

- Date: 2026-04-23
- Status: accepted
- Owner: Jason

## Decision

Before any real Threads evidence is collected, run the dataset validation, audit, conversion, and rule-baseline workflow on synthetic/redacted examples and record the results as workflow QA.

The synthetic dry run is allowed because it uses no real Threads evidence, no personal data, no live URLs, and no raw screenshots.

## Context

The repo now contains the phase-1 schema, annotation guideline, synthetic samples, pilot governance docs, and local QA/baseline scripts. The next risk is trying the full workflow for the first time on real stakeholder evidence.

Running the workflow on synthetic records gives the project a low-risk way to test:

- whether CSV and JSON examples validate
- whether CSV-to-JSONL conversion works
- whether the audit script reports missing fields, source skew, and duplicates
- whether rule-baseline variants use the intended evidence fields
- whether generated outputs stay in ignored local folders

## Options Considered

| Option | Pros | Cons | Decision |
|---|---|---|---|
| Wait for real pilot data before testing scripts | Tests only realistic data | Risks discovering schema/tooling problems during governed pilot | Rejected |
| Add more automation or collection scripts | Could speed future work | Would cross the project boundary before authorization | Rejected |
| Run a synthetic workflow dry run | Tests the pipeline safely and cheaply | Does not measure real performance | Accepted |

## Rationale

The dry run protects the first real pilot from avoidable tooling friction while preserving the hard boundary against unauthorized collection.

The results also confirmed that:

- strict validation passes on the synthetic CSV and JSON batch
- conversion to JSONL works
- audit correctly flags synthetic-only source skew
- OCR and reply fields materially affect synthetic rule-baseline decisions
- `uncertain` should remain outside binary metrics

## Consequences

- Keep using synthetic examples for local workflow QA.
- Do not treat synthetic metrics as real Threads performance.
- Use the same commands after the 50-item pilot is authorized and annotated.
- Keep generated predictions and local processed outputs out of git.
- Record aggregate findings only in `experiments/` and `docs/`.

## Next Review

Review this decision after the authorized 50-item pilot audit and baseline comparison.
