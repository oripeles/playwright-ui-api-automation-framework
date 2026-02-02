from pages.base_page import BasePage

class ContactUsFormPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.get_in_touch_title = page.get_by_role("heading", name="Get In Touch")
        self.name_input = page.locator("[data-qa='name']")
        self.subject_input = page.locator("[data-qa='subject']")
        self.email_input = page.locator("[data-qa='email']")
        self.message_input = page.locator("[data-qa='message']")
        self.submit_button = page.locator("[data-qa='submit-button']")
        self.get_in_touch_success = page.locator(".status.alert.alert-success")
        self.home_button = page.get_by_role("link", name="Home")

    def fill_details(self, name, email, subject, message):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.subject_input.fill(subject)
        self.message_input.fill(message)

    def click_submit(self):
        self.submit_button.click()

    def click_home(self):
        self.home_button.click()


