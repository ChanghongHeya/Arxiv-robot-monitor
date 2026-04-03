from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Paper:
    paper_id: str
    title: str
    abstract: str
    abs_url: str
    pdf_url: str
    published_at: datetime
    updated_at: datetime
    authors: list[str]
    categories: list[str]
    matched_queries: list[str]


@dataclass(slots=True)
class AnalysisResult:
    is_relevant: bool
    topic: str
    reason: str
    summary_zh: str
    confidence: int
    method: str
    score: int
