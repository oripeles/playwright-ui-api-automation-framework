import pytest
import allure
from playwright.sync_api import expect

pytestmark = pytest.mark.regression

@allure.feature("Contact Us")
class TestContactUsForm:

    @allure.title("Submit contact us form successfully with valid details")
    def test_contact_us_form(self, home, existing_user):
        details_data = {
            "name": "Test User",
            "email": existing_user["email"],
            "subject": "QA Automation",
            "message": "123 Test"
        }
        with allure.step("Navigate to Contact Us page"):
            contact = home.click_contact_us_tab()
            expect(contact.get_in_touch_title).to_be_visible()

        with allure.step("Fill and submit form"):
            contact.fill_details(**details_data)
            contact.click_submit()

        with allure.step("Verify redirect to home"):
            contact.click_home()

