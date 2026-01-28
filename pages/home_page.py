from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.cart_tab= page.get_by_role("link", name="Cart")
        self.products_tab = page.get_by_role("link", name="Products")
        self.login_tab = page.get_by_role("link", name="Signup / Login")
        self.contact_us_tab = page.get_by_role("link", name="Contact us")
        self.test_cases_tab = page.get_by_role("link", name="Test Cases")
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
        self.men_category = page.get_by_role("link", name="Men")
        self.category_title_women = page.get_by_role("heading",name="Women - Dress Products")
        self.shirts_category = page.get_by_role("link", name="Tshirts")
















