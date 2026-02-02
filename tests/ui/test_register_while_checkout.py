import allure
from playwright.sync_api import expect

@allure.feature("Checkout")
class TestRegisterCheckout:

    @allure.title("Redirect to login page when checking out as a guest")
    def test_register_while_checkout_redirects_to_login(self, home):
        product_name = "Blue Top"
        product = home.click_product_tab()
        product.add_to_cart_by_name(product_name)
        product.continue_shopping()
        cart = product.open_cart()
        cart.click_checkout()
        expect(cart.register_login_message).to_be_visible()
        cart.click_login()


