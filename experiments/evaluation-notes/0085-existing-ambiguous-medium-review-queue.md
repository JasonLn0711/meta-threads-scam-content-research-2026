# Existing Ambiguous And Medium-Risk Review Queue

## Purpose

Summarize the second-review queue for existing checkpoint 0076 records with `uncertain`, `insufficient_evidence`, or `medium` risk status.

This note is repo-safe. It does not include raw Threads URLs, handles, screenshots, raw post text, raw reply text, contact IDs, stock names, stock codes, price values, credentials, browser/session artifacts, exact controlled-store paths, or stakeholder case IDs.

## Queue Summary

| Measure | Count |
|---|---:|
| Checkpoint 0076 total records | 76 |
| `uncertain` records | 29 |
| `insufficient_evidence` records | 6 |
| `medium` risk records | 13 |
| Deduplicated review queue | 35 |

Queue file:

```text
data/interim/review_queue_checkpoint_0076_uncertain_insufficient_medium.csv
```

## Priority Rationale

This review is valuable because:

- `uncertain` items may hide false negatives if evidence actually supports scam/high-risk;
- `insufficient_evidence` items may need explicit controlled-context follow-up or should remain excluded;
- `medium` risk items often sit near the threshold between low-risk comparator and high-risk scam-like record;
- second review can improve the existing dataset without opening new collection.

## Review Buckets

| Bucket | Review question |
|---|---|
| `uncertain` + `medium` | Can existing evidence support promotion to `scam` / `high`, downgrade to `non_scam` / `low`, or should it stay uncertain? |
| `uncertain` + `low` | Is uncertainty caused by weak evidence, benign context, or missing context? |
| `insufficient_evidence` | Is there enough existing evidence to review, or should missing context remain blocking? |
| `medium` risk without high-confidence label | Should risk be adjusted after second review? |

## Guardrails

This review queue does not authorize:

- item `0080` or later;
- new source discovery;
- browser/crawler expansion;
- account/profile graph capture;
- landing-page or redirect-chain capture;
- private-message access;
- embedding or model training;
- production detection;
- legal fraud determinations;
- raw evidence in git.

## Next Step

Review queued items one by one using existing redacted records. Record item-level adjudication before changing labels, rebuilding records, or updating aggregate metrics.

## Review Progress

| Item | Prior status | Updated recommendation | Basis |
|---|---|---|---|
| `threads_pilot_v1_0012` | `uncertain` / `low` | `scam` / `high` | CIB-confirmed escort or fake-dating scam starter pattern; support request plus private-message migration. |
| `threads_pilot_v1_0017` | `insufficient_evidence` / `low` | `scam` / `high` | CIB-confirmed crypto wallet plus LINE private-channel scam pattern. |
| `threads_pilot_v1_0020` | `uncertain` / `medium` | `scam` / `high` | CIB-confirmed earnings-sheet/testimonial plus external-link funnel precursor in an investment-teacher or investment-guidance context. |
| `threads_pilot_v1_0021` | `uncertain` / `medium` | `scam` / `high` | CIB-confirmed coordinated comment-account reinforcement / double-act funnel with profit/testimonial cues. |
| `threads_pilot_v1_0025` | `uncertain` / `medium` | `scam` / `high` | CIB-confirmed implausible third-party account/deposit custody delegation narrative with crypto/contact/link signals. |
| `threads_pilot_v1_0027` | `uncertain` / `medium` | keep `uncertain` / `medium` | Context too thin; could be anti-scam education or evasion instruction. Future captures should preserve fuller text and reply context. |
| `threads_pilot_v1_0047` | `uncertain` / `medium` | keep `uncertain` / `medium` | Short-term/swing-trading stock group language is high-risk, but retained context is too thin for scam labeling. |
| `threads_pilot_v1_0048` | `insufficient_evidence` / `low` | keep `insufficient_evidence` / `low` | Stock-holder audience opening is a high-risk starter candidate, but capture completeness is inadequate for adjudication. |
| `threads_pilot_v1_0049` | `insufficient_evidence` / `low` | `scam` / `high` | Public stock-tip / named-stock-pick behavior on Threads is high-risk scam behavior; not based on generic stock keywords alone. |
| `threads_pilot_v1_0050` | `uncertain` / `low` | `scam` / `high` | Named-stock reassurance plus external-site funnel context. |
| `threads_pilot_v1_0051` | `insufficient_evidence` / `low` | `scam` / `high` | Day-trading plus wealth-password lure language is fast-profit/secret-method scam-risk framing. |
| `threads_pilot_v1_0052` | `uncertain` / `medium` | `scam` / `high` | Day-trading plus LINE/private-group migration is a private-channel investment funnel. |
| `threads_pilot_v1_0053` | `insufficient_evidence` / `low` | keep `insufficient_evidence` / `low` | Fragment could be ordinary market-scope sharing; capture completeness is inadequate for adjudication. |
| `threads_pilot_v1_0054` | `insufficient_evidence` / `low` | keep `insufficient_evidence` / `low` | Fragment could be rule explanation or anti-scam warning; fuller funnel context is required before scam labeling. |
| `threads_pilot_v1_0055` | `uncertain` / `medium` | `scam` / `high` | Comment-plus-DM action gate with private-group/contact/link context. |
| `threads_pilot_v1_0056` | `uncertain` / `medium` | `scam` / `high` | Investment-content migration to IG/private messages with trust-softening disclaimers. |
| `threads_pilot_v1_0057` | excluded duplicate trace | keep excluded duplicate | Duplicate of item `0047`; high-risk candidate family but not a new promoted scam record. |
| `threads_pilot_v1_0058` | `uncertain` / `medium` | `scam` / `high` | Profit-plus-social-good stock framing with external-site context. |
| `threads_pilot_v1_0059` | excluded duplicate trace | keep excluded duplicate | Duplicate of item `0048`; stock-holder audience opening is high-risk starter candidate but not a new promoted scam record. |
| `threads_pilot_v1_0060` | excluded duplicate trace | keep excluded duplicate | Duplicate of item `0049`; public stock-tip / named-stock-pick behavior is high-risk scam behavior but not a new promoted scam record. |
| `threads_pilot_v1_0061` | excluded duplicate trace | keep excluded duplicate | Duplicate of item `0050`; named-stock reassurance plus funnel context is scam behavior but not a new promoted scam record. |
| `threads_pilot_v1_0062` | `uncertain` / `low` | `scam` / `high` | Short-time large-wealth investment story plus external-site context; experience-sharing camouflage can become funnel conversion. |
| `threads_pilot_v1_0063` | `uncertain` / `low` | keep `uncertain` / `low` | Wealth-milestone journaling is insufficient without private-message, stock-tip, reassurance, link-conversion, or other funnel context. |
| `threads_pilot_v1_0064` | `uncertain` / `low` | `uncertain` / `medium` | Detailed public holdings/amount disclosure is a high-risk trust-building starter but needs funnel context before scam labeling. |
| `threads_pilot_v1_0065` | `uncertain` / `low` | `uncertain` / `medium` | Detailed public pledge/amount/market-operation disclosure is a high-risk trust-building starter but needs funnel context before scam labeling. |
| `threads_pilot_v1_0066` | `uncertain` / `low` | `uncertain` / `medium` | Detailed public asset-goal/fund/US-stock amount disclosure with external-site context is a high-risk trust-building starter but needs funnel context before scam labeling. |
| `threads_pilot_v1_0067` | excluded duplicate trace; `uncertain` / `low` | `scam` / `high`; keep excluded duplicate trace | CIB-confirmed feature combination: stock-investment/Taiwan-stock/wealth-management domain, day-trading fast-action cue, trending-topic capture, wealth-password lure, and external-link context. |
| `threads_pilot_v1_0068` | excluded duplicate trace; `uncertain` / `medium` | `scam` / `high`; keep excluded duplicate trace | CIB-confirmed feature combination: day-trading group creation, LINE/private-channel migration, contact/private-channel cue, and external-link context. |
| `threads_pilot_v1_0069` | excluded duplicate trace; `uncertain` / `low` | keep `insufficient_evidence`; raise risk to `medium`; keep excluded duplicate trace | Market-scope narrowing can be a trust-building setup before investment views, disclaimers, and later funnel conversion, but the retained single sentence is too thin for scam labeling. |
| `threads_pilot_v1_0070` | excluded duplicate trace; `uncertain` / `low` | keep `insufficient_evidence`; raise risk to `medium`; keep excluded duplicate trace | Negated sensitive-intake language can be a trust-softening setup before investment views, disclaimers, and later funnel conversion, but the retained single sentence is too thin for scam labeling. |
| `threads_pilot_v1_0071` | excluded duplicate trace; `uncertain` / `medium` | `scam` / `high`; keep excluded duplicate trace | CIB-confirmed feature combination: interest-based action gate, comment request, private-message request, contact/private-channel cue, and external-link context. |
| `threads_pilot_v1_0072` | `uncertain` / `low` | keep `uncertain`; raise risk to `medium` | Investment-experience and trading-psychology trust-building language plus a redacted external-link category deserves higher-risk review, but missing reply/private-message/group/stock-tip/reassurance/guarantee/contact/conversion context blocks a scam label. |
| `threads_pilot_v1_0073` | `uncertain` / `low` | keep `insufficient_evidence`; raise risk to `medium` | Single-sentence market-scope narrowing plus a redacted external-link category is too thin for scam labeling, but can become trust-building when paired with investment views, private-message, community, stock-tip, reassurance, guarantee, contact, or conversion context. |
| `threads_pilot_v1_0074` | `uncertain` / `low` | keep `insufficient_evidence`; raise risk to `medium` | Single-sentence negated sensitive-intake language plus a redacted external-link category could be anti-scam education, rule explanation, or trust-softening; fuller funnel context is required before scam labeling. |
| `threads_pilot_v1_0075` | `uncertain` / `medium` | `scam` / `high` | Profit-plus-social-good framing co-occurs with redacted external-link category, guaranteed/risk-free signal, unrealistic-benefit signal, and investment-lure type. |

These updates are confirmation-based. They should not be generalized into a rule that query terms, topic-only words, private-message wording, earnings language, external links, ordinary comment activity, or ordinary assistant/operations language alone are sufficient for a `scam` label.

The `0027` review adds an evidence-quality lesson: minimized fragments can erase the distinction between anti-scam explanation and scammer evasion instruction. For future approved captures, preserve the fullest allowed post text and selected reply context rather than only a short risk phrase.

The `0047` review adds a candidate-family lesson: short-term or swing-trading stock group offers deserve higher-priority review, especially when they include private groups, contact handles, external links, guaranteed outcomes, stock-pick playbooks, or reply/comment lures, but the group phrase alone is not enough for a final `scam` label.

The `0048` and `0059` reviews reinforce capture completeness and starter-pattern handling: "people who hold stocks" audience openings can be high-risk stock-scam starters, but they need fuller text and related reply/link/private-message/contact/funnel context before final scam labeling.

The `0049` review adds a stock-tip boundary: public stock-tip or named-stock-pick behavior on Threads can be a high-risk scam behavior, but ordinary stock-market keywords alone remain non-evidence.

The `0050` review adds a named-stock reassurance boundary: "good stock / feel at ease" style language becomes scam-risk behavior when paired with link/funnel context.

The `0051` review adds a wealth-password boundary: day-trading plus secret-wealth or fast-profit framing can be scam-risk lure language, while ordinary financial keywords alone remain non-evidence.

The `0052` review adds a private day-trading group boundary: day-trading plus LINE/private-group migration is a high-risk scam funnel.

The `0053` review reinforces capture completeness: short market-scope fragments need fuller text and related link/contact/private-message/reply/funnel context before any scam label.

The `0054` review adds a negated-intake boundary: saying a process will not ask age or stock holdings can be benign rule explanation or anti-scam warning unless broader context shows funnel behavior.

The `0055` review reinforces the implicit-DM funnel boundary: "comment and private-message me" becomes scam-risk behavior when paired with private-group, contact, external-site, investment, or other conversion context.

The `0056` review adds a trust-softening private-channel boundary: humility, no-profit, or "not financial guru" disclaimers do not neutralize an investment private-message funnel.

The `0057` review reinforces dedupe discipline: high-risk family membership does not justify counting near-duplicates as new scam records.

The `0058` review adds an altruistic guru framing boundary: profit claims framed as giving back to society can be scam-risk trust packaging when tied to stock trading and funnel context.

The `0062` review adds an experience-sharing camouflage boundary: short-time large-wealth investment stories can function as testimonial proof or conversion bait when paired with external-site, private-message, community, or stock-tip context.

The `0063` review adds a wealth-milestone boundary: asset-goal journaling alone remains insufficient unless paired with conversion or persuasion signals.

The `0064` review adds a detailed-holdings disclosure boundary: public investment-product and amount disclosures can build credibility for later scams, but require conversion context for a final scam label.

The `0065` review extends that boundary to pledged funds and planned market operations.

The `0066` review extends that boundary to explicit asset targets and fund/US-stock amount disclosures with external-site context.

The `0067` review reinforces the wealth-password rule family: finance keywords alone remain insufficient, but finance-domain framing plus day-trading, trending-topic capture, wealth-password/secret-method language, and external-link context is a confirmed scam-risk feature combination. The item remains an excluded duplicate/near-duplicate trace for counting discipline.

The `0068` review reinforces the private day-trading group rule family: day-trading plus LINE/private-group migration is a confirmed scam-risk funnel feature combination. The item remains an excluded duplicate/near-duplicate trace for counting discipline.

The `0069` review adds a market-scope trust-building feature: saying certain markets will not be covered can look neutral, but in broader context it may help the poster appear selective and trustworthy before giving investment views, adding soft disclaimers, and later converting readers into stock-tip, private-message, community, or other funnel paths. The retained sentence alone remains insufficient.

The `0070` review adds a negated sensitive-intake trust-building feature: saying the poster will not ask age or holdings can look like safety guidance, but in broader investment context it may lower suspicion before investment views, soft disclaimers, and later conversion into stock-tip, private-message, community, or other funnel paths. The retained sentence alone remains insufficient.

The `0071` review reinforces the comment-plus-DM funnel family: asking interested readers to comment and private-message the poster is a confirmed scam-risk conversion mechanic when paired with contact, private-channel, link, investment, or other funnel context. The item remains an excluded duplicate/near-duplicate trace for counting discipline.

The `0072` review adds an investment-experience trust-building boundary: posts about trading methods, accumulated experience, and risk tolerance can prepare trust in the poster, especially when paired with an external-link category, but they remain `uncertain` until broader context shows private-message conversion, community migration, stock-tip guidance, reassurance, guarantees, contact cues, or other funnel mechanics.

The `0073` review applies the market-scope trust-building boundary to a non-duplicate item: market exclusions or scope-narrowing claims can help the poster appear selective or trustworthy, but a single sentence with an external-link category is still insufficient without conversion context.

The `0074` review applies the negated sensitive-intake boundary to a non-duplicate item: saying the poster will not ask age or holdings can reduce suspicion in a later funnel, but the same fragment can also be benign safety guidance. Preserve `insufficient_evidence` unless broader context shows conversion mechanics.

The `0075` review extends the profit-plus-social-good boundary: a message that presumes future investment profit and reframes it as helping others becomes scam/high when paired with external-link, guaranteed/risk-free, unrealistic-benefit, and investment-lure signals. Do not generalize this to ordinary charity language without investment-profit and funnel context.

For this evidence family, reply/comment context is decisive: future captures should check whether private messages, community migration, recommendations, stock tips, reassurance, guarantees, or other funnel cues appear below the post.
