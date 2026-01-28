import pytest
from utilities.config import BASE_URL
from utilities.json_loader import load_json

pytest_plugins = ("utilities.allure_hooks",)

@pytest.fixture(scope="session")
def base_url() -> str:
    return BASE_URL

@pytest.fixture(scope="session")
def user_data():
    return load_json("user_data")

@pytest.fixture
def existing_user(user_data):
    return user_data["existing_user"]
