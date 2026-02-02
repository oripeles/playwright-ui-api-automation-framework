import allure
from playwright.sync_api import expect

@allure.feature("Subscription")
class TestSubscription:

    @allure.title("Subscribe successfully from home page")
    def test_subscription_from_home_page(self, home, existing_user):
        email = existing_user["email"]
        home.scroll_down()
        expect(home.subscription_title).to_be_visible()
        home.subscribe(email)
        expect(home.subscription_success).to_be_visible()
