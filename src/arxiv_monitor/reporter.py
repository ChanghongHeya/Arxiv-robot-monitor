from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from .models import AnalysisResult, Paper


def build_report(pairs: list[tuple[Paper, AnalysisResult]]) -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# arXiv Monitor Report",
        "",
        f"- Generated at: {timestamp}",
        f"- Relevant papers: {len(pairs)}",
        "",
    ]

    if not pairs:
        lines.append("No relevant papers found in this run.")
        lines.append("")
        return "\n".join(lines)

    for paper, analysis in pairs:
        lines.extend(
            [
                f"## {paper.title}",
                "",
                f"- arXiv: {paper.abs_url}",
                f"- Published: {paper.published_at.date().isoformat()}",
                f"- Queries: {', '.join(paper.matched_queries)}",
                f"- Method: {analysis.method}",
                f"- Topic: {analysis.topic}",
                f"- Confidence: {analysis.confidence}",
                f"- Reason: {analysis.reason}",
                f"- Summary: {analysis.summary_zh}",
                "",
            ]
        )

    return "\n".join(lines)


def save_report(path: str | Path, content: str) -> None:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding="utf-8")
