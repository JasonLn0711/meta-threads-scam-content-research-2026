# Adaptive Policy Logs

This directory is for local adaptive policy state and deployment-loop logs.

Tracked:

- `README.md`

Ignored generated files:

- `context_action_log.jsonl`
- `feedback_log.jsonl`
- `evaluation_reports.jsonl`
- `policy_state.json`

Rules:

- Store metadata-only context, action, outcome, and reward records.
- Do not store raw Threads posts, screenshots, personal data, credentials, browser exports, or external collection output.
- `shadow` mode must not affect real workflow.
- `assist` mode may only suggest.
- `partial` mode may only perform limited metadata routing with human final judgment.
- Policy logs are research artifacts, not production detector evidence or enforcement records.
