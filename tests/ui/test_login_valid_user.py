import os
import pytest
import allure
from playwright.sync_api import expect

@allure.feature("Login")
class TestLoginValidUser:

    @pytest.mark.smoke
    @allure.title("Login successfully with valid credentials")
    def test_login_valid_user(self, home, existing_user,user_password):
        password = user_password
        email = existing_user["email"]
        login = home.click_login_tab()
        expect(login.login_title).to_be_visible()
        expect(login.login_title).to_have_text("Login to your account")
        login.enter_email_and_password(email, password)
        login.click_login_button()
        expect(home.logout_tab).to_be_visible()
        expect(home.logout_tab).to_have_text("Logout")

