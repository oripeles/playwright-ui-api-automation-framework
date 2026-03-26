import json
from typing import Any

from utilities.exceptions import TestDataError
from utilities.logger import get_logger

logger = get_logger("data")


def load_json(filename: str) -> Any:
    """Load and return data from a JSON file in the data/ directory."""
    path = f"data/{filename}.json"
    logger.debug("Loading test data from %s", path)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise TestDataError(f"Test data file not found: {path}")
    except json.JSONDecodeError as e:
        raise TestDataError(f"Invalid JSON in {path}: {e}")
