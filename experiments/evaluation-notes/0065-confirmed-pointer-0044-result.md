# Confirmed Pointer 0044 Result

## Purpose

Record the repo-safe result for the next confirmed Threads scam pointer.

This note contains no raw Threads content, full item URL, raw handle, screenshot, raw reply text, credential, browser artifact, storage-state material, raw storage path, or stakeholder case ID.

## Result

| Field | Value |
|---|---|
| Item ID | `threads_pilot_v1_0044` |
| Source path | confirmed scam pointer intake |
| Capture run | `CAPTURE-THREADS-PILOT-V1-0044-FULL-THREAD` |
| Decision link | `0056-record-trading-rules-wealth-authority-follow-gate-rule` |
| Label after second review | `scam` |
| Risk after second review | `high` |
| Evidence family | `trading_rules_wealth_authority_follow_gate` |
| Strict validation | pass: `manual_record_0044.json` and 44-record aggregate, 0 errors, 0 warnings |

## Controlled Full-Thread Capture

The controlled browser run preserved the approved browser-rendered raw evidence in the controlled store:

- source pointer
- browser-rendered body text
- browser-rendered HTML
- screenshot
- visible text blocks
- href list

The accepted capture recorded 37 `[dir='auto']` text blocks, 92 visible text blocks, and 26 hrefs. The `article` selector returned 0, so the preserved raw evidence relies on body text, visible text blocks, HTML, and screenshot rather than `article` nodes.

## Interpretation

This case adds a trading-rules wealth-authority follow-gate family. The public thread uses wealth and long-experience authority to make a compact trading-rule checklist feel credible, then uses an action gate such as like, follow, `+1`, or get-on-board language to move interested readers toward follow-up stock help or buy-timing guidance.

The rule should remain narrow: ordinary stock education, risk-discipline checklists, and harmless engagement prompts are not scam-like by themselves. The risk signal is the convergence of investment authority, simple rule/playbook framing, and action-gated follow-up.

## Validation

Commands run after record build:

```bash
python3 scripts/validate_thread_dataset.py data/interim/manual_record_0044.json --strict
python3 scripts/validate_thread_dataset.py data/interim/manual_records_checkpoint_0044.jsonl --strict
python3 scripts/audit_thread_dataset.py data/interim/manual_records_checkpoint_0044.jsonl
.venv/bin/python scripts/run_rule_baseline.py data/interim/manual_records_checkpoint_0044.jsonl --variant all --run-name checkpoint-0044-trading-rules-wealth-authority-smoke-v1 --output-dir experiments/baselines/outputs
```

Results:

- item validation: 1 checked, 0 errors, 0 warnings
- aggregate validation: 44 checked, 0 errors, 0 warnings
- aggregate labels: 22 `non_scam`, 5 `uncertain`, 16 `scam`, 1 `insufficient_evidence`
- aggregate risk: 24 `low`, 4 `medium`, 16 `high`
- baseline all-signal smoke v1: precision 0.727, recall 1.000, F1 0.842, 6 false positives, 0 false negatives
- item `0044` baseline prediction: `scam_like` / `high`
- item `0044` baseline reasons include `TRADING_RULES_WEALTH_AUTHORITY_FOLLOW_GATE`, `INDIVIDUAL_STOCK_ADVICE_REPLY_FUNNEL`, `MENTOR_COPYTRADE_LANGUAGE`, `REPLY_FUNNEL_PATTERN`, and `MULTI_SIGNAL_CONVERGENCE`
- item `0044` total score: 16.5; high guardrail passed
