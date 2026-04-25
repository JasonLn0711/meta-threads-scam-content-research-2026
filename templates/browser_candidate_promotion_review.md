# Browser Candidate Promotion Review

Use this template before any browser-session candidate is promoted into an official selected item after run `0039`.

Keep this file free of raw Threads content, full source URLs, raw handles, screenshots, HTML, cookies, browser storage state, API responses, raw comments, contact IDs, stock names, stock codes, price values, case IDs, raw storage paths, and sensitive investigative notes. Raw/session/candidate artifacts remain in the approved controlled store.

## Review Identity

| Field | Value |
|---|---|
| Promotion review ID |  |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Candidate source run |  |
| Candidate local reference |  |
| Review date |  |
| Review owner |  |
| Second reviewer |  |
| Intended item ID if promoted |  |
| Confirmed pointer available? | yes / no |
| Source path | confirmed_pointer / browser_session / api_session_aware |
| Raw evidence controlled-store reference recorded? | yes / no |

## Gate Summary

| Gate | Result | Notes |
|---|---|---|
| Authorization gate | pass / fail | Approved run record exists with candidate and selected-item caps. |
| Access gate | pass / fail | Approved browser/session-aware or API/session-aware readiness passed. |
| Dedupe gate | pass / fail | Candidate is not an exact or near duplicate of existing items/candidates. |
| Source-context gate | pass / fail | Visible claim can be interpreted without relying on query terms. |
| Reply-context gate | pass / fail | Replies/comments captured, unavailable, or not needed due to confirmed-pointer context. |
| Evidence attribution gate | pass / fail | Page-level links/search context are not treated as item-level evidence unless tied to the item. |
| Redaction gate | pass / fail | Repo-safe fields only; raw evidence remains in controlled store. |
| Strict-validation gate | pass / fail / pending | One-item and aggregate validation have 0 errors and 0 warnings. |
| Second-review gate | pass / fail / pending | Different-angle review accepts final label/risk/evidence family. |

Promotion rule:

```text
promote only if every required gate is pass
```

## Dedupe Review

| Dedupe check | Result | Notes |
|---|---|---|
| Exact post-text duplicate checked | pass / fail |  |
| Minimized-text duplicate checked | pass / fail |  |
| Candidate bucket/hash checked | pass / fail |  |
| Dedupe key checked | pass / fail |  |
| Previous browser-session tranche checked | pass / fail |  |
| Existing official checkpoint records checked | pass / fail |  |
| New reply/source context changes duplicate assessment | yes / no / n/a |  |

Dedupe decision:

```text
not_duplicate / near_duplicate_promotable_with_new_context / duplicate_exclude
```

## Evidence Context Review

| Question | Answer | Notes |
|---|---|---|
| Does the candidate have item-level source context? | yes / no |  |
| Does the candidate have reply/comment context? | yes / no / unavailable / not_needed |  |
| Are visible links tied to the item rather than only the page? | yes / no / none_visible |  |
| Are contact/action gates tied to the item? | yes / no / none_visible |  |
| Are query terms excluded from label evidence? | yes / no |  |
| Is anti-scam or warning language protective rather than conversion-oriented? | yes / no / not_observed |  |
| Is the evidence sufficient for a final `scam` or `non_scam` label? | yes / no |  |

## Proposed Label

| Field | Value |
|---|---|
| Preliminary label | scam / non_scam / uncertain / insufficient_evidence |
| Preliminary risk | high / medium / low |
| Evidence sufficiency | sufficient / partial / insufficient / not_reviewable |
| Confidence | high / medium / low |
| Candidate role | official_item / local_trace_only / duplicate_exclude / needs_more_context |

## Second Review Challenge

The second reviewer must explicitly challenge:

- whether the candidate should be downgraded to `uncertain` or `insufficient_evidence`;
- whether reply/comment context changes interpretation;
- whether page-level evidence was incorrectly attributed to the item;
- whether query terms leaked into the label;
- whether an exact or near duplicate should be excluded;
- whether the proposed signal family is reusable or overgeneralized.

Second-review result:

```text
accept_promotion / accept_with_label_change / keep_local_trace_only / duplicate_exclude / reject
```

## Final Decision

Choose one:

- `promote_to_official_selected_item`
- `keep_as_local_candidate_trace`
- `exclude_duplicate_or_near_duplicate`
- `pause_for_full_thread_capture`
- `reject_candidate`

Decision:

```text

```

Rationale:

- 

## Required Follow-Up

| Follow-up | Owner | Required before promotion? |
|---|---|---|
|  |  | yes / no |

## Recording Boundary

- Commit only aggregate, sanitized, repo-safe conclusions.
- Keep full candidate evidence, raw outputs, screenshots, URLs, handles, browser/session artifacts, and exact storage paths in the approved controlled store.
- If the candidate is promoted, update the run record, evaluation note, decision log if a new rule family is accepted, run index, and checkpoint synthesis only after strict validation and second review pass.
