import pytest
import allure
from playwright.sync_api import expect

@allure.feature("Cart")
class TestAddProductsInCart:

    @pytest.mark.smoke
    @allure.title("Add two products to cart and verify price and quantity")
    def test_add_products_in_cart(self, home):
        expected_first_price = "Rs. 500"
        expected_second_price = "Rs. 400"
        expected_first_qty = "1"
        expected_second_qty = "1"
        first_product_name = "Blue Top"
        second_product_name = "Men Tshirt"
        product = home.click_product_tab()
        product.add_to_cart_by_name(first_product_name)
        product.continue_shopping()
        product.add_to_cart_by_name(second_product_name)
        product.continue_shopping()
        cart = product.open_cart()
        expect(cart.price_by_product_name(first_product_name)).to_have_text(expected_first_price)
        expect(cart.price_by_product_name(second_product_name)).to_have_text(expected_second_price)
        expect(cart.quantity_by_product_name(first_product_name)).to_have_text(expected_first_qty)
        expect(cart.quantity_by_product_name(second_product_name)).to_have_text(expected_second_qty)

