import pytest
import allure
from playwright.sync_api import expect
from tests.base_test import BaseTest
from utilities.json_loader import load_json

pytestmark = pytest.mark.regression

@allure.feature("Search")
class TestSearchProduct(BaseTest):

    @pytest.mark.smoke
    @allure.title("Search for product and verify relevant results are displayed")
    def test_search_product(self, home):
        product_search = load_json("products_data")["products"]["second"]["name"]
        with allure.step("Navigate to products page"):
            product = home.click_product_tab()
            expect(product.cases_title).to_be_visible()

        with allure.step("Search for product"):
            product.search_product_fill(product_search)
            product.search_product_click()

        with allure.step("Verify search results"):
            expect(product.searched_products_title).to_be_visible()
            expect(product.view_product_result).to_contain_text(product.get_search_value())
