# Decision 0045: Record Account Multi-Post Style Cluster Rule

## Date

2026-04-25

## Status

Accepted

## Decision

Add `account_multi_post_style_cluster` as a generic signal tag and controlled research method.

When CIB or an approved stakeholder identifies an investment-scam account, the project may run a small account-level sampling rehearsal to identify whether multiple posts/replies under the same account show complementary scam-like persuasion styles. The method is for candidate discovery, dedupe, repeat-source context, and prioritization of later item-level full-thread captures.

## Trigger

The project owner supplied a CIB-detected investment scam account and noted that some scam accounts contain many posts whose posts and replies may show two or more different styles. The project owner asked to preserve this as a reusable rule and method.

## Rationale

A single post may not contain the full funnel. Account-level sampling can reveal recurring style families such as:

- profile-level group, community, or synchronized-operation framing;
- past-performance or stock-picking proof;
- strong market-direction calls;
- individualized operation language such as buy, add, hold, switch, or continue holding;
- follower action chorus or authority-building replies;
- private-channel, contact, or off-platform migration cues.

For high-recall CIB triage, this helps select better candidate posts without relying only on topic search seeds.

## Boundaries

- Use only CIB-detected or otherwise approved accounts.
- Keep candidate review capped and recorded in the run record.
- Do not capture follower/following graphs, broad account history, profile photos, or unrelated personal data by default.
- Do not store raw account handles, raw profile URLs, raw post URLs, raw text, screenshots, or HTML in git.
- Do not label every post under the account as `scam` by association.
- Each selected item still needs item-level evidence from the post, replies/comments, OCR, links, contact handles, payment/credential cues, or approved profile context.

## Files Updated

- `docs/04-taxonomy.md`
- `docs/06-annotation-guideline-v1.md`
- `docs/30-annotator-onboarding-quickstart.md`
- `docs/51-stakeholder-evidence-expansion-memo.md`
- `data-contracts/labeling_schema_v1.json`
- `data-contracts/thread_item_schema_v1.json`
- `governance/pilot-launch/threads_pilot_v1_2026-05_guideline_revision_log.md`

## Next Action

Use account-level sampling only to choose a small number of candidate posts for full-thread capture. After selection, create normal item-level manual entries and run strict validation before adding any item to the aggregate checkpoint.
