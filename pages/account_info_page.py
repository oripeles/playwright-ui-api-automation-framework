from __future__ import annotations

from pages.account_created_page import AccountCreatedPage
from pages.base_page import BasePage, logger
from playwright.sync_api import Page


class AccountInfoPage(BasePage):
    """Account registration form page."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.enter_account_info_title = page.get_by_text("Enter Account Information")
        self.title_mr = page.locator("#id_gender1")
        self.title_mrs = page.locator("#id_gender2")
        self.password_input = page.locator("[data-qa='password']")
        self.days_select = page.locator("[data-qa='days']")
        self.months_select = page.locator("[data-qa='months']")
        self.years_select = page.locator("[data-qa='years']")
        self.newsletter_checkbox = page.locator("#newsletter")
        self.optin_checkbox = page.locator("#optin")
        self.first_name_input = page.locator("[data-qa='first_name']")
        self.last_name_input = page.locator("[data-qa='last_name']")
        self.company_input = page.locator("[data-qa='company']")
        self.address1_input = page.locator("[data-qa='address']")
        self.address2_input = page.locator("[data-qa='address2']")
        self.country_select = page.locator("[data-qa='country']")
        self.state_input = page.locator("[data-qa='state']")
        self.city_input = page.locator("[data-qa='city']")
        self.zipcode_input = page.locator("[data-qa='zipcode']")
        self.mobile_input = page.locator("[data-qa='mobile_number']")
        self.create_account_button = page.locator("[data-qa='create-account']")

    def select_title(self, title: str) -> None:
        """Select Mr or Mrs title radio button."""
        logger.info("Selecting title: %s", title)
        if title == "Mr":
            self.title_mr.check()
        elif title == "Mrs":
            self.title_mrs.check()
        else:
            raise ValueError("Title must be 'Mr' or 'Mrs'")

    def fill_password(self, password: str) -> None:
        """Fill in the account password."""
        logger.info("Filling password")
        self.password_input.fill(password)

    def select_date(self, day: int, month: str, year: int) -> None:
        """Select date of birth from dropdowns."""
        logger.info("Selecting DOB: %s/%s/%s", day, month, year)
        self.days_select.select_option(str(day))
        self.years_select.select_option(str(year))
        self.months_select.select_option(label=month)

    def select_newsletter(self) -> None:
        """Check the newsletter checkbox."""
        self.newsletter_checkbox.check()

    def select_optin(self) -> None:
        """Check the special offers opt-in checkbox."""
        self.optin_checkbox.check()

    def fill_details(self, first: str, last: str, company: str, addr1: str, addr2: str, country: str, state: str, city: str, zipcode: str, mobile: str) -> None:
        """Fill in all address and personal details."""
        logger.info("Filling details: %s %s, %s, %s", first, last, city, country)
        self.first_name_input.fill(first)
        self.last_name_input.fill(last)
        self.company_input.fill(company)
        self.address1_input.fill(addr1)
        self.address2_input.fill(addr2)
        self.country_select.select_option(label=country)
        self.state_input.fill(state)
        self.city_input.fill(city)
        self.zipcode_input.fill(zipcode)
        self.mobile_input.fill(mobile)

    def click_create_account(self) -> AccountCreatedPage:
        """Click 'Create Account' and return AccountCreatedPage."""
        logger.info("Clicking Create Account")
        self.create_account_button.click()
        return AccountCreatedPage(self.page)
