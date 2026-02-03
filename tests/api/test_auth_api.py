from tests.api.helpers.assertions import assert_missing_required_parameter, assert_method_not_supported


def test_verify_login_valid_details(auth_client, existing_user,user_password):
    password = user_password
    res = auth_client.verify_login(existing_user["email"], password)
    print("EMAIL:", existing_user["email"])
    print("PW_LEN:", len(user_password))
    data = res.json()
    print(data)
    assert data["responseCode"] == 200
    assert "exists" in data["message"].lower()

def test_verify_login_invalid_password(auth_client, existing_user):
    res = auth_client.verify_login(existing_user["email"], "wrong_password_123")
    data = res.json()
    assert data["responseCode"] == 404

def test_verify_login_missing_email(auth_client, user_password):
    res = auth_client.verify_login_without_email(user_password)
    assert_missing_required_parameter(res)

def test_verify_login_delete_method_not_supported(auth_client):
    res = auth_client.delete_verify_login()
    assert_method_not_supported(res)

def test_verify_login_invalid_password_user_not_found(auth_client, existing_user):
    res = auth_client.verify_login(existing_user["email"], "wrong_password_123")
    data = res.json()

    assert data["responseCode"] == 404
    assert "not found" in data["message"].lower()

def test_get_user_detail_by_email(auth_client, existing_user):
    res = auth_client.get_user_detail_by_email(existing_user["email"])
    data = res.json()

    assert data["responseCode"] == 200
    assert "user" in data

    user = data["user"]
    assert user["email"] == existing_user["email"]


