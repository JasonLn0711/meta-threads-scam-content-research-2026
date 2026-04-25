# Aggressive Dedupe-First Browser Candidate Quality Run Record 0044

This is the repo-safe run record for an aggressive browser-session candidate-quality test after run `0043`.

Do not add raw Threads content, full URLs, handles, screenshots, HTML, browser/session artifacts, raw comments, exact controlled-store paths, contact IDs, stock names, stock codes, price values, or sensitive investigative notes to this file.

## Run Identity

| Field | Value |
|---|---|
| Run ID | `AGGRESSIVE-DEDUPE-FIRST-BROWSER-CANDIDATE-QUALITY-THREADS-PILOT-V1-0044` |
| Date opened | `2026-04-26` |
| Decision | `decision-log/0087-authorize-aggressive-dedupe-first-browser-candidate-quality-run-0044.md` |
| Related prior run | `0043` |
| Related checkpoint | `threads_pilot_v1_0055` |
| Source path | approved browser session |
| Purpose | aggressive candidate-quality test and negative/calibration case discovery |
| Raw output location | controlled store only |
| Repo-visible raw output | no |
| Manual entry creation | no |
| Official checkpoint promotion | no |
| Run status | `completed_no_item_created` |

## Scope And Caps

| Check | Value |
|---|---:|
| Search seed cap | 48 |
| Candidate review cap | 200 |
| Candidate review target | 180-200 |
| Per-family candidate cap | 32 |
| Local selected candidate cap | 180 |
| Local selected candidate target | 150-180 |
| Post-href/full-thread context attempt cap | 180 |
| Official selected item cap | 0 |

## Required Gates

| Gate | Requirement |
|---|---|
| Query-diversification gate | vary risk domain, visible signal family, and wording style |
| Dedupe gate | exclude exact or near duplicates before local selection |
| Full-thread/reply-ready gate | attempt item/reply context through post-like hrefs or record unavailable |
| Evidence attribution gate | do not treat page-level context as item-level evidence unless tied to item |
| Redaction gate | raw output stays controlled-store only |
| Negative-case retention | non-scam, uncertain, and insufficient-evidence candidates can be retained as controlled local traces |

## Query Matrix Rule

Run `0044` must not simply repeat run `0043`.

It may reuse a small number of high-yield families, but must expand the matrix across:

- investment/profit;
- stock help or stock-pick;
- crypto/wallet/deposit;
- easy income or recruitment;
- giveaway/reward;
- recovery/support;
- impersonation/authority;
- anti-scam camouflage;
- comment/DM gate;
- ordinary comparator and warning styles for negative calibration.

Query terms are candidate-finding tools only. They must not become labels.

## Candidate Ledger

| Counter | Limit | Current |
|---|---:|---:|
| Search seeds checked | 48 | 0 |
| Candidates reviewed | 200 | 200 |
| Dedupe-pass candidates | 200 | 190 |
| Local selected candidates | 180 | 180 |
| Post-href/full-thread context attempts | 180 | 131 |
| Official checkpoint items promoted | 0 | 0 |

## Execution Result

Run `0044` completed as a controlled-store-only candidate-quality test.

Aggregate result:

- stop condition: `candidate_cap_reached`;
- seeds checked: 26 of 48;
- candidates reviewed: 200;
- dedupe-pass candidates: 190;
- exact duplicates: 10;
- local selected candidates: 180;
- post-href/full-thread context attempts: 131;
- context-ready attempts: 131;
- candidate body-line count observed: 617;
- post-like href count observed: 147;
- manual entries created: 0;
- official checkpoint items promoted: 0.

The run reached the candidate review cap before all seeds were needed. Context attempts stopped below the 180 cap because the rendered search pages exposed 131 unique post-like context targets under the run method.

Negative, non-scam, uncertain, and insufficient-evidence candidates remain valid controlled local traces for calibration. No final labels are created by this run.

Repo-safe signal-family counts:

- investment or authority domain: 35;
- warning, recovery, or support domain: 32;
- private-channel migration: 21;
- comment or reward gate: 15;
- wallet, deposit, or verification: 11;
- crypto domain: 9;
- guaranteed or easy outcome: 6;
- testimonial or proof: 3;
- urgency or scarcity: 1.

## Stop Conditions

Stop if:

- 200 candidates have been reviewed;
- 180 local candidates have been selected;
- 180 context attempts have been made;
- one query family dominates beyond the per-family cap;
- raw output is about to enter git;
- browser-session access fails;
- the run starts requiring private messages, broad profile graph, landing pages, redirect chains, model training, production detection, or legal determinations.

## Current Decision

Run `0044` is complete as a candidate-quality test only.

It must not create manual entries, manual records, or official checkpoint items.
