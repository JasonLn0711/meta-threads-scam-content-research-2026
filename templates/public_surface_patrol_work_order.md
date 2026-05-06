# Public-Surface Patrol Work Order

Use this template before any public-surface browser patrol is executed.

This template is for the `public_surface_human_reproducible_patrol_v0`
sub-mode described in `docs/74-public-surface-human-reproducible-patrol-v0.md`.
It does not authorize execution by itself.

Do not put raw Threads URLs, handles, source names, credentials, cookies,
browser/session artifacts, screenshots, raw post text, raw reply text, raw OCR
text, raw API responses, or exact controlled-store paths in this file.

## Identity

| Field | Value |
|---|---|
| Work order ID |  |
| Date opened |  |
| Decision record |  |
| Source arm ID | `controlled_browser_run_scoped` |
| Source access submode | `public_surface_human_reproducible_patrol_v0` |
| Operator |  |
| Reviewer owner |  |
| Purpose | public-surface candidate discovery viability / hard-negative calibration / query-route reproducibility test |

## Authorization

| Question | Answer |
|---|---|
| Is official API access unavailable or insufficient for this purpose? |  |
| Is a run-scoped decision recorded? |  |
| Is platform/legal/stakeholder approval recorded if required? |  |
| Is the route public without login or special access? |  |
| Is personal-account login excluded? |  |
| Are stealth, bypass, hidden API, proxy rotation, and CAPTCHA bypass excluded? |  |
| Are raw storage, retention, access, and redaction rules recorded outside git? |  |
| Are allowed fields and forbidden fields listed? |  |

If any required authorization answer is unclear, stop at `planning_only`.

## Public Surface Check

| Question | Answer |
|---|---|
| Entry point category | public search / public hashtag-like surface / public post from manual seed / other |
| Login required? | yes / no |
| Private, follower-only, or group-only content possible? | yes / no |
| Personalized feed dependency? | yes / no |
| Human can manually repeat the route? | yes / no |
| Reviewer-visible route description is repo-safe? | yes / no |

## Query And Route Plan

Queries must be approved search phrases or query references. Do not include
handles, URLs, emails, phone numbers, or private identifiers.

| Query strategy ID | Approved query text or query ref | Signal-family hints | Hard-negative control included? | Entry point | Scroll-depth bucket cap |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Scope

| Field | Value |
|---|---|
| Query count cap |  |
| Visible candidate cap per query |  |
| Selected candidate stub cap |  |
| Runtime cap |  |
| Parallel workers | `1` |
| Interaction pacing rule |  |
| Candidate capture rule |  |
| Screenshot/artifact policy | outside git only / not captured |
| Raw artifact reference policy | controlled artifact ID or hash only; no path |

## Allowed Actions

Check every allowed action for this work order:

- [ ] Open approved public entry points.
- [ ] Enter approved queries or route references.
- [ ] Perform bounded scroll actions.
- [ ] Inspect a small visible window.
- [ ] Select candidate stubs for human review.
- [ ] Capture raw screenshot/artifact outside git only if authorized.
- [ ] Write repo-safe metadata candidate records.

## Forbidden Actions

These remain forbidden:

- logged-in personal-account browser crawling;
- direct messages or follower-only content;
- broad profile, follower, or account-graph capture;
- DOM text scraping as the default method;
- hidden APIs, stealth, proxy rotation, CAPTCHA bypass, or rate-limit bypass;
- rapid-fire interactions or parallel sessions;
- raw Threads content, URLs, handles, screenshots, or browser artifacts in git;
- final automated scam, legal fraud, enforcement, public-warning, or takedown
  decisions.

## Repo-Safe Candidate Trace

Each selected candidate should produce a metadata-only trace:

```yaml
human_reproducibility_trace:
  route_type:
  query_text_or_query_ref:
  entry_point:
  capture_time:
  scroll_depth_bucket:
  surface_position_bucket:
  public_surface_check:
  raw_artifact_ref:
```

Use `data-contracts/discovery_candidate_v1.schema.yaml`.

## Review Metrics

| Metric | Value |
|---|---|
| queries attempted |  |
| visible candidates inspected |  |
| selected candidate stubs |  |
| reviewed count |  |
| review-worthy yield |  |
| high-risk yield per reviewer hour |  |
| average review time |  |
| median review time |  |
| p95 review time |  |
| duplicate rate |  |
| hard-negative false-positive pressure |  |
| insufficient-evidence rate |  |
| human-reproducible route rate |  |
| raw-evidence leakage incidents |  |

## Stop Rules

Stop immediately if:

- the path requires login;
- the public-surface check fails;
- the route cannot be reproduced from repo-safe metadata;
- the run drifts into broad crawling or feed monitoring;
- raw evidence would need to enter git;
- unapproved private or personal data appears;
- caps are reached;
- official API access becomes available and covers the same purpose more
  cleanly.

## Decision

Choose one:

- `planning_only`
- `ready_for_capped_controlled_browser_run`
- `revise_source_arm`
- `reject_source_arm`

Decision:

```text

```

Rationale:

```text

```
