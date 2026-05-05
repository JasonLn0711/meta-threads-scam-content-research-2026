# Adaptive Policy Deployment Loop v1

Status: governed bridge layer

Date opened: 2026-05-05

## First Principle

This layer bridges simulation and real-world feedback without turning the repo into a production detector.

The decision policy answers:

```text
Given metadata-only context, which query seeds and candidate priorities should be suggested next?
```

The success metric remains:

```text
scam-worthy candidates per reviewer hour
```

Policy learning is allowed only as stable, logged, human-governed support for discovery and review routing. It does not authorize automated Threads collection, final scam decisions, legal fraud determinations, enforcement actions, or public warnings.

Historical case logs and reviewed slices are partial feedback, not a representative map of all Threads investment scams. The policy must treat learned weights as bounded routing hypotheses. It should be evaluated on new governed slices before any claim that a routing rule generalizes beyond the current fragments.

## Loop

```text
self-play priorities
real-world metadata logs
        ↓
offline policy training
        ↓
deployment mode policy
        ↓
context/action logging
        ↓
human labels + delayed outcomes + system errors
        ↓
evaluation report
        ↓
safe bounded policy update
```

## Modules

```text
src/policy/policy.py       stable policy(context) action selection
src/policy/logging.py      ignored local context/action/feedback/state logs
src/policy/feedback.py     human, delayed-outcome, and system-error feedback
src/policy/evaluation.py   reward, latency, and robustness reports
src/policy/training.py     offline training and bounded safe updates
src/policy/deployment.py   shadow/assist/partial deployment loop
policy_run.py              CLI smoke test
```

## Policy

`policy(context)` returns:

- query selection;
- candidate prioritization;
- reason codes;
- deployment effect;
- guardrails;
- policy version.

The policy uses bounded, interpretable weights over:

- historical query reward;
- candidate score;
- concept confidence;
- predictive risk;
- self-play reward signal;
- robustness/exploration priority;
- human-feedback bonus.

## Deployment Modes

```text
shadow  -> record-only, no workflow impact
assist  -> suggestion-only, human decides
partial -> limited metadata routing, human final judgment required
```

`partial` mode is still not a production detector. It may route metadata-only candidate records into a review queue, but it may not collect external data, label scam, enforce, warn, or take down.

## Logging

Generated policy logs are ignored by git:

```text
data/policy/context_action_log.jsonl
data/policy/feedback_log.jsonl
data/policy/evaluation_reports.jsonl
data/policy/policy_state.json
```

Each decision log stores:

- sanitized context;
- action;
- outcome;
- reward;
- `raw_source_included: false`.

## Feedback

The feedback layer accepts:

- human labels;
- review minutes;
- delayed outcomes;
- system errors.

Reward is bounded and shaped from reviewer-hour yield, delayed validation, and error penalties. Feedback does not override human judgment and does not create legal or enforcement labels.

## Offline Learning

`train_policy(logs)` updates weights from past metadata logs.

`update_policy(new_data)` applies a safe update with:

- bounded per-weight movement;
- reduced learning rate when recent reward drops;
- no sudden policy shift;
- persisted state for auditability.

Self-play priorities can be converted into training signals, but they are treated as robustness/exploration pressure, not real-world ground truth.

## Evaluation

`evaluate_policy(logs)` reports:

- reward per reviewer hour;
- detection latency;
- robustness;
- system error count;
- deployment-mode counts.

## Usage

```bash
python3 policy_run.py --mode shadow --rounds 5 --reset --train-first
python3 policy_run.py --mode assist --rounds 5 --train-first
python3 policy_run.py --mode partial --rounds 5 --train-first
```

The CLI uses metadata-only local contexts and synthetic feedback for smoke testing unless a governed caller supplies real metadata feedback.

Synthetic sample result on 2026-05-05:

```text
mode=shadow decisions=5 reward_per_reviewer_hour=8.265 latency=1.0 robustness=0.927
policy_version=3 training_examples=14
```

This demonstrates policy-loop mechanics only. It is not real-world deployment evidence.

## Boundary Rules

- Keep all logs metadata-only.
- Do not store raw posts, screenshots, browser exports, credentials, or personal data.
- Do not connect live Threads or Meta collection without a later governance decision.
- Do not let policy output make final scam determinations.
- Do not automate enforcement, public warnings, takedowns, legal conclusions, or production detector claims.
- Prefer stability over rapid reward chasing.
