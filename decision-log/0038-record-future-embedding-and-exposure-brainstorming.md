# Decision 0038: Record Future Embedding And Exposure Brainstorming

## Date

2026-04-25

## Status

Accepted as deferred brainstorming

## Decision

Record two future research ideas without adding them to the active pilot scope:

1. embedding-based scam-spectrum analysis after the confirmed scam-pointer dataset is large enough;
2. potential exposure or possible victim-risk study around users who reshare, reply to, or otherwise interact with confirmed scam posts.

## Rationale

The ideas may become useful after enough governed examples exist. Embeddings could help discover scam families and boundary cases. Interaction data could support exposure or prevention research.

Both ideas also carry high overreach risk. Embedding similarity is not proof of scam. Interaction with a scam post is not proof of victimization.

## Boundaries

- No immediate collection is authorized by this decision.
- No embedding model experiment is authorized until a later decision record defines data, model, storage, redaction, and evaluation limits.
- No interaction-level user dataset is authorized until stakeholders approve user-identifier handling, retention, pseudonymization, access control, and ethics/legal constraints.
- Use "potential exposure" or "possible victim-risk" language unless independent evidence supports stronger victim-status claims.
- Do not store raw user identifiers, profile graphs, or interaction graphs in git.

## Files Updated

- `docs/53-future-research-brainstorming.md`
- `docs/09-phase-1-experiment-plan.md`
- `docs/16-open-questions-for-stakeholders.md`
- `docs/13-risk-register.md`

## Next Action

Keep these ideas parked until the confirmed scam-pointer dataset and rule library are mature enough to justify a separate method decision.
