import pytest
import allure
from playwright.sync_api import expect
from tests.base_test import BaseTest
from utilities.json_loader import load_json

pytestmark = pytest.mark.regression

@allure.feature("Cart")
class TestRemoveProductsFromCart(BaseTest):

    @allure.title("Remove product from cart successfully")
    def test_remove_products_from_cart(self, home):
        products = load_json("products_data")["products"]
        product_name = products["first"]["name"]
        product_id = products["first"]["id"]
        with allure.step("Add product to cart"):
            product = home.click_product_tab()
            product.add_to_cart_by_name(product_name)
            product.continue_shopping()

        with allure.step("Remove product from cart"):
            cart = product.open_cart()
            cart.click_delete(product_id)

        with allure.step("Verify cart is empty"):
            expect(cart.empty_cart).to_be_visible()


