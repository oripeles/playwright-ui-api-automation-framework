import pytest
import allure
from playwright.sync_api import expect

pytestmark = pytest.mark.regression

@allure.feature("Categories")
class TestViewCategoryProducts:

    @allure.title("View products in Women > Dress category")
    def test_view_women_category_products(self, home):
        with allure.step("Verify sidebar is visible"):
            expect(home.left_sidebar).to_be_visible()

        with allure.step("Navigate to Women > Dress category"):
            home.click_women_category()
            home.click_dress_category()

        with allure.step("Verify category page"):
            expect(home.category_title_women).to_be_visible()

    @allure.title("View products in Men > Shirt category")
    def test_view_men_category_products(self, home):
        with allure.step("Verify sidebar is visible"):
            expect(home.left_sidebar).to_be_visible()

        with allure.step("Navigate to Men > Shirt category"):
            home.click_men_category()
            home.click_shirt_category()

        with allure.step("Verify category page"):
            expect(home.men_shirts_title).to_be_visible()

