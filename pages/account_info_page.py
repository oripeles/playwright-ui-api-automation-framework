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
        self.create_account_button = page.locator("button[data-qa='create-account']")






