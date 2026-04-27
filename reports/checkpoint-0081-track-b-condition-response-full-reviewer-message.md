# Reviewer Message: Checkpoint 0081 Track B Condition Response

Subject: Track B Condition Response Request: Checkpoint 0081 Capped Investment-Scam Discovery Method Test

您好，

隨信附上 `checkpoint-0081-track-b-condition-response-full-reviewer-package`。

這不是請求啟動新的無限制蒐集，也不是請求啟動 item `0082`。這次請求的目的，是請您用 repo-safe 方式回覆 Track B capped live method test 是否已經滿足執行前的硬條件，或還有哪些條件必須先補齊。

本研究的 FIRST PRINCIPLE 目標是：

```text
找出一套可以大量、穩定、可審查地發現 Threads 投資詐騙候選貼文 / thread / funnel 的方法。
```

目前 checkpoint `threads_pilot_v1_0081` 已作為 CIB-approved research checkpoint 使用。Track A zero-new-evidence dry run 已完成，沒有新增 evidence，也沒有使用 browser session。Track B 則仍然處於：

```text
conditionally approved but blocked pending hard-condition signoff
```

也就是說，Track B 只有在法律/隱私、CIB/internal owner、technical/governance、controlled-store、reviewer role、validation、reporting、raw-evidence exclusion check 等條件全部明確通過後，才可以開始。

## 請您優先閱讀

請先看：

1. `REVIEWER_README.md`
2. `reports/checkpoint-0081-track-b-condition-response-request.md`
3. `reports/checkpoint-0081-track-b-condition-resolution-tracker.md`
4. `reports/checkpoint-0081-track-b-capped-live-method-test-condition-checklist.md`
5. `reports/checkpoint-0081-track-a-zero-new-evidence-dry-run-report.md`

如果需要完整執行邊界，請看：

1. `reports/checkpoint-0081-final-capped-method-test-authorization-request.md`
2. `reports/checkpoint-0081-final-capped-method-test-execution-sop.md`
3. `reports/checkpoint-0081-final-capped-method-test-legal-privacy-gate-memo.md`
4. `reports/checkpoint-0081-final-capped-method-test-controlled-store-boundary.md`
5. `reports/checkpoint-0081-final-capped-method-test-reviewer-assignment-table.md`
6. `reports/checkpoint-0081-final-capped-method-test-candidate-record-template.md`
7. `reports/checkpoint-0081-final-capped-method-test-stop-rule-incident-template.md`
8. `reports/checkpoint-0081-final-capped-method-test-aggregate-report-template.md`

## 請您檢查什麼

### Legal/privacy reviewer

請確認：

- reviewer-supplied candidates 是否可用；
- approved browser-session risk-probe candidates 是否可在固定 cap 下使用；
- reply/comment cues 是否可用 category/flag 方式記錄，而不讓 raw reply text 進 git；
- OCR-derived text 是否可處理，前提是 screenshot/raw OCR controlled-store-only；
- profile-context categories 是否可記錄，前提是不做 account graph capture；
- external contact/link categories 是否可記錄，前提是不讓 raw URLs/contact IDs 進 git；
- retention、deletion、redaction、incident ownership；
- aggregate-only output 可否在 CIB/internal 內分享；
- 是否有任何 evidence surface 必須禁止。

### CIB/internal owner

請確認：

- Track B 是否被接受為 internal research method test，而不是 enforcement；
- caps 是否可接受；
- source-arm mix 是否可接受；
- hard-negative probe arm 是否必須保留；
- aggregate-only reporting 是否可接受；
- no-overflow queue 與 stop-rule 是否可接受。

### Technical/governance reviewer

請確認：

- caps 與 no-overflow rule 是否足夠清楚；
- source-arm caps 是否合理；
- candidate record template 是否足以記錄 source、signal、dedupe、evidence completeness、reviewer workflow、stop-rule audit；
- daily stop-rule process 是否足夠；
- raw-evidence exclusion check 是否足夠；
- strict validation command/output target 是否足夠；
- pass/pause thresholds 是否可審查；
- Track A limitations 是否已轉成 Track B controls。

### Controlled-store / reviewer role owners

請確認：

- controlled-store custodian alias；
- primary reviewer alias；
- second reviewer alias；
- stop-rule owner alias；
- daily stop-check owner alias；
- validation owner alias；
- reporting owner alias；
- strict validation output target；
- aggregate reporting target；
- raw-evidence exclusion check procedure。

## 請用這個格式回覆

請回覆 repo-safe 文字，不要放真名、私密聯絡方式、email、account ID、raw Threads URLs、handles、screenshots、raw post text、raw reply text、contact IDs、credentials、browser/session artifacts、exact controlled-store paths、stakeholder case IDs 或任何 private recipient details。

```text
Track B condition response

Legal/privacy status:
no_veto / approved_with_conditions / veto

Legal/privacy conditions:
[repo-safe text only]

CIB/internal owner status:
accepted_boundary / accepted_with_conditions / not_accepted

CIB/internal owner conditions:
[repo-safe text only]

Technical/governance status:
confirmed_controls / confirmed_with_conditions / not_confirmed

Technical/governance conditions:
[repo-safe text only]

Controlled-store custodian alias:
[repo-safe alias only]

Reviewer role aliases:
- primary:
- second:
- technical/governance owner:
- legal/privacy owner:
- controlled-store custodian:
- stop-rule owner:
- daily stop-check owner:
- validation owner:
- reporting owner:
- CIB/internal owner:

Raw-evidence exclusion check:
ready / not_ready / ready_with_conditions

Raw-evidence exclusion check procedure:
[repo-safe command or procedure summary only]

Strict validation output target:
[repo-safe path or artifact name only]

Aggregate reporting target:
[repo-safe path or artifact name only]

Explicit non-authorizations confirmed:
yes / no

Additional conditions:
[repo-safe text only]
```

## Track B caps

Track B caps 已由 decision `0121` 鎖定，除非後續另開 decision，否則不得變更。

| Source arm | Surfaced candidate cap |
|---|---:|
| Checkpoint-derived seed replay | 30 |
| Reviewer-supplied candidates | 30 |
| Approved browser-session risk-probe matrix | 110 |
| Reply/comment funnel cue candidates | 60 |
| OCR/image-cue candidates | 20 |
| Hard-negative probe arm | 50 |
| Total | 300 |

Overall caps:

| Cap | Value |
|---|---:|
| Human-reviewed candidates | 150 |
| Accepted strict-valid records | 75 |
| Intake window | 14 calendar days |

No overflow queue is allowed.

## 明確不授權

本次 package 不授權：

- Track B 在條件全綠前執行；
- item `0082`；
- open-ended collection；
- broad crawler/browser expansion；
- private-message access；
- account/profile graph capture；
- landing-page or redirect-chain capture；
- model or embedding training；
- production detector；
- legal fraud determination；
- automated enforcement；
- public release；
- raw evidence in git。

請您回覆的重點不是「泛泛批准」，而是把 Track B checklist 裡的 pending 條件逐項變成：

```text
pass
pass_with_conditions
blocked
veto
```

只要任何硬條件未通過，Track B 就會維持 blocked。

謝謝。
