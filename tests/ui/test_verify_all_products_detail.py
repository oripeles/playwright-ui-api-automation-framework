import allure
from playwright.sync_api import expect

@allure.feature("Products")
class TestVerifyAllProductsDetail:

    @allure.title("Verify product details page is accessible from all products list")
    def test_verify_all_products_detail(self, home):
        product = home.click_product_tab()
        expect(product.cases_title).to_be_visible()
        expect(product.view_product.first).to_be_visible()
        product.click_product_view()
