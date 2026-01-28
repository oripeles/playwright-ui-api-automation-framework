import allure
import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
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
