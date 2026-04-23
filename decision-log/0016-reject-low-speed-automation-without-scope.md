# Decision 0016: Reject Low-Speed Automation Without Scope

## Identity

- Date: 2026-04-23
- Status: accepted
- Owner: Jason

## Decision

Reject the request to treat low-speed automated Threads/Meta collection as accepted without legal approval, platform access conditions, stakeholder authorization, and approved scope.

Low-speed automation remains out of scope unless a later written authorization record explicitly approves:

- source or source category
- collection method
- platform access conditions
- allowed fields
- storage location
- access list
- retention rule
- redaction rule
- audit log requirements
- publication and sharing limits

## Context

The project owner requested recording that low-speed automated Threads/Meta collection is accepted and does not need legal approval, platform access conditions, stakeholder authorization, or approved scope.

That proposed change conflicts with the repository's hard boundary and the active governance posture. The current pilot is approved only for manual or stakeholder-provided collection under `go_with_limits`.

## Options Considered

| Option | Pros | Cons | Decision |
|---|---|---|---|
| Accept low-speed automation without scope controls | Faster collection and less upfront paperwork | Violates governance boundary; creates platform, privacy, evidence, and audit risk | Rejected |
| Treat rate limiting as sufficient control | Reduces operational load | Rate limiting does not define lawful access, field limits, storage, redaction, retention, or source suitability | Rejected |
| Keep manual-only pilot and require explicit authorization before any automation | Slower | Preserves auditability, privacy minimization, platform boundary, and evidence defensibility | Accepted |

## Rationale

Low speed changes collection volume, not collection authority.

Even a slow automated collector can:

- collect unapproved fields
- retain unnecessary personal data
- violate platform or source conditions
- create misleading source skew
- store raw evidence or URLs beyond approved limits
- normalize automation before the project has real pilot evidence

The project can revisit automation later, but only as a governed scope expansion.

## Consequences

- Do not build or run Threads/Meta scraping, crawling, browser automation, redirect expansion, landing-page capture, or profile review.
- Keep the first pilot manual-only or stakeholder-provided.
- Keep `configs/manual_collection_assistant.yaml` with automation flags disabled.
- Record any future automation proposal as a new authorization request before code or collection begins.

## Next Review

Review only after the 50-item manual pilot and pilot decision memo show whether automation is necessary and after stakeholders define source, platform, storage, retention, redaction, and audit limits.
