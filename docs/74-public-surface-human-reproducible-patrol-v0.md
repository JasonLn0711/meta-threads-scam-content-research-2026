# Public-Surface Human-Reproducible Patrol v0

Status: design only; not execution authorization

Date opened: 2026-05-06

Reference links checked on `2026-05-06`:

- Meta Threads API reference: `https://developers.facebook.com/docs/threads/reference`
- Meta Terms of Service: `https://www.facebook.com/terms`
- Meta Automated Data Collection Terms:
  `https://www.facebook.com/legal/automated_data_collection_terms`

## Purpose

This document defines a safer fallback shape for Discovery Method v1 when
official Threads API access is unavailable or insufficient.

The goal is not to turn this repo into a crawler. The goal is to test whether
a very small, public-surface, human-reproducible patrol can surface
review-worthy Threads investment-scam candidates while preserving governance,
privacy, platform-risk, and reviewer-burden controls.

This is a sub-mode of `controlled_browser_run_scoped`, not a new standing
permission.

## First Principle

The patrol is acceptable to consider only if a human reviewer could perform
substantially the same path manually:

```text
open a public Threads surface
-> use an approved query
-> review a bounded visible window
-> pause and inspect a small number of candidates
-> record repo-safe metadata only
-> store raw artifacts outside git if the run is authorized
```

If the system depends on login-only material, private surfaces, hidden APIs,
stealth, bypass, parallel harvesting, raw content extraction, or unreproducible
personalized feeds, it is outside this v0 design.

## Three Safety Conditions

| Condition | Meaning | Research reason |
|---|---|---|
| Public surface | The candidate path is visible without login, special permission, follower status, private-group access, or workaround. | Keeps the observation closer to public social information instead of account/session mining. |
| Low frequency | The run uses one worker, small caps, visible dwell time, bounded scrolls, and conservative interaction intervals. | Reduces load, review pressure, and accidental broad collection. It is not an anti-detection tactic. |
| Human reproducibility | The repo records the route, not the raw content: query, entry point, scroll-depth bucket, capture time, signal codes, and review status. | Lets a reviewer reconstruct the discovery path without committing raw Threads content to git. |

## Public Surface Definition

Allowed public surfaces are limited to surfaces that are visible without a
logged-in personal account or special access, such as:

- public search or keyword result pages;
- public hashtag-like result pages if available;
- public post pages reached from an approved public route;
- manually supplied public seeds, if the source is authorized.

Disallowed surfaces include:

- private accounts;
- follower-only content;
- login-only extra fields or expanded reply context;
- direct messages;
- account graphs, follower/following lists, or broad profile history;
- material reached through workaround, bypass, hidden API, proxy rotation,
  stealth mode, CAPTCHA bypass, or anti-rate-limit evasion.

## Low-Frequency Default

The first v0 viability run, if later authorized, should be tiny:

| Control | Default v0 limit |
|---|---|
| Query count | 1 to 3 approved queries |
| Visible-window review | at most 10 visible candidates per query |
| Selected candidate stubs | at most 3 total |
| Runtime cap | 20 to 30 minutes |
| Parallel workers | 1 |
| Scroll actions | bounded and manually explainable |
| Interaction pacing | no rapid-fire interactions; use conservative dwell time before capture |
| Candidate capture | one repo-safe metadata stub per selected candidate |
| Raw artifacts | outside git only, if the run-scoped record permits them |

The work order may make these limits stricter. It must not make them broader
without a later decision record.

Do not describe pacing as "avoid bot detection" or tune it to defeat platform
controls. Pacing is a research-scope, load, and review-burden control.

## Human-Reproducibility Trace

Each candidate surfaced by this patrol should preserve a repo-safe route:

```yaml
human_reproducibility_trace:
  route_type: public_search
  query_text_or_query_ref: approved_query_ref_only
  entry_point: threads_public_search
  capture_time: 2026-05-06T00:00:00+08:00
  scroll_depth_bucket: "01_10"
  surface_position_bucket: "visible_window"
  public_surface_check: true
  raw_artifact_ref: controlled_store_artifact_id_only
```

Allowed trace fields:

- approved query text or query reference, with no handles, URLs, or private
  identifiers;
- entry point category;
- capture timestamp;
- scroll-depth bucket, not a raw page dump;
- surface-position bucket;
- public-surface check;
- controlled artifact ID or hash, not a screenshot path;
- signal-family reason codes.

Forbidden trace fields:

- raw Threads post text;
- raw reply text;
- raw OCR text;
- raw URLs;
- raw handles, usernames, profile IDs, email addresses, phone numbers, or
  contact IDs;
- screenshots or screenshot paths;
- browser profiles, cookies, tokens, HAR files, or session artifacts;
- exact controlled-store paths.

## Playwright Boundary

Playwright can be considered only as an operator-assist harness after a
run-scoped decision and work order exist.

The first acceptable Playwright v0 shape is:

- open only approved public entry points;
- enforce query, runtime, and candidate caps;
- avoid DOM text extraction as the default;
- avoid stealth, proxy rotation, CAPTCHA bypass, hidden APIs, or login-session
  harvesting;
- produce a repo-safe metadata shell;
- store any raw screenshot or browser artifact outside git only when the
  run-scoped record allows it;
- stop before review if the surface requests login, exposes private material,
  or requires unapproved fields.

This repo should not add or run a live Playwright patrol against Threads until
`templates/public_surface_patrol_work_order.md` is filled and a matching
decision record explicitly authorizes a capped run.

## Output Contract

Repo-facing output must use `data-contracts/discovery_candidate_v1.schema.yaml`
with `source_arm_id: controlled_browser_run_scoped` and
`source_access_mode: controlled_browser_run_scoped`.

The patrol-specific method should be recorded as:

```yaml
source_access_submode: public_surface_human_reproducible_patrol_v0
```

The final label remains human-reviewed. The patrol may say a candidate is
review-worthy or route it to review; it must not make final scam, legal fraud,
enforcement, public-warning, or takedown decisions.

## Stop Rules

Stop immediately if:

- the path requires login or personal-account session state;
- the candidate cannot be reached from the approved public route;
- the run starts to behave like broad crawling or feed monitoring;
- rapid interactions, parallelism, infinite scroll, or bulk extraction become
  necessary;
- the surface exposes private, follower-only, or unrelated personal data;
- raw evidence would need to enter git;
- the reviewer cannot reproduce the route from the metadata trace;
- the official API becomes available and covers the same purpose under clearer
  authorization.

## Immediate Next Action

Do not run a browser patrol from this document alone.

The next action is to fill `templates/public_surface_patrol_work_order.md` for
one tiny v0 viability proposal and decide whether it remains `planning_only` or
can move to `ready_for_capped_controlled_browser_run`.
