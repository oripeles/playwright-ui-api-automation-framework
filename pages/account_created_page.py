from pages.base_page import BasePage

class AccountCreatedPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.continue_button = page.locator("[data-qa='continue-button']")
        self.account_created_title = page.locator("[data-qa='account-created']")

    def click_continue(self):
        self.continue_button.click()




