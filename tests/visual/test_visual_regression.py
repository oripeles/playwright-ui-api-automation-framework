import pytest
import allure
from playwright.sync_api import expect

pytestmark = pytest.mark.visual


@allure.feature("Visual Regression")
class TestVisualRegression:

    @allure.title("Login page visual check")
    def test_login_page_visual(self, home):
        login = home.click_login_tab()
        expect(login.login_title).to_be_visible()

        expect(login.page).to_have_screenshot("login.png", max_diff_pixel_ratio=0.05)
