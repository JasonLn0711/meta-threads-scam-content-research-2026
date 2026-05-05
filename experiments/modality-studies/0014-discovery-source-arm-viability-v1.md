# 0014 - Discovery Source-Arm Viability v1

Date opened: 2026-05-05

Status: design and readiness plan

## Purpose

Move the repo back to the core project goal:

```text
continuously discovering new review-worthy Threads investment-scam candidates
```

This experiment plan replaces the habit of opening more reviewer-only batches.
It defines how to test source arms that may surface new candidates, while still
measuring reviewer burden, hard-negative pressure, and governance risk.

## Hypothesis

If Discovery Method v1 compares authorized source arms instead of reusing old
review batches, the project can learn which access path produces new
review-worthy candidates per reviewer hour.

## Source Arms Under Test

| Source arm | First test | Execution status |
|---|---|---|
| `official_threads_api_keyword_search` | Check whether the project has official keyword/media retrieval access and required permissions. | planning only until API access is verified |
| `official_threads_api_reply_context` | Check whether official API can complete thread/reply context for surfaced candidates. | planning only until API access is verified |
| `controlled_browser_run_scoped` | Reuse historical controlled browser-run procedure as fallback if API is unavailable or insufficient. | planning only until a new run-scoped decision is recorded |
| `stakeholder_or_reviewer_pointer` | Use controlled pointers as high-value seeds or verification targets. | allowed only under existing pointer/source controls |
| `hard_negative_comparator` | Keep ordinary investment and anti-scam warning controls in the mix. | allowed with minimal metadata |

## Non-Goals

This plan does not authorize:

- broad logged-in browser crawling;
- personal-account automation as standing permission;
- one-second-per-item or one-second-per-group fetching as a default;
- scraping to evade official API limits;
- raw Threads content in git;
- raw URLs, handles, screenshots, browser artifacts, credentials, tokens, or
  raw API responses in git;
- final automated scam labels;
- legal fraud determinations;
- enforcement or public warning workflows.

## Readiness Sequence

1. Complete a `discovery_source_arm_work_order.md` for each proposed source arm.
2. For official API arms, verify app access, permissions, endpoint coverage,
   allowed fields, token handling, and rate or usage limits.
3. For controlled browser fallback, create a new decision record before any
   run; use the historical controlled crawler plan only as a procedural
   reference.
4. Produce metadata-only discovery candidate records using
   `data-contracts/discovery_candidate_v1.schema.yaml`.
5. Review candidates with human labels and reviewer-time fields.
6. Compare source arms by review-worthy yield and reviewer burden.

## First Capped Execution Shape

The first executable run, after authorization, should be tiny:

| Limit | Default |
|---|---:|
| source arms | 1 primary plus 1 hard-negative/control arm |
| query strategies | 5 maximum |
| surfaced candidates | 20 maximum |
| reviewer-visible candidates | 10 maximum |
| human-reviewed candidates | 10 maximum |
| workers | 1 |
| browser fallback delay | conservative and run-recorded; never one-second default |
| raw evidence in git | 0 incidents allowed |

## Metrics

Required:

- surfaced candidate count;
- deduped candidate count;
- reviewer-visible candidate count;
- review-worthy yield;
- final label counts;
- average, median, and p95 review time;
- candidates reviewed per hour;
- high-risk yield per reviewer hour;
- duplicate rate;
- thread/reply context dependency rate;
- hard-negative false-positive pressure;
- insufficient-evidence rate;
- raw-evidence leakage incidents.

## Decision Implication

Possible outcomes:

- `use_official_api_source_arm`;
- `use_controlled_browser_fallback_with_limits`;
- `revise_query_strategy`;
- `revise_evidence_fields`;
- `pause_for_authorization`;
- `reject_source_arm`.

No outcome from this plan can authorize production monitoring, broad crawling,
private-message access, model training, legal fraud claims, or enforcement.
