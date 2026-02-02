import allure
from playwright.sync_api import expect

@allure.feature("Cart")
class TestVerifyProductQuantityInCart:

    @allure.title("Add product with specific quantity and verify it appears in cart")
    def test_verify_product_quantity_in_cart(self, home):
        qty = 4
        number_product = 1
        product = home.click_view_product(number_product)
        product.set_quantity(qty)
        product.click_add_to_cart()
        product.click_continue_shopping()
        cart = home.go_to_cart()
        expect(cart.quantities).to_have_text(str(qty))


