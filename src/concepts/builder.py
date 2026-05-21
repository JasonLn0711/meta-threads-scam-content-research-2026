"""Cluster-to-concept builder with conservative local reasoning."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

from src.evidence.storage import REPO_ROOT, utc_now


CONCEPTS_DIR = REPO_ROOT / "data/concepts"
CONCEPT_EVOLUTION_LOG = CONCEPTS_DIR / "concept_evolution.jsonl"
TOKEN_PATTERN = re.compile(r"[A-Za-z0-9_]+|[\u4e00-\u9fff]{2,}")


SIGNAL_PROFILES = {
    "hard_negative_warning": {
        "concept_name": "Anti-scam or risk-warning discussion",
        "description": "Content warns about investment risk or scam tactics rather than recruiting victims.",
        "attack_pattern": "No attack pattern; treat as hard-negative calibration unless a conversion path appears.",
        "psychological_hook": "victim prevention",
        "risk_floor": "low",
    },
    "guaranteed_return": {
        "concept_name": "Guaranteed-return investment lure",
        "description": "Content frames investment gains as stable, guaranteed, or unusually low risk.",
        "attack_pattern": "Promise certainty -> build confidence -> route toward private action.",
        "psychological_hook": "greed plus certainty",
        "risk_floor": "medium",
    },
    "authority_impersonation": {
        "concept_name": "Mentor-led authority investment lure",
        "description": "Content uses a teacher, analyst, assistant, or expert persona to create trust.",
        "attack_pattern": "Claim expertise -> offer guidance -> move the user toward a managed channel.",
        "psychological_hook": "authority plus trust",
        "risk_floor": "medium",
    },
    "off_platform_contact": {
        "concept_name": "Private-channel migration lure",
        "description": "Content moves readers from public discussion into private chat or group channels.",
        "attack_pattern": "Tease value -> request DM or group join -> continue persuasion off-platform.",
        "psychological_hook": "exclusivity plus access",
        "risk_floor": "medium",
    },
    "urgency": {
        "concept_name": "Urgency-driven investment teaser",
        "description": "Content pressures readers with limited time, limited slots, or imminent market moves.",
        "attack_pattern": "Create time pressure -> reduce scrutiny -> push immediate contact or action.",
        "psychological_hook": "fear of missing out",
        "risk_floor": "medium",
    },
}


def build_concept_prompt(cluster_data: dict[str, Any]) -> str:
    """Build the prompt an approved LLM adapter would receive."""
    safe_context = {
        "cluster_id": cluster_data.get("cluster_id"),
        "keywords": list(cluster_data.get("keywords", []))[:12],
        "scam_rate": float(cluster_data.get("scam_rate", 0.0) or 0.0),
        "sample_count": len(cluster_data.get("samples", []) or []),
    }
    return (
        "You are analyzing a cluster of social media posts for research triage.\n"
        "Summarize the underlying behavioral pattern conservatively.\n"
        "Do not infer guilt, legal fraud, or facts not supported by samples.\n"
        "Output concept_id, concept_name, description, attack_pattern, psychological_hook, risk_level.\n"
        f"Metadata-only context:\n{json.dumps(safe_context, ensure_ascii=False, sort_keys=True)}"
    )


def generate_concept(cluster_data: dict[str, Any]) -> dict[str, Any]:
    """Generate a metadata-only concept record from cluster samples and metrics."""
    prompt = build_concept_prompt(cluster_data)
    keywords = [str(keyword) for keyword in cluster_data.get("keywords", [])][:12]
    samples = [str(sample) for sample in cluster_data.get("samples", [])]
    scam_rate = float(cluster_data.get("scam_rate", 0.0) or 0.0)
    signal = _dominant_signal(keywords, samples)
    profile = SIGNAL_PROFILES[signal]
    concept_id = _concept_id(str(cluster_data.get("cluster_id", "unknown")), keywords, profile["concept_name"])

    return {
        "schema_version": "concept_v1",
        "concept_id": concept_id,
        "concept_name": profile["concept_name"],
        "description": profile["description"],
        "attack_pattern": profile["attack_pattern"],
        "psychological_hook": profile["psychological_hook"],
        "risk_level": _risk_level(signal, scam_rate, profile["risk_floor"]),
        "derived_from_cluster": str(cluster_data.get("cluster_id", "")),
        "keywords": keywords,
        "dominant_signal": signal,
        "metrics": {
            "scam_rate": round(scam_rate, 6),
            "sample_count": len(samples),
            "avg_review_time": cluster_data.get("avg_review_time"),
        },
        "sample_hashes": [_content_hash(sample) for sample in samples[:8]],
        "created_at": utc_now(),
        "llm_prompt_hash": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
        "llm_backend": "local_concept_policy_v1",
        "raw_samples_included": False,
        "human_review_required": True,
    }


def store_concept(concept: dict[str, Any], *, concepts_dir: Path = CONCEPTS_DIR) -> Path:
    """Store one concept and append a metadata-only evolution entry."""
    concepts_dir.mkdir(parents=True, exist_ok=True)
    path = concepts_dir / f"{concept['concept_id']}.json"
    path.write_text(json.dumps(concept, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _append_jsonl(
        concepts_dir / "concept_evolution.jsonl",
        {
            "schema_version": "concept_evolution_v1",
            "timestamp": utc_now(),
            "action": "generate_concept",
            "concept_id": concept["concept_id"],
            "derived_from_cluster": concept.get("derived_from_cluster"),
            "risk_level": concept.get("risk_level"),
            "dominant_signal": concept.get("dominant_signal"),
            "raw_samples_included": False,
        },
    )
    return path


def load_concepts(concepts_dir: Path = CONCEPTS_DIR) -> list[dict[str, Any]]:
    if not concepts_dir.exists():
        return []
    concepts = []
    for path in sorted(concepts_dir.glob("concept_*.json")):
        concepts.append(json.loads(path.read_text(encoding="utf-8")))
    return concepts


def extract_keywords(samples: list[str], *, limit: int = 12) -> list[str]:
    counts: dict[str, int] = {}
    for sample in samples:
        for token in TOKEN_PATTERN.findall(sample.lower()):
            if token.startswith("合成"):
                continue
            counts[token] = counts.get(token, 0) + 1
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return [token for token, _ in ranked[:limit]]


def _dominant_signal(keywords: list[str], samples: list[str]) -> str:
    text = " ".join(keywords + samples).lower()
    if any(term in text for term in ("反詐", "不要相信", "風險", "虧損", "金融教育")):
        return "hard_negative_warning"
    if any(term.lower() in text for term in ("line", "telegram", "whatsapp", "私訊", "dm", "加群", "群組", "社群")):
        return "off_platform_contact"
    if any(term in text for term in ("老師", "助理", "分析師", "專家", "官方", "帶單")):
        return "authority_impersonation"
    if any(term in text for term in ("保證", "穩賺", "零風險", "保本", "翻倍", "收益")):
        return "guaranteed_return"
    if any(term in text for term in ("限時", "名額", "倒數", "最後", "立刻", "開盤")):
        return "urgency"
    return "hard_negative_warning"


def _risk_level(signal: str, scam_rate: float, risk_floor: str) -> str:
    if signal == "hard_negative_warning":
        return "low"
    if scam_rate >= 0.65:
        return "high"
    if scam_rate >= 0.3 or risk_floor == "medium":
        return "medium"
    return "low"


def _concept_id(cluster_id: str, keywords: list[str], name: str) -> str:
    material = json.dumps({"cluster_id": cluster_id, "keywords": keywords, "name": name}, ensure_ascii=False, sort_keys=True)
    digest = hashlib.sha1(material.encode("utf-8")).hexdigest()[:12]
    return f"concept_{digest}"


def _content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _append_jsonl(path: Path, entry: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, ensure_ascii=False, sort_keys=True) + "\n")
