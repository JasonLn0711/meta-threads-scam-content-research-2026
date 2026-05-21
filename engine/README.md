# v2 Engine

The v2 engine is a metadata-only research operating system.

```text
engine/sparse/             primary explainable SVS, sparse clustering, signal ranking,
                           and contrast-aware reviewer routing
engine/embedding/          discovery-only cosine similarity and clustering
engine/discrepancy/        sparse-vs-embedding disagreement reports
engine/feature_discovery/  human-reviewed emergent feature proposals
```

The sparse engine is the only decision-support layer. Contrast-aware routing is
for reviewer-effort allocation, not automated labeling. The embedding engine is
exploratory only and must not write labels, enforcement recommendations,
sparse-feature changes, or final scam determinations.
