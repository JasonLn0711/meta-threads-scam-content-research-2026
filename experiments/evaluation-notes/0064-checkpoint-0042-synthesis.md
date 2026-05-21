# Checkpoint 0042 Synthesis

## Purpose

Synthesize the repo-safe 42-record checkpoint into a reviewable research checkpoint.

This note contains no raw Threads content, full item URLs, raw handles, screenshots, raw reply text, credentials, browser artifacts, storage-state material, raw storage paths, contact IDs, stock names, stock codes, price values, or stakeholder case IDs.

## First-Principles Read

The repo has moved from "can we find data?" to "can the evidence system be reviewed?" The immediate research value is no longer another isolated item. The value is an auditable chain from run design to controlled capture, redacted item record, rule update, strict validation, baseline output, and checkpoint decision.

## Checkpoint Scope

| Field | Value |
|---|---|
| Checkpoint | `threads_pilot_v1_0042` |
| Dataset file | `data/interim/manual_records_checkpoint_0042.jsonl` |
| Records | 42 |
| Latest included item | `threads_pilot_v1_0042` |
| Latest included run record | `threads_pilot_v1_2026-05_item_0042_full_thread_capture_run_record_0034.md` |
| Run index | `governance/pilot-launch/run_index.md` |
| Post-checkpoint items excluded | `0043`, `0044`, `0045` |

## Validation

Commands run for this synthesis:

```bash
python3 scripts/validate_thread_dataset.py data/interim/manual_records_checkpoint_0042.jsonl --strict
python3 scripts/audit_thread_dataset.py data/interim/manual_records_checkpoint_0042.jsonl
.venv/bin/python scripts/run_rule_baseline.py data/interim/manual_records_checkpoint_0042.jsonl --variant all --run-name checkpoint-0042-synthesis-smoke-v1 --output-dir experiments/baselines/outputs
```

Results:

| Check | Result |
|---|---|
| Strict validation | pass |
| Checked records | 42 |
| Validation errors | 0 |
| Validation warnings | 0 |
| Audit threshold flags | 0 |
| Raw evidence in git | no |

## Aggregate Result

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

## Baseline Performance

Rule baseline run: `checkpoint-0042-synthesis-smoke-v1`.

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

Interpretation: this is a high-recall triage baseline. The current false-positive burden is acceptable for research review only because CIB policy prioritizes avoiding false negatives and because all high-risk outputs remain human-review candidates, not enforcement decisions.

## Rule Families Added By This Checkpoint

The 42-record checkpoint added or exercised these reusable evidence families:

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

## Hard-Negative Lesson

Item `0042` is the key hard negative: an anti-scam warning is not itself a scam item. A post can mention scam methods, investment groups, private contacts, promised returns, or victim-loss narratives while its persuasive direction is prevention rather than conversion.

The rule baseline correctly predicted item `0042` as `not_scam_like` / `low` with no reason codes. This is now a calibration guardrail: future rules must not over-trigger on warning, education, victim-prevention, or anti-scam commentary unless the item itself introduces a new conversion path.

## Acquisition Lesson

Confirmed-pointer intake is the current highest-yield acquisition method for high-risk scam-like rule learning. Earlier broad or topic-only collection was useful for low-risk comparators, link/contact boundaries, and false-positive pressure, but it did not reliably produce high-risk confirmed cases.

This does not justify broad crawler expansion. Query strings, seed terms, and topical search are candidate-finding aids only; they cannot become labels. The current best path is one approved confirmed pointer at a time, controlled capture, redacted record, second review, strict validation, and rule update only when a reusable evidence family appears.

## Limits

- The checkpoint is still small.
- Confirmed-pointer examples introduce source bias and cannot support prevalence claims.
- The non-scam bucket is useful for false-positive pressure, but not yet representative of all legitimate Threads finance discussion.
- OCR remains under-tested because `ocr_text` is empty across the checkpoint.
- The rule baseline is a triage baseline, not a detector.
- Embedding/model training should not start from this checkpoint. The dataset is not large or balanced enough, and model/artifact governance has not been separately approved.

## Checkpoint Decision

Recommended decision:

```text
checkpoint_ready_for_review_decision
```

The next decision should be explicit rather than automatic:

- Option A: continue approved confirmed-pointer intake, one item at a time, with controlled capture, redacted record, strict validation, and second review.
- Option B: pause new collection and start a CIB/165-facing checkpoint report v0.1 based on the 42-record pilot.

Preferred next step: hold the checkpoint decision first. If the audience needs a reviewable artifact soon, choose Option B. If rule-family coverage is still too thin for stakeholder review, choose Option A with a fixed small tranche and another checkpoint boundary.
