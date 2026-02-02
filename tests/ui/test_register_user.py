import os
import allure
from playwright.sync_api import expect
from utilities.email_generator import generate_unique_email

@allure.feature("Registration")

class TestRegisterUser:

    @allure.title("Register new user successfully and delete account")
    def test_register_user(self, home, existing_user):
        email = generate_unique_email()
        password = os.getenv("USER_PASSWORD")
        name = existing_user["name"]
        gender = "Mr"
        date_data = {
            "day": 10,
            "month": "January",
            "year": "2000"
        }
        address_data = {
            "first": "Ori",
            "last": "Peles",
            "company": "global",
            "addr1": "123 Test Street",
            "addr2": "Building 4",
            "country": "Israel",
            "state": "Center",
            "city": "Petah Tikva",
            "zipcode": "4950000",
            "mobile": "0501234567"
        }

        login = home.click_login_tab()
        expect(login.new_user_signup_title).to_be_visible()
        login.enter_name_and_email(name, email)
        info = login.click_signup_button()
        expect(info.enter_account_info_title).to_be_visible()
        info.select_title(gender)
        info.fill_password(password)
        info.select_date(**date_data)
        info.select_newsletter()
        info.select_optin()
        info.fill_details(**address_data)
        created = info.click_create_account()
        expect(created.account_created_title).to_be_visible()
        created.click_continue()
        expect(home.logged_in_user).to_be_visible()
        expect(home.logged_in_user).to_have_text(f"Logged in as {name}")
        delete_account =  home.click_delete_account()
        delete_account.click_continue()
        expect(home.login_tab).to_be_visible()
        expect(home.login_tab).to_have_text("Signup / Login")






