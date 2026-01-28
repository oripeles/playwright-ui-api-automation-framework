import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page
from utilities.config import HEADLESS
from pages.home_page import HomePage


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
    assert home.is_home_page_visible(), "Home page not active or visible"
    return home