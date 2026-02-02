import allure
from playwright.sync_api import expect

@allure.feature("Cart")
class TestRemoveProductsFromCart:

    @allure.title("Remove product from cart successfully")
    def test_remove_products_from_cart(self, home):
        product_name = "Blue Top"
        product_id = 1
        product = home.click_product_tab()
        product.add_to_cart_by_name(product_name)
        product.continue_shopping()
        cart = product.open_cart()
        cart.click_delete(product_id)
        expect(cart.empty_cart).to_be_visible()


