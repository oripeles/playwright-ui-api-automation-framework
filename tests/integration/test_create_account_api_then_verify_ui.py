import pytest
import allure
from playwright.sync_api import expect
from tests.base_test import BaseTest
from utilities.email_generator import generate_unique_email
from utilities.json_loader import load_json


@allure.feature("Account")
class TestCreateAccountApiThenVerifyUi(BaseTest):

    @pytest.mark.integration
    @allure.title("Integration: Create account via API then login via UI")
    def test_create_account_api_login_ui(self, auth_client, home, user_password):
        reg = load_json("account_data")["registration"]
        email = generate_unique_email()
        password = user_password

        create_payload = {
            "name": reg["name"],
            "email": email,
            "password": password,
            "title": reg["gender"],
            "birth_date": reg["birth_date"],
            "birth_month": reg["birth_month_num"],
            "birth_year": reg["birth_year"],
            "firstname": reg["first"],
            "lastname": reg["last"],
            "company": reg["company"],
            "address1": reg["addr1"],
            "address2": reg["addr2"],
            "country": reg["country"],
            "zipcode": reg["zipcode"],
            "state": reg["state"],
            "city": reg["city"],
            "mobile_number": reg["mobile"],
        }

        with allure.step("Create account via API"):
            res = auth_client.create_account(create_payload)
            data = res.json()
            assert data["responseCode"] == 201, f"Expected 201, got {data['responseCode']}"

        with allure.step("Login via UI with the new account"):
            login = home.click_login_tab()
            expect(login.login_title).to_be_visible()
            login.enter_email_and_password(email, password)
            login.click_login_button()

        with allure.step("Verify logged in as the new user"):
            expect(home.logout_tab).to_be_visible()

        with allure.step("Cleanup: delete account via API"):
            del_res = auth_client.delete_account(email, password)
            del_data = del_res.json()
            assert del_data["responseCode"] == 200
