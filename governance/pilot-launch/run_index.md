# Pilot Run Index

This index is repo-safe. It does not contain raw Threads text, raw URLs, handles, screenshots, HTML, browser/session artifacts, contact IDs, stock names, stock codes, price values, or stakeholder case IDs.

## Scope

| Field | Value |
|---|---|
| Dataset | `threads_pilot_v1_2026-05` |
| Checkpoint synthesized here | 42 records, ending at `threads_pilot_v1_0042` |
| Latest local work visible in tree | items `0043` through `0045` also exist as post-checkpoint work, but are not part of the 42-record checkpoint synthesis |
| Next authorized prospective tranche | Option A run `0038`, items `0046-0055`, at most 20 candidates reviewed and 10 selected |
| Raw evidence location | controlled store only |
| Review posture | high-recall research triage, not legal determination or production enforcement |

## Run-Type Legend

| Type | Meaning |
|---|---|
| `crawler` | Controlled crawler or browser-rendered candidate-finding experiment. |
| `risk-probe` | Bounded seed-matrix experiment to test whether higher-risk candidates can be found. |
| `browser-session` | Approved browser/session-aware access path preparation or execution. |
| `confirmed-pointer` | Stakeholder/CIB/project-owner supplied confirmed pointer captured one item at a time. |
| `account-source` | Approved account-level source sample used for candidate discovery or style context. |
| `hard-negative` | Confirmed non-scam warning or comparator used to protect against false positives. |

## Operational Run Index

| Run | Type | Run record | Evaluation note | Selected item(s) | Validation / outcome | Decision or implication |
|---|---|---|---|---|---|---|
| `0001` | crawler | `threads_pilot_v1_2026-05_controlled_crawler_run_record_0001.md` | `0015-controlled-crawler-rehearsal-run-0001.md` | none | no item built; build correctly blocked | Static fetch path did not produce extractable item evidence. |
| `0002` | browser-session | `threads_pilot_v1_2026-05_controlled_crawler_run_record_0002.md` | `0016-controlled-browser-rehearsal-run-0002.md` | `0001` | strict-valid one-item rehearsal | Allowed first 10-item checkpoint with limits. |
| `0003` | browser-session | `threads_pilot_v1_2026-05_checkpoint_browser_run_record_0003.md` | `0018-first-10-item-checkpoint-result.md` | `0001-0010` | 10 records strict-valid | `continue_with_limits`; sample skewed low-risk/text-only. |
| `0004` | browser-session | `threads_pilot_v1_2026-05_limited_extension_run_record_0004.md` | `0019-first-15-item-limited-extension-result.md` | `0011-0015` | 15 records strict-valid | Continue only to source-strategy/risk-probe design. |
| `0005` | risk-probe | `threads_pilot_v1_2026-05_risk_probe_run_record_0005.md` | `0021-risk-probe-run-0005-result.md` | none | no accepted item | Topic-only seeds were insufficient. |
| `0006` | risk-probe | `threads_pilot_v1_2026-05_risk_probe_run_record_0006.md` | `0022-risk-probe-run-0006-result.md` | none | no accepted item | Public search path still did not expose item content. |
| `0007` | browser-session | `threads_pilot_v1_2026-05_access_path_review_run_record_0007.md` | `0023-access-path-review-run-0007-result.md` | none | existing 15-record aggregate remained strict-valid | Required approved browser storage-state or API/session-aware path before item 16. |
| `0008` | browser-session | `threads_pilot_v1_2026-05_access_path_preparation_run_record_0008.md` | `0024-access-path-preparation-run-0008-result.md` | none | existing aggregate remained strict-valid | Prepared access-path tooling; readiness still required real approved artifact. |
| `0009` | browser-session | `threads_pilot_v1_2026-05_browser_session_execution_run_record_0009.md` | `0025-browser-session-run-0009-result.md` | `0016` | strict-valid one item | Item `0016` second-review result: `non_scam` / `low`. |
| `0010` | browser-session | `threads_pilot_v1_2026-05_browser_session_limited_extension_run_record_0010.md` | `0027-run-0010-method-review.md` | none | no item built | Paused for method review before more item `0017` attempts. |
| `0011` | browser-session | `threads_pilot_v1_2026-05_method_revision_run_record_0011.md` | `0028-run-0011-method-revision-start.md` | none | design/start record | Revised method rather than extending failed path. |
| `0012` | browser-session | `threads_pilot_v1_2026-05_evidence_path_design_run_record_0012.md` | `0032-run-0012-evidence-path-design-start.md` | none | local aggregate remained strict-valid | Opened scoped execution design. |
| `0013` | browser-session | `threads_pilot_v1_2026-05_scoped_evidence_execution_run_record_0013.md` | `0034-run-0013-method-review.md` | method trace only | no accepted item | Stopped item `0017` extension; no reviewable candidate. |
| `0015` | browser-session | `threads_pilot_v1_2026-05_evidence_expansion_run_record_0015.md` | `0039-checkpoint-0023-interpretation.md` | `0018-0023` | 23 records strict-valid | Link/contact/reply evidence improved, but still no scam/high-risk labels. |
| `0016` | browser-session | `threads_pilot_v1_2026-05_reply_aware_recall_run_record_0016.md` | `0044-checkpoint-0027-interpretation.md` | `0024-0027` | 27 records strict-valid | Better false-positive pressure; still no final scam/high-risk records. |
| `0017` | confirmed-pointer | `threads_pilot_v1_2026-05_targeted_exemplar_intake_record_0017.md` | `0047-targeted-exemplar-0028-result.md` | `0028` | 28 records strict-valid | Targeted confirmed-pointer intake became high-yield. |
| `0018-0024` | confirmed-pointer | item run records `0028-0034` | evaluation notes `0047-0053` | `0028-0034` | all strict-valid | Confirmed-pointer method created first scam/high-risk evidence families. |
| `0025-0026` | account-source | account source run records `0025-0026` | `0054-account-source-0001-result.md`, `0055-account-source-0002-result.md` | account samples only | repo-safe context only | Account-level samples support candidate discovery, not standalone labels. |
| `0027-0033` | confirmed-pointer | item run records `0035-0041` | evaluation notes `0056-0062` | `0035-0041` | all strict-valid | Additional scam/high-risk evidence families added. |
| `0034` | hard-negative | `threads_pilot_v1_2026-05_item_0042_full_thread_capture_run_record_0034.md` | `0063-confirmed-non-scam-warning-0042-result.md` | `0042` | 42 records strict-valid | Anti-scam warning hard negative recorded. |
| `0038` | browser-session | `threads_pilot_v1_2026-05_option_a_limited_browser_tranche_run_record_0038.md` | pending | prospective `0046-0055` | open, not executed | Option A selected: primary approved browser-session capture; supplemental confirmed pointers allowed; 20-candidate and 10-selected caps. |

## Confirmed Pointer And Hard-Negative Item Index

| Item | Type | Run record | Evaluation note | Decision log | Label | Risk | Evidence family | Validation | Baseline outcome |
|---|---|---|---|---|---|---|---|---|---|
| `0028` | confirmed-pointer | `threads_pilot_v1_2026-05_item_0028_full_thread_capture_run_record_0018.md` | `0047-targeted-exemplar-0028-result.md` | `0035-record-cib-confirmed-implicit-dm-funnel-rule.md` | `scam` | `high` | `implicit_dm_contact_request` | pass, 28 records | scam-like/high |
| `0029` | confirmed-pointer | `threads_pilot_v1_2026-05_item_0029_full_thread_capture_run_record_0019.md` | `0048-confirmed-pointer-0029-result.md` | `0036-adopt-confirmed-scam-pointer-intake-method.md` | `scam` | `high` | `high_fee_course_or_membership_funnel` | pass, 29 records | scam-like/high |
| `0030` | confirmed-pointer | `threads_pilot_v1_2026-05_item_0030_full_thread_capture_run_record_0020.md` | `0049-confirmed-pointer-0030-result.md` | `0039-record-comment-code-lead-magnet-rule.md` | `scam` | `high` | `comment_code_lead_magnet` | pass, 30 records | scam-like/high |
| `0031` | confirmed-pointer | `threads_pilot_v1_2026-05_item_0031_full_thread_capture_run_record_0021.md` | `0050-confirmed-pointer-0031-result.md` | `0040-record-past-performance-profit-proof-rule.md` | `scam` | `high` | `past_performance_profit_proof` | pass, 31 records | scam-like/high |
| `0032` | confirmed-pointer | `threads_pilot_v1_2026-05_item_0032_full_thread_capture_run_record_0022.md` | `0051-confirmed-pointer-0032-result.md` | `0041-record-stock-rescue-group-funnel-rule.md` | `scam` | `high` | `stock_rescue_group_funnel` | pass, 32 records | scam-like/high |
| `0033` | confirmed-pointer | `threads_pilot_v1_2026-05_item_0033_full_thread_capture_run_record_0023.md` | `0052-confirmed-pointer-0033-result.md` | `0042-record-individual-stock-advice-reply-funnel-rule.md` | `scam` | `high` | `individual_stock_advice_reply_funnel` | pass, 33 records | scam-like/high |
| `0034` | confirmed-pointer | `threads_pilot_v1_2026-05_item_0034_full_thread_capture_run_record_0024.md` | `0053-confirmed-pointer-0034-result.md` | `0043-record-market-direction-herding-chorus-rule.md` | `scam` | `high` | `market_direction_herding_chorus` | pass, 34 records | scam-like/high |
| `0035` | confirmed-pointer | `threads_pilot_v1_2026-05_item_0035_full_thread_capture_run_record_0027.md` | `0056-confirmed-pointer-0035-result.md` | `0046-record-institutional-flow-authority-lure-rule.md` | `scam` | `high` | `institutional_flow_authority_lure` | pass, 35 records | scam-like/high |
| `0036` | confirmed-pointer | `threads_pilot_v1_2026-05_item_0036_full_thread_capture_run_record_0028.md` | `0057-confirmed-pointer-0036-result.md` | `0048-record-reply-impersonation-contact-hijack-rule.md` | `scam` | `high` | `reply_impersonation_contact_hijack` | pass, 36 records | scam-like/high |
| `0037` | confirmed-pointer | `threads_pilot_v1_2026-05_item_0037_full_thread_capture_run_record_0029.md` | `0058-confirmed-pointer-0037-result.md` | `0049-record-stock-pick-playbook-keyword-funnel-rule.md` | `scam` | `high` | `stock_pick_playbook_keyword_funnel` | pass, 37 records | scam-like/high |
| `0038` | confirmed-pointer | `threads_pilot_v1_2026-05_item_0038_full_thread_capture_run_record_0030.md` | `0059-confirmed-pointer-0038-result.md` | `0050-record-trapped-position-dm-playbook-reply-rule.md` | `scam` | `high` | `trapped_position_dm_playbook_reply` | pass, 38 records | scam-like/high |
| `0039` | confirmed-pointer | `threads_pilot_v1_2026-05_item_0039_full_thread_capture_run_record_0031.md` | `0060-confirmed-pointer-0039-result.md` | `0051-record-lifestyle-trust-market-reassurance-funnel-rule.md` | `scam` | `high` | `lifestyle_trust_market_reassurance_funnel` | pass, 39 records | scam-like/high |
| `0040` | confirmed-pointer | `threads_pilot_v1_2026-05_item_0040_full_thread_capture_run_record_0032.md` | `0061-confirmed-pointer-0040-result.md` | `0052-record-dark-horse-stock-target-price-dm-funnel-rule.md` | `scam` | `high` | `dark_horse_stock_target_price_dm_funnel` | pass, 40 records | scam-like/high |
| `0041` | confirmed-pointer | `threads_pilot_v1_2026-05_item_0041_full_thread_capture_run_record_0033.md` | `0062-confirmed-pointer-0041-result.md` | `0053-record-mass-stock-command-list-group-funnel-rule.md` | `scam` | `high` | `mass_stock_command_list_group_funnel` | pass, 41 records | scam-like/high |
| `0042` | hard-negative | `threads_pilot_v1_2026-05_item_0042_full_thread_capture_run_record_0034.md` | `0063-confirmed-non-scam-warning-0042-result.md` | `0054-record-anti-scam-warning-hard-negative-boundary.md` | `non_scam` | `low` | anti-scam warning hard negative | pass, 42 records | not-scam-like/low |

## Checkpoint 0042 Aggregate

| Metric | Value |
|---|---:|
| Total records | 42 |
| `scam` | 14 |
| `non_scam` | 22 |
| `uncertain` | 5 |
| `insufficient_evidence` | 1 |
| `high` risk | 14 |
| `medium` risk | 4 |
| `low` risk | 24 |
| Strict validation errors | 0 |
| Strict validation warnings | 0 |
| Baseline precision | 0.700 |
| Baseline recall | 1.000 |
| Baseline F1 | 0.824 |
| Baseline false positives | 6 |
| Baseline false negatives | 0 |

## Post-Checkpoint Work Not Included In 0042 Synthesis

Items `0043`, `0044`, and `0045` were captured after the 42-record checkpoint and should remain post-checkpoint work until a later checkpoint synthesis explicitly includes them. Stakeholder Option A now opens a prospective item `0046-0055` tranche under run `0038`; the new run does not retroactively consume the `0043-0045` post-checkpoint items.

| Item | Evaluation note | Decision log | Status |
|---|---|---|---|
| `0043` | `0064-confirmed-pointer-0043-result.md` | `0055-record-coded-animal-stock-limit-up-group-funnel-rule.md` | post-checkpoint, strict-valid locally |
| `0044` | `0065-confirmed-pointer-0044-result.md` | `0056-record-trading-rules-wealth-authority-follow-gate-rule.md` | post-checkpoint, strict-valid locally |
| `0045` | `0066-confirmed-pointer-0045-result.md` | `0057-record-brand-patent-extreme-roi-contact-funnel-rule.md` | post-checkpoint, strict-valid locally |
