from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from .models import AnalysisResult, Paper


def append_title_archive(path: str | Path, pairs: list[tuple[Paper, AnalysisResult]], lookback_days: int) -> None:
    archive_path = Path(path)
    archive_path.parent.mkdir(parents=True, exist_ok=True)

    if archive_path.exists():
        content = json.loads(archive_path.read_text(encoding="utf-8"))
    else:
        content = {"runs": []}

    run_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    titles = [paper.title for paper, _ in pairs]

    content["runs"].append(
        {
            "run_at": run_at,
            "lookback_days": lookback_days,
            "paper_count": len(titles),
            "titles": titles,
        }
    )

    archive_path.write_text(json.dumps(content, ensure_ascii=False, indent=2), encoding="utf-8")
