import pytest
import allure
from playwright.sync_api import expect
from tests.base_test import BaseTest

pytestmark = pytest.mark.regression


@allure.feature("Negative Scenarios")
class TestNegativeScenarios(BaseTest):

    @allure.title("Empty cart shows no products")
    def test_empty_cart(self, home):
        with allure.step("Navigate to cart without adding products"):
            cart = home.go_to_cart()

        with allure.step("Verify cart is empty"):
            expect(cart.empty_cart).to_be_visible()

    @allure.title("Search with empty string shows no searched products title")
    def test_search_empty_string(self, home):
        with allure.step("Navigate to products page"):
            product_page = home.click_product_tab()
            expect(product_page.cases_title).to_be_visible()

        with allure.step("Search with empty string"):
            product_page.search_product_fill("")
            product_page.search_product_click()

        with allure.step("Verify searched products title is not visible"):
            expect(product_page.searched_products_title).not_to_be_visible()

    @allure.title("Checkout empty cart shows register/login message")
    def test_checkout_empty_cart_requires_login(self, home):
        with allure.step("Navigate to cart"):
            cart = home.go_to_cart()

        with allure.step("Verify proceed to checkout is not clickable"):
            expect(cart.proceed_to_checkout).not_to_be_visible()
