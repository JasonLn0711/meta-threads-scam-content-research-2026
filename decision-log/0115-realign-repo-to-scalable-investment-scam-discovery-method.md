# Decision 0115: Realign Repo To Scalable Investment Scam Discovery Method

## Status

accepted

## Date

2026-04-27

## Decision

Realign the repository's first-principle goal around finding a scalable, stable, and reviewable method for discovering Threads scam-post candidates at volume, starting with investment-scam content.

Governance, checkpoint packages, readiness analyses, baselines, and shadow-pilot planning remain important, but they are support structures for the discovery-method goal. They are not the final goal by themselves.

## Scope

This decision updates repo guidance so future work must explain how it advances at least one of:

- investment-scam candidate discovery;
- signal-family learning;
- full-thread/reply-aware evidence capture;
- hard-negative protection;
- dedupe/source-linkage quality;
- reviewer workflow and second-review clarity;
- discovery-yield and reviewer-burden measurement;
- capped discovery experiment design;
- future expansion from investment scams to other scam families.

The first-principle guidance is recorded in:

```text
docs/56-first-principle-investment-scam-discovery-method.md
```

## Non-Authorizations

This decision does not authorize:

- item `0082` or later;
- new evidence collection;
- browser/crawler expansion;
- open-ended search;
- new confirmed-pointer intake;
- account/profile graph capture;
- private-message access;
- landing-page or redirect-chain capture;
- embedding or model training;
- production detection;
- legal fraud determinations;
- public release;
- raw evidence in git.

## Rationale

The repo had naturally accumulated strong checkpoint, package, validation, and governance artifacts. Those artifacts are necessary for real-world use, but they can make the project appear to be circling package readiness instead of pursuing the central research goal.

The central goal is to learn how to discover Threads scam candidates at scale in a way that CIB/internal reviewers can actually inspect, trust, and govern. Investment scams are the correct first domain because they are high-volume, high-harm, and rich in visible public signal families.

## Consequences

- Future charters, readiness reports, and experiments should use the investment-scam discovery-method goal as their north star.
- Future capped experiments should measure discovery yield, duplicate load, full-thread availability, reviewer burden, false-positive pressure, false-negative pressure, and hard-negative protection.
- Generic record-count growth is not sufficient progress.
- Model training remains premature until the discovery question, evidence fields, labels, and reviewer workflow are stable.
- Expansion beyond investment scams should wait until the investment-scam method is useful enough to adapt.

## Next Step

Update the planned shadow-pilot charter draft so it is framed as a design-only candidate-discovery method test for investment scams.

No execution should begin until a separate capped decision records source boundary, candidate cap, reviewer roles, legal/privacy status, evidence boundary, retention, redaction, metrics, stop rules, and reporting format.
