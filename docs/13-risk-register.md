# Risk Register

## Current Risk Posture

As of `2026-04-23`, tooling risk has been reduced by the synthetic workflow dry run and stakeholder approval has been recorded for bounded pilot launch preparation. The active blocker is now controlled launch detail: no real Threads evidence should be collected until exact source, storage, access, retention, and redaction limits are written outside git.

| Risk | Why it matters | Likelihood | Impact | Mitigation |
|---|---|---:|---:|---|
| Controlled launch-detail risk | Source, storage, access, retention, or redaction details may remain incomplete or too sensitive for git. | High | High | Complete controlled launch record outside git before first item. |
| Data access risk | Threads data access may be limited or legally constrained. | Medium | High | Use only approved manual/stakeholder samples; no automation. |
| Annotation inconsistency | Reviewers may disagree on ambiguous finance or marketing content. | High | High | Use clear labels, second review, disagreement logs, and guideline revisions. |
| Legal and ethical risk | Mishandled data could expose personal information or investigative material. | Medium | High | Follow data governance, minimize personal data, store raw material outside git. |
| Scope creep | Project may expand into all Meta platforms, video, or production tooling. | High | High | Use decision logs and budget-fit checks before expanding. |
| Overclaiming risk | Research outputs may be mistaken for legal or production conclusions. | Medium | High | Use triage language, uncertainty labels, and explicit disclaimers. |
| Model brittleness | Keyword/rule baselines may fail under wording variation. | High | Medium | Evaluate robustness and treat failures as research findings. |
| Platform change risk | Threads formats, policies, or access paths may change. | Medium | Medium | Keep schema flexible and avoid overfitting to current UI details. |
| False accusation risk | False positives may unfairly characterize benign users or businesses. | Medium | High | Preserve evidence, use human review, avoid public accusations. |
| OCR quality risk | OCR may miss or distort key text, especially in screenshots. | Medium | Medium | Track OCR error cases and require reviewer verification. |
| Link interpretation risk | Legitimate links may be overflagged as suspicious. | High | Medium | Distinguish link presence from maliciousness; avoid crawling without approval. |
| Budget exhaustion | Too many workstreams could consume funds before learning occurs. | Medium | High | Rank work by ROI and stop low-value branches early. |
| Synthetic overconfidence | Dry-run metrics may be mistaken for real-world baseline performance. | Medium | High | Label synthetic dry-run results as workflow QA only; repeat all metrics on authorized pilot data. |

## Review Cadence

Review this register at:

- End of week 1 after report review and pilot authorization decision.
- End of week 2 after the first authorized annotation batch, if approved.
- End of week 4 before deciding the next phase.

Any high-impact risk that becomes active should trigger a decision-log entry.
