#!/usr/bin/env python3
"""Verify the Evidence Layer v1 audit hash chain."""

from __future__ import annotations

import json

from src.evidence.audit import verify_chain


def main() -> int:
    result = verify_chain()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
