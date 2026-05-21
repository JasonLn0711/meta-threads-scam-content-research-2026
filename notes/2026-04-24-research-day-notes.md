# 2026-04-24 Research Day Notes

## Day Thesis

Today moved the project from "ready to try controlled evidence" into actual checkpoint evidence about what the current acquisition path can and cannot do.

The important lesson is not that the project should collect more aggressively. The important lesson is that governed collection can work mechanically while still failing to produce the right risk composition. That means the next bottleneck is source/access design, not annotation tooling.

## What Changed Today

- Controlled browser-rendered rehearsal produced the first strict-valid local record.
- The project entered the first 10-item checkpoint and completed it at the lower bound.
- The first checkpoint decision was `continue_with_limits`, not broad readiness for 50 items.
- The item 11-15 limited extension completed under run 0004.
- The 15-record local aggregate strict-validated with zero errors and zero warnings.
- The only prior `uncertain` checkpoint item was second-reviewed and adjudicated to final `non_scam` / `low`.
- A new private-message boundary item was second-reviewed and stayed final `uncertain` / `low`.
- Risk-probe method work started because topic-only seeds were overproducing low-risk comparators.
- Public unauthenticated risk-probe runs 0005 and 0006 produced no extractable item content.
- Access-path review run 0007 found controlled-store governance and credential material, but no loadable browser storage-state/session artifact and no ready API/session-aware client path.

## Current Evidence State

The local ignored dataset now has 15 controlled records:

| Label or risk dimension | Count |
|---|---:|
| `non_scam` | 14 |
| `uncertain` | 1 |
| `scam` | 0 |
| `insufficient_evidence` | 0 |
| low risk | 15 |
| medium/high risk | 0 |
| text-only | 14 |
| private-message boundary | 1 |

Validation snapshot:

- 15-record JSONL strict validation: pass.
- 15-record CSV strict validation: pass.
- Validation errors: 0.
- Validation warnings: 0.
- Preflight: `ERROR: 0`.

## Key Decisions And Records

New or updated repo-safe records from today:

- `governance/pilot-launch/threads_pilot_v1_2026-05_limited_extension_run_record_0004.md`
- `governance/pilot-launch/threads_pilot_v1_2026-05_risk_probe_run_record_0005.md`
- `governance/pilot-launch/threads_pilot_v1_2026-05_risk_probe_run_record_0006.md`
- `governance/pilot-launch/threads_pilot_v1_2026-05_access_path_review_run_record_0007.md`
- `experiments/evaluation-notes/0019-first-15-item-limited-extension-result.md`
- `experiments/evaluation-notes/0020-high-risk-case-finding-method-study.md`
- `experiments/evaluation-notes/0021-risk-probe-run-0005-result.md`
- `experiments/evaluation-notes/0022-risk-probe-run-0006-result.md`
- `experiments/evaluation-notes/0023-access-path-review-run-0007-result.md`
- `decision-log/0023-require-risk-probe-method-before-item-16.md`
- `decision-log/0024-require-approved-session-or-api-risk-probe-access.md`

## Practical Lesson

The current public browser-rendered search path can support some text-only comparator and boundary collection, but it is not enough for high-risk case discovery.

Risk-probe query terms are useful as candidate-generation probes, but they cannot be treated as evidence. Runs 0005 and 0006 showed why this matters: the search page can surface the query itself or generic interface text. Turning that into an item would contaminate the dataset.

## Current Blocker

Item 0016 remains uncreated.

The blocker is now executable access path:

- controlled-store credential/governance material exists outside git;
- browser/session manifest exists outside git;
- no loadable browser storage-state/session artifact was found;
- no ready API/session-aware client path exists in the repo;
- therefore run 0007 did not attempt collection.

## Next Research Move

Before item 16, prepare one approved access path:

1. A loadable browser storage-state/session artifact in controlled storage, or
2. An approved API/session-aware client path that can execute without logging raw tokens, cookies, browser profiles, source URLs, handles, or raw responses into git.

Then open the next execution run record and reuse the risk-probe seed matrix only as candidate generation.

## What Not To Do Next

Do not:

- create item 0016 from query echoes, UI text, access-review metadata, or placeholders;
- continue toward 50 items under the same low-risk topic-only seed method;
- copy credentials, cookies, tokens, browser profiles, HAR files, source URLs, raw handles, screenshots, or raw API responses into git;
- treat search terms as labels;
- make legal fraud conclusions.

## Human-Control Rationale

The strict human control is not bureaucracy for its own sake. It protects the project from three failure modes:

- privacy failure: raw identifiers, session material, or sensitive investigative material leaks into git;
- evidence failure: query terms or UI text get mistaken for real item content;
- research failure: a low-risk, source-skewed sample gets misread as evidence about high-risk scam prevalence.

The controls keep the project small, auditable, reversible, and credible.
