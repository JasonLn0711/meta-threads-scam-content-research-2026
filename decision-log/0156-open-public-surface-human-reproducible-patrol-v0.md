# 0156 - Open Public-Surface Human-Reproducible Patrol v0 Design

Date: 2026-05-06

## Decision

Open `public_surface_human_reproducible_patrol_v0` as a design-only sub-mode
of `controlled_browser_run_scoped`.

This accepts the safer research idea that a future fallback browser source arm
should behave like a bounded human research patrol over public surfaces, not
like a crawler scanning a site.

## Boundary

The patrol can be considered only when all of these are true:

- official Threads API access is unavailable or insufficient for the specific
  source-arm purpose;
- the route is public without login, special access, follower status, or
  workaround;
- a human reviewer can substantially repeat the path from repo-safe metadata;
- a run-scoped decision and work order exist before execution;
- raw screenshots, text, URLs, handles, browser artifacts, cookies, tokens,
  session state, and exact controlled-store paths stay outside git;
- the run uses one worker, tiny caps, bounded scroll, conservative dwell time,
  and explicit stop rules;
- the system does not use stealth, bypass, proxy rotation, hidden APIs,
  CAPTCHA bypass, rate-limit bypass, or personal-account session harvesting.

## Explicit Non-Authorization

This decision does not authorize:

- live Threads collection;
- a Playwright patrol against Threads;
- personal-account browser crawling;
- one-second automated fetching;
- login-only collection;
- DOM text scraping as the default method;
- broad profile, follower, feed, or account-graph capture;
- production monitoring;
- final automated scam, legal fraud, enforcement, public-warning, or takedown
  decisions.

## New Artifacts

- `docs/74-public-surface-human-reproducible-patrol-v0.md`
- `templates/public_surface_patrol_work_order.md`

## Consequences

The next useful fallback step, if the official API path is unavailable or
insufficient, is to fill `templates/public_surface_patrol_work_order.md` for
one tiny public-surface viability proposal.

No live browser automation begins from this decision alone.
