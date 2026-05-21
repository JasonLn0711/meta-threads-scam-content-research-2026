# Existing Ambiguous And Medium-Risk Second Review Work Order 0050

Do not add raw Threads content, screenshots, full item URLs, raw handles, stakeholder case IDs, credentials, cookies, tokens, browser profiles, HAR files, full HTML, exact raw storage paths, access-list details, stock names, stock codes, price values, or sensitive investigative notes to this file.

## Work Order Identity

| Field | Value |
|---|---|
| Work order ID | `REVIEW-THREADS-PILOT-V1-0076-AMBIGUOUS-MEDIUM` |
| Date | `2026-04-26` |
| Related decision | `0101-authorize-existing-ambiguous-medium-second-review` |
| Dataset | `manual_records_checkpoint_0076.jsonl` |
| Review queue | `data/interim/review_queue_checkpoint_0076_uncertain_insufficient_medium.csv` |
| Queue size | 35 records |
| Operator | `AUTO-OP-01` |
| Purpose | second-review existing ambiguous, insufficient, and medium-risk records |
| Raw output location | not applicable; existing redacted records only |
| Repo-visible raw output | no |

## Queue Definition

Include any existing checkpoint 0076 record where:

- `scam_label == uncertain`; or
- `scam_label == insufficient_evidence`; or
- `risk_level == medium`.

## Review Lanes

| Lane | Items | Review goal |
|---|---:|---|
| `uncertain` | 29 | Decide whether evidence supports `scam`, `non_scam`, or remains mixed. |
| `insufficient_evidence` | 6 | Decide whether evidence remains not reviewable or can move to `uncertain`/another label. |
| `medium` risk | 13 | Decide whether risk should move to `high`, `low`, or remain `medium`. |
| Deduplicated queue | 35 | One row per item needing review. |

## Review Rules

For each item:

1. Use existing redacted record fields first.
2. Do not use raw source URLs, handles, screenshots, private messages, or external browsing.
3. Do not infer legal fraud.
4. Prefer `uncertain` when signals are mixed but evidence exists.
5. Prefer `insufficient_evidence` when decisive context is missing or not reviewable.
6. Promote to `scam` / `high` only when the existing evidence shows a review-worthy scam-like funnel or strong risk pattern.
7. Downgrade to `non_scam` / `low` only when the evidence is benign, warning/education, duplicate/excluded, or lacks scam-like persuasion.

## Output Fields

Each item-level review should record:

- item ID;
- prior label/risk;
- reviewer decision;
- final label/risk recommendation;
- evidence sufficiency recommendation;
- rule-family or signal rationale;
- whether controlled full-thread/reply capture is required;
- whether manual record rebuild is required.

## Current Status

Work order opened. Item-level adjudication has started.

## Recorded Queue Decisions

| Item | Prior queue status | Reviewer/CIB input | Updated recommendation | Notes |
|---|---|---|---|---|
| `threads_pilot_v1_0012` | `uncertain` / `low` | CIB-confirmed escort or fake-dating scam starter pattern | `scam` / `high` | Support-request plus private-message migration may be sufficient when CIB confirmation establishes the downstream scam pattern. |
| `threads_pilot_v1_0017` | `insufficient_evidence` / `low` | CIB-confirmed crypto wallet plus LINE private-channel scam pattern | `scam` / `high` | Preserve the query-echo provenance caveat; the label is based on CIB confirmation, not query terms alone. |
| `threads_pilot_v1_0020` | `uncertain` / `medium` | CIB-confirmed earnings-sheet/testimonial plus external-link funnel precursor | `scam` / `high` | In investment-teacher or investment-guidance contexts, public profit-proof sharing plus an external link is a trust-building funnel signal. |
| `threads_pilot_v1_0021` | `uncertain` / `medium` | CIB-confirmed coordinated comment-account reinforcement / double-act funnel | `scam` / `high` | Comment-area accounts can echo the original poster and amplify profit/testimonial claims to create false social proof. |
| `threads_pilot_v1_0025` | `uncertain` / `medium` | CIB-confirmed implausible third-party account/deposit custody delegation narrative | `scam` / `high` | Claims of delegating personal social accounts, crypto exchange accounts, and deposit/withdrawal tools to an outside assistant are suspicious when combined with crypto/contact/link signals. |
| `threads_pilot_v1_0027` | `uncertain` / `medium` | Context too thin; could be anti-scam education or evasion instruction | keep `uncertain` / `medium` | Preserve fuller post text and relevant reply context in future captures; the short retained fragment is not enough for scam/non-scam adjudication. |
| `threads_pilot_v1_0047` | `uncertain` / `medium` | Short-term/swing-trading stock group is a high-risk candidate family, but retained context is too thin | keep `uncertain` / `medium` | More context is required before scam labeling; escalate if paired with private groups, contact handles, external links, guaranteed outcomes, stock-pick playbooks, or reply/comment lures. |
| `threads_pilot_v1_0048` | `insufficient_evidence` / `low` | Stock-holder audience opening is high-risk starter candidate, but capture completeness is inadequate | keep `insufficient_evidence` / `low` | Future approved collection should preserve complete available text and relevant replies, links, private-message cues, contact handles, proof claims, and conversion cues. |
| `threads_pilot_v1_0049` | `insufficient_evidence` / `low` | Public stock-tip / named-stock-pick behavior on Threads | `scam` / `high` | Publicly reporting or promoting specific stock picks can feed follow-trading, group conversion, or later private-channel manipulation; not based on generic stock keywords alone. |
| `threads_pilot_v1_0050` | `uncertain` / `low` | Named-stock reassurance plus external-site funnel context | `scam` / `high` | Multiple named stocks plus "good stocks / just feel at ease" reassurance is a trust lure when paired with link/funnel context. |
| `threads_pilot_v1_0051` | `insufficient_evidence` / `low` | Day-trading plus wealth-password lure language | `scam` / `high` | The combination of day-trading, trending-topic, and "wealth password" framing is a fast-profit/secret-method lure, not ordinary finance vocabulary. |
| `threads_pilot_v1_0052` | `uncertain` / `medium` | Day-trading plus LINE/private-group migration | `scam` / `high` | Explicit day-trading group creation/migration to LINE or private group is a private-channel investment funnel. |
| `threads_pilot_v1_0053` | `insufficient_evidence` / `low` | Fragment could be ordinary scope-setting; capture completeness is inadequate | keep `insufficient_evidence` / `low` | Requires fuller text and any related link/contact/reply/stock-tip/reassurance/private-message/private-group/proof context before scam adjudication. |
| `threads_pilot_v1_0054` | `insufficient_evidence` / `low` | Fragment could be rule explanation or anti-scam warning | keep `insufficient_evidence` / `low` | Do not label scam unless fuller context shows private-message migration, group recruitment, stock-pick guidance, external links, contact handles, individualized holdings intake, or other funnel cues. |
| `threads_pilot_v1_0055` | `uncertain` / `medium` | Comment-plus-DM action gate with private-group/contact/link context | `scam` / `high` | Asking interested readers to comment and private-message creates an implicit private funnel when paired with private-group/contact/external-site categories. |
| `threads_pilot_v1_0056` | `uncertain` / `medium` | Investment-content migration to IG/private messages with trust-softening disclaimers | `scam` / `high` | Humility or no-profit language does not neutralize an investment private-message path. |
| `threads_pilot_v1_0057` | excluded duplicate trace | Duplicate of item `0047` short-term/swing-trading stock group family | keep excluded duplicate | Do not count as a new scam item; preserve as dedupe evidence and require fuller context for future promotion. |
| `threads_pilot_v1_0058` | `uncertain` / `medium` | Profit-plus-social-good stock framing with external-site context | `scam` / `high` | "Profit then give back to society" is altruistic guru trust packaging and is inconsistent with market mechanics when tied to stock-tip/funnel behavior. |
| `threads_pilot_v1_0059` | excluded duplicate trace | Duplicate of item `0048` stock-holder audience opening | keep excluded duplicate | Preserve as dedupe evidence and high-risk starter candidate; do not count as a new scam item without fuller distinct context. |
| `threads_pilot_v1_0060` | excluded duplicate trace | Duplicate of item `0049` public stock-tip / named-stock-pick behavior | keep excluded duplicate | Preserve as dedupe evidence for the named-stock-pick rule family; do not count as a new scam item. |
| `threads_pilot_v1_0061` | excluded duplicate trace | Duplicate of item `0050` named-stock reassurance plus funnel context | keep excluded duplicate | Preserve as dedupe evidence for the named-stock reassurance rule family; do not count as a new scam item. |
| `threads_pilot_v1_0062` | `uncertain` / `low` | Short-time large-wealth investment story plus external-site context | `scam` / `high` | Experience-sharing camouflage can convert readers to private messages, communities, external sites, or later stock-pick guidance. |
| `threads_pilot_v1_0063` | `uncertain` / `low` | Wealth-milestone journaling is insufficient without funnel context | keep `uncertain` / `low` | Requires additional text, conversion-link function, private-message requests, community migration, stock tips, reassurance/guarantee language, or proof/funnel cues. |
| `threads_pilot_v1_0064` | `uncertain` / `low` | Detailed public holdings/amount disclosure is a high-risk trust-building starter | `uncertain` / `medium` | Not enough for scam labeling without private messages, community migration, recommendations, reassurance/guarantee, conversion-link function, or other funnel cues. |
| `threads_pilot_v1_0065` | `uncertain` / `low` | Detailed public pledge/amount/market-operation disclosure is a high-risk trust-building starter | `uncertain` / `medium` | Not enough for scam labeling without private messages, community migration, recommendations, reassurance/guarantee, conversion-link function, or other funnel cues. |
| `threads_pilot_v1_0066` | `uncertain` / `low` | Detailed public asset-goal/fund/US-stock amount disclosure with external-site context is a high-risk trust-building starter | `uncertain` / `medium` | Not enough for scam labeling without fuller post/reply context, private messages, community migration, recommendations, stock tips, reassurance/guarantee, conversion-link function, or other funnel cues. |
| `threads_pilot_v1_0067` | excluded duplicate trace; `uncertain` / `low` | CIB-confirmed stock-investment/day-trading/trending-topic/wealth-password lure with external-link context | `scam` / `high`; keep excluded duplicate trace | Feature lesson may be used, but do not count as a new independent selected item because duplicate/near-duplicate status remains. |
| `threads_pilot_v1_0068` | excluded duplicate trace; `uncertain` / `medium` | CIB-confirmed day-trading LINE/private-group migration with contact/link context | `scam` / `high`; keep excluded duplicate trace | Feature lesson may be used, but do not count as a new independent selected item because duplicate/near-duplicate status remains. |
| `threads_pilot_v1_0069` | excluded duplicate trace; `uncertain` / `low` | Market-scope narrowing can be trust-building before investment views and funnel conversion | keep `insufficient_evidence`; raise risk to `medium`; keep excluded duplicate trace | Single sentence is too thin for scam labeling, but the feature should be tracked when paired with trust-softening disclaimers, private messages, recommendations, stock tips, or other funnel cues. |
| `threads_pilot_v1_0070` | excluded duplicate trace; `uncertain` / `low` | Negated sensitive-intake language can lower suspicion before investment views and funnel conversion | keep `insufficient_evidence`; raise risk to `medium`; keep excluded duplicate trace | Single sentence is too thin for scam labeling, but the feature should be tracked when paired with trust-softening disclaimers, private messages, recommendations, stock tips, or other funnel cues. |
| `threads_pilot_v1_0071` | excluded duplicate trace; `uncertain` / `medium` | CIB-confirmed comment-plus-DM action gate with contact/link context | `scam` / `high`; keep excluded duplicate trace | Feature lesson may be used, but do not count as a new independent selected item because duplicate/near-duplicate status remains. |
| `threads_pilot_v1_0072` | `uncertain` / `low` | Reviewer-confirmed investment-experience / trading-psychology trust-building starter with redacted external-link category | keep `uncertain`; raise risk to `medium` | Existing context does not show private-message conversion, community migration, stock-tip guidance, reassurance, guarantee, contact cue, or other funnel mechanics; do not label scam from investment-experience language alone. |
| `threads_pilot_v1_0073` | `uncertain` / `low` | Reviewer-confirmed market-scope narrowing starter with redacted external-link category | keep `insufficient_evidence`; raise risk to `medium` | Single retained sentence is too thin for scam labeling; track the feature for future context that shows investment views, private-message conversion, community migration, stock tips, reassurance, guarantee, contact cues, or other funnel mechanics. |
| `threads_pilot_v1_0074` | `uncertain` / `low` | Reviewer-confirmed negated sensitive-intake starter with redacted external-link category | keep `insufficient_evidence`; raise risk to `medium` | Could be safety guidance or trust-softening before conversion; do not label scam until fuller context shows investment views, private-message conversion, community migration, stock tips, reassurance, guarantee, contact cues, or other funnel mechanics. |
| `threads_pilot_v1_0075` | `uncertain` / `medium` | Reviewer-confirmed profit-plus-social-good investment lure with redacted external-link and benefit/guarantee signals | `scam` / `high` | Presumed future gain plus social-good framing is scam-risk trust packaging when paired with external-link, guaranteed/risk-free, unrealistic-benefit, and investment-lure signals; not based on generic charity or investment words alone. |

## Queue Review Rule Update

CIB-confirmed patterns may override a prior low-confidence or insufficient-evidence status when the confirmation is explicit and the retained redacted evidence contains at least the relevant starter, reply/comment, custody, or funnel signal. This does not authorize automatic labeling from query terms, private-message wording, topic vocabulary, earnings language, links, ordinary comment activity, or ordinary assistant/operations language alone.

Short fragments about private-channel properties, such as LINE being private or hard to report, should remain `uncertain` unless fuller context shows either anti-scam education or evasion/funnel instruction. Future controlled captures should preserve enough post text and selected reply context to distinguish those cases.

Short-term or swing-trading stock group offers should be treated as a high-risk candidate family because they can exploit impatience and fast-profit seeking, but they should remain `uncertain` unless additional funnel evidence is visible or CIB confirmation is explicit.

Fragmentary stock-audience wording, such as addressing people who hold stocks, should be treated as a high-risk starter candidate because it can target position anxiety, loss rescue, or desire for guidance. It should remain `insufficient_evidence` when no conversion, contact, payment, proof, private-message, stock-tip, reassurance, or link signal is retained. Future collection should maximize allowed text completeness so reviewers are not forced to adjudicate isolated sentence fragments.

Public stock-tip or named-stock-pick behavior on social platforms should be treated as high risk when reviewers identify it as "reporting stock tips" rather than generic stock vocabulary. Do not generalize this to all Taiwan-stock, stock-market, or investment keywords.

Named-stock reassurance language, such as telling readers that named stocks are good and they only need to feel at ease, should be treated as scam-risk behavior when paired with link, group, contact, reply, or other funnel context.

Day-trading plus "wealth password" or secret-method framing should be treated as scam-risk lure language when reviewers identify it as fast-profit persuasion rather than neutral financial discussion.

Stock investment/Taiwan-stock/wealth-management terms become stronger scam evidence when combined with day-trading, trending-topic capture, "wealth password" or secret-method language, and external-link context. The rule is feature-combination based; do not label from finance keywords alone.

Day-trading plus LINE/private-group migration should be treated as a high-risk scam funnel because it moves fast-trading persuasion into a less visible private channel.

Day-trading group creation plus LINE, private group, contact-handle, or external-link context is a high-risk investment-funnel feature combination. Treat it as stronger than topic-only day-trading language because it includes an explicit off-platform or less-visible conversion path.

Market-scope fragments, such as saying a space will not include Hong Kong or US stocks, should remain `insufficient_evidence` unless paired with already confirmed scam-risk logic such as public stock tips, named-stock reassurance, private-message requests, private groups, contact handles, links, profit proof, or other conversion cues.

Market-scope narrowing can also work as a trust-building setup: a poster may exclude certain markets, offer investment views with "do not necessarily follow me" style disclaimers, and gradually build credibility before leading readers into stock tips, private messages, communities, or other funnel paths. Track this feature, but do not label it `scam` unless the broader context shows the conversion path.

Fragments that negate sensitive intake, such as saying the poster will not ask age or stock holdings, may be rule explanation or anti-scam warning. Treat them as `insufficient_evidence` unless the broader context turns the same language into a funnel or evasion pattern.

Negated sensitive-intake language can also be trust-softening in an investment funnel: saying the poster will not ask age, holdings, or other sensitive facts may reduce suspicion before investment views, "do not necessarily follow me" disclaimers, stock-tip guidance, private messages, communities, or external conversion paths. Track the feature, but do not label it `scam` unless fuller context shows the conversion path.

Comment-plus-DM action gates should be treated as scam-risk behavior when paired with private-group, contact, link, stock-tip, investment, profit, or other conversion context. Interest language alone remains insufficient.

Interest-based action gates, such as asking interested readers to leave a comment and private-message the poster, are especially important because they convert a public post into a private or semi-private lead funnel. Track comment request, DM request, contact cue, and link/private-group context separately so later reviewers can distinguish ordinary engagement from conversion mechanics.

Trust-softening disclaimers such as not wanting to mislead, being humble, or not earning money here should not reduce risk when the same item moves investment/finance discussion to IG, DM, LINE, private groups, or other private channels.

Near-duplicate traces should not be promoted into new scam records solely because the family is high-risk. Keep them excluded unless a future full-context capture adds distinct evidence.

Profit-plus-social-good stock framing should be treated as scam-risk behavior when paired with stock trading/investment, profit, external-site, stock-tip, or funnel context. The claim that stock-tip activity "gives back to society" is not a neutral charitable signal.

Short-time large-wealth investment stories should be treated as scam-risk behavior when paired with external-site, private-message, community, stock-tip, or other funnel context. They can look like experience sharing while functioning as testimonial proof or conversion bait.

Wealth-milestone or goal-update posts should not be automatically labeled scam. Escalate only when they connect to private messages, community migration, actionable stock guidance, external conversion links, reassurance/guarantee language, or other funnel cues.

Detailed public disclosure of investment products, amounts, yield-like figures, and current purchase amounts should be treated as a high-risk trust-building starter, because it can be used to build credibility. It remains `uncertain` without conversion or persuasion context.

Detailed public disclosure of pledged amounts, fund collateral, asset targets, fund/US-stock amounts, and planned market operations should be treated similarly: it can build credibility for later persuasion, but remains `uncertain` without conversion or recommendation context.

For detailed public holdings, amounts, or market-operation narratives, future controlled review should inspect the reply/comment area for private-message requests, community migration, recommendations, stock tips, reassurance, guarantees, or other funnel cues. The main post may be trust-building while the conversion signal appears in comments.

Investment-experience and trading-psychology language can be a trust-building starter, especially when paired with a redacted external-link category. Keep it `uncertain` and raise risk when evidence is partial, but do not promote to `scam` unless fuller context shows private-message conversion, community migration, stock-tip guidance, reassurance, guarantees, contact cues, or other funnel mechanics.
