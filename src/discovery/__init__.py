"""Synthetic discovery helpers for closed-loop research runs."""

from .connector import fetch_candidates
from .query_generator import generate_queries

__all__ = ["fetch_candidates", "generate_queries"]
