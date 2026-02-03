import pytest
import allure
from playwright.sync_api import expect


@allure.feature("Login")
class TestLoginApiUi:

    @pytest.mark.integration
    @pytest.mark.smoke
    @allure.title("Integration: API verify login + UI login with same user")
    def test_login_valid_user_api_then_ui(self, auth_client, home, existing_user, user_password):
        email = existing_user["email"]
        password = user_password
        res = auth_client.verify_login(email, password)
        assert res.status == 200, f"Expected HTTP 200, got {res.status}"
        data = res.json()
        assert data["responseCode"] == 200
        assert "exists" in data["message"].lower()
        login = home.click_login_tab()
        expect(login.login_title).to_be_visible()
        expect(login.login_title).to_have_text("Login to your account")
        login.enter_email_and_password(email, password)
        login.click_login_button()
        expect(home.logout_tab).to_be_visible()
        expect(home.logout_tab).to_have_text("Logout")