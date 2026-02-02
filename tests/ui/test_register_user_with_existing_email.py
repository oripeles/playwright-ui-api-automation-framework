import allure
from playwright.sync_api import expect

@allure.feature("Registration")
class TestRegisterUserWithExistingEmail:

    @allure.title("Registration fails when using an existing email")
    def test_register_user_with_existing_email(self, home, existing_user):
        email = existing_user["email"]
        name = existing_user["name"]
        login = home.click_login_tab()
        expect(login.new_user_signup_title).to_be_visible()
        login.enter_name_and_email(name, email)
        login.click_signup_button()
        expect(login.email_exist_title).to_be_visible()