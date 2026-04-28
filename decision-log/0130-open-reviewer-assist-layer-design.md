# Decision 0130: Open Reviewer Assist Layer Design

Date: 2026-04-28

## Decision

Open a design layer for labor-efficient reviewer assistance:

```text
Reviewer Assist Layer
```

The layer is designed to reduce reading, summarization, signal extraction, schema filling, triage, and aggregate-reporting burden while preserving human final judgment.

This record does not replace the existing Track B decision file that also uses the `0130` prefix. It preserves the historical Track B primary-review record and opens a separate forward-looking design layer.

## Context

The repo's updated first-principle goal is to use a small amount of human labor to find enough review-worthy Threads investment-scam candidates.

Track B should therefore measure not only whether candidates are found, but also which reviewer tasks consume time and which parts of review can be safely assisted.

## Rationale

Reviewer assistance is the next logical research layer because the candidate-discovery method is only operationally useful if it reduces avoidable human work.

The layer should help reviewers:

- understand candidates faster;
- avoid full raw-thread reading when summaries are sufficient;
- inspect signal-family summaries;
- see hard-negative warnings;
- accept or correct schema prefill;
- prioritize candidates;
- record decisions faster;
- generate aggregate labor and yield metrics.

## Non-Authorizations

This decision does not authorize:

- model training;
- production deployment;
- production detector claims;
- final machine-only scam determinations;
- legal fraud determinations;
- enforcement recommendations;
- automated takedowns;
- public warning lists;
- account targeting;
- open-ended collection;
- broad crawler/browser expansion;
- private-message access;
- account/profile graph capture;
- landing-page or redirect-chain capture unless separately authorized;
- raw evidence in git.

## Human Role

Human reviewers retain final decisions, final labels, final risk levels, uncertainty handling, second review, adjudication, exception escalation, and governance interpretation.

The Reviewer Assist Layer may suggest, summarize, extract, prefill, rank, and aggregate. It must not decide.

## Consequences

- [../docs/62-reviewer-assist-layer-design.md](../docs/62-reviewer-assist-layer-design.md) becomes the forward-looking design artifact for reviewer assistance.
- Future Track B and post-Track-B work should capture labor observations needed to evaluate assisted review.
- UI/API/schema examples remain demonstration surfaces. The research contribution remains the validated method and workflow.

## Follow-Up

Before implementation, create or update:

- reviewer-assist evaluation plan;
- assisted-review worksheet template;
- schema-prefill correction log template;
- summary-usefulness rubric;
- signal-family extraction QA table;
- hard-negative hesitation log;
- priority-ranking evaluation table;
- labor-savings aggregate report template;
- governance review checklist for any assisted-review prototype.

