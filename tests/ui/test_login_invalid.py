import pytest
import allure
from utilities.json_loader import load_json
from playwright.sync_api import expect

@allure.feature("Login")
@allure.title("Login fails with invalid credentials")
@pytest.mark.parametrize(
    "case",
    load_json("invalid_logins")
)
def test_login_invalid_user(home, case):
        login = home.click_login_tab()
        expect(login.login_title).to_be_visible()
        login.enter_email_and_password(
            case["email"],
            case["password"]
        )
        login.click_login_button()
        expect(login.login_error).to_be_visible()
        expect(login.login_error).to_have_text("Your email or password is incorrect!")