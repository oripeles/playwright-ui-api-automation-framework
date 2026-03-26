import pytest
import allure
from playwright.sync_api import expect
from tests.base_test import BaseTest
from utilities.json_loader import load_json

@allure.feature("Cart")
class TestAddProductsInCart(BaseTest):

    @pytest.mark.smoke
    @allure.title("Add two products to cart and verify price and quantity")
    def test_add_products_in_cart(self, home):
        products = load_json("products_data")["products"]
        first_product_name = products["first"]["name"]
        second_product_name = products["second"]["name"]
        expected_first_price = products["first"]["price"]
        expected_second_price = products["second"]["price"]
        expected_first_qty = products["first"]["quantity"]
        expected_second_qty = products["second"]["quantity"]
        with allure.step("Add products to cart"):
            product = home.click_product_tab()
            product.add_to_cart_by_name(first_product_name)
            product.continue_shopping()
            product.add_to_cart_by_name(second_product_name)
            product.continue_shopping()

        with allure.step("Verify prices and quantities in cart"):
            cart = product.open_cart()
            expect(cart.price_by_product_name(first_product_name)).to_have_text(expected_first_price)
            expect(cart.price_by_product_name(second_product_name)).to_have_text(expected_second_price)
            expect(cart.quantity_by_product_name(first_product_name)).to_have_text(expected_first_qty)
            expect(cart.quantity_by_product_name(second_product_name)).to_have_text(expected_second_qty)

