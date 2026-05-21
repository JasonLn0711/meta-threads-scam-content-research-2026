# Threads Scam Content Checkpoint 0042 Report v0.1

## Report Identity

| Field | Value |
|---|---|
| Report | Threads scam-content checkpoint 0042 report v0.1 |
| Date | 2026-04-25 |
| Repo | `meta-threads-scam-content-research-2026` |
| Dataset checkpoint | `threads_pilot_v1_0042` |
| Records | 42 |
| Audience | CIB/165-facing review, research reviewers, investigators, professors, engineers |
| Status | Checkpoint report, not production detector, not legal determination |
| Decision request | `reports/checkpoint-0042-decision-request.md` |
| Review checklist | `reports/checkpoint-0042-review-checklist.md` |

## Executive Summary

The project has moved from source acquisition feasibility into evidence-system reviewability. The 42-record checkpoint shows that the repo can preserve controlled raw evidence outside git, convert selected evidence into redacted local records, strict-validate aggregate data, maintain rule-family decisions, and run an explainable high-recall baseline.

The checkpoint is strong enough for stakeholder review. It is not strong enough for prevalence claims, broad crawler expansion, embedding/model training, or production enforcement.

Recommended checkpoint decision:

```text
pause_new_collection_and_review_checkpoint_v0_1
```

After review, stakeholders should choose either:

- resume bounded confirmed-pointer intake with a fixed next tranche; or
- continue report/guideline hardening before collecting more examples.

## What This Checkpoint Proves

| Claim | Status |
|---|---|
| Controlled capture can preserve raw evidence outside git | Supported |
| Redacted item records can be built and strict-validated | Supported |
| Confirmed-pointer intake is high-yield for scam-like rule learning | Supported |
| Reply/comment context matters for scam-like triage | Supported |
| Hard negatives are necessary to avoid overflagging warnings | Supported |
| Baseline output can prioritize recall while preserving review reasons | Supported |

## What This Checkpoint Does Not Prove

| Non-claim | Reason |
|---|---|
| Scam prevalence on Threads | Confirmed-pointer and manual-public sources are not representative. |
| Legal fraud determination | This is research triage, not legal adjudication. |
| Production detector readiness | Dataset is small and review-governed. |
| Embedding/model-training readiness | Dataset is too small, biased, and not governed for model artifacts. |
| Broad crawler readiness | Broad crawler expansion would add governance, privacy, and source-skew risk. |

## Aggregate Distribution

| Label / risk | Count |
|---|---:|
| `scam` | 14 |
| `non_scam` | 22 |
| `uncertain` | 5 |
| `insufficient_evidence` | 1 |
| `high` risk | 14 |
| `medium` risk | 4 |
| `low` risk | 24 |

Source mix:

| Source type | Count |
|---|---:|
| `manual_public` | 27 |
| `stakeholder_provided` | 15 |

Content shape:

| Content shape | Count |
|---|---:|
| `text_only` | 16 |
| `link_or_redirect` | 11 |
| `reply_context` | 11 |
| `text_image_post` | 4 |

## Baseline Result

Rule baseline run:

```text
checkpoint-0042-synthesis-smoke-v1
```

| Metric | Value |
|---|---:|
| Binary metric items | 36 |
| Accuracy | 0.833 |
| Precision | 0.700 |
| Recall | 1.000 |
| F1 | 0.824 |
| True positives | 14 |
| True negatives | 16 |
| False positives | 6 |
| False negatives | 0 |

Interpretation:

- Recall is the most important metric at this stage because CIB policy prefers avoiding false negatives.
- False positives remain meaningful and must be reviewed, not ignored.
- The baseline should be treated as a review queue generator, not a final classifier.

## Rule Families In Scope

The checkpoint added or exercised these rule families:

- `implicit_dm_contact_request`
- `high_fee_course_or_membership_funnel`
- `comment_code_lead_magnet`
- `past_performance_profit_proof`
- `stock_rescue_group_funnel`
- `individual_stock_advice_reply_funnel`
- `market_direction_herding_chorus`
- `poster_identity_context`
- `account_multi_post_style_cluster`
- `institutional_flow_authority_lure`
- `account_posting_cadence_metadata`
- `reply_impersonation_contact_hijack`
- `stock_pick_playbook_keyword_funnel`
- `trapped_position_dm_playbook_reply`
- `lifestyle_trust_market_reassurance_funnel`
- `dark_horse_stock_target_price_dm_funnel`
- `mass_stock_command_list_group_funnel`

The rule library is strongest when it records converging evidence families. It should not turn a single keyword, topic, or account association into a scam label.

## Hard-Negative Lesson

The checkpoint includes a confirmed non-scam warning item. This matters because anti-scam education can mention the same vocabulary that appears in scam lures: investment groups, promised returns, private contacts, victim stories, and suspicious tactics.

The annotation rule is:

```text
label the direction of persuasion, not isolated scam vocabulary
```

If the item warns readers not to join, not to trust, or not to chase the offer, it should not be treated as scam-like unless the item itself introduces a new conversion path.

## Acquisition Lesson

Confirmed-pointer intake is the current highest-yield approved acquisition method for high-risk rule learning. Earlier topic-only or broad candidate-finding runs were useful for comparator examples and false-positive pressure, but they did not reliably produce confirmed high-risk scam-like evidence.

Recommended acquisition posture after this report:

- use approved confirmed pointers one at a time;
- preserve raw evidence only in the controlled store;
- create redacted local records;
- strict-validate every item and aggregate;
- add rules only for reusable evidence families;
- checkpoint after each fixed tranche.

## Governance Boundaries

The repo must continue to exclude:

- raw Threads URLs;
- raw handles or profile URLs;
- raw post text and raw reply text;
- screenshots and HTML;
- visible contact IDs;
- stock names, stock codes, and price values from controlled evidence;
- credentials, cookies, browser profiles, storage state, and tokens;
- stakeholder case IDs or sensitive investigative details.

Raw evidence remains in the approved controlled store. Git contains only redacted research records, hashes/counts, rule-family summaries, run indices, decision logs, and validation outcomes.

## Recommended Decision

Choose one path explicitly:

| Path | Meaning | When to choose |
|---|---|---|
| A. Resume bounded confirmed-pointer intake | Continue one item at a time with a fixed next tranche and checkpoint boundary. | Choose if reviewers need more rule-family coverage before report delivery. |
| B. Keep collection paused and review this report | Turn checkpoint v0.1 into the stakeholder-facing deliverable. | Choose if reviewers need a readable evidence-system checkpoint now. |

This report recommends Path B first: review the evidence system before more collection.

## Next Work Items

1. Review this report against `governance/pilot-launch/run_index.md`.
2. Decide whether CIB/165 review needs more item examples or a cleaner report package.
3. If continuing collection, define the next tranche size before collecting item `0046`.
4. If pausing collection, refine this report into a delivery-ready checkpoint packet.
