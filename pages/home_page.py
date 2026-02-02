from pages.account_deleted_page import AccountDeletedPage
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.cases_page import CasesPage
from pages.contact_us_form_page import ContactUsFormPage
from pages.login_page import LoginPage
from pages.product_detail_page import ProductsDetailPage
from pages.products_page import ProductsPage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.cart_tab= page.get_by_role("link", name="Cart")
        self.products_tab = page.get_by_role("link", name="Products")
        self.login_tab = page.get_by_role("link", name="Signup / Login")
        self.contact_us_tab = page.get_by_role("link", name="Contact us")
        self.test_cases_tab = page.get_by_role("link", name="Test Cases", exact=True)
        self.logout_tab = page.get_by_role("link", name="Logout")
        self.logged_in_user = page.get_by_text("Logged in as")
        self.active_tab = page.locator("*[style*='color: orange']")
        self.delete_account_tab = page.get_by_role("link", name="Delete Account")
        self.subscription_title = page.get_by_role("heading", name="Subscription")
        self.subscription_button = page.locator("#subscribe")
        self.subscription_success = page.get_by_text("You have been successfully subscribed!")
        self.women_category = page.get_by_role("link", name="Women")
        self.dress_category = page.get_by_role("link", name="Dress")
        self.category_title_men = page.locator("li.active", has_text="Men > Tshirts")
        self.view_product = page.get_by_role("link", name="View Product")
        self.left_sidebar = page.locator(".left-sidebar")
        self.subscription_input = page.locator("#susbscribe_email")
        self.men_category = page.locator("a[href='#Men']")
        self.category_title_women = page.get_by_role("heading",name="Women - Dress Products")
        self.men_shirts_title = page.get_by_role("heading", name="Men - Tshirts Products")
        self.shirts_category = page.get_by_role("link", name="Tshirts")

    def click_login_tab(self):
        self.login_tab.click()
        return LoginPage(self.page)

    def click_logout_tab(self):
        self.logout_tab.click()
        return LoginPage(self.page)

    def click_contact_us_tab(self):
        self.contact_us_tab.click()
        return ContactUsFormPage(self.page)

    def click_delete_account(self):
        self.delete_account_tab.click()
        return AccountDeletedPage(self.page)

    def click_test_cases_tab(self):
        self.test_cases_tab.click()
        return CasesPage(self.page)

    def click_product_tab(self):
        self.products_tab.click()
        return ProductsPage(self.page)

    def click_view_product(self, index):
        self.view_product.nth(index).click()
        return ProductsDetailPage(self.page)

    def go_to_cart(self):
        self.cart_tab.click()
        return CartPage(self.page)

    def scroll_down(self):
        self.scroll_to_bottom()

    def subscribe(self, email):
        self.subscription_input.fill(email)
        self.subscription_button.click()

    def click_women_category(self):
        self.women_category.click()

    def click_dress_category(self):
        self.dress_category.click()

    def click_men_category(self):
        self.men_category.click()

    def click_shirt_category(self):
        self.shirts_category.click()

    def get_logged_in_as_text(self):
        return self.logged_in_user.inner_text().strip()














