"""Stable rule-baseline signal taxonomy.

The names here are intentionally reviewer-readable and stable. They are
research triage signals, not legal findings.
"""

from __future__ import annotations

from .types import SignalDefinition


TEXTUAL_LURE = "textual_lure"
REDIRECT_CONTACT = "redirect_contact"
URGENCY_PRESSURE = "urgency_pressure"
TESTIMONIAL_SCREENSHOT = "testimonial_screenshot"
PSEUDO_OFFICIAL_ENDORSEMENT = "pseudo_official_endorsement"
PAYMENT_CREDENTIAL = "payment_credential"
OCR_CONTEXT = "ocr_context"
REPLY_FUNNEL = "reply_funnel"


SIGNAL_DEFINITIONS: dict[str, SignalDefinition] = {
    "GUARANTEED_PROFIT": SignalDefinition(
        signal_code="GUARANTEED_PROFIT",
        reason_code="GUARANTEED_PROFIT",
        category=TEXTUAL_LURE,
        description="Guaranteed, risk-free, fixed-return, or no-loss claim.",
        default_weight=4.0,
        patterns=(
            r"\bguaranteed (daily )?(profit|return|income|payout)\b",
            r"\brisk[- ]?free\b",
            r"\bno loss(es)?\b",
            r"\bfixed roi\b",
            r"\bdaily profit\b",
            r"\bguaranteed\b",
        ),
    ),
    "LOW_EFFORT_HIGH_RETURN": SignalDefinition(
        signal_code="LOW_EFFORT_HIGH_RETURN",
        reason_code="LOW_EFFORT_HIGH_RETURN",
        category=TEXTUAL_LURE,
        description="Low-effort or unusually large benefit claim.",
        default_weight=3.0,
        patterns=(
            r"\bturn\s+\$?\d+[\d,]*\s+into\s+\$?\d+[\d,]*\b",
            r"\b\d+%\s+(a|per|each)?\s*(day|week|month)\b",
            r"\b(passive|easy)\s+income\b",
            r"\beasy money\b",
            r"\bmake\s+\$?\d+[\d,]*\b",
            r"\bhigh return\b",
            r"\bcopy and earn\b",
        ),
    ),
    "HIGH_FEE_COURSE_FUNNEL": SignalDefinition(
        signal_code="HIGH_FEE_COURSE_FUNNEL",
        reason_code="HIGH_FEE_COURSE_FUNNEL",
        category=TEXTUAL_LURE,
        description="High-fee course, academy, membership, coaching, or trading-education funnel.",
        default_weight=2.5,
        patterns=(
            r"\b(high[- ]?ticket|paid)\s+(course|coaching|academy|membership)\b",
            r"\bhigh[- ]?(fee|price)\s+(course|coaching|academy|membership)\b",
            r"\b(course|coaching|academy|membership)\s+(fee|price)s?\b",
            r"\btrading\s+(course|academy|coaching|school|membership)\b",
            r"(\d+\s*)?萬.{0,8}(課程|學費|費用|收費|報名|入會|會員)",
            r"(課程|學院|教學|導師|會員|社群).{0,12}(交易|投資|股票|外匯|加密貨幣|獲利)",
            r"(交易|投資|股票|外匯|加密貨幣|獲利).{0,12}(課程|學院|教學|導師|會員|社群)",
        ),
    ),
    "BEGINNER_EASY_MONEY": SignalDefinition(
        signal_code="BEGINNER_EASY_MONEY",
        reason_code="BEGINNER_EASY_MONEY",
        category=TEXTUAL_LURE,
        description="Beginner, no-experience, or anyone-can-earn framing.",
        default_weight=2.0,
        patterns=(
            r"\bbeginners? can (earn|make|start)\b",
            r"\bno experience (needed|required)\b",
            r"\banyone can (earn|make|join)\b",
            r"\bstart earning today\b",
            r"\bwork from home\b",
        ),
    ),
    "MENTOR_COPYTRADE_LANGUAGE": SignalDefinition(
        signal_code="MENTOR_COPYTRADE_LANGUAGE",
        reason_code="MENTOR_COPYTRADE_LANGUAGE",
        category=TEXTUAL_LURE,
        description="Mentor, teacher, signal group, or copy-trade lure.",
        default_weight=3.0,
        patterns=(
            r"\b(copy[- ]?trade|copy trading)\b",
            r"\btrading signals?\b",
            r"\bsignal group\b",
            r"\bteacher\b",
            r"\bmentor\b",
            r"\banalyst\b",
            r"\bprivate trading method\b",
        ),
    ),
    "PRIVATE_REDIRECT": SignalDefinition(
        signal_code="PRIVATE_REDIRECT",
        reason_code="PRIVATE_REDIRECT",
        category=REDIRECT_CONTACT,
        description="Instruction to move into private chat, group, or off-platform contact.",
        default_weight=4.0,
        patterns=(
            r"\bdm (me|for|to)\b",
            r"\bdirect message\b",
            r"\bprivate (message|group|chat)\b",
            r"\bjoin (the )?(group|channel)\b",
            r"\bmessage (me|the assistant|support)\b",
            r"\binbox me\b",
            r"\badd (me|account|line|whatsapp|telegram)\b",
            r"\btelegram\b",
            r"\bwhatsapp\b",
            r"\bline\b",
        ),
    ),
    "IMPLICIT_DM_CONTACT_REQUEST": SignalDefinition(
        signal_code="IMPLICIT_DM_CONTACT_REQUEST",
        reason_code="IMPLICIT_DM_CONTACT_REQUEST",
        category=REDIRECT_CONTACT,
        description="Private-message request that withholds the public contact route.",
        default_weight=2.5,
        patterns=(
            r"\bdm (me|for|to|get|details?)\b",
            r"\bdirect message (me|for|to|get|details?)\b",
            r"\bprivate[- ]message\b",
            r"\binbox me\b",
            r"私訊(我|貼文者|作者|版主|小編|了解|詢問|索取|領取|報名|即可|才|後)?",
            r"私我",
            r"(請|歡迎|想知道|想了解|有興趣|需要).{0,12}私訊",
            r"私訊.{0,12}(投資|賺錢|獲利|收益|群|方法|資訊|名額|機會)",
        ),
    ),
    "CONTACT_HANDLE_PRESENT": SignalDefinition(
        signal_code="CONTACT_HANDLE_PRESENT",
        reason_code="CONTACT_HANDLE_PRESENT",
        category=REDIRECT_CONTACT,
        description="Visible contact handle, phone, email, or messaging ID.",
        default_weight=3.0,
        patterns=(
            r"@\w{3,}",
            r"\b(line|telegram|whatsapp)\s*(id|account|handle)?\b",
            r"\b\+?\d[\d\s().-]{7,}\d\b",
            r"\b[\w.+-]+@[\w.-]+\.[a-z]{2,}\b",
        ),
    ),
    "EXTERNAL_LINK_PRESENT": SignalDefinition(
        signal_code="EXTERNAL_LINK_PRESENT",
        reason_code="EXTERNAL_LINK_PRESENT",
        category=REDIRECT_CONTACT,
        description="Visible external link, shortener, or URL-like destination.",
        default_weight=1.5,
        patterns=(
            r"https?://\S+",
            r"\bwww\.\S+",
            r"\b(bit\.ly|tinyurl|t\.co|linktr\.ee|wa\.me|t\.me)/\S*",
            r"\bclick (the )?(link|bio)\b",
        ),
    ),
    "URGENCY_PRESSURE": SignalDefinition(
        signal_code="URGENCY_PRESSURE",
        reason_code="URGENCY_PRESSURE",
        category=URGENCY_PRESSURE,
        description="Scarcity, deadline, or act-now pressure.",
        default_weight=2.0,
        patterns=(
            r"\blimited (spots|seats|time|members|slots)\b",
            r"\blast chance\b",
            r"\btoday only\b",
            r"\bfew spots\b",
            r"\bfirst\s+\d+\s+(members|people|spots|users)\b",
            r"\bact now\b",
            r"\bdon'?t miss\b",
            r"\bdeadline\b",
        ),
    ),
    "TESTIMONIAL_PATTERN": SignalDefinition(
        signal_code="TESTIMONIAL_PATTERN",
        reason_code="TESTIMONIAL_PATTERN",
        category=TESTIMONIAL_SCREENSHOT,
        description="Proof, results, testimonial, or earnings screenshot pattern.",
        default_weight=2.5,
        patterns=(
            r"\btestimonial(s)?\b",
            r"\bproof\b",
            r"\bmember results\b",
            r"\bstudent success\b",
            r"\bsuccess stor(y|ies)\b",
            r"\bearnings? screenshot\b",
            r"\bprofit screenshot\b",
            r"\baccount balance\b",
            r"\bwithdrawal proof\b",
            r"\bscreenshot(s)? (are|is) in\b",
        ),
    ),
    "SCREENSHOT_EVIDENCE": SignalDefinition(
        signal_code="SCREENSHOT_EVIDENCE",
        reason_code="SCREENSHOT_EVIDENCE",
        category=TESTIMONIAL_SCREENSHOT,
        description="Screenshot-heavy item or screenshot-as-proof framing.",
        default_weight=1.0,
        patterns=(
            r"\bscreenshot(s)?\b",
            r"\bshown in the image\b",
            r"\bin the image\b",
        ),
    ),
    "PSEUDO_OFFICIAL_LANGUAGE": SignalDefinition(
        signal_code="PSEUDO_OFFICIAL_LANGUAGE",
        reason_code="PSEUDO_OFFICIAL_LANGUAGE",
        category=PSEUDO_OFFICIAL_ENDORSEMENT,
        description="Official-looking, verification, subsidy, support, or institutional framing.",
        default_weight=3.0,
        patterns=(
            r"\bofficial\b",
            r"\bverify your account\b",
            r"\bverification\b",
            r"\bsupport account\b",
            r"\breward notice\b",
            r"\bsubsidy\b",
            r"\bgrant approved\b",
            r"\bregistration page\b",
            r"\bgovernment\b",
        ),
    ),
    "CELEBRITY_ENDORSEMENT_PATTERN": SignalDefinition(
        signal_code="CELEBRITY_ENDORSEMENT_PATTERN",
        reason_code="CELEBRITY_ENDORSEMENT_PATTERN",
        category=PSEUDO_OFFICIAL_ENDORSEMENT,
        description="Celebrity, expert, news, or authority endorsement framing.",
        default_weight=2.5,
        patterns=(
            r"\bcelebrity\b",
            r"\bendorsed by\b",
            r"\bas seen on\b",
            r"\bdoctor recommended\b",
            r"\bexpert approved\b",
            r"\bnews report\b",
            r"\bfamous (investor|doctor|professor|analyst)\b",
        ),
    ),
    "PAYMENT_OR_CREDENTIAL_REQUEST": SignalDefinition(
        signal_code="PAYMENT_OR_CREDENTIAL_REQUEST",
        reason_code="PAYMENT_OR_CREDENTIAL_REQUEST",
        category=PAYMENT_CREDENTIAL,
        description="Payment, fee, wallet, credential, bank, identity, or verification ask.",
        default_weight=5.0,
        patterns=(
            r"\bdeposit\b",
            r"\b(release|shipping|verification)\s+fee\b",
            r"\bwallet transfer\b",
            r"\bcredit card\b",
            r"\blogin\b",
            r"\bpassword\b",
            r"\bbank (info|account|details)\b",
            r"\bpersonal information\b",
            r"\bid number\b",
            r"\bpay (a|the|small)\b",
        ),
    ),
    "OCR_SUSPICIOUS_TEXT": SignalDefinition(
        signal_code="OCR_SUSPICIOUS_TEXT",
        reason_code="OCR_SUSPICIOUS_TEXT",
        category=OCR_CONTEXT,
        description="Suspicious signal appears in OCR text from image or screenshot evidence.",
        default_weight=1.0,
        patterns=(),
    ),
    "REPLY_FUNNEL_PATTERN": SignalDefinition(
        signal_code="REPLY_FUNNEL_PATTERN",
        reason_code="REPLY_FUNNEL_PATTERN",
        category=REPLY_FUNNEL,
        description="Suspicious funneling signal appears in replies/comments.",
        default_weight=1.5,
        patterns=(),
    ),
}


REASON_CODE_ORDER = [
    "PAYMENT_OR_CREDENTIAL_REQUEST",
    "GUARANTEED_PROFIT",
    "LOW_EFFORT_HIGH_RETURN",
    "HIGH_FEE_COURSE_FUNNEL",
    "BEGINNER_EASY_MONEY",
    "MENTOR_COPYTRADE_LANGUAGE",
    "PRIVATE_REDIRECT",
    "IMPLICIT_DM_CONTACT_REQUEST",
    "CONTACT_HANDLE_PRESENT",
    "EXTERNAL_LINK_PRESENT",
    "URGENCY_PRESSURE",
    "TESTIMONIAL_PATTERN",
    "SCREENSHOT_EVIDENCE",
    "PSEUDO_OFFICIAL_LANGUAGE",
    "CELEBRITY_ENDORSEMENT_PATTERN",
    "OCR_SUSPICIOUS_TEXT",
    "REPLY_FUNNEL_PATTERN",
    "MULTI_SIGNAL_CONVERGENCE",
]


FIELD_LABELS = {
    "post_text": "post text",
    "reply_texts": "replies",
    "ocr_text": "OCR text",
    "external_links": "external link fields",
    "visible_contact_handles": "visible contact handles",
    "visible_platform_redirects": "visible platform redirects",
    "screenshot_style": "screenshot style field",
}
