from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from .models import AnalysisResult, Paper


START_MARKER = "<!-- AUTO_RESULTS_START -->"
END_MARKER = "<!-- AUTO_RESULTS_END -->"


def update_readme(path: str | Path, pairs: list[tuple[Paper, AnalysisResult]], lookback_days: int) -> None:
    readme_path = Path(path)
    content = readme_path.read_text(encoding="utf-8")
    generated = _build_section(pairs, lookback_days)

    start = content.find(START_MARKER)
    end = content.find(END_MARKER)
    if start == -1 or end == -1 or end < start:
        raise RuntimeError("README auto-result markers are missing.")

    updated = content[: start + len(START_MARKER)] + "\n" + generated + "\n" + content[end:]
    readme_path.write_text(updated, encoding="utf-8")


def _build_section(pairs: list[tuple[Paper, AnalysisResult]], lookback_days: int) -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "## Latest Results",
        "",
        f"- Window: last {lookback_days} day(s)",
        f"- Updated at: {timestamp}",
        f"- Relevant papers: {len(pairs)}",
        "",
    ]

    if not pairs:
        lines.append("最近时间窗口内没有筛选到相关论文。")
        return "\n".join(lines)

    lines.extend(
        [
            "| Title | Type | Authors |",
            "|---|---|---|",
        ]
    )

    for paper, analysis in pairs:
        title = _escape(f"[{paper.title}]({paper.abs_url})")
        topic = _escape(_topic_label(analysis.topic))
        authors = _escape(", ".join(paper.authors))
        lines.append(f"| {title} | {topic} | {authors} |")

    return "\n".join(lines)


def _topic_label(topic: str) -> str:
    return {
        "world_model": "World Model",
        "robot_foundation": "Robot Foundation / VLA",
    }.get(topic, topic)


def _escape(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")
