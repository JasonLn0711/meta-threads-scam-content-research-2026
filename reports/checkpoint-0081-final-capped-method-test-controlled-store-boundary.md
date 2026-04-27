# Checkpoint 0081 Final Capped Method-Test Controlled-Store Boundary

## Purpose

Define what may appear in tracked repo artifacts and what must remain controlled-store-only for any authorized Track B execution.

This boundary is also used by Track A as a dry-run check, even though Track A should use no new evidence.

## Allowed In Tracked Repo Artifacts

- repo-safe candidate IDs;
- source-arm names;
- source-family labels;
- signal-family labels;
- evidence-surface presence flags;
- category-level contact or external-link indicators;
- dedupe status;
- evidence completeness score;
- review time;
- reviewer role aliases;
- labels and risk tiers;
- hard-negative flags;
- stop-rule IDs;
- aggregate metrics;
- redacted reviewer notes.

## Controlled-Store-Only

- raw Threads URLs;
- raw handles;
- screenshots;
- raw post text;
- raw reply/comment text;
- raw OCR text if it contains sensitive or directly identifying content;
- contact IDs;
- stock names or stock codes when sensitive to the case context;
- price values when sensitive to the case context;
- credentials, tokens, cookies, HAR files, storage state, or browser/session artifacts;
- exact controlled-store paths;
- stakeholder case IDs;
- private recipient details.

## Prohibited Collection Surfaces

Unless a later decision explicitly authorizes otherwise:

- private messages;
- account/profile graph capture;
- follower/following graph capture;
- landing-page or redirect-chain capture;
- credentialed external-site traversal;
- any automated enforcement action.

## Incident Rule

Any raw evidence leakage into tracked repo artifacts triggers immediate pause and incident note.
