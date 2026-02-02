import allure
from playwright.sync_api import expect

@allure.feature("Subscription")
class TestSubscriptionFromCart:

    @allure.title("Subscribe successfully from cart page")
    def test_subscription_card(self, home, existing_user):
        email = existing_user["email"]
        cart = home.go_to_cart()
        cart.scroll_down_to_footer()
        expect(cart.subscription_title).to_be_visible()
        cart.subscribe(email)
