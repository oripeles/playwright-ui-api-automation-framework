import pytest
from playwright.sync_api import expect
from utilities.config import HEADLESS
from pages.home_page import HomePage


@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(
        headless=HEADLESS,
        args=["--disable-gpu", "--no-sandbox", "--disable-dev-shm-usage"],
    )
    yield browser
    browser.close()


@pytest.fixture
def context(browser, base_url, request):
    context = browser.new_context(
        base_url=base_url,
        viewport={"width": 1920, "height": 1080},
    )
    context.tracing.start(screenshots=True, snapshots=True)
    yield context
    context.tracing.stop(path=f"traces/{request.node.name}.zip")
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
