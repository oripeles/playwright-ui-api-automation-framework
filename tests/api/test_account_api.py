import pytest
import allure
from utilities.email_generator import generate_unique_email
from utilities.json_loader import load_json

pytestmark = pytest.mark.regression

def test_create_account_success(auth_client, user_password):
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
        create_res = auth_client.create_account(create_payload)
        create_data = create_res.json()
        assert create_data["responseCode"] == 201, f"Expected responseCode 201, got {create_data['responseCode']}"

    with allure.step("Delete account via API"):
        delete_res = auth_client.delete_account(email, password)
        delete_data = delete_res.json()
        assert delete_data["responseCode"] == 200, f"Expected responseCode 200, got {delete_data['responseCode']}"
        assert "deleted" in delete_data["message"].lower(), f"Expected 'deleted' in message, got: {delete_data['message']}"
