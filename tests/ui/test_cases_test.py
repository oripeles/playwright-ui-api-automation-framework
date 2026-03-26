import pytest
import allure
from playwright.sync_api import expect
from tests.base_test import BaseTest

pytestmark = pytest.mark.regression

@allure.feature("Test Cases")
class TestCasesTest(BaseTest):

    @allure.title("Verify test cases page is accessible and title is visible")
    def test_cases_test(self, home):
        with allure.step("Navigate to Test Cases page"):
            cases = home.click_test_cases_tab()

        with allure.step("Verify page title"):
            expect(cases.cases_title).to_be_visible()
            expect(cases.cases_title).to_have_text("Test Cases")