# Decision 0142: Add Adaptive Policy Deployment Loop v1

Date: 2026-05-05

Status: accepted as governed bridge support tooling

## Decision

Add Adaptive Policy Deployment Loop v1. The layer:

- implements `policy(context)` for query selection and candidate prioritization;
- supports `shadow`, `assist`, and `partial` deployment modes;
- logs context, action, outcome, and reward under ignored `data/policy/`;
- collects metadata-only human labels, delayed outcomes, and system errors;
- trains policy weights offline from past logs;
- updates policy safely with bounded weight movement;
- evaluates reward per reviewer hour, detection latency, robustness, and system errors;
- combines self-play simulation pressure with local policy logs.

## First-Principle Rationale

The goal remains:

```text
scam-worthy candidates per reviewer hour
```

The previous layers can simulate, predict, and stress-test discovery. This layer adds the missing decision-control loop: policy action, governed deployment mode, feedback, evaluation, and safe update.

The bridge is useful only if it remains stable and auditable. Sudden policy shifts would create review instability and hard-negative risk.

## Scope Boundary

This decision does not authorize:

- automated Threads or Meta collection;
- real-world live deployment;
- real LLM/API calls;
- production detector claims;
- raw evidence in git;
- final scam determinations;
- legal fraud determinations;
- enforcement recommendations;
- public warnings or automated takedowns.

`partial` mode means limited metadata routing only, with human final judgment required.

## Artifacts

- `docs/72-adaptive-policy-deployment-loop-v1.md`
- `data/policy/README.md`
- `policy_run.py`
- `src/policy/policy.py`
- `src/policy/logging.py`
- `src/policy/feedback.py`
- `src/policy/evaluation.py`
- `src/policy/training.py`
- `src/policy/deployment.py`
- `tests/test_adaptive_policy_layer.py`

## Generated Local Outputs

The policy runner writes ignored metadata-only files:

- `data/policy/context_action_log.jsonl`
- `data/policy/feedback_log.jsonl`
- `data/policy/evaluation_reports.jsonl`
- `data/policy/policy_state.json`

## Synthetic Demonstration

Command:

```bash
python3 policy_run.py --mode shadow --rounds 5 --reset --train-first
```

The demonstration output should be read as a smoke test for policy-loop mechanics only. It is not real-world deployment evidence.

Observed sample result on 2026-05-05:

```text
mode=shadow decisions=5 reward_per_reviewer_hour=8.265 latency=1.0 robustness=0.927
policy_version=3 training_examples=14
```

## Decision Implication

Future governed experiments can compare shadow, assist, and partial modes using reviewer-hour reward, latency, robustness, and error logs. Any real-world use must remain metadata-safe, human-reviewed, and explicitly authorized.
