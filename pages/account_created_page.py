from pages.base_page import BasePage, logger
from playwright.sync_api import Page


class AccountCreatedPage(BasePage):
    """Page shown after successful account creation."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.continue_button = page.locator("[data-qa='continue-button']")
        self.account_created_title = page.locator("[data-qa='account-created']")

    def click_continue(self) -> None:
        """Click 'Continue' to proceed to homepage."""
        logger.info("Clicking continue after account creation")
        self.continue_button.click()
