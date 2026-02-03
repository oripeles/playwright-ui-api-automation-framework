import os

import pytest
from utilities.config import BASE_URL
from utilities.json_loader import load_json

pytest_plugins = ("utilities.allure_hooks",)

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def user_data():
    return load_json("user_data")

@pytest.fixture
def existing_user(user_data):
    return user_data["existing_user"]

@pytest.fixture(scope="session")
def user_password():
    password = os.getenv("USER_PASSWORD")
    assert password, "Missing USER_PASSWORD env var"
    return password
