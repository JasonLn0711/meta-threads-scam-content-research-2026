# Run 0039 Aggressive Prospective Tranche Result

## Purpose

Record the repo-safe result of run `0039`, the aggressive but bounded prospective tranche for items `0056-0075`.

This note contains no raw Threads content, full item URLs, raw handles, screenshots, raw reply text, credentials, browser artifacts, storage-state material, raw storage paths, contact IDs, stock names, stock codes, brand names, price values, stakeholder case IDs, or sensitive investigative notes.

## Execution Scope

| Field | Value |
|---|---|
| Run ID | `AGGRESSIVE-THREADS-PILOT-V1-0056-0075-PROSPECTIVE-TRANCHE` |
| Run record | `governance/pilot-launch/threads_pilot_v1_2026-05_aggressive_prospective_tranche_run_record_0039.md` |
| Related decision | `decision-log/0070-authorize-aggressive-prospective-tranche-0056-0075.md` |
| Preflight note | `experiments/evaluation-notes/0069-run-0039-preflight.md` |
| Source path used | approved browser-session supplement |
| Reason supplemental path was used | no new confirmed pointer was available at execution time |
| Candidate cap | 50 |
| Selected candidate cap | 20 |
| Raw output | controlled store only |

## Result

| Check | Result |
|---|---:|
| Candidates reviewed | 50 |
| Local selected candidate entries created | 20 |
| Local manual records built | 20 |
| Local aggregate records checked | 75 |
| Strict validation errors | 0 |
| Strict validation warnings | 0 |
| Fast second-reviewed candidate entries | 20 |
| Adjudicated uncertain candidate entries | 11 |
| Excluded duplicate or near-duplicate candidate entries | 9 |
| New final scam/high-risk items added | 0 |

## Second Review Finding

The fast different-angle second review did not accept run `0039` as a high-yield evidence expansion.

The review found:

- the browser-session path remained operational and strict-valid;
- the aggressive query matrix quickly exhausted the 50-candidate review cap;
- 9 selected candidate entries were duplicate or near-duplicate evidence from the previous browser-session tranche;
- the remaining 11 candidate entries were context-thin and stayed `uncertain`;
- no candidate produced enough repo-safe post/reply/source context to become a new final scam/high-risk rule-family example;
- query terms and page-level link context remain candidate-finding signals only, not label evidence.

## Dataset State

A local ignored 75-record candidate aggregate was built for validation and audit:

```text
data/interim/manual_records_checkpoint_0075.jsonl
```

It is not promoted as a new official checkpoint package.

The current official reviewed checkpoint remains:

```text
threads_pilot_v1_0055
```

## Interpretation

First-principles read: this run tested whether increasing browser-session breadth would solve the high-risk evidence shortage.

It did not.

The limiting factor is not only volume. The limiting factor is evidence quality:

- browser search snippets are often too thin;
- reply context is usually missing;
- source context is usually missing;
- page-level link signals can be over-attributed to individual candidate snippets;
- broad or aggressive browser search can recycle the same candidates from a previous tranche.

## Decision Implication

Do not continue browser-session expansion by adding more seeds or higher caps.

The next high-value path is one of:

- return to CIB/stakeholder/project-owner confirmed pointers, captured one item at a time;
- add a dedupe-first browser candidate gate before any future browser-session tranche;
- require reply/full-thread capture readiness before browser candidates are allowed to become final scam/high-risk examples.
