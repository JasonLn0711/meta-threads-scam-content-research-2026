# Decision 0007: Reject Unlimited 500-Item Collection

## Identity

- Date: 2026-04-23
- Status: accepted
- Owner: Jason

## Decision

Reject immediate "500-item real pilot batch without limitations" collection.

The project may plan for a 500-item expansion, but real collection must remain governed, staged, source-specific, and privacy-preserving.

## Context

The project owner requested moving directly to a 500-item real Threads batch and stated that all approvals were granted without limitations.

That request is useful as a scale target, but "without limitations" conflicts with the project's hard boundaries:

- data access constraints are part of the research design
- raw personal data and unnecessary screenshots must not enter git
- source type, collection method, allowed fields, storage, access, retention, and redaction rules must be recorded
- automated collection, scraping, crawling, browser automation, bulk export, and landing-page crawling remain unapproved unless separately authorized
- suspicion is not guilt, and weak evidence must remain weak evidence

## Options Considered

| Option | Pros | Cons | Decision |
|---|---|---|---|
| Collect 500 immediately without limits | Fastest route to volume | Violates governance, privacy, platform, annotation, and evidence-quality boundaries | Rejected |
| Treat chat approval as enough for unlimited collection | Simple | Does not define source, method, storage, retention, redaction, or access | Rejected |
| Plan a governed 500-item expansion after staged gates | Supports scale target while protecting evidence quality | Slower than unrestricted collection | Accepted |

## Rationale

A 500-item dataset is large enough that small early mistakes become systemic. The first real dataset should not scale until the project has evidence that:

- annotators can apply labels consistently
- redaction rules work on real evidence
- screenshots, OCR, links, handles, and replies can be handled safely
- source and content-form skew are understood
- baseline outputs remain explainable and not dominated by false positives

## Consequences

- Do not collect 500 real Threads items now.
- Do not collect real examples without a scoped authorization record.
- Use `docs/32-500-item-expansion-plan.md` as the safe path to a 500-item dataset.
- Use `templates/500_item_expansion_work_order.md` only after the 50-item pilot and expansion authorization are complete.
- Update the authorization register to show the unlimited 500-item request as `rejected_or_paused`.

## Next Review

Review after the authorized 50-item pilot completes and the pilot result summary recommends whether to expand.

