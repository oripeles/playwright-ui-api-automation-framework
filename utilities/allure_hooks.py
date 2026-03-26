import allure
import pytest
from typing import Generator

from utilities.logger import get_logger

logger = get_logger("hooks")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo[None]) -> Generator[None, None, None]:
    """Capture screenshot, URL and HTML on test failure."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        logger.error("Test FAILED: %s", item.name)
        page = item.funcargs.get("page")
        if page:
            try:
                allure.attach(
                    page.screenshot(full_page=True),
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

                allure.attach(
                    page.url,
                    name="Current URL",
                    attachment_type=allure.attachment_type.TEXT
                )

                allure.attach(
                    page.content(),
                    name="Page HTML",
                    attachment_type=allure.attachment_type.HTML
                )
                logger.info("Captured failure artifacts for: %s", item.name)
            except Exception as e:
                logger.error("Failed to capture artifacts: %s", e)
