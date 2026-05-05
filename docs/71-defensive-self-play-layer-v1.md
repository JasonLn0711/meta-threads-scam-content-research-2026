# Defensive Self-Play Layer v1

Status: synthetic implementation layer

Date opened: 2026-05-05

## First Principle

Self-play here is a defensive robustness test. It does not create a scam assistant and does not produce usable scam scripts.

The layer asks:

```text
If known scam-like concepts mutate in subtle, abstract ways,
can the detection scaffold still recognize the behavioral structure?
```

The goal remains maximizing review-worthy candidate discovery per reviewer hour, with human final judgment, hard-negative protection, and no raw evidence in git.

## Loop

```text
concept
-> Adversary Simulator: abstract evasion variant
-> Simulation: safe synthetic sample
-> Detection System: confidence, concept match, novelty
-> Judge: adversary and detector rewards
-> State update: harder variants and stronger detector context
-> Discovery hooks: query generation, concept evolution, bandit context
```

## Modules

```text
src/selfplay/adversary.py    safe abstract variant generator
src/selfplay/simulation.py   non-actionable synthetic data generator
src/selfplay/detector.py     concept-aware detection scaffold
src/selfplay/judge.py        reward calculator
src/selfplay/runner.py       runnable self-play loop and priority loader
src/selfplay/logging.py      ignored local JSONL/state logs
selfplay_run.py              CLI entry point
```

## Safety Contract

`generate_variant(concept)` returns only abstract evasion strategies:

- `variant_strategy`;
- `evasion_characteristic`;
- `abstract_example`;
- `difficulty`;
- `non_actionable: true`;
- `actionable_content_included: false`.

The simulator must not output platform handles, real contact paths, payment details, transfer steps, credentials, or step-by-step scam instructions.

`generate_simulated_data(variant)` creates `candidate_type: selfplay_simulated` records tagged as `source: defensive_selfplay`.

These records are not evidence. They are local synthetic robustness tests.

## Detection

`detect(simulated_data, concepts)` returns:

- `confidence`;
- `matched_concept`;
- `novelty`;
- `is_scam_like`;
- short `reasoning`.

Conservative novelty is acceptable when the concept match is weak but the abstract structure is still suspicious. The detector output is a research signal, not a final scam determination.

## Rewards

`compute_rewards(A_output, B_output)` uses:

```text
adversary_reward = 1 - detection_confidence
detector_reward  = accuracy_component + confidence component
```

The adversary reward highlights weak detector confidence. The detector reward prefers correct concept recovery, partial novelty detection when appropriate, and higher confidence.

## Integration

Self-play priorities are written into ignored local state and can influence:

- query generation via `mode: selfplay_explore`;
- candidate features via `selfplay_variant_id`, `selfplay_evasion_characteristic`, `selfplay_reward_signal`, and `selfplay_detector_confidence`;
- contextual bandit features via self-play reward and query flags;
- concept evolution review by surfacing hard-to-detect abstract variants.

## Generated Local Outputs

Generated self-play files are ignored by git:

```text
data/selfplay/variants.jsonl
data/selfplay/simulated_data.jsonl
data/selfplay/detection_results.jsonl
data/selfplay/rewards.jsonl
data/selfplay/selfplay_state.json
```

## Usage

```bash
python3 selfplay_run.py --rounds 5 --reset
```

The CLI prints detector reward, adversary reward, detection confidence, and reward trends across rounds. The numbers are synthetic smoke-test signals only.

Synthetic sample result on 2026-05-05:

```text
detector_reward_trend=0.576 -> 0.578 -> 0.883 -> 0.885 -> 0.887
adversary_reward_trend=0.434 -> 0.426 -> 0.418 -> 0.411 -> 0.405
detection_confidence_trend=0.566 -> 0.574 -> 0.582 -> 0.589 -> 0.595
detector_reward_change=+0.311
```

This demonstrates loop mechanics only. It is not real-world performance evidence.

## Boundary Rules

- Keep self-play abstract, simulated, and non-actionable.
- Do not publish generated variants as real scam examples.
- Do not treat self-play logs as evidence of real behavior.
- Do not use self-play output for enforcement, public warning, automated takedown, legal fraud determination, or final scam labels.
- Do not connect real LLM APIs, live source collection, crawler expansion, or platform automation without a later decision and governance review.
- Preserve human final judgment and uncertainty.
