# Decision 0078: Authorize Dedupe-First Browser Candidate Quality Run

## Status

Accepted.

## Decision

Authorize run `0041` as a more aggressive but bounded dedupe-first browser candidate quality test.

The run settings are:

- review cap: maximum 60 candidates;
- selected quality-review cap: maximum 30 candidates;
- source: approved browser session;
- required gates: dedupe-first, full-thread/reply-ready, evidence attribution, redaction, strict validation when local records are built, and fast different-angle second review;
- goal: candidate quality test, not official scam expansion.

## Context

Run `0039` showed that aggressive browser-session discovery can produce strict-valid local candidate records, but it also produced duplicate and context-thin pressure with no new final scam/high-risk examples.

The project owner requested a more active non-confirmed-pointer alternative:

```text
review cap: 50-60 candidates
selected cap: 20-30 items
source: approved browser session
required: dedupe-first + full-thread/reply-ready
goal: candidate quality test, not official scam expansion
```

## Consequence

Run `0041` can proceed only after preflight confirms access readiness, controlled-store boundaries, dedupe inputs, and full-thread/reply-ready feasibility.

No candidate from run `0041` may become an official checkpoint item unless a later decision explicitly promotes validated candidates.
