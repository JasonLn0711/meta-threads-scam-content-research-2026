# Decision 0022: Record Controlled Low-Speed Crawler Acquisition Path

## Date

2026-04-24

## Decision

Accept a controlled low-speed crawler as the next practical acquisition path for the first Threads rehearsal item and first 10-15 item checkpoint, under the existing CIB-authorized API and automation scope.

This is not approval for open-ended scraping, bulk crawling, evasion, production monitoring, enforcement, or platform-scale data collection.

## Context

The project owner clarified that:

- CIB and other units currently cannot provide 1-2 redacted case examples.
- Manual controlled sampling is not available as the first practical path.
- Official API and research-required automation have CIB approval under Decision 0018 and the controlled launch record.
- A low-speed crawler is currently the most feasible way to acquire the first controlled item.

Decision 0016 remains valid for unscope automation. This decision records a scoped exception for the current CIB-authorized pilot, not a general permission to crawl Meta or Threads data.

## Controlled Crawler Definition

For this project, a controlled crawler means:

- one approved operator
- one run record before execution
- one source category and purpose
- explicit item or candidate limit
- explicit field allowlist
- low request rate
- no parallel crawling
- no credential/session artifacts in git
- raw outputs outside git only
- redacted local `thread_item` records only
- immediate stop on access, redaction, or policy uncertainty

## Initial Rehearsal Limits

The first crawler rehearsal must use these default limits unless a later controlled run record narrows them further:

| Limit | Default |
|---|---|
| Target output | 1 controlled rehearsal item |
| Candidate review cap | 5 candidates maximum |
| Runtime cap | 30 minutes maximum |
| Parallelism | 1 worker only |
| Request pacing | at least 30 seconds between page/API/object fetches |
| Burst behavior | no bursts |
| Retry behavior | at most 1 retry per failed fetch |
| Login/session handling | approved account/session only; credentials, tokens, cookies, profiles, and HAR files outside git |
| Raw output | controlled store outside git |
| Repo-visible output | redacted local-only `data/interim/manual_entry_0001.json` and generated `manual_record_0001.json` |

## Stop Conditions

Stop the crawler run immediately if any of the following occurs:

- login, access, rate-limit, captcha, challenge, or block state appears
- the crawler needs fields outside the run record
- raw URLs, handles, screenshots, credentials, tokens, cookies, profiles, HAR files, or unrelated personal data would enter git
- redaction cannot be completed before local annotation handoff
- the run drifts from one-item rehearsal into bulk collection
- the crawler begins capturing profile graph, follower/following, broad comments, unrelated accounts, or unrelated personal context
- destination, redirect, or landing-page capture becomes necessary but is not stated in the run record

## Rationale

The project cannot learn anything operational from an empty intake skeleton. It needs one real controlled item.

Because CIB redacted handoff and manual sampling are unavailable, the crawler path is now the smallest feasible way to produce the first controlled rehearsal item. The strict low-speed and one-item rehearsal limits keep the run aligned with the research scaffold:

- test collection and redaction mechanics
- test schema fit
- test whether approved fields are enough
- avoid premature 10-15 or 50-item accumulation
- preserve uncertainty and human review

## Consequences

- Add a controlled crawler acquisition plan.
- Add a controlled crawler run-record template.
- Update the collection SOP to distinguish controlled crawler acquisition from unscope scraping.
- Keep `data/interim/` and generated item-level outputs ignored.
- Do not start the first 10-15 item checkpoint until the one-item crawler rehearsal produces a strict-valid local record and the aggregate rehearsal review records `pass_ready_for_calibration_or_first_10_15` or `pass_with_limits`.

## Follow-Up

Before running any crawler:

1. Fill a local or controlled copy of `templates/controlled_crawler_run_record.md`.
2. Confirm the run limit is one rehearsal item.
3. Confirm raw output and session artifacts stay outside git.
4. Run the crawler only under the recorded low-speed limits.
5. Redact the selected item into `data/interim/manual_entry_0001.json`.
6. Build and strict-validate `data/interim/manual_record_0001.json`.
7. Complete the local rehearsal checklist and aggregate review.
