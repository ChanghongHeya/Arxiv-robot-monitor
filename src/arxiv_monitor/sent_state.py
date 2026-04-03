from __future__ import annotations

import json
from pathlib import Path


def load_sent_ids(path: str | Path) -> set[str]:
    state_path = Path(path)
    if not state_path.exists():
        return set()

    content = json.loads(state_path.read_text(encoding="utf-8"))
    return set(content.get("sent_paper_ids", []))


def save_sent_ids(path: str | Path, sent_ids: set[str]) -> None:
    state_path = Path(path)
    state_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "sent_paper_ids": sorted(sent_ids),
    }
    state_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
