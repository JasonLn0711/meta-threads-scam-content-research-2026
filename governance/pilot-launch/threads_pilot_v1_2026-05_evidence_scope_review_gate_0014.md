# Evidence-Scope Review Gate 0014

This is the non-sensitive tracked review gate after item 0017 was stopped. It is not a collection run record.

Do not add raw Threads content, screenshots, full item URLs, raw handles, stakeholder case IDs, credentials, cookies, tokens, browser profiles, HAR files, full API responses, exact raw storage paths, access-list details, or sensitive investigative notes to this file. Exact sensitive values remain in the approved controlled location.

## Gate Identity

| Field | Value |
|---|---|
| Gate ID | `EVIDENCE-SCOPE-THREADS-PILOT-V1-0014` |
| Date opened | `2026-04-25` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Collection batch ID | `threads_pilot_v1_2026-05` |
| Prior decision | `0030-require-stakeholder-evidence-scope-review` |
| Prior run | `CRAWL-THREADS-PILOT-V1-0013` |
| Current accepted records | 16 |
| Current excluded traces | 1 item 0017 method-review trace |
| Current gate status | `pending_stakeholder_scope_decision` |
| Collection status | `paused` |
| Item 0018 status | `blocked` |

## Evidence Reviewed

| Artifact | Review status |
|---|---|
| `decision-log/0029-stop-item-0017-extension-after-run-0013.md` | required |
| `experiments/evaluation-notes/0035-pilot-synthesis-after-item-0017-stop.md` | required |
| `docs/51-stakeholder-evidence-expansion-memo.md` | required |
| controlled-store raw/session details | outside git; stakeholder-controlled review only if needed |

## Decision To Record

Choose exactly one outcome:

| Outcome | Meaning | Can collection resume? |
|---|---|---|
| `approve_narrow_expansion` | Stakeholders approve a tightly bounded new evidence-expansion run. | yes, after a new run record defines fields and stop conditions |
| `approve_redacted_stakeholder_examples_only` | Stakeholders provide or approve a small number of already-redacted examples for calibration. | only for those examples under a new intake record |
| `hold_at_16_and_report` | The current tranche stops and the project moves to method reporting. | no |
| `reject_expansion` | No richer evidence collection is approved. | no |

## Scope Questions

| Area | Decision needed | Current status |
|---|---|---|
| Redacted stakeholder exemplars | allowed / not allowed / pending | pending |
| Risk-relevant OCR excerpt | allowed / not allowed / pending | pending |
| Screenshot raw storage | controlled-store only / not allowed / pending | pending |
| Narrow adjacent reply context | allowed / not allowed / pending | pending |
| Visible-link domain/category | allowed / not allowed / pending | pending |
| Full raw URL in git | prohibited | prohibited |
| Redirect or landing-page evidence | allowed / not allowed / pending | pending |
| Profile/account graph review | allowed / not allowed / pending | pending |
| Candidate cap | exact number required before any run | pending |
| Second-review owner | required before any run | pending |
| Counting rule | counts toward pilot / method-only / pending | pending |

## Default Safe Position

If no stakeholder decision is recorded:

- do not open item 0018;
- do not retry item 0017;
- do not collect screenshots, OCR, replies, landing pages, redirect chains, profile context, raw URLs, or broader comments;
- do not treat query terms, aggregate domain counts, or schema-valid excluded traces as accepted research items;
- continue only with repo-safe synthesis, reporting, or governance clarification.

## Approval Record

| Field | Value |
|---|---|
| Stakeholder decision outcome | pending |
| Decision owner | pending |
| Decision date | pending |
| Approved evidence families | pending |
| Approved raw storage category | pending |
| Approved redaction rule | pending |
| Approved review cap | pending |
| Approved second-review owner | pending |
| Approved next artifact | pending |

## Next Action

Obtain and record the stakeholder evidence-scope decision. If the outcome approves a narrow expansion, open a new run record that cites this gate and defines exact allowed fields, raw-storage boundaries, redaction checks, candidate caps, and stop conditions before any collection starts.
