# Decision 0073: Adopt Dedupe-First Full-Thread-Ready Gate

## Status

Accepted.

## Decision

Adopt `docs/53-dedupe-first-full-thread-ready-gate.md` as the required promotion gate before any future browser-session candidate can become an official selected item.

The current official checkpoint remains `threads_pilot_v1_0055`.

## Context

Run `0039` tested whether a larger approved browser-session supplement could solve the high-risk evidence shortage.

It did not. The run reached 50 reviewed candidates and 20 local selected candidate entries, but second review found 11 `uncertain` entries, 9 duplicate or near-duplicate exclusions, and 0 new final scam/high-risk examples.

The evidence bottleneck is source/reply context and dedupe quality, not raw browser-search volume.

## Consequence

Future browser-session runs must pass a dedupe-first and full-thread-ready gate before promotion.

The next preferred evidence path remains confirmed-pointer intake. Browser-session search can still be used for bounded candidate discovery, false-positive pressure, and uncertainty calibration, but not as an automatic source of official checkpoint expansion.
