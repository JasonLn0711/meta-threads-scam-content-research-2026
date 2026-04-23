# Source Directory

Reserved for small research prototype code once experiments justify implementation.

The first phase should prioritize:

1. Research framing
2. Data contracts
3. Annotation guidance
4. Experiment logs
5. Small, inspectable baselines

Avoid building a web app, dashboard, database product, or heavy ML platform during phase 1.

## Current Prototype Code

```text
baselines/    Modular transparent rule baseline for phase-1 Threads triage
data_collection/ Manual-only record-building and governance checks; no scraping or network access
evaluation/   Binary, triage, and error-analysis helpers for local baseline runs
review/       Local-only reviewer packet builders for item-level baseline inspection
```

The primary API is:

```python
from src.baselines.rule_based import predict_item, predict_batch
from src.baselines.risk_scoring import load_rule_config
```

The baseline reads local structured records only. It does not collect Threads data, crawl links, inspect profiles, or make enforcement decisions.

Data-collection helpers only structure manually supplied fields into schema-valid records and local collection-log rows. They do not fetch Threads pages, crawl links, capture landing pages, or authorize collection.

Evaluation helpers also include calibration and pilot-synthesis modules that produce aggregate-only outputs for decision memos.
Review helpers produce item-level Markdown packets for local reviewer inspection; do not commit real packet outputs that contain raw evidence.
