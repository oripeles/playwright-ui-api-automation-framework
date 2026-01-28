import os

def env_bool(name: str, default: bool) -> bool:
    v = os.getenv(name)
    if v is None:
        return default
    return v.strip().lower() in ("1", "true", "yes", "y", "on")

BASE_URL = os.getenv("BASE_URL", "https://www.automationexercise.com/")
HEADLESS = env_bool("HEADLESS", True)
