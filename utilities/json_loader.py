import json
from typing import Any


def load_json(filename: str) -> Any:
    with open(f"data/{filename}.json", "r", encoding="utf-8") as f:
        return json.load(f)
