# Decision 0131: Update Track B Dual-Success Evaluation Framing

Date: 2026-04-28

## Decision

Track B will evaluate both:

1. candidate-discovery effectiveness;
2. reviewer-labor efficiency.

This decision opens [../reports/checkpoint-0081-track-b-dual-success-evaluation-plan.md](../reports/checkpoint-0081-track-b-dual-success-evaluation-plan.md) as the repo-safe plan for measuring both sides.

This record does not replace the existing Track B decision file that also uses the `0131` prefix. It preserves the historical batch `0002` second-review record and opens a separate forward-looking evaluation-framing decision.

## Context

The repo's updated north star is:

```text
Use a small amount of human labor to find enough review-worthy Threads investment-scam candidates.
```

Track B should no longer be interpreted only as a capped live discovery method test. It is also a measurement opportunity for reviewer burden and future Reviewer Assist Layer design.

## Rationale

Track B must answer two questions:

1. Does the method surface enough review-worthy Threads investment-scam candidates?
2. Can the method operate with acceptable reviewer burden?

The second question is not secondary. It is required for the first question to matter operationally.

Candidate counts, high-risk yield, and final scam-label yield are not enough if the workflow requires excessive full-thread reading, manual schema filling, hard-negative hesitation, second review, and reviewer disagreement.

## Consequences

- Track B aggregate reports should separate discovery metrics, reviewer-labor metrics, and joint yield-per-reviewer-hour metrics.
- Candidate-review worksheets should collect repo-safe burden fields such as review duration, full-thread-read requirement, schema fields manually filled, hesitation reason, second-review reason, and hard-negative uncertainty reason.
- [../templates/track_b_candidate_review_template.md](../templates/track_b_candidate_review_template.md) is the repo-safe template for those fields.
- The future Reviewer Assist Layer should use Track B burden observations to decide what to summarize, prefill, rank, or flag.

## Non-Authorizations

This decision does not authorize:

- changing Track B caps;
- new evidence collection beyond existing Track B authorization;
- new source arms;
- open-ended collection;
- broad crawler/browser expansion;
- private-message access;
- account/profile graph capture;
- landing-page or redirect-chain capture;
- model training;
- production use or production detector claims;
- legal fraud determination;
- enforcement recommendation or automated enforcement;
- public release;
- raw evidence in git.

## Follow-Up

Use the dual-success evaluation plan when preparing future Track B aggregate reporting, stop-rule interpretation, and Reviewer Assist Layer evaluation artifacts.

