import pytest
import allure
from playwright.sync_api import expect

pytestmark = pytest.mark.regression

@allure.feature("Products")
class TestVerifyAllProductsDetail:

    @allure.title("Verify product details page is accessible from all products list")
    def test_verify_all_products_detail(self, home):
        with allure.step("Navigate to products page"):
            product = home.click_product_tab()
            expect(product.cases_title).to_be_visible()

        with allure.step("Click on product to view details"):
            expect(product.view_product.first).to_be_visible()
            product.click_product_view()
