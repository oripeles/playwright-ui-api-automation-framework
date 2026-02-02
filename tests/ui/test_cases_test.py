import allure
from playwright.sync_api import expect

@allure.feature("Test Cases")
class TestCasesTest:

    @allure.title("Verify test cases page is accessible and title is visible")
    def test_cases_test(self, home):
        cases = home.click_test_cases_tab()
        expect(cases.cases_title).to_be_visible()
        expect(cases.cases_title).to_have_text("Test Cases")