import pytest
import allure
from playwright.sync_api import expect

pytestmark = pytest.mark.regression

@allure.feature("Cart")
class TestVerifyProductQuantityInCart:

    @allure.title("Add product with specific quantity and verify it appears in cart")
    def test_verify_product_quantity_in_cart(self, home):
        qty = 4
        number_product = 1
        with allure.step("Set product quantity and add to cart"):
            product = home.click_view_product(number_product)
            product.set_quantity(qty)
            product.click_add_to_cart()
            product.click_continue_shopping()

        with allure.step("Verify quantity in cart"):
            cart = home.go_to_cart()
            expect(cart.quantities).to_have_text(str(qty))


