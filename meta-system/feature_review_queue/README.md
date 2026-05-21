# Feature Review Queue

Human reviewers use this directory to decide whether emergent feature candidates should be accepted into the sparse schema.

Allowed decisions:

- `pending`
- `accepted`
- `rejected`

Only `accepted` candidates may be promoted into the sparse schema, and promotion must preserve explainability, governance boundaries, and the rule that embeddings never make decisions.
