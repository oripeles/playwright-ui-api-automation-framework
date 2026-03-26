import pytest
import allure
from playwright.sync_api import expect
from tests.base_test import BaseTest

pytestmark = pytest.mark.regression

@allure.feature("Registration")
class TestRegisterUserWithExistingEmail(BaseTest):

    @allure.title("Registration fails when using an existing email")
    def test_register_user_with_existing_email(self, home, existing_user):
        email = existing_user["email"]
        name = existing_user["name"]
        with allure.step("Navigate to signup page"):
            login = home.click_login_tab()
            expect(login.new_user_signup_title).to_be_visible()

        with allure.step("Attempt registration with existing email"):
            login.enter_name_and_email(name, email)
            login.click_signup_button()

        with allure.step("Verify error message is displayed"):
            expect(login.email_exist_title).to_be_visible()