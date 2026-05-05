# 0155 - Open Authorized Discovery Method v1 And Access Boundary

Date: 2026-05-05

## Decision

Stop opening reviewer-only batches by default and open Discovery Method v1 as
the next project path.

The project should now test authorized source arms for repeatedly discovering
new review-worthy Threads investment-scam candidates. Reviewer Assist remains a
support layer for reducing reviewer burden after candidates are surfaced.

## Access Boundary

Use official Threads API access first if available and authorized.

The official Threads API reference lists endpoints including media retrieval by
ID or keyword, reply management, user/profile access, insights, publishing, and
oEmbed. Any API use still requires documented app access, permissions, token
handling, field limits, platform usage rules, and run records.

Controlled browser runs may be reused only as a run-scoped fallback method.
They are not standing permission for broad browser crawling, personal-account
automation, or one-second-per-item collection.

## Explicit Rejection

This decision rejects changing the repo governance red lines to allow:

- broad personal Threads account browser crawling;
- default one-second-per-item or one-second-per-group automated fetching;
- using rate limiting as a substitute for platform/legal/stakeholder approval;
- committing raw Threads content, replies, OCR, URLs, handles, screenshots,
  browser/session artifacts, raw API responses, or controlled-store locators to
  git.

## New Artifacts

- `docs/73-authorized-threads-discovery-method-v1.md`
- `data-contracts/discovery_candidate_v1.schema.yaml`
- `templates/discovery_source_arm_work_order.md`
- `experiments/modality-studies/0014-discovery-source-arm-viability-v1.md`

## Consequences

The next action is source-arm readiness, not Batch `0014`.

The first concrete check is:

```text
Can the project use official Threads API keyword/media/reply retrieval under
documented permissions and field limits?
```

If not, the fallback check is:

```text
Can a new controlled browser run be authorized as a tiny, run-scoped,
repo-safe source-arm viability test?
```

Neither path authorizes live collection from this decision alone. A source-arm
work order and any required run-scoped authorization must be completed first.
