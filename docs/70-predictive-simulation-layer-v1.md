# Predictive Simulation Layer v1

Status: synthetic implementation layer

Date opened: 2026-05-05

## First Principle

Prediction here does not mean claiming to know the future. It means using known scam-like concepts to create plausible, subtle strategy variants and test whether the discovery loop should explore them.

This layer turns concept intelligence into synthetic foresight:

```text
known concept
-> subtle mutation
-> simulated post
-> risk score
-> predictive query seed
-> later validation hook
```

It is not a real-world prediction system, adversary playbook, production detector, crawler, enforcement system, or legal fraud determination system.

## Modules

```text
src/prediction/mutation.py    prompt-shaped local mutation engine
src/prediction/simulation.py  simulated post generator
src/prediction/scoring.py     embedding, concept-match, novelty, and evasion risk score
src/prediction/validation.py  later-observation validation hooks
src/prediction/logging.py     ignored local JSONL logs
```

## Mutation Engine

`mutate_concept(concept)` returns predicted variants with:

- `variant_name`;
- `modified_strategy`;
- `evasion_type`;
- `evasion_strength`;
- `example_text`;
- `search_query`.

The implementation builds the prompt shape an approved LLM adapter would receive, but uses `local_mutation_policy_v1`. It prioritizes subtle evasion such as softening guarantee language, dropping explicit platform names, replacing authority with peer-sharing, or reframing contact as note sharing.

## Simulation Generator

`generate_simulated_posts(variants)` creates tagged synthetic posts:

- `candidate_type: simulated`;
- `source: predictive_layer`;
- `tag: simulated_prediction`;
- `simulated: true`.

These are not evidence. They are local synthetic exploration seeds.

## Risk Scoring

`score_simulation(simulated_post, concept)` uses:

- deterministic embedding similarity;
- conservative concept matching;
- novelty score;
- evasion strength.

The output `risk_score` is a prioritization score for exploration, not a scam label.

## Validation

`track_prediction_validation(predicted_variants, observed_candidates)` records whether a variant later appears similar to observed candidate metadata and computes `time_lag_rounds` when possible.

Current validation mode is synthetic metadata only. Real validation requires a later governed decision, controlled evidence handling, and aggregate reporting.

## Integration

The advanced runner now:

- mutates selected concepts after each synthetic round;
- generates simulated posts;
- logs simulation risk scores;
- stores prediction priorities in ignored learning state;
- feeds high-risk predicted variants into the next round's query generator;
- adds `predicted_variant_id`, `prediction_evasion_type`, and `predictive_risk_score` to candidate features and bandit context.

## Generated Local Outputs

Generated prediction logs are ignored by git:

```text
data/predictions/predicted_variants.jsonl
data/predictions/simulated_posts.jsonl
data/predictions/simulation_scores.jsonl
data/predictions/validation_results.jsonl
```

## Usage

```bash
python3 advanced_run.py --rounds 5 --reset
```

Synthetic sample result on 2026-05-05:

```text
reward_trend=14.913 -> 22.723 -> 8.418 -> 8.963 -> 15.931
reward_change=+1.018 scam-worthy_candidates_per_reviewer_hour
```

This demonstrates loop mechanics only. It is not real-world performance evidence.

## Boundary Rules

- Keep simulations plausible, subtle, and synthetic-tagged.
- Do not use simulated posts as evidence.
- Do not treat predictive risk as a label.
- Do not publish generated variants as real scam examples.
- Do not connect real LLM APIs, source APIs, live Threads collection, or crawler expansion without a new decision and governance review.
- Preserve human final judgment and uncertainty.
