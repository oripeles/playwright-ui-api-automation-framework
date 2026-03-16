from pages.base_page import BasePage
from playwright.sync_api import Page


class AccountDeletedPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.account_deleted_title = page.locator("[data-qa='account-deleted']")
        self.continue_button = page.locator("[data-qa='continue-button']")

    def click_continue(self) -> None:
        self.continue_button.click()
