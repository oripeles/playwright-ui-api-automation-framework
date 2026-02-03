from utilities.email_generator import generate_unique_email

def test_create_account_success(auth_client):
    email =  generate_unique_email,
    password = "Password123!"

    create_payload = {
        "name": "Ori Peles",
        "email": email,
        "password": password,
        "title": "Mr",
        "birth_date": "10",
        "birth_month": "1",
        "birth_year": "2000",
        "firstname": "Ori",
        "lastname": "Peles",
        "company": "global",
        "address1": "123 Test Street",
        "address2": "Building 4",
        "country": "Israel",
        "zipcode": "4950000",
        "state": "Center",
        "city": "Petah Tikva",
        "mobile_number": "0501234567",
    }

    create_res = auth_client.create_account(create_payload)
    create_data = create_res.json()
    assert create_data["responseCode"] == 201

    delete_res = auth_client.delete_account(email, password)
    delete_data = delete_res.json()

    assert delete_data["responseCode"] == 200
    assert "deleted" in delete_data["message"].lower()

