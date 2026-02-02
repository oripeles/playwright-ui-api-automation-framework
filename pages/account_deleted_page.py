from pages.base_page import BasePage

class AccountDeletedPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.account_deleted_title = page.get_by_text("Account Deleted!")
        self.continue_button = page.get_by_role("link", name="Continue")

    def click_continue(self):
        self.continue_button.click()


