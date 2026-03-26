from __future__ import annotations

from pages.account_deleted_page import AccountDeletedPage
from pages.base_page import BasePage, logger
from pages.cart_page import CartPage
from pages.cases_page import CasesPage
from pages.contact_us_form_page import ContactUsFormPage
from pages.login_page import LoginPage
from pages.product_detail_page import ProductsDetailPage
from pages.products_page import ProductsPage
from playwright.sync_api import Page


class HomePage(BasePage):
    """Main landing page with navigation to all site sections."""

    def __init__(self, page: Page) -> None:
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
        self.category_title_women = page.get_by_role("heading", name="Women - Dress Products")
        self.men_shirts_title = page.get_by_role("heading", name="Men - Tshirts Products")
        self.shirts_category = page.get_by_role("link", name="Tshirts")

    def click_login_tab(self) -> LoginPage:
        """Click 'Signup / Login' nav link and return LoginPage."""
        logger.info("Navigating to Login page")
        self.login_tab.click()
        return LoginPage(self.page)

    def click_logout_tab(self) -> LoginPage:
        """Click 'Logout' and return to LoginPage."""
        logger.info("Logging out")
        self.logout_tab.click()
        return LoginPage(self.page)

    def click_contact_us_tab(self) -> ContactUsFormPage:
        """Navigate to Contact Us form."""
        logger.info("Navigating to Contact Us page")
        self.contact_us_tab.click()
        return ContactUsFormPage(self.page)

    def click_delete_account(self) -> AccountDeletedPage:
        """Click 'Delete Account' and return AccountDeletedPage."""
        logger.info("Deleting account")
        self.delete_account_tab.click()
        return AccountDeletedPage(self.page)

    def click_test_cases_tab(self) -> CasesPage:
        """Navigate to Test Cases page."""
        logger.info("Navigating to Test Cases page")
        self.test_cases_tab.click()
        return CasesPage(self.page)

    def click_product_tab(self) -> ProductsPage:
        """Navigate to Products page."""
        logger.info("Navigating to Products page")
        self.products_tab.click()
        return ProductsPage(self.page)

    def click_view_product(self, index: int) -> ProductsDetailPage:
        """Click on a product by index to view its details."""
        logger.info("Viewing product at index %d", index)
        self.view_product.nth(index).click()
        return ProductsDetailPage(self.page)

    def go_to_cart(self) -> CartPage:
        """Navigate to Cart page."""
        logger.info("Navigating to Cart")
        self.cart_tab.click()
        return CartPage(self.page)

    def scroll_down(self) -> None:
        """Scroll to the bottom of the page."""
        self.scroll_to_bottom()

    def subscribe(self, email: str) -> None:
        """Subscribe with the given email address."""
        logger.info("Subscribing with email: %s", email)
        self.subscription_input.fill(email)
        self.subscription_button.click()

    def click_women_category(self) -> None:
        """Open Women category in sidebar."""
        logger.info("Clicking Women category")
        self.women_category.click()

    def click_dress_category(self) -> None:
        """Select Dress sub-category."""
        logger.info("Clicking Dress category")
        self.dress_category.click()

    def click_men_category(self) -> None:
        """Open Men category in sidebar."""
        logger.info("Clicking Men category")
        self.men_category.click()

    def click_shirt_category(self) -> None:
        """Select Tshirts sub-category."""
        logger.info("Clicking Tshirts category")
        self.shirts_category.click()

    def get_logged_in_as_text(self) -> str:
        """Return the 'Logged in as ...' text."""
        return self.logged_in_user.inner_text().strip()
