import allure
from playwright.sync_api import expect

@allure.feature("Search")
class TestSearchProduct:

    @allure.title("Search for product and verify relevant results are displayed")
    def test_search_product(self, home):
        product_search = "Men Tshirt"
        product = home.click_product_tab()
        expect(product.cases_title).to_be_visible()
        product.search_product_fill(product_search)
        product.search_product_click()
        expect(product.searched_products_title).to_be_visible()
        expect(product.view_product_result).to_contain_text(product.get_search_value())
