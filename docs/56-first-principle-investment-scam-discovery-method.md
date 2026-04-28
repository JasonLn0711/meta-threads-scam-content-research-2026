# First-Principle Investment Scam Discovery Method

## Purpose

Record the repo's supporting discovery-method goal so future work does not drift into package maintenance, generic governance, or model enthusiasm by habit.

From this point forward, the first-principle goal is:

```text
Build a scalable, stable, reviewable, and labor-efficient method for discovering enough review-worthy Threads investment-scam candidates with as little human review burden as possible.
```

Use [61-labor-efficient-investment-scam-candidate-discovery-north-star.md](61-labor-efficient-investment-scam-candidate-discovery-north-star.md) as the current north-star document.

This is a candidate-discovery research goal. It is not a production detector, platform enforcement system, legal fraud determination process, public warning list, or authorization for broad data collection.

## Why Investment Scam First

Investment scam content is the first priority because:

- it appears to be one of the largest and highest-harm scam categories in the current stakeholder context;
- it has repeated visible signal families across posts, replies, images, profiles, and private-channel migration cues;
- it often exposes public candidate-discovery signals before the final victimization step;
- it gives the repo a focused domain for measuring discovery yield, reviewer burden, false-positive pressure, and hard-negative protection;
- a working investment-scam discovery method can later be adapted to other common scam families.

## Objective Hierarchy

1. Discover enough review-worthy Threads investment-scam candidates with as little human review burden as possible.
2. Preserve enough post, reply/comment, OCR, link/contact, and profile-context evidence for human review.
3. Measure candidate quality, discovery yield, duplicate load, reviewer burden, false-positive pressure, and false-negative pressure as coupled success conditions.
4. Protect hard negatives such as ordinary investment discussion, financial education, and anti-scam warnings.
5. Keep labels human-review-centered: `scam`, `non_scam`, `uncertain`, and `insufficient_evidence`.
6. Use AI/system support to reduce reading, summarization, signal extraction, schema prefill, triage, hard-negative checking, and repo-safe reporting burden without making final scam determinations.
7. Use governance, validation, and package work as support for scalable discovery, not as the final goal.
8. Expand to other scam families only after the investment-scam discovery method is demonstrably useful.

## What Counts As Progress

Work counts as progress when it improves at least one of these:

- candidate-discovery method design;
- investment-scam signal-family coverage;
- full-thread/reply readiness;
- visible funnel and private-channel migration cue detection;
- profile-context and account-pattern use without graph overreach;
- dedupe and source-linkage quality;
- hard-negative protection;
- reviewer workflow and second-review clarity;
- metrics for discovery yield and reviewer burden;
- reviewer-assist design, schema prefill, summary-assisted review, priority ranking, and labor-savings measurement;
- strict validation and repo-safe reporting;
- decision gates for capped discovery experiments.

Work is not enough by itself when it only:

- creates another package without improving discovery learning;
- increases record count without measuring candidate quality;
- broadens collection before the source boundary and stop rules are clear;
- trains a model before the discovery question, labels, and evidence fields are stable;
- treats smoke-test baseline metrics as operational readiness;
- treats investment keywords alone as scam evidence;
- ignores replies/comments, where many funnel cues appear.
- treats labor reduction as a secondary convenience instead of an operational feasibility constraint.

## Scalable Discovery Method Tracks

### Track 1: Signal-Family Learning

Use confirmed and reviewed examples to refine signal families such as:

- investment teacher, assistant, advisor, or expert framing;
- profit-proof, earnings-sheet, testimonial, or witness-style reassurance;
- public stock-tip, watchlist, holdings help, or individualized investment help;
- no-fee or anti-scam trust-building language used as funnel protection;
- private-channel migration cues, including DM, group, LINE, Telegram, WhatsApp, Messenger, or similar contact movement;
- comment-layer contact hijack, safe-contact claims, or supporting-account coordination;
- external-link, domain-category, or redirect-presence signals;
- account-level repetition, posting frequency, and multi-style profile behavior when authorized and repo-safe.

### Track 2: Candidate Discovery Source Design

Future candidate discovery should compare bounded source families, not rely on one repeated keyword set:

- CIB/stakeholder confirmed pointers;
- reviewer-supplied candidates;
- approved browser-session candidates under explicit caps;
- diversified risk-probe seed matrices;
- existing checkpoint records and hard negatives;
- account-source context only when a decision record authorizes it.

Open-ended crawler expansion, broad keyword search, graph capture, private-message access, landing-page capture, and redirect-chain capture remain blocked unless a later decision explicitly authorizes them.

### Track 3: Evidence Completeness

Investment scam discovery must be full-thread and reply-aware because the top-level post may look ordinary while the funnel appears in:

- replies or comments;
- screenshots or image text;
- external-link/contact signals;
- profile text or account pattern;
- repost/share context if authorized;
- private-channel migration cues visible in public evidence.

When evidence is too thin, keep the record `uncertain` or `insufficient_evidence` instead of forcing a scam label.

### Track 4: Hard-Negative Protection

The discovery method must deliberately preserve hard negatives:

- anti-scam warning posts;
- ordinary investment discussion;
- non-directed financial education;
- market commentary without funnel behavior;
- personal investment journaling without contact, proof, or conversion cues.

False positives are not just a metric problem. They are a governance and trust problem.

### Track 5: Discovery And Labor Metrics

Future capped discovery experiments should measure:

| Metric | Meaning |
|---|---|
| candidates reviewed | Total candidate load |
| review-worthy yield | Share worth human review after dedupe |
| final scam/high yield | Share ending as `scam` / `high` after review |
| hard-negative yield | Share useful for false-positive calibration |
| duplicate rate | Candidate waste from repeated/near-duplicate items |
| full-thread availability | Whether replies/comments were available enough for review |
| average review time per candidate | Mean human burden |
| median review time | Typical human burden |
| p95 review time | Worst-tail human burden and scaling risk |
| candidates reviewed per hour | Reviewer throughput |
| percentage of fields auto-filled | Schema-prefill assistance level |
| percentage of fields manually corrected | Automation correction burden |
| summary usefulness rating | Whether summaries reduce review effort |
| percentage of candidates requiring full original-thread reading | Residual manual-reading burden |
| second-review rate | Rule instability and review complexity |
| disagreement rate | Reviewer alignment pressure |
| uncertain/insufficient rate | Evidence incompleteness pressure |
| false-positive pressure | Risk of overflagging lawful or warning content |
| false-negative pressure | Risk of missing high-risk funnel behavior |
| review-worthy yield per source arm | Source-arm usefulness |
| high-risk yield per reviewer hour | Joint discovery and labor-efficiency outcome |

Precision, recall, and F1 remain useful, but they are not enough to judge discovery method usefulness.

## Next Method Question

The next research question should be:

```text
What bounded, reviewable candidate-discovery method produces enough review-worthy Threads investment-scam candidates while minimizing reviewer burden, preserving hard-negative boundaries, controlling false-positive pressure, and keeping evidence handling governance-safe?
```

Any future capped experiment should answer this question directly.

## Expansion Beyond Investment Scams

Do not expand to other scam families merely because the repo wants more categories.

Expand only after investment-scam discovery has a useful method and reviewer workflow. Likely later families include:

- romance or fake-friendship scam openings;
- escort or adult-service scam openings;
- loan or debt-relief scams;
- job or work-from-home scams;
- shopping or fake seller scams;
- impersonation or pseudo-official service scams;
- charity, recovery, or public-good trust scams.

Each later family should have its own signal families, hard negatives, evidence boundary, and discovery-yield metrics.

## Relationship To Governance

Governance is not a detour. It is what allows the discovery method to be used in reality.

However, governance artifacts should always support one of these discovery-method needs:

- keep evidence usable for review;
- prevent raw data leakage;
- preserve uncertainty;
- control false positives;
- define who can approve collection or use;
- make capped experiments auditable;
- stop expansion when method quality or legal/privacy status is insufficient.

## Immediate Repo Implication

Future work should default to:

```text
investment-scam scalable candidate-discovery method
→ capped method test design
→ human review and second review
→ discovery-yield and reviewer-burden evaluation
→ reviewer-assist and labor-savings evaluation
→ decision on expansion, revision, or pause
```

It should not default to:

```text
more package maintenance
→ more broad collection
→ more records without yield metrics
→ model training
→ production claims
```

The current checkpoint 0081 readiness and shadow-pilot planning work should be interpreted as preparation for a controlled candidate-discovery method test, not as a replacement for the discovery-method goal.

## Current Design Artifacts

- [57-investment-scam-discovery-signal-family-matrix.md](57-investment-scam-discovery-signal-family-matrix.md) defines the signal-family matrix for post, thread, account-context, and funnel candidates.
- [62-reviewer-assist-layer-design.md](62-reviewer-assist-layer-design.md) defines the next research layer for reducing reviewer reading, summarization, signal extraction, schema filling, triage, and reporting burden while preserving human final judgment.
- [../reports/checkpoint-0081-investment-scam-discovery-method-test-charter-draft.md](../reports/checkpoint-0081-investment-scam-discovery-method-test-charter-draft.md) is the design-only charter draft for a future capped method test.
- [../decision-log/0116-open-checkpoint-0081-investment-scam-discovery-method-test-charter-draft.md](../decision-log/0116-open-checkpoint-0081-investment-scam-discovery-method-test-charter-draft.md) opens these design artifacts without authorizing execution.
