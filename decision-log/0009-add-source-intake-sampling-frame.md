# Decision 0009: Add Source Intake And Sampling Frame

## Identity

- Date: 2026-04-23
- Status: accepted
- Owner: Jason

## Decision

Add a source intake and sampling-frame gate before any real Threads source can feed the pilot dataset.

Every real source candidate must be reviewed for authorization clarity, privacy exposure, redaction burden, evidence quality, content-form coverage, label-bucket value, operational burden, and source-skew risk.

## Context

The project now has governance, pilot execution, annotation QA, expansion planning, and post-pilot decision frameworks. The remaining upstream risk is source selection.

Without a source intake step, the first real pilot could accidentally rely on a source that is:

- not actually approved for annotation
- too privacy-heavy
- too incomplete for labeling
- too skewed to support baseline interpretation
- dependent on unapproved account, profile, link, or landing-page context

## Options Considered

| Option | Pros | Cons | Decision |
|---|---|---|---|
| Let authorization request handle all source selection | Simpler | Does not force sampling balance or source-skew review | Rejected |
| Add source intake and sampling frame | Makes source quality explicit before collection | Adds one more pre-collection artifact | Accepted |
| Collect first, assess source quality later | Fast | Risks wasting annotation time on unusable or unsafe evidence | Rejected |

## Rationale

Source selection shapes the entire dataset. A balanced diagnostic sample needs positive, negative, ambiguous, and insufficient-evidence examples across content forms. It also needs a clear record of source limitations so the project does not overclaim.

## Consequences

Before real collection:

- complete `templates/source_candidate_intake.md`
- add source candidates to `governance/source-intake-register.md`
- build `templates/source_sampling_frame_template.csv`
- include approved source candidates in the pilot work order

No real source should enter collection solely because it is convenient or high-volume.

## Next Review

Review after the first real source is proposed or after the 50-item pilot sampling frame is built.

