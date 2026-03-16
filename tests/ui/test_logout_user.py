import pytest
import allure
from playwright.sync_api import expect

pytestmark = pytest.mark.regression

@allure.feature("Login")
class TestLogoutUser:

    @allure.title("Logout successfully and return to login page")
    def test_logout_user(self, home, existing_user,user_password):
        password = user_password
        email = existing_user["email"]
        with allure.step("Login with valid credentials"):
            login_page = home.click_login_tab()
            expect(login_page.login_title).to_be_visible()
            expect(login_page.login_title).to_have_text("Login to your account")
            login_page.enter_email_and_password(email, password)
            login_page.click_login_button()

        with allure.step("Logout and verify redirect to login page"):
            home.click_logout_tab()
            expect(login_page.login_title).to_be_visible()
            expect(home.login_tab).to_be_visible()


