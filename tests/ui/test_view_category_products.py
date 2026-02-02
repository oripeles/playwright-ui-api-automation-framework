import allure
from playwright.sync_api import expect

@allure.feature("Categories")
class TestViewCategoryProducts:

    @allure.title("View products in Women > Dress category")
    def test_view_women_category_products(self, home):
        expect(home.left_sidebar).to_be_visible()
        home.click_women_category()
        home.click_dress_category()
        expect(home.category_title_women).to_be_visible()

    @allure.title("View products in Men > Shirt category")
    def test_view_men_category_products(self, home):
        expect(home.left_sidebar).to_be_visible()
        home.click_men_category()
        home.click_shirt_category()
        expect(home.men_shirts_title).to_be_visible()

