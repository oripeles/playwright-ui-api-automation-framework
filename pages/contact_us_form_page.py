from pages.base_page import BasePage

class ContactUsFormPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.get_in_touch_title = page.get_by_role("heading", name="Get In Touch")
        self.name_input = page.locator("input[data-qa='name']")
        self.subject_input = page.locator("input[data-qa='subject']")
        self.message_input = page.locator("textarea[data-qa='message']")
        self.submit_button = page.locator("input[data-qa='submit-button']")
        self.get_in_touch_success = page.locator(".status.alert.alert-success")
        self.home_button = page.get_by_role("link", name="Home")




