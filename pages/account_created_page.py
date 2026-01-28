from pages.base_page import BasePage

class AccountCreatedPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.continue_button = page.get_by_role("link", name="Continue")
        self.account_created_title = page.get_by_text("Account Created!")

        def is_account_created_title_visible(self) -> bool:
            return self.account_created_title.i

        def click_continue(self):
            self.continue_button.cli


