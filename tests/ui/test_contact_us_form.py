import allure
from playwright.sync_api import expect

@allure.feature("Contact Us")
class TestContactUsForm:

    @allure.title("Submit contact us form successfully with valid details")
    def test_contact_us_form(self, home, existing_user):
        details_data = {
            "name": "Ori peles",
            "email": existing_user["email"],
            "subject": "QA Automation",
            "message": "123 Test"
        }
        contact = home.click_contact_us_tab()
        expect(contact.get_in_touch_title).to_be_visible()
        contact.fill_details(**details_data)
        contact.click_submit()
        contact.click_home()

