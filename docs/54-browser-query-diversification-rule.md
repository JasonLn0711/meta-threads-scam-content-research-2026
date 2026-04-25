# Browser Query Diversification Rule

## Purpose

Use this rule before any future approved browser-session or API/session-aware candidate-discovery run that relies on search queries or seed terms.

Run `0043` showed that repeating similar topic-heavy terms creates avoidable bias and review load. A more diverse matrix reached the 60-candidate cap after 10 seeds while preserving the boundary that query terms are retrieval hints only, not labels.

This is an acquisition rule, not a scam-label rule.

## Core Rule

Every browser candidate-discovery run must define a query matrix before execution.

The matrix must vary at least three dimensions:

| Dimension | Required variation |
|---|---|
| Risk domain | Include at least four distinct domains when the run cap is 20 candidates or more. |
| Visible signal family | Include at least four distinct signal families when the run cap is 20 candidates or more. |
| Wording style | Include at least three search styles, such as direct lure, warning/camouflage, complaint/question, casual invitation, or coded action. |

Do not run a new browser candidate tranche using only topic labels such as investment, money, stock, or crypto.

## Allowed Query Families

Use a balanced matrix across examples like:

| Family | Candidate-finding intent |
|---|---|
| Investment/profit | Find finance lure candidates without treating finance discussion as scam. |
| Stock rescue or stock-pick | Find trapped-position, stock-help, or stock-playbook funnels. |
| Crypto/wallet/deposit | Find wallet, verification, airdrop, USDT, or exchange-like cues. |
| Easy income/recruitment | Find side-hustle, task-work, or passive-income lures. |
| Giveaway/reward | Find prize, shipping-fee, claim, or reward-verification lures. |
| Recovery/support | Find fake recovery, account-help, or suspicious support migration. |
| Impersonation/authority | Find teacher, expert, celebrity, institution, or support framing. |
| Anti-scam camouflage | Find items that say they oppose scams while also offering a replacement investment path. |
| Comment/DM gate | Find candidates that move details into replies, comments, codes, DMs, or groups. |

## Prohibited Query Practices

Do not:

- reuse the same query set unless a decision record explains why repetition is necessary;
- let one risk domain consume the full candidate cap;
- use exact personal handles, raw post URLs, case IDs, credentials, or private identifiers as tracked query text;
- use exact stock names, stock codes, price values, or sensitive investigative details in tracked query text;
- treat query terms as evidence, labels, rule matches, or final scam determinations;
- continue broad crawling after the candidate cap or stop condition is reached.

## Minimum Matrix Contract

Each future browser run record must include:

| Field | Required content |
|---|---|
| Query purpose | candidate discovery / calibration / false-positive pressure / other |
| Query dimensions | risk domains, signal families, wording styles |
| Seed cap | maximum number of seeds |
| Candidate cap | maximum reviewed candidates |
| Per-family cap | maximum candidates or seeds from one family |
| Reuse check | whether prior run seeds are repeated and why |
| Query-as-label guardrail | explicit statement that search terms are not evidence |
| Stop condition | when to stop if cap is hit before all seeds are tested |

## Suggested Caps

| Run size | Seed guidance | Candidate guidance |
|---|---|---|
| Diagnostic | 4-8 seeds across at least 3 families | 10-20 candidates |
| Candidate quality test | 12-24 seeds across at least 6 families | 40-60 candidates |
| Promotion-oriented run | Smaller seed set, stricter full-thread readiness | selected-item cap must be explicit |

If the candidate cap is reached before all seeds run, stop. Do not continue just to exhaust the seed list.

## Review Rule

After execution, report only repo-safe aggregate results:

- seeds checked;
- family coverage;
- candidates reviewed;
- dedupe-pass count;
- quality-review count;
- context-ready count;
- duplicate pressure;
- whether one family dominated the result;
- whether a later promotion review is justified.

Raw Threads text, URLs, handles, screenshots, HTML, exact storage paths, credentials, cookies, session artifacts, contact IDs, stock names, stock codes, price values, or sensitive investigative details must remain outside tracked files.

## Relationship To Labeling

This rule improves candidate discovery only.

The final label still requires item-level evidence, reply/comment context when relevant, dedupe review, second review, strict validation, and the promotion gate in [53-dedupe-first-full-thread-ready-gate.md](53-dedupe-first-full-thread-ready-gate.md).

Query terms cannot create or increase a label by themselves.
