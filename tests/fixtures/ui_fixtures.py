import pytest
from playwright.sync_api import expect
from utilities.config import HEADLESS, BROWSER
from utilities.logger import get_logger
from pages.home_page import HomePage

logger = get_logger("fixtures")


@pytest.fixture(scope="session")
def browser(playwright):
    """Launch a browser for the entire test session."""
    logger.info("Launching %s browser (headless=%s)", BROWSER, HEADLESS)
    browser = getattr(playwright, BROWSER).launch(
        headless=HEADLESS,
        args=["--disable-gpu", "--no-sandbox", "--disable-dev-shm-usage"],
    )
    yield browser
    logger.info("Closing browser")
    browser.close()


@pytest.fixture
def context(browser, base_url, request):
    """Create a new browser context with tracing enabled."""
    logger.info("Creating browser context for test: %s", request.node.name)
    context = browser.new_context(
        base_url=base_url,
        viewport={"width": 1920, "height": 1080},
    )
    context.tracing.start(screenshots=True, snapshots=True)
    yield context
    context.tracing.stop(path=f"traces/{request.node.name}.zip")
    logger.info("Closed browser context for test: %s", request.node.name)
    context.close()


@pytest.fixture
def page(context):
    """Open a new page in the current browser context."""
    page = context.new_page()
    page.route("**/*googlesyndication*", lambda route: route.abort())
    page.route("**/*fundingchoicesmessages*", lambda route: route.abort())
    page.route("**/*adtrafficquality*", lambda route: route.abort())
    yield page
    page.close()


@pytest.fixture
def home(page):
    """Navigate to homepage and verify it loaded."""
    page.goto("/")
    home = HomePage(page)
    expect(home.active_tab).to_be_visible()
    return home
