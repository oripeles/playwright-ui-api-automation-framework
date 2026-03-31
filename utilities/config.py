import os

from dotenv import load_dotenv

load_dotenv()


def env_bool(name: str, default: bool) -> bool:
    """Read a boolean from an environment variable."""
    v = os.getenv(name)
    if v is None:
        return default
    return v.strip().lower() in ("1", "true", "yes", "y", "on")


ENV_URLS = {
    "prod": "https://www.automationexercise.com/",
    "staging": "https://staging.automationexercise.com/",
}

ENV = os.getenv("ENV", "prod")
BASE_URL = os.getenv("BASE_URL", ENV_URLS.get(ENV, ENV_URLS["prod"]))
HEADLESS = env_bool("HEADLESS", True)
BROWSER = os.getenv("BROWSER", "chromium")
DEVICE = os.getenv("DEVICE", "")
VISUAL_DEVICES = ["desktop", "iPhone 13", "Pixel 5"]
