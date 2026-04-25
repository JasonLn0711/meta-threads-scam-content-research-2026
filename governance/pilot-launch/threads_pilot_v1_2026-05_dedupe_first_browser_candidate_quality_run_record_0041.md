# Dedupe-First Browser Candidate Quality Run Record 0041

This is the non-sensitive tracked run record for an aggressive but bounded dedupe-first browser candidate quality test after run `0039`.

Do not add raw Threads content, screenshots, full item URLs, raw handles, stakeholder case IDs, credentials, cookies, tokens, browser profiles, HAR files, full HTML, exact raw storage paths, access-list details, contact handles, stock names, stock codes, price values, or sensitive investigative notes to this file. Exact sensitive values remain in the approved controlled store.

## Run Identity

| Field | Value |
|---|---|
| Run ID | `DEDUPE-FIRST-THREADS-PILOT-V1-0041-BROWSER-CANDIDATE-QUALITY` |
| Date opened | `2026-04-26` |
| Related checkpoint | `threads_pilot_v1_0055` |
| Related prior run | `0039` |
| Related gate | `docs/53-dedupe-first-full-thread-ready-gate.md` |
| Related review template | `templates/browser_candidate_promotion_review.md` |
| Operator | `AUTO-OP-01` |
| Purpose | aggressive candidate quality test using approved browser session, dedupe-first filtering, and full-thread/reply-ready promotion gates |
| Source path | approved browser session |
| Raw output location | controlled store only |
| Repo-visible raw output | no |
| Official checkpoint promotion | no, unless a later decision explicitly promotes validated items |
| Run status | `completed_closed_no_candidates` |

## Authorization And Scope

| Check | Result |
|---|---|
| Approved browser-session source path | yes |
| Candidate review cap | 60 candidates maximum |
| Candidate review target | 50-60 candidates |
| Selected quality-review candidate cap | 30 candidates maximum |
| Selected quality-review target | 20-30 candidates |
| Official selected item cap | 0 for this run |
| Dedupe-first gate required | yes |
| Full-thread/reply-ready gate required | yes |
| Evidence attribution gate required | yes |
| Fast different-angle second review required | yes |
| Strict validation required before any local record counts | yes |
| Broad crawler expansion | no |
| Private-message access | no |
| Profile graph capture | no |
| Landing-page or redirect-chain capture | no |
| Embedding/model training | no |
| Production detection | no |
| Raw output in git | no |

## Candidate And Selection Ledger

| Counter | Limit | Current |
|---|---:|---:|
| Candidates reviewed | 60 | 0 |
| Candidates passing dedupe screen | 60 | 0 |
| Candidates selected for quality review | 30 | 0 |
| Candidates passing full-thread/reply-ready gate | 30 | 0 |
| Candidates second-reviewed | 30 | 0 |
| Official checkpoint items promoted | 0 | 0 |

## Execution Result

| Field | Value |
|---|---|
| Execution status | completed |
| Source path used | approved browser session |
| Search seeds attempted | 12 |
| Candidates extracted | 0 |
| Quality-review candidates selected | 0 |
| Full-thread attempts | 0 |
| Manual entries created | 0 |
| Official checkpoint items promoted | 0 |
| Result note | `experiments/evaluation-notes/0073-run-0041-result.md` |

## Required Candidate Workflow

Each candidate must move through these gates:

1. approved browser-session candidate discovery;
2. raw output preserved in the controlled store only;
3. exact and near-duplicate screen against existing official records and local candidate traces;
4. source-context check;
5. full-thread/reply-ready check;
6. evidence attribution check to prevent page-level evidence from being treated as item-level evidence;
7. redaction check before any repo-visible note;
8. repo-safe browser candidate promotion review template;
9. fast different-angle second review;
10. strict validation only if a local candidate record is built.

No candidate may become an official selected item in this run. A later decision is required before official checkpoint promotion.

## Aggressive Candidate Strategy

Use a risk-probe seed matrix that combines risk domain and visible-signal family, but do not use query terms as labels.

Prioritize candidates with item-level evidence of:

- private-channel migration or implicit DM funnel;
- comment/reply-driven action gate;
- visible contact/action gate;
- wallet/deposit/payment cue;
- urgency, guarantee, testimonial proof, or past-performance proof;
- anti-scam camouflage plus conversion-oriented investment/profit path;
- repeat-source pattern only if item-level evidence remains sufficient.

## Dedupe-First Rule

Stop or downgrade candidates when:

- exact post text duplicates an existing official record or previous browser candidate;
- minimized text is near-duplicate without new source/reply context;
- the same redacted action/contact pattern repeats without new evidence family value;
- source/reply context is too thin to distinguish from run `0038` or run `0039` candidates.

## Full-Thread/Reply-Ready Rule

A candidate is quality-review eligible only if:

- the controlled capture can open the candidate's item-level context; and
- relevant replies/comments are captured, explicitly unavailable, or not needed because item-level evidence is sufficient; and
- page-level links/search-page context are not attributed to the item unless tied to the item.

Search-rendered snippets alone are insufficient for promotion.

## Stop Conditions

Stop the run if:

- 60 candidates have been reviewed;
- 30 candidates have been selected for quality review;
- duplicate or near-duplicate pressure shows the run is repeating run `0038` or run `0039`;
- full-thread/reply-ready capture fails repeatedly;
- strict validation produces unresolved errors;
- redaction boundary fails;
- raw evidence is about to enter git;
- the approved browser-session path becomes unavailable;
- the run starts requiring private messages, profile graph capture, broad account history, landing pages, redirect chains, model training, production detection, or legal determinations;
- stakeholder scope changes.

## Current Decision

Run `0041` is completed and closed.

It is not an official checkpoint expansion and does not create item `0076` or any later official item.

Run-level preflight passed in `experiments/evaluation-notes/0072-run-0041-preflight.md`.

Execution result is recorded in `experiments/evaluation-notes/0073-run-0041-result.md`.

The article-based browser-search extractor produced no candidates. The next browser method must revise extraction rather than repeat this run with higher caps.
