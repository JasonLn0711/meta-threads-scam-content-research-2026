# Decision 0011: Add Stakeholder Authorization Packet

## Date

2026-04-23

## Decision

Add a stakeholder authorization packet and decision-record template before any real Threads source is used.

The packet defines what the project owner should bring to the approval meeting, what questions stakeholders must answer, what approval outcomes are valid, and how the decision should be recorded without exposing raw or sensitive evidence.

## Context

The project now has:

- dataset schema and labeling schema
- annotation guideline
- synthetic dry-run results
- source intake and sampling-frame package
- pilot execution plan
- go/no-go checklist
- real-pilot readiness review

The remaining blocker is not tooling. It is stakeholder authorization for a specific source, field set, storage plan, access list, retention rule, and redaction approach.

## Options Considered

1. Ask stakeholders informally and fill templates afterward.
2. Use only the existing pilot kickoff memo and data authorization request.
3. Add a packet that turns the approval meeting into a structured decision workflow.

## Rationale

Option 3 reduces ambiguity. The project should not rely on informal approval, and the data authorization request alone is too narrow to guide a full stakeholder conversation about source choice, sampling, storage, redaction, annotation, and reporting limits.

The packet also reinforces that "approved without limitations" is not a valid data-governance state.

## Consequences

- Real collection remains blocked until the stakeholder authorization decision is recorded.
- Every real source must have a source candidate intake, sampling frame, data authorization request, and stakeholder decision record.
- The first real pilot still requires go/no-go review, pilot batch work order, and real-pilot readiness review.
- No raw Threads evidence or sensitive material should be placed in the packet.

## Follow-Up

The project owner should use `docs/36-stakeholder-authorization-packet.md` and `templates/stakeholder_authorization_decision_record.md` for the next stakeholder approval meeting.

If the outcome is `approved` or `approved_with_limits`, update the governance registers and proceed to the go/no-go checklist.

If the outcome is `revise_request` or `rejected_or_paused`, keep the project synthetic-only and revise the source proposal or scope.
