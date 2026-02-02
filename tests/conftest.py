import pytest
from utilities.config import BASE_URL
from utilities.json_loader import load_json
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page
from utilities.config import HEADLESS
from pages.home_page import HomePage
from playwright.sync_api import expect

pytest_plugins = ("utilities.allure_hooks",)

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=HEADLESS,
            args=["--disable-gpu", "--no-sandbox", "--disable-dev-shm-usage"],
        )
        yield browser
        browser.close()

@pytest.fixture
def context(browser, base_url):
    context = browser.new_context(
        base_url=base_url,
        viewport={"width": 1920, "height": 1080},
    )
    yield context
    context.close()

@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture
def home(page):
    page.goto("/")
    home = HomePage(page)
    expect(home.active_tab).to_be_visible()
    return home

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def user_data():
    return load_json("user_data")

@pytest.fixture
def existing_user(user_data):
    return user_data["existing_user"]
