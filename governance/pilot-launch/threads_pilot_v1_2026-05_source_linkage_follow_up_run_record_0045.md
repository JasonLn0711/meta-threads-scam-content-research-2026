# Source-Linkage Follow-Up Run Record 0045

This is the repo-safe run record for a narrow source-linkage/full-thread follow-up after the run `0043` promotion first pass.

Do not add raw Threads content, full URLs, handles, screenshots, HTML, browser/session artifacts, raw comments, exact controlled-store paths, contact IDs, stock names, stock codes, price values, or sensitive investigative notes to this file.

## Run Identity

| Field | Value |
|---|---|
| Run ID | `SOURCE-LINKAGE-FOLLOW-UP-THREADS-PILOT-V1-0045` |
| Date opened | `2026-04-26` |
| Decision | `decision-log/0090-authorize-run-0045-source-linkage-follow-up.md` |
| Source candidates | run `0043` promotion packet |
| Related review | `threads_pilot_v1_2026-05_run_0043_promotion_review_record.md` |
| Source path | approved browser session plus controlled-store packet |
| Purpose | test item-level source linkage for a small subset before any `manual_entry_0076` build |
| Raw output location | controlled store only |
| Repo-visible raw output | no |
| Manual entry creation | no |
| Official checkpoint promotion | no |
| Run status | `completed_no_item_created` |

## Scope And Caps

| Counter | Limit | Current |
|---|---:|---:|
| Candidate attempts | 5 | 5 |
| Source-linkage-ready candidates | 5 | 2 |
| Candidates eligible for second review | 5 | 2 |
| Candidates promoted to `manual_entry_0076` | 0 | 0 |

## Execution Result

Run `0045` completed as a controlled-store-only source-linkage follow-up.

Aggregate result:

- candidate matches available from the controlled packet: 15;
- candidates attempted: 5;
- exact live matches after re-query/re-open: 2;
- source-linkage-ready candidates: 2;
- second-review-eligible candidates: 2;
- reply-context status for ready candidates: `body_text_only_unstructured`;
- manual entries created: 0;
- official checkpoint items promoted: 0.

The follow-up improved the evidence state for a small subset of run `0043` candidates. Two candidates are now tied to item-level context strongly enough for second-review consideration.

However, this run still does not create `manual_entry_0076`. The ready candidates need fast different-angle second review, redacted field construction, one-item validation, aggregate validation, and explicit final promotion decision before any official item is created.

## Required Workflow

1. Load the controlled run `0043` promotion packet.
2. Select up to 5 candidates with strongest surface-signal and existing controlled context hints.
3. Match candidate text against controlled post-href context.
4. Re-open matched post-href contexts through approved browser session.
5. Record item-level source linkage and reply-context status in controlled store.
6. Write only repo-safe aggregate results here.

## Stop Conditions

Stop if:

- 5 candidates have been attempted;
- no candidate can be tied to a specific post-href context;
- browser-session access fails;
- the run starts requiring private messages, profile graph capture, landing pages, redirect chains, model training, production detection, or legal determinations;
- raw evidence is about to enter git.

## Current Decision

Run `0045` is complete as a source-linkage follow-up only.

It must not create `manual_entry_0076`, manual records, or official checkpoint items.
