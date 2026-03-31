import pytest
import allure
from playwright.sync_api import expect
from tests.base_test import BaseTest


@allure.feature("Search")
class TestSearchProductApiThenUi(BaseTest):

    @pytest.mark.integration
    @allure.title("Integration: Search product via API then verify in UI")
    def test_search_product_api_then_ui(self, products_client, home):
        search_term = "top"

        with allure.step("Search product via API and get results"):
            res = products_client.search_product(search_term)
            data = res.json()
            assert data["responseCode"] == 200, f"Expected 200, got {data['responseCode']}"
            api_products = data["products"]
            assert len(api_products) > 0, "API returned no products"
            api_product_name = api_products[0]["name"]

        with allure.step("Search same term in UI"):
            product_page = home.click_product_tab()
            product_page.search_product_fill(search_term)
            product_page.search_product_click()

        with allure.step("Verify API product appears in UI results"):
            expect(product_page.searched_products_title).to_be_visible()
            matching_product = product_page.view_product_result.filter(has_text=api_product_name)
            expect(matching_product.first).to_be_visible()
