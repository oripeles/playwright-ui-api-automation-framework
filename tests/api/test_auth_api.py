import pytest
import allure
from tests.api.helpers.assertions import assert_missing_required_parameter, assert_method_not_supported

pytestmark = pytest.mark.regression

def test_verify_login_invalid_password(auth_client, existing_user):
    with allure.step("Send login request with wrong password"):
        res = auth_client.verify_login(existing_user["email"], "wrong_password_123")
        data = res.json()
        assert data["responseCode"] == 404, f"Expected responseCode 404, got {data['responseCode']}"

def test_verify_login_missing_email(auth_client, user_password):
    with allure.step("Send login request without email"):
        res = auth_client.verify_login_without_email(user_password)
        assert_missing_required_parameter(res)

def test_verify_login_delete_method_not_supported(auth_client):
    with allure.step("Send DELETE request to verify login endpoint"):
        res = auth_client.delete_verify_login()
        assert_method_not_supported(res)

def test_verify_login_invalid_password_user_not_found(auth_client, existing_user):
    with allure.step("Send login request with wrong password and verify error message"):
        res = auth_client.verify_login(existing_user["email"], "wrong_password_123")
        data = res.json()
        assert data["responseCode"] == 404, f"Expected responseCode 404, got {data['responseCode']}"
        assert "not found" in data["message"].lower(), f"Expected 'not found' in message, got: {data['message']}"

def test_get_user_detail_by_email(auth_client, existing_user):
    with allure.step("Get user detail by email"):
        res = auth_client.get_user_detail_by_email(existing_user["email"])
        data = res.json()
        assert data["responseCode"] == 200, f"Expected responseCode 200, got {data['responseCode']}"
        assert "user" in data, "Response missing 'user' key"

    with allure.step("Verify user email matches"):
        user = data["user"]
        assert user["email"] == existing_user["email"], f"Expected email '{existing_user['email']}', got '{user['email']}'"
