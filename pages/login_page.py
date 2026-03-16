from __future__ import annotations

from pages.account_info_page import AccountInfoPage
from pages.base_page import BasePage
from playwright.sync_api import Page


class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.new_user_signup_title = page.get_by_role("heading", name="New User Signup!")
        self.login_title = page.get_by_role("heading", name="Login to your account")
        self.name_input = page.locator("[data-qa='signup-name']")
        self.email_input = page.locator("[data-qa='signup-email']")
        self.password_input_login = page.locator("[data-qa='login-password']")
        self.email_input_login = page.locator("[data-qa='login-email']")
        self.signup_button = page.locator("[data-qa='signup-button']")
        self.login_button = page.locator("[data-qa='login-button']")
        self.login_error = page.get_by_text("Your email or password is incorrect!")
        self.email_exist_title = page.get_by_text("Email Address already exist!")

    def enter_name_and_email(self, name: str, email: str) -> None:
        self.name_input.fill(name)
        self.email_input.fill(email)

    def enter_email_and_password(self, email: str, password: str) -> None:
        self.email_input_login.fill(email)
        self.password_input_login.fill(password)

    def click_signup_button(self) -> AccountInfoPage:
        self.signup_button.click()
        return AccountInfoPage(self.page)

    def click_login_button(self) -> None:
        self.login_button.click()
