import pytest
import allure
from playwright.sync_api import expect
from utilities.email_generator import generate_unique_email
from tests.base_test import BaseTest
from utilities.json_loader import load_json

pytestmark = pytest.mark.regression

@allure.feature("Registration")
class TestRegisterUser(BaseTest):

    @allure.title("Register new user successfully and delete account")
    def test_register_user(self, home, existing_user, user_password):
        reg = load_json("account_data")["registration"]
        email = generate_unique_email()
        password = user_password
        name = reg["name"]
        gender = reg["gender"]
        date_data = {
            "day": int(reg["birth_date"]),
            "month": reg["birth_month"],
            "year": reg["birth_year"]
        }
        address_data = {
            "first": reg["first"],
            "last": reg["last"],
            "company": reg["company"],
            "addr1": reg["addr1"],
            "addr2": reg["addr2"],
            "country": reg["country"],
            "state": reg["state"],
            "city": reg["city"],
            "zipcode": reg["zipcode"],
            "mobile": reg["mobile"]
        }

        with allure.step("Navigate to signup page"):
            login = home.click_login_tab()
            expect(login.new_user_signup_title).to_be_visible()
            login.enter_name_and_email(name, email)
            info = login.click_signup_button()

        with allure.step("Fill account information"):
            expect(info.enter_account_info_title).to_be_visible()
            info.select_title(gender)
            info.fill_password(password)
            info.select_date(**date_data)
            info.select_newsletter()
            info.select_optin()
            info.fill_details(**address_data)

        with allure.step("Verify account created"):
            created = info.click_create_account()
            created.wait_until_stable()
            expect(created.account_created_title).to_be_visible(timeout=15000)
            created.click_continue()
            home.wait_until_stable()
            expect(home.logged_in_user).to_be_visible(timeout=10000)
            expect(home.logged_in_user).to_have_text(f"Logged in as {name}")

        with allure.step("Delete account"):
            delete_account = home.click_delete_account()
            delete_account.wait_until_stable()
            delete_account.click_continue()
            home.wait_until_stable()
            expect(home.login_tab).to_be_visible(timeout=10000)
            expect(home.login_tab).to_have_text("Signup / Login")
