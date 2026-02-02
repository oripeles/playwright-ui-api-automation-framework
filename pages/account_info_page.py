from pages.account_created_page import AccountCreatedPage
from pages.base_page import BasePage

class AccountInfoPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.enter_account_info_title = page.get_by_text("Enter Account Information")
        self.title_mr = page.locator("#id_gender1")
        self.title_mrs = page.locator("#id_gender2")
        self.password_input = page.locator("#password")
        self.days_select = page.locator("#days")
        self.months_select = page.locator("#months")
        self.years_select = page.locator("#years")
        self.newsletter_checkbox = page.locator("#newsletter")
        self.optin_checkbox = page.locator("#optin")
        self.first_name_input = page.locator("#first_name")
        self.last_name_input = page.locator("#last_name")
        self.company_input = page.locator("#company")
        self.address1_input = page.locator("#address1")
        self.address2_input = page.locator("#address2")
        self.country_select = page.locator("#country")
        self.state_input = page.locator("#state")
        self.city_input = page.locator("#city")
        self.zipcode_input = page.locator("#zipcode")
        self.mobile_input = page.locator("#mobile_number")
        self.create_account_button = page.locator("[data-qa='create-account']")

    def select_title(self, title):
            if title == "Mr":
                self.title_mr.check()
            elif title == "Mrs":
                self.title_mrs.check()
            else:
                raise ValueError("Title must be 'Mr' or 'Mrs'")

    def fill_password(self, password):
        self.password_input.fill(password)

    def select_date(self, day, month, year):
        self.days_select.select_option(str(day))
        self.years_select.select_option(str(year))
        self.months_select.select_option(label=month)

    def select_newsletter(self):
        self.newsletter_checkbox.check()

    def select_optin(self):
        self.optin_checkbox.check()

    def fill_details(self, first, last, company, addr1, addr2, country, state, city, zipcode, mobile):
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

    def click_create_account(self):
        self.create_account_button.click()
        return AccountCreatedPage(self.page)






