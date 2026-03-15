import pytest
import allure
from playwright.sync_api import expect

pytestmark = pytest.mark.regression

@allure.feature("Subscription")
class TestSubscriptionFromCart:

    @allure.title("Subscribe successfully from cart page")
    def test_subscription_card(self, home, existing_user):
        email = existing_user["email"]
        with allure.step("Navigate to cart"):
            cart = home.go_to_cart()

        with allure.step("Scroll to subscription section"):
            cart.scroll_down_to_footer()
            expect(cart.subscription_title).to_be_visible()

        with allure.step("Subscribe with email"):
            cart.subscribe(email)
