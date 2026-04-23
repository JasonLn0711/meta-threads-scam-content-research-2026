"""Extract visible, manually supplied metadata without network access."""

from __future__ import annotations

import re
from urllib.parse import urlparse


URL_RE = re.compile(r"(?i)\b(?:https?://|www\.)[^\s<>()]+")
EMAIL_RE = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
PHONE_RE = re.compile(r"(?<!\d)(?:\+?\d[\d\s().-]{7,}\d)(?!\d)")

PLATFORM_ORDER = (
    "line",
    "whatsapp",
    "telegram",
    "messenger",
    "instagram_dm",
    "threads_dm",
    "external_site",
    "private_group",
    "phone",
    "email",
    "other",
)


def extract_visible_metadata(
    *,
    post_text: str = "",
    reply_texts: list[str] | None = None,
    ocr_text: str = "",
    explicit_links: list[str] | None = None,
    explicit_handles: list[str] | None = None,
    explicit_redirects: list[str] | None = None,
    external_link_storage: str = "domain_only",
) -> dict[str, list[str]]:
    text = "\n".join([post_text, *(reply_texts or []), ocr_text])
    links = normalize_links(
        [*(explicit_links or []), *URL_RE.findall(text)],
        storage=external_link_storage,
    )
    handles = normalize_handles([*(explicit_handles or []), *extract_contact_handles(text)])
    redirects = normalize_redirects([*(explicit_redirects or []), *extract_platform_redirects(text, links)])
    return {
        "external_links": links,
        "visible_contact_handles": handles,
        "visible_platform_redirects": redirects,
    }


def normalize_links(values: list[str], *, storage: str = "domain_only") -> list[str]:
    normalized: list[str] = []
    for value in values:
        cleaned = clean_token(value)
        if not cleaned:
            continue
        if storage == "domain_only":
            cleaned = domain_from_visible_link(cleaned)
        normalized.append(cleaned)
    return unique_preserving_order(normalized)


def domain_from_visible_link(value: str) -> str:
    candidate = value.strip()
    if not candidate:
        return ""
    if "[redacted" in candidate.lower():
        return candidate
    if not candidate.lower().startswith(("http://", "https://")):
        candidate = "https://" + candidate
    parsed = urlparse(candidate)
    domain = parsed.netloc.lower()
    if domain.startswith("www."):
        domain = domain[4:]
    return domain or value.strip().lower()


def extract_contact_handles(text: str) -> list[str]:
    lowered = text.lower()
    handles: list[str] = []
    if "telegram" in lowered or "t.me/" in lowered or "tg " in lowered:
        handles.append("telegram:[redacted]")
    if re.search(r"(?i)\bline\b|line\s*id", text):
        handles.append("line:[redacted]")
    if "whatsapp" in lowered or "wa.me/" in lowered:
        handles.append("whatsapp:[redacted]")
    if EMAIL_RE.search(text):
        handles.append("email:[redacted]")
    if PHONE_RE.search(text):
        handles.append("phone:[redacted]")
    return handles


def normalize_handles(values: list[str]) -> list[str]:
    handles: list[str] = []
    for value in values:
        cleaned = clean_token(value)
        if not cleaned:
            continue
        lowered = cleaned.lower()
        if "[redacted" in lowered:
            handles.append(cleaned)
        elif "telegram" in lowered:
            handles.append("telegram:[redacted]")
        elif "line" in lowered:
            handles.append("line:[redacted]")
        elif "whatsapp" in lowered:
            handles.append("whatsapp:[redacted]")
        elif "email" in lowered or EMAIL_RE.search(cleaned):
            handles.append("email:[redacted]")
        elif "phone" in lowered or PHONE_RE.search(cleaned):
            handles.append("phone:[redacted]")
        else:
            handles.append("other:[redacted]")
    return unique_preserving_order(handles)


def extract_platform_redirects(text: str, links: list[str] | None = None) -> list[str]:
    lowered = text.lower()
    redirects: set[str] = set()
    if "telegram" in lowered or "t.me/" in lowered:
        redirects.add("telegram")
    if re.search(r"(?i)\bline\b|line\s*id", text):
        redirects.add("line")
    if "whatsapp" in lowered or "wa.me/" in lowered:
        redirects.add("whatsapp")
    if "messenger" in lowered or "m.me/" in lowered:
        redirects.add("messenger")
    if "instagram dm" in lowered or "ig dm" in lowered:
        redirects.add("instagram_dm")
    if "threads dm" in lowered or "dm me" in lowered or "private message" in lowered:
        redirects.add("threads_dm")
    if "private group" in lowered or "join group" in lowered:
        redirects.add("private_group")
    if EMAIL_RE.search(text):
        redirects.add("email")
    if PHONE_RE.search(text):
        redirects.add("phone")
    if links:
        redirects.add("external_site")
    return sorted(redirects, key=PLATFORM_ORDER.index)


def normalize_redirects(values: list[str]) -> list[str]:
    redirects = [clean_token(value).lower() for value in values if clean_token(value)]
    if not redirects:
        return ["none"]
    allowed = set(PLATFORM_ORDER) | {"none"}
    cleaned = [value if value in allowed else "other" for value in redirects]
    cleaned = [value for value in cleaned if value != "none"]
    if not cleaned:
        return ["none"]
    return sorted(set(cleaned), key=PLATFORM_ORDER.index)


def clean_token(value: str) -> str:
    return value.strip().strip(".,;:!?)\"'}")


def unique_preserving_order(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value and value not in seen:
            seen.add(value)
            result.append(value)
    return result
