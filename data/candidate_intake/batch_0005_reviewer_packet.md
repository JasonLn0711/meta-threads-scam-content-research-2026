# Batch 0005 Reviewer Packet

## Purpose

This packet turns Batch 0005 into a low-burden human review task.

The goal is not to decide legal fraud. The goal is to learn whether `保證收益`
or `成果展示` produces more high-value research candidates per unit reviewer
effort.

Use this packet together with:

- `data/candidate_intake/batch_0005_intake.yaml`
- `data/candidate_stubs/batch_0005.yaml`
- `experiments/batch_variants/0005-guarantee-vs-result-display-contrast.md`

## First-Principle Decision

Batch 0005 answers one operating-system question:

```text
Should the next exploration loop prioritize 保證收益 + funnel/contact structure,
or keep broad 成果展示 as a discovery source?
```

This batch is capped at 10 intake entries because the purpose is directional
learning, not volume.

## Contrast Arms

Arm A:

```text
保證收益 + funnel/contact structure
```

Reviewer checks whether a guarantee-like value anchor becomes review-stable
when it appears with contact, group, or reply-funnel structure.

Arm B:

```text
成果展示 without explicit 保證收益
```

Reviewer checks whether result display is useful by itself, or whether it mainly
creates ambiguity, thread-reading burden, and second-review need.

## Field Dictionary

Fill sparse features as `0` or `1` only.

`誘導聯絡`:
Structured metadata supports movement toward direct contact, private follow-up,
or a contact transition. Do not store the contact method itself.

`保證收益`:
Structured metadata supports explicit or near-explicit certainty, guaranteed
benefit, or no-loss/value-certainty framing.

`社群導流`:
Structured metadata supports movement toward a group, community, audience pool,
or off-post community funnel. Do not store group names or links.

`情緒操控`:
Structured metadata supports urgency, fear, FOMO, reassurance pressure,
scarcity, or emotional leverage.

`成果展示`:
Structured metadata supports result display, proof-like presentation,
testimonial-like framing, or performance/showcase anchoring.

`reply_funnel`:
The candidate depends on reply or comment-layer behavior to understand the
funnel.

`needs_thread`:
The reviewer needed broader thread or reply context to make a safe research
decision.

`review_stable_funnel_anchor`:
The reviewer could identify the funnel or value-stage anchor with low burden and
without needing second review.

## Review Metadata

`decision`:
Use `scam`, `non_scam`, or `uncertain` as a research label only. This is not a
legal fraud label and not an enforcement recommendation.

`confidence`:
Use a decimal from `0` to `1` for reviewer confidence.

`review_time_seconds`:
Record actual elapsed review time. Do not estimate after the fact if timing was
not observed.

`second_review_required`:
Use `true` if a second reviewer is needed because the case is ambiguous,
high-impact, or hard to classify from structured metadata.

## Structured Hints

Fill these with category-level descriptions only:

- `common_behaviors`
- `structural_patterns`
- `reviewer_signals`
- `hard_negative_contrast`

Allowed examples:

- `contact_transition`
- `group_funnel`
- `result_display_anchor`
- `guarantee_anchor`
- `thread_context_required`
- `pure_result_display_negative`

Do not paste raw wording, handles, identifiers, links, screenshots, browser
artifacts, or controlled-store locators.

## Entry Review Cues

`INTAKE_0005_A_01`:
Focus on `保證收益`, `誘導聯絡`, and `reply_funnel`. Test whether contact
transition plus guarantee makes the candidate review-stable.

`INTAKE_0005_A_02`:
Focus on `保證收益`, `社群導流`, and `review_stable_funnel_anchor`. Test whether
group-funnel structure reduces reviewer burden.

`INTAKE_0005_A_03`:
Focus on `保證收益`, `誘導聯絡`, and `review_stable_funnel_anchor`. Test whether
contact transition is enough without broad thread reading.

`INTAKE_0005_A_04`:
Focus on `保證收益`, `成果展示`, and `reply_funnel`. Test whether proof-like result
display strengthens or distracts from the guarantee anchor.

`INTAKE_0005_A_05`:
Focus on `保證收益`, `情緒操控`, and `needs_thread`. This is the Arm A burden and
hard-negative check.

`INTAKE_0005_B_01`:
Focus on `成果展示`, `誘導聯絡`, and `needs_thread`, with `保證收益` expected absent.
Test result display plus contact transition without explicit guarantee.

`INTAKE_0005_B_02`:
Focus on `成果展示`, `社群導流`, and `needs_thread`, with `保證收益` expected absent.
Test group cue without guarantee.

`INTAKE_0005_B_03`:
Focus on `成果展示` and `needs_thread`, with `保證收益` expected absent. This is the
standalone display hard-negative check.

`INTAKE_0005_B_04`:
Focus on `成果展示`, `情緒操控`, and `needs_thread`, with `保證收益` expected absent.
Test emotional pressure without guarantee.

`INTAKE_0005_B_05`:
Focus on `成果展示`, `reply_funnel`, and `needs_thread`, with `保證收益` expected
absent. This is the uncertain funnel-boundary check.

## Stop Rules

Stop the batch entry instead of filling it if any of these are required:

- raw Threads content would need to be pasted into this repo
- PII, handles, links, screenshots, browser artifacts, or credentials would need
  to be stored
- a controlled-store locator would need to be stored
- the reviewer cannot separate Arm A and Arm B without raw evidence leakage
- review time becomes too high for the capped contrast study
- the case would require an enforcement, legal, or public-warning judgment

## Done Condition

The batch is ready to enter the v2 ROS only when:

- all 10 intake entries have `fill_status: completed`
- every sparse feature is `0` or `1`
- every review field is filled
- every completion gate is `true`
- the conversion report shows `blocked_count: 0`

Then run:

```bash
./.venv/bin/python scripts/validate_candidate_intake_v2.py data/candidate_intake/batch_0005_intake.yaml --expected-count 10
./.venv/bin/python scripts/convert_candidate_intake_v2.py data/candidate_intake/batch_0005_intake.yaml --report-output data/candidate_intake/batch_0005_conversion_report.yaml
./.venv/bin/python scripts/convert_candidate_intake_v2.py data/candidate_intake/batch_0005_intake.yaml --report-output data/candidate_intake/batch_0005_conversion_report.yaml --write-candidates
./.venv/bin/python scripts/validate_candidate_v2.py data/candidates
./.venv/bin/python scripts/run_v2_ros.py
./.venv/bin/python scripts/generate_feature_candidates_v1.py
./.venv/bin/python scripts/generate_exploration_tasks.py
```

## Interpretation

If Arm A keeps higher SVS with lower `needs_thread` and low second-review rate,
the next exploration loop should prioritize `保證收益 + funnel/contact structure`.

If Arm B remains slower, more uncertain, or second-review heavy, broad `成果展示`
should be treated as a mixed discovery signal rather than a primary source arm.

If Arm B becomes strong only under one narrow condition, write that condition as
a feature candidate. Do not auto-promote it into the sparse schema.
