from __future__ import annotations

import os
from pathlib import Path

import yaml


def load_config(config_path: str | Path) -> dict:
    path = Path(config_path)
    with path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)

    config["email"]["recipient"] = os.getenv(
        "EMAIL_TO",
        config["email"]["recipient"],
    )
    config["analysis"]["openai_model"] = os.getenv(
        "OPENAI_MODEL",
        config["analysis"]["openai_model"],
    )
    return config
