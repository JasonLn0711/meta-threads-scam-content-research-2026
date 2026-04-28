# Decision 0129: Realign Repo To Labor-Efficient Candidate Discovery

Date: 2026-04-28

## Decision

From this point forward, the repo's forward-looking goal is labor-efficient investment-scam candidate discovery:

```text
Build a scalable, stable, reviewable, and labor-efficient method for discovering enough review-worthy Threads investment-scam candidates with as little human review burden as possible.
```

This record preserves prior checkpoint, Track A, Track B, report, and experiment history. It does not replace the existing Track B decision file that also uses the `0129` prefix; the filename here follows the requested realignment path.

## Context

The repo had already shifted from general scaffold work toward scalable investment-scam candidate discovery. The next correction is sharper: discovery yield and reviewer burden are not primary and secondary goals. They are joint success conditions.

A method that surfaces many suspicious candidates but requires excessive manual reading, sorting, summarization, schema filling, and second-review work is not operationally scalable. A method that reduces labor but fails to surface enough review-worthy candidates is also not useful.

## Options Considered

1. Continue framing the repo as investment-scam detection with reviewer-burden metrics.
2. Treat reviewer-burden reduction as a secondary workflow improvement.
3. Realign the repo around labor-efficient candidate discovery as the core operational goal.

## Rationale

Option 3 is selected because the operational problem is to use a small amount of human labor to find enough candidates worth reviewing.

Discovery yield and reviewer burden are coupled success conditions. Future experiments should jointly evaluate:

- review-worthy yield per source arm;
- high-risk yield per reviewer hour;
- average, median, and p95 review time per candidate;
- candidates reviewed per hour;
- percentage of fields auto-filled;
- percentage of fields manually corrected;
- summary usefulness rating;
- percentage of candidates requiring full original-thread reading;
- second-review rate;
- reviewer disagreement rate;
- hard-negative false-positive pressure;
- insufficient-evidence rate.

UI, API, and schema demos are demonstration surfaces. The research output is the validated method and workflow.

## AI/System Support Boundary

AI and system support should reduce:

- reading burden for long posts and threads;
- summarization burden for posts, replies, and OCR content;
- signal-family extraction burden;
- schema prefill burden;
- triage and priority-ranking burden;
- hard-negative risk identification burden;
- repo-safe reviewer-note and aggregate-reporting burden.

AI and system support must not:

- make legal fraud determinations;
- make final scam-label decisions without human review;
- recommend enforcement, takedown, account action, or public warning;
- claim production detector status;
- conduct automated enforcement;
- infer private-message content;
- authorize broad crawler/browser expansion, private-message access, account/profile graph capture, landing-page or redirect-chain capture, model training, public release, or raw evidence in git.

## Consequences

- `docs/61-labor-efficient-investment-scam-candidate-discovery-north-star.md` becomes the forward-looking north-star document.
- Existing discovery-method docs should be read through the joint yield-plus-labor lens.
- Track B work should be interpreted as testing candidate discovery yield, reviewer burden, hard-negative false-positive pressure, and the feasibility of AI/system-assisted reviewer workflow.
- The next research layer after Track B should focus on reviewer assist layer design, schema prefill evaluation, summary-assisted review evaluation, priority-ranking evaluation, labor-savings measurement, and decision-support UI/API demonstration.
- Historical checkpoint records, prior reports, Track A/Track B history, decision logs, and experiment notes remain unchanged.

## Follow-Up

Future forward-looking docs, experiment logs, and report templates should include yield, reviewer-burden, hard-negative, and AI/system-assist metrics before treating a method as scalable.

