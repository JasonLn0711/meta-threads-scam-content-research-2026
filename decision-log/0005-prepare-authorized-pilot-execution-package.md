# Decision 0005: Prepare Authorized Pilot Execution Package

## Identity

- Date: 2026-04-23
- Status: accepted
- Owner: Jason

## Decision

Prepare a concrete post-authorization pilot execution package before any real Threads evidence is collected.

The package defines what to do after a stakeholder `go` or `go_with_limits` decision, while preserving the current default of `no_go` for real data until authorization is recorded.

## Context

The project now has:

- dataset schema and labeling schema
- annotation guide
- collection/redaction SOP
- pilot go/no-go checklist
- synthetic samples and dry-run results
- validation, audit, conversion, annotation-agreement, and rule-baseline scripts
- report-v0 review package

The remaining risk is operational: once stakeholders approve a pilot, the team needs a precise work order, file naming plan, command sequence, and post-pilot summary template so the first real batch does not improvise its data handling.

## Options Considered

| Option | Pros | Cons | Decision |
|---|---|---|---|
| Wait until approval to write the execution plan | Avoids unused process docs | Risks rushed or inconsistent pilot setup | Rejected |
| Start a real pilot draft now | Faster once examples arrive | Could imply approval or encourage premature collection | Rejected |
| Prepare execution docs without collecting data | Makes the pilot ready while preserving the authorization gate | Adds a small amount of process documentation | Accepted |

## Rationale

The first real pilot will set the project's evidence standard. A clear execution package reduces avoidable mistakes:

- raw evidence entering git
- unclear field approvals
- ad hoc filenames
- missing redaction notes
- annotation before validation
- binary metrics that force `uncertain` or `insufficient_evidence`
- post-pilot results without governance context

## Consequences

The pilot should now use:

- `docs/29-authorized-pilot-execution-plan.md`
- `templates/pilot_batch_work_order.md`
- `templates/pilot_result_summary.md`
- `governance/pilot-authorization-register.md`

No real data collection is authorized by this decision.

## Next Review

Review this decision after the first stakeholder authorization decision or after the 50-item pilot completes, whichever comes first.

