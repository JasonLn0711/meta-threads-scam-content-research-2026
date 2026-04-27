# Pilot Run Index

This index is repo-safe. It does not contain raw Threads text, raw URLs, handles, screenshots, HTML, browser/session artifacts, contact IDs, stock names, stock codes, price values, or stakeholder case IDs.

## Scope

| Field | Value |
|---|---|
| Dataset | `threads_pilot_v1_2026-05` |
| Checkpoint synthesized here | 42 records, ending at `threads_pilot_v1_0042` |
| Latest checkpoint synthesis | 78 records, ending at `threads_pilot_v1_0081`; CIB-approved research checkpoint |
| Latest local work visible in tree | run `0054`; Track B Day 1 batch `0001` surfaced 6 checkpoint-derived seed replay candidates; 0 reviewed and 0 accepted so far |
| Current collection gate | Track B may begin under decision `0122` locked caps, daily stop-rule checks, strict validation, raw-evidence exclusion, and aggregate-only reporting |
| Next authorized prospective tranche | Track B capped live method test only; no overflow queue and no item `0082` |
| Next stakeholder request | none; next output is Track B human review of batch `0001` or a pause/zero-review note |
| Next intake scaffold | run `0054` batch `0001` review ledger; no item `0082`; no broad expansion |
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
| `capped-method-test` | Authorized candidate-discovery method test with fixed caps, human review, stop rules, and aggregate-only reporting. |

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
| `0038` | browser-session | `threads_pilot_v1_2026-05_option_a_limited_browser_tranche_run_record_0038.md` | `0067-option-a-run-0038-result.md` | `0046-0055` | 55 records strict-valid | Option A completed and closed after 20 candidates reviewed and 10 selected; no final scam/high-risk items added. |
| `0039` | confirmed-pointer + browser-session supplement | `threads_pilot_v1_2026-05_aggressive_prospective_tranche_run_record_0039.md` | `0069-run-0039-preflight.md`; `0070-run-0039-aggressive-tranche-result.md` | `0056-0075` local candidate entries | local 75-record candidate aggregate strict-valid; no official checkpoint promoted | Run closed after 50 candidates reviewed and 20 local candidate entries; second review found 11 uncertain and 9 duplicate/excluded, with 0 new final scam/high-risk items. |
| `0040` | confirmed-pointer | `threads_pilot_v1_2026-05_post_run_0039_confirmed_pointer_intake_record_0040.md` | `0071-run-0040-receipt-readiness.md` | `0076-0080` prospective only | receipt-ready; waiting for pointer delivery; no item built | Intake scaffold is ready for 3-5 confirmed pointers, maximum 5 before checkpoint; collection has not started. |
| `0041` | browser-session | `threads_pilot_v1_2026-05_dedupe_first_browser_candidate_quality_run_record_0041.md` | `0072-run-0041-preflight.md`; `0073-run-0041-result.md` | none | completed; no candidates extracted; no item built | Article-based browser-search extractor produced no candidates across 12 seeds; next browser method must revise extraction before another run. |
| `0042` | browser-session diagnostic | `threads_pilot_v1_2026-05_browser_rendering_diagnostic_run_record_0042.md` | `0074-run-0042-browser-rendering-diagnostic-result.md` | none | completed; no item built | Diagnostic found 0 article elements, 21 post-like hrefs, and 110 candidate body lines; next method should use body-line segmentation plus post-href discovery. |
| `0043` | browser-session | `threads_pilot_v1_2026-05_diverse_body_line_post_href_candidate_run_record_0043.md` | `0075-run-0043-diverse-body-line-post-href-result.md` | none | completed; no item built | Diverse body-line/post-href method reached 60 reviewed candidates after 10 seeds, with 51 dedupe-pass candidates and 24 quality-review selections; no manual entries or official promotion. |
| `0043-review` | browser-session promotion review | `threads_pilot_v1_2026-05_run_0043_promotion_review_record.md` | `0077-run-0043-promotion-review-first-pass-result.md` | `0076` prospective only | first pass completed; no item built | All 24 candidates failed source-context, reply-context, and evidence-attribution gates; next step is narrow source-linkage/full-thread capture before any promotion. |
| `0044` | browser-session | `threads_pilot_v1_2026-05_aggressive_dedupe_first_browser_candidate_quality_run_record_0044.md` | `0076-run-0044-aggressive-dedupe-first-browser-candidate-quality-result.md` | none | completed; no item built | Aggressive controlled-store-only candidate-quality test reviewed 200 candidates, found 190 dedupe-pass, selected 180 local traces, and completed 131 context-ready attempts; no manual entries or official promotion. |
| `0045` | browser-session follow-up | `threads_pilot_v1_2026-05_source_linkage_follow_up_run_record_0045.md` | `0078-run-0045-source-linkage-follow-up-result.md` | `0076` prospective only | completed; no item built | Attempted 5 run `0043` candidates; 2 became source-linkage-ready and second-review-eligible; no manual entries or official promotion. |
| `0045-build` | browser-session hard-negative build | `threads_pilot_v1_2026-05_source_linkage_follow_up_run_record_0045.md` | `0079-manual-entry-0076-hard-negative-build-result.md` | `0076` local redacted hard negative | strict-valid local item | Second review selected one source-linked candidate as `non_scam` / `low`; local `manual_entry_0076` and `manual_record_0076` built with 0 validation errors and warnings. |
| `0046` | confirmed-pointer | `threads_pilot_v1_2026-05_item_0077_confirmed_pointer_intake_run_record_0046.md` | `0081-confirmed-pointer-0077-preliminary-rule-result.md` | `0077` prospective only | preliminary top-level rule extracted; no manual entry built | Single stakeholder-confirmed pointer opened under decision `0097`; full reply/comment capture remains pending before promotion. |
| `0047` | confirmed-pointer | `threads_pilot_v1_2026-05_item_0078_confirmed_pointer_intake_run_record_0047.md` | `0082-confirmed-pointer-0078-preliminary-rule-result.md` | `0078` prospective only | preliminary top-level rule extracted; no manual entry built | Single stakeholder-confirmed pointer opened under decision `0098`; full reply/comment capture remains pending before promotion. |
| `0048` | confirmed-pointer | `threads_pilot_v1_2026-05_item_0079_confirmed_pointer_intake_run_record_0048.md` | `0083-confirmed-pointer-0079-preliminary-rule-result.md` | `0079` prospective only | preliminary top-level rule extracted; no manual entry built | Single stakeholder-confirmed pointer opened under decision `0099`; full reply/comment capture remains pending before promotion. |
| `0049` | confirmed-pointer work order | `threads_pilot_v1_2026-05_items_0077_0079_full_thread_capture_work_order_0049.md` | `0084-confirmed-pointer-0077-0079-mini-tranche-synthesis.md` | `0077-0079` prospective only | work order opened; no manual entries built | Decision `0100` authorizes controlled full-thread/reply capture attempts for existing items `0077-0079` only; no item `0080` or broader tranche. |
| `0050` | second-review work order | `threads_pilot_v1_2026-05_existing_ambiguous_medium_second_review_work_order_0050.md` | `0085-existing-ambiguous-medium-review-queue.md`; `0088-existing-ambiguous-medium-second-review-synthesis.md` | existing items only | completed; local 78-record aggregate strict-valid after adjudication | Decision `0101` authorized second review of 35 existing checkpoint 0076 `uncertain`, `insufficient_evidence`, or `medium` risk records using existing redacted records only; next decision is checkpoint packaging, not new collection. |
| `0051` | confirmed-pointer | `threads_pilot_v1_2026-05_item_0080_full_thread_capture_run_record_0051.md` | `0086-confirmed-pointer-0080-result.md` | `0080` | strict-valid local item; 77-record local aggregate strict-valid | Decision `0102` authorizes one supplied CIB/project-owner confirmed pointer only; no item `0081` or broader tranche. |
| `0052` | confirmed-pointer | `threads_pilot_v1_2026-05_item_0081_full_thread_capture_run_record_0052.md` | `0087-confirmed-pointer-0081-result.md` | `0081` | strict-valid local item; 78-record local aggregate strict-valid | Decision `0104` authorizes one supplied CIB/project-owner confirmed pointer only; no item `0082` or broader tranche. |
| `0053` | checkpoint synthesis | `run_index.md` | `0088-existing-ambiguous-medium-second-review-synthesis.md`; `0089-checkpoint-0081-cib-approved-synthesis.md` | `0001-0081` local aggregate | CIB-approved 78-record research checkpoint; strict-valid | Decision `0105` approves checkpoint `0081` synthesis; next step is reviewer-facing package/report addendum, not new collection. |
| `0054` | capped-method-test | `threads_pilot_v1_2026-05_track_b_capped_method_test_run_record_0054.md` | `0090-track-b-day-0-start-record.md`; `0091-track-b-day-1-source-arm-intake-start.md`; `0092-track-b-day-1-batch-0001-checkpoint-seed-replay.md` | `track_b_day_1_batch_0001_checkpoint_seed_replay` | Day 0 gate confirmed; Day 1 source-arm intake started; batch `0001` surfaced 6 checkpoint-derived seed replay candidates; 0 reviewed, 0 accepted records | Decision `0125` records first surfaced candidate batch under locked caps, not item `0082`; next step is Track B human review. |

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
| `0076` | hard-negative | `threads_pilot_v1_2026-05_source_linkage_follow_up_run_record_0045.md` | `0079-manual-entry-0076-hard-negative-build-result.md` | `0092-promote-run-0045-hard-negative-as-manual-entry-0076.md` | `non_scam` | `low` | anti-scam warning / victim-prevention hard negative | pass, one local record | not-scam-like/low |
| `0080` | confirmed-pointer | `threads_pilot_v1_2026-05_item_0080_full_thread_capture_run_record_0051.md` | `0086-confirmed-pointer-0080-result.md` | `0102-authorize-single-confirmed-pointer-0080-intake.md` | `scam` | `high` | past-performance profit proof plus no-fee wealth-authority trust funnel | pass, 77 local records | checkpoint 0081 baseline: scam-like/high |
| `0081` | confirmed-pointer | `threads_pilot_v1_2026-05_item_0081_full_thread_capture_run_record_0052.md` | `0087-confirmed-pointer-0081-result.md` | `0104-authorize-single-confirmed-pointer-0081-intake.md` | `scam` | `high` | top-level trust-building plus reply-level contact-hijack/private-group funnel | pass, 78 local records | checkpoint 0081 baseline: scam-like/high |

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

Items `0043`, `0044`, and `0045` were captured after the 42-record checkpoint and are now included in the 55-record checkpoint synthesis. They remain listed here to preserve the transition from checkpoint 0042 to checkpoint 0055.

| Item | Evaluation note | Decision log | Status |
|---|---|---|---|
| `0043` | `0064-confirmed-pointer-0043-result.md` | `0055-record-coded-animal-stock-limit-up-group-funnel-rule.md` | included in 55-record synthesis |
| `0044` | `0065-confirmed-pointer-0044-result.md` | `0056-record-trading-rules-wealth-authority-follow-gate-rule.md` | included in 55-record synthesis |
| `0045` | `0066-confirmed-pointer-0045-result.md` | `0057-record-brand-patent-extreme-roi-contact-funnel-rule.md` | included in 55-record synthesis |

## Option A Run 0038 Post-Checkpoint Tranche

Items `0046-0055` were selected under stakeholder Option A run `0038`. They are strict-valid, second-reviewed, and included in the 55-record checkpoint synthesis.

| Range | Evaluation note | Decision log | Status |
|---|---|---|---|
| `0046-0055` | `0067-option-a-run-0038-result.md` | `0060-close-option-a-run-0038-after-caps.md` | post-checkpoint, 55-record aggregate strict-valid; run closed after caps |

## Checkpoint 0055 Aggregate

| Metric | Value |
|---|---:|
| Total records | 55 |
| `scam` | 17 |
| `non_scam` | 23 |
| `uncertain` | 9 |
| `insufficient_evidence` | 6 |
| `high` risk | 17 |
| `medium` risk | 7 |
| `low` risk | 31 |
| Strict validation errors | 0 |
| Strict validation warnings | 0 |
| Baseline precision | 0.708 |
| Baseline recall | 1.000 |
| Baseline F1 | 0.829 |
| Baseline false positives | 7 |
| Baseline false negatives | 0 |

Synthesis: `experiments/evaluation-notes/0068-checkpoint-0055-synthesis.md`.

## Current Gate After Run 0039

The checkpoint 0055 report package is complete. `checkpoint_0055_stakeholder_decision_record.md` records `C2`.

Current state:

- run `0039` completed and closed;
- local candidate entries `0056-0075` were strict-valid but not promoted into a new official checkpoint;
- second review found 11 `uncertain` entries and 9 duplicate/excluded entries;
- no new final scam/high-risk example was added by the aggressive browser-session supplement;
- the 55-record checkpoint package is approved as the current CIB/165-facing evidence-system checkpoint;
- future selected items must complete controlled capture, redacted record build, strict validation, and second review before they count.

The next preferred path is confirmed-pointer intake. If browser-session search is used again, it must pass `docs/53-dedupe-first-full-thread-ready-gate.md` before candidate promotion.

Stakeholder request artifact: `reports/post-run-0039-confirmed-pointer-request.md`.

Confirmed-pointer intake scaffold: `governance/pilot-launch/threads_pilot_v1_2026-05_post_run_0039_confirmed_pointer_intake_record_0040.md`.

Dedupe-first browser candidate quality test result: run `0041` closed with no extracted candidates. Do not repeat the same article-based extraction path with higher caps.
