from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.new_user_signup_title = page.get_by_role("heading",name="New User Signup!")
        self.login_title = page.get_by_role("heading", name="Login to your account")
        self.name_input = page.locator("input[data-qa='signup-name']")
        self.email_input = page.locator("input[data-qa='signup-email']")
        self.password_input_login = page.locator("input[data-qa='login-password']")
        self.email_input_login = page.locator("input[data-qa='login-email']")
        self.signup_button = page.locator("button[data-qa='signup-button']")
        self.login_button = page.locator("button[data-qa='login-button']")
        self.login_error = page.get_by_text("Your email or password is incorrect!")
        self.email_exist_title = page.get_by_text("Email Address already exist!")











