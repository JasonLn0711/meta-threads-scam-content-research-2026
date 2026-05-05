# Discovery Source-Arm Work Order

Use this template before any Discovery Method v1 source arm is executed.

Do not put raw Threads URLs, handles, source names, credentials, cookies,
browser/session artifacts, screenshots, raw post text, raw reply text, raw OCR
text, raw API responses, or exact controlled-store paths in this file.

## Identity

| Field | Value |
|---|---|
| Work order ID |  |
| Date opened |  |
| Decision record |  |
| Source arm ID | `official_threads_api_keyword_search` / `official_threads_api_reply_context` / `controlled_browser_run_scoped` / `stakeholder_or_reviewer_pointer` / `manual_public_seed` / `hard_negative_comparator` / `synthetic_query_probe` |
| Operator |  |
| Reviewer owner |  |
| Purpose | candidate discovery / context completion / hard-negative calibration / API viability check / browser fallback viability check |

## Authorization

| Question | Answer |
|---|---|
| Is official API access documented? |  |
| Are required API permissions documented? |  |
| Is browser automation proposed? |  |
| If browser run is proposed, is a run-scoped decision recorded? |  |
| Is platform/legal/stakeholder approval recorded? |  |
| Are account/session boundaries recorded outside git if needed? |  |
| Are raw storage, retention, access, and redaction rules recorded? |  |
| Are allowed fields and forbidden fields listed? |  |

If any required authorization answer is unclear, stop at planning.

## Scope

| Field | Value |
|---|---|
| Query window |  |
| Query count cap |  |
| Surfaced candidate cap |  |
| Human-reviewed candidate cap |  |
| Runtime cap |  |
| Parallel workers |  |
| Minimum delay or official API rate rule |  |
| Retry limit |  |
| Allowed evidence surfaces | metadata / post / reply / OCR / link-contact category / account-context metadata |
| Forbidden evidence surfaces |  |

## Query Strategy

| Query strategy ID | Signal family hints | Hard-negative control included? | Notes |
|---|---|---|---|
|  |  |  |  |

## Repo-Safe Output Contract

Use `data-contracts/discovery_candidate_v1.schema.yaml`.

Allowed repo-facing output:

- metadata-only discovery candidate records;
- source-arm aggregate metrics;
- redacted review notes;
- decision implication.

Forbidden repo-facing output:

- raw Threads content;
- raw reply text;
- raw OCR text;
- raw URLs;
- raw handles or contact IDs;
- screenshots;
- browser/session artifacts;
- credentials or tokens;
- raw API responses;
- exact controlled-store locators.

## Review Metrics

| Metric | Value |
|---|---|
| surfaced candidate count |  |
| deduped candidate count |  |
| reviewer-visible candidate count |  |
| reviewed count |  |
| review-worthy yield |  |
| high-risk yield per reviewer hour |  |
| average review time |  |
| median review time |  |
| p95 review time |  |
| duplicate rate |  |
| hard-negative false-positive pressure |  |
| insufficient-evidence rate |  |
| thread/reply context dependency rate |  |
| raw-evidence leakage incidents |  |

## Stop Rules

Stop immediately if:

- authorization becomes unclear;
- API permissions do not cover the action;
- browser use would become broad personal-account crawling;
- raw evidence would need to enter git;
- rate or usage limits are unclear;
- caps are reached;
- duplicate load becomes excessive;
- hard-negative false-positive pressure rises;
- reviewer p95 time becomes unacceptable;
- the evidence needed for review is outside the approved fields.

## Decision

Choose one:

- `planning_only`
- `ready_for_capped_api_viability_run`
- `ready_for_capped_controlled_browser_run`
- `revise_source_arm`
- `reject_source_arm`

Decision:

```text

```

Rationale:

```text

```
