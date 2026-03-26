from pages.base_page import BasePage
from playwright.sync_api import Page


class CasesPage(BasePage):
    """Test Cases listing page."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.cases_title = page.locator("h2.title", has_text="Test Cases")
