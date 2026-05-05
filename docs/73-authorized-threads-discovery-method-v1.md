# Authorized Threads Discovery Method v1

Status: design and gated execution plan

Date opened: 2026-05-05

Reference links checked on `2026-05-05`:

- Meta Threads API reference: `https://developers.facebook.com/docs/threads/reference`
- Meta Terms of Service: `https://www.facebook.com/terms`
- Meta Automated Data Collection Terms: `https://www.facebook.com/legal/automated_data_collection_terms`

## First Principle

The next useful work is not another reviewer-only batch.

The core method problem is:

```text
How can this project repeatedly discover new review-worthy Threads
investment-scam candidates under a governed, auditable, low-burden workflow?
```

Reviewer Assist, context gates, schemas, summaries, and metrics are support
layers. They help only if the upstream discovery engine can keep surfacing
new review-worthy candidates beyond the known fragments.

## Current Access Answer

Official Threads API access may be usable if a Meta developer app, required
permissions, token handling, app review or tester access, usage requirements,
and platform limits are all documented.

The official Threads API reference currently lists endpoints for:

- publishing;
- media retrieval, including retrieval by ID or keyword;
- reply management;
- user/profile access;
- insights;
- oEmbed.

That means the preferred live-source path is not browser scraping by default.
The preferred path is:

```text
official Threads API access check
-> permission and field review
-> source-arm work order
-> capped query/media/reply retrieval
-> repo-safe metadata candidate records
-> human review
-> yield plus reviewer-burden metrics
```

If official API access is unavailable or insufficient for the research
question, a controlled browser run can be considered only as a fallback source
arm under a new run-scoped authorization record.

## Browser Run Boundary

A personal Threads login does not, by itself, authorize automated collection.
Rate limiting does not create authorization. "One second per group" or
"one second per item" is not an acceptable default governance control.

Controlled browser runs remain possible as a research method only when all of
these are true:

- the run is explicitly opened by a decision record;
- the run is tied to the approved research purpose;
- the operator, account/session boundary, source scope, query set, item cap,
  candidate-review cap, field allowlist, raw storage location, retention,
  redaction, and stop rules are recorded before execution;
- credentials, cookies, browser profiles, screenshots, raw text, raw URLs,
  raw handles, session artifacts, logs, and exact controlled-store locators
  stay outside git;
- repo-visible artifacts contain only redacted metadata, aggregate metrics, or
  approved derived fields;
- the run uses one worker, conservative pacing, and small caps unless a later
  authorization record explicitly narrows or revises those limits;
- no evasion, stealth, anti-rate-limit bypass, account graph capture,
  private-message access, production monitoring, or enforcement action is
  attempted.

The existing controlled crawler plan remains a historical and procedural
reference. It is not a standing permission for broad logged-in browser crawling.

## Source Arms

Discovery Method v1 compares source arms. It does not keep creating reviewer
batches from the same old records.

| Source arm | Default status | Purpose | Main boundary |
|---|---|---|---|
| `official_threads_api_keyword_search` | pending access check | Discover new public candidates through official API keyword or media retrieval where available. | Requires documented API access, permissions, field limits, token controls, and rate/usage rules. |
| `official_threads_api_reply_context` | pending access check | Add thread/reply context for already surfaced candidates. | Requires endpoint availability, field approval, and context minimization. |
| `controlled_browser_run_scoped` | fallback, pending run decision | Discover or complete candidates when official API does not expose required context. | Requires a new run-scoped decision; no broad personal-account crawler. |
| `stakeholder_or_reviewer_pointer` | allowed if authorized | High-value seed and validation source for known suspicious candidates. | Source IDs and raw pointers stay controlled and outside git. |
| `manual_public_seed` | allowed with limits | Small manually curated examples or comparators. | Manual only unless a run record changes the method. |
| `hard_negative_comparator` | allowed with limits | Protect ordinary investment discussion and anti-scam warnings from overflagging. | Must not dominate the source mix or become a fake discovery result. |
| `synthetic_query_probe` | allowed | Dry-run query strategy and schema flow without real evidence. | Cannot support real-world yield claims. |

## Discovery Loop

```text
source-arm authorization check
-> query and signal-family plan
-> capped source-arm execution
-> metadata-only candidate stub
-> dedupe and source-linkage check
-> context gate
-> Reviewer Assist summary/prefill where allowed
-> human review
-> source-arm yield and reviewer-hour metrics
-> next source-arm allocation decision
```

## Query Strategy

Query generation should use signal families as discovery hypotheses, not final
labels.

Minimum query dimensions:

| Dimension | Examples | Reason |
|---|---|---|
| investment domain | stocks, trading, options, crypto, passive income, investment class | Finds the broad domain but has high false-positive risk. |
| guarantee/profit cue | guaranteed return, fixed income, daily profit, doubled capital | Targets high-value source priority. |
| authority cue | teacher, analyst, assistant, expert, mentor, holdings help | Finds authority-framed funnels. |
| private-channel cue | DM, private group, LINE, Telegram, WhatsApp, assistant | Finds migration and conversion paths. |
| result-display cue | profit screenshot, win rate, earnings table, testimonial | Finds proof-based lures and hard-negative controls. |
| reply-funnel cue | comment code, reply plus one, send keyword, ask holdings | Finds candidates where replies carry the conversion path. |
| hard-negative cue | anti-scam warning, financial education, market commentary | Protects ordinary and warning content. |

Every query plan must include at least one hard-negative or calibration arm so
the method does not optimize only for suspicious-looking vocabulary.

## Repo-Safe Candidate Record

Discovery Method v1 writes only metadata to git-facing records.

Allowed repo-facing fields include:

- `discovery_candidate_id`;
- `discovery_round_id`;
- `source_arm_id`;
- `source_access_mode`;
- `query_strategy_id`;
- `query_signal_family_hints`;
- `surface_type_hints`;
- `context_needed`;
- `evidence_availability_flags`;
- `dedupe_key_ref`;
- `priority_score`;
- `priority_reason_codes`;
- `hard_negative_reason_codes`;
- `review_status`;
- `review_time_seconds`;
- aggregate source-arm metrics.

Forbidden repo-facing fields include:

- raw Threads post text;
- raw reply text;
- raw OCR text;
- screenshots or screenshot paths;
- raw URLs;
- raw handles, usernames, IDs, emails, phone numbers, or contact handles;
- browser profiles, cookies, tokens, HAR files, or session artifacts;
- exact controlled-store paths;
- raw API responses.

## Metrics

Each source-arm run must report:

| Metric | Required |
|---|---|
| surfaced candidate count | yes |
| deduped candidate count | yes |
| reviewer-visible candidate count | yes |
| review-worthy yield | yes |
| final `scam` / `non_scam` / `uncertain` / `insufficient_evidence` counts | yes |
| average review time | yes |
| median review time | yes |
| p95 review time | yes |
| candidates reviewed per hour | yes |
| high-risk yield per reviewer hour | yes |
| hard-negative false-positive pressure | yes |
| thread/reply context dependency rate | yes |
| OCR dependency rate | when applicable |
| duplicate rate | yes |
| raw-evidence leakage incidents | yes |
| source-arm continuation decision | yes |

## Stop Rules

Pause or stop the source arm when:

- authorization or platform access is unclear;
- official API permissions do not cover the intended action;
- a browser run would require personal-account broad crawling;
- raw evidence would need to enter git;
- the run hits the candidate cap, time cap, or stop condition;
- duplicate rate is too high to justify reviewer time;
- hard-negative false-positive pressure rises;
- p95 review time becomes operationally unacceptable;
- thread/reply context is required but not available under approved fields;
- reviewers cannot make stable decisions from the approved evidence.

## Immediate Next Action

Do not open Batch `0014`.

Open a source-arm readiness packet for Discovery Method v1:

1. Check whether official Threads API keyword/media/reply retrieval is actually
   available to the project account and permissions.
2. If API access is available, draft a capped API source-arm work order.
3. If API access is unavailable, draft a controlled browser source-arm work
   order using the historical controlled-run procedure as a reference.
4. In either case, keep the first execution tiny: source-arm readiness first,
   then a capped run, then human review and reviewer-hour metrics.

No live collection begins from this document alone.
