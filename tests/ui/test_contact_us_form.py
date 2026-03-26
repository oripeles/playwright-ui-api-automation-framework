import pytest
import allure
from playwright.sync_api import expect
from tests.base_test import BaseTest
from utilities.json_loader import load_json

pytestmark = pytest.mark.regression

@allure.feature("Contact Us")
class TestContactUsForm(BaseTest):

    @allure.title("Submit contact us form successfully with valid details")
    def test_contact_us_form(self, home, existing_user):
        contact_data = load_json("account_data")["contact_us"]
        details_data = {
            "name": contact_data["name"],
            "email": existing_user["email"],
            "subject": contact_data["subject"],
            "message": contact_data["message"]
        }
        with allure.step("Navigate to Contact Us page"):
            contact = home.click_contact_us_tab()
            expect(contact.get_in_touch_title).to_be_visible()

        with allure.step("Fill and submit form"):
            contact.fill_details(**details_data)
            contact.click_submit()

        with allure.step("Verify redirect to home"):
            contact.click_home()

