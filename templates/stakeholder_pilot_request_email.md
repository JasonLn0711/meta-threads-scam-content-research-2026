# Stakeholder Pilot Request Email

Subject: Approval request: 50-item Threads scam-content research pilot

Hi [Name],

We are ready to begin the first small Threads scam-content research pilot, pending your approval of source, fields, retention, and redaction rules.

This is a research pilot, not production detection or enforcement. The proposed scope is:

- 5-item synthetic/redacted annotator calibration
- 50-item first pilot batch if calibration passes
- manual or stakeholder-provided examples only
- no scraping, browser automation, crawling, bulk export, or landing-page crawling
- raw evidence stored outside git
- redacted or derived annotation files only
- human labels for `scam`, `non_scam`, `uncertain`, and `insufficient_evidence`
- first audit and rule-baseline comparison after annotation

The approval questions are:

1. Which source type may we use first: stakeholder-provided cases, manually identified public examples, or another approved source?
2. Which fields may we store: post text, selected replies, OCR text, visible links, redacted contact handles, screenshots, source URL references?
3. Can screenshots be retained? If yes, must they be redacted before annotation?
4. Can URLs or visible links be stored? If yes, should we store full URL, normalized domain, or redacted reference?
5. Who may access raw evidence and annotation files?
6. What is the retention/deletion rule?
7. Can aggregate metrics and redacted examples be included in internal memos?

The detailed kickoff memo is in `docs/25-stakeholder-pilot-kickoff.md`, the approval packet is in `docs/36-stakeholder-authorization-packet.md`, and the authorization record templates are `templates/stakeholder_authorization_decision_record.md` and `templates/data_authorization_request.md`.

Once approval is recorded, we will run the pilot through the go/no-go checklist in `docs/26-pilot-go-no-go-checklist.md` and the real-pilot readiness review in `docs/35-real-pilot-readiness-review.md`.

Best,

[Your name]
