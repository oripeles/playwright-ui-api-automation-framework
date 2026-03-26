from pages.base_page import BasePage, logger
from playwright.sync_api import Page


class AccountDeletedPage(BasePage):
    """Page shown after successful account deletion."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.account_deleted_title = page.locator("[data-qa='account-deleted']")
        self.continue_button = page.locator("[data-qa='continue-button']")

    def click_continue(self) -> None:
        """Click 'Continue' to proceed to homepage."""
        logger.info("Clicking continue after account deletion")
        self.continue_button.click()
