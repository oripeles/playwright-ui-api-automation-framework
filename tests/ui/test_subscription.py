import pytest
import allure
from playwright.sync_api import expect

pytestmark = pytest.mark.regression

@allure.feature("Subscription")
class TestSubscription:

    @allure.title("Subscribe successfully from home page")
    def test_subscription_from_home_page(self, home, existing_user):
        email = existing_user["email"]
        with allure.step("Scroll to subscription section"):
            home.scroll_down()
            expect(home.subscription_title).to_be_visible()

        with allure.step("Subscribe with email"):
            home.subscribe(email)

        with allure.step("Verify success message"):
            expect(home.subscription_success).to_be_visible()
