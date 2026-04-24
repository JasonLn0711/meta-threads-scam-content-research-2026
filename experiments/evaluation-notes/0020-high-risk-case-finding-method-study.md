# High-Risk Case-Finding Method Study

## Purpose

Define the next repo-safe research step after the first 15 controlled items produced no high-risk examples.

This note does not authorize new collection by itself. It defines a method-study design that must be paired with a new run record before item 16.

## Current Evidence

| Observation | Interpretation |
|---|---|
| 15 local records built and strict-validated | The redaction/build/validation pipeline works. |
| 0 `scam` labels and 0 medium/high-risk records | Current topic-only search seeds are low-yield for high-risk discovery. |
| 14 `non_scam`, 1 final `uncertain` | The current path is better at collecting comparators and boundary cases. |
| 1 visible private-message boundary item | A signal-family probe can surface useful ambiguity, but not necessarily high risk. |
| No screenshots, OCR, replies, external links, redirects, landing pages, or profile context | Many high-risk signals may be outside the currently allowed text-only visible search-result field. |

## Research Question

Can a controlled, low-speed risk-probe seed strategy find higher-risk Threads examples without expanding into bulk scraping, profile review, landing-page capture, raw identifier retention, or legal conclusions?

## Hypothesis

Topic-only seeds such as investment, money-making, stocks, virtual currency, and cryptocurrency mostly retrieve ordinary discussion. Higher-risk yield should improve when seeds combine a risk domain with one visible scam-like signal family.

## Candidate Signal Families

Use these as candidate-generation probes, not as labels:

| Signal family | Examples of probe terms | Why it may help |
|---|---|---|
| guaranteed outcome | guaranteed profit, no loss, stable return, double return | Tests high-risk promise language. |
| private-channel migration | LINE, Telegram, private group, DM, investment group | Tests funnel behavior. |
| trading authority or mentorship | teacher, analyst, signal, copy trading, trading mentor | Tests authority-led investment lure patterns. |
| payment or wallet action | deposit, wallet, transfer, fee, withdrawal, verification | Tests direct harm or account-risk cues. |
| urgency or scarcity | limited slots, today only, last chance, urgent | Tests pressure tactics. |
| proof or testimonial | earnings screenshot, profit proof, student result, success case | Tests persuasion via unverifiable proof. |
| reward or giveaway | free claim, airdrop, subsidy, prize, reward | Tests reward lures beyond investment. |

## Proposed Risk-Probe Design

Before item 16, open a new run record with an explicit risk-probe seed matrix.

Recommended first probe:

| Probe group | Max seeds | Max candidates per seed | Target selected items |
|---|---:|---:|---:|
| investment plus guarantee/private-channel terms | 2 | 5 | 1-2 |
| crypto plus wallet/deposit/airdrop terms | 2 | 5 | 1-2 |
| side-income/recruitment plus easy-income/private-channel terms | 1 | 5 | 1 |

Controls:

- One browser-rendered page/object at a time.
- 30-second minimum delay between fetches.
- Stop after 5 selected items or sooner if stop conditions trigger.
- Record candidate reviewed count and selected count.
- Do not store raw URLs, handles, screenshots, cookies, session artifacts, or raw page text in git.
- Do not open profiles, broad comments, landing pages, or redirect chains unless the new run record explicitly authorizes that field.
- Do not label an item `scam` because a probe term matched; label only observable retained evidence.

## Measurement

For the risk-probe run, report:

| Metric | Meaning |
|---|---|
| high-risk candidate yield | selected items with multiple strong visible signal families |
| medium/uncertain yield | selected items with one concrete suspicious signal but incomplete evidence |
| false-positive pressure | items that contain risk terms but are ordinary discussion |
| redaction burden | whether terms increase personal data, handles, links, or screenshots |
| stop-condition rate | whether higher-risk search requires unapproved evidence |
| second-review load | number of uncertain, low-confidence, or high-risk cases routed to review |

## Decision Logic

| Outcome | Next decision |
|---|---|
| Risk-probe finds 2-3 reviewable medium/high-risk items without new fields | Continue with limits toward item 20 or 25, still checkpointed. |
| Risk-probe mostly finds ordinary discussion | Revise seed strategy; do not scale to 50. |
| Risk-probe requires screenshots/OCR/replies/links to be meaningful | Pause and update the run record/authorization scope before collecting those fields. |
| Risk-probe creates privacy-heavy or raw-identifier pressure | Narrow or stop the source path. |
| Risk-probe produces repeated label ambiguity | Add guideline examples before further collection. |

## Initial Experiment Result

Runs 0005 and 0006 tested the seed-matrix idea through the public unauthenticated browser-rendered search path. Both runs returned no extractable real item content. Run 0005 exposed query echoes and interface text; run 0006 excluded exact query echoes and still exposed only generic onboarding/user-interface text.

This means the method should move to an approved browser-rendered session/access or API/session-aware access-path review before item 16. It does not justify treating query terms as item evidence.

## Why This Is A Method Study

Finding high-risk cases is not just "search harder." It is a sampling and evidence-design problem:

- high-risk lures may hide in images, replies, private-channel funnels, or links rather than top-level text;
- topic terms create many false positives from legitimate finance and crypto discussion;
- risk terms can bias annotators if they are treated as labels instead of candidate-generation hints;
- privacy burden rises when candidates include contact routes, personal hardship, screenshots, or payment details.

The next step should therefore test a small, auditable risk-probe method before adding more items to the pilot.
