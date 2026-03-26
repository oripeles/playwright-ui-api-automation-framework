from __future__ import annotations

from pages.base_page import BasePage, logger
from pages.cart_page import CartPage
from playwright.sync_api import Page, Locator


class ProductsPage(BasePage):
    """All Products listing page with search and add-to-cart functionality."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.cases_title = page.get_by_role("heading", name="All Products")
        self.searched_products_title = page.get_by_role("heading", name="Searched Products")
        self.view_product = page.locator("[href^='/product_details/']")
        self.view_product_first_button = page.locator("[href='/product_details/1']")
        self.search_product = page.locator("#search_product")
        self.search_product_button = page.locator("#submit_search")
        self.view_product_result = page.locator(".productinfo.text-center p")
        self.continue_shopping_btn = page.get_by_role("button", name="Continue Shopping")
        self.view_cart_top = page.get_by_role("link", name="Cart")
        self.product_cards = page.locator(".product-image-wrapper")

    def click_product_view(self) -> None:
        """Click the first product's 'View Product' link."""
        logger.info("Clicking first product view")
        self.view_product_first_button.click()

    def search_product_fill(self, product: str) -> None:
        """Type a product name into the search box."""
        logger.info("Searching for product: %s", product)
        self.search_product.fill(product)

    def search_product_click(self) -> None:
        """Click the search button."""
        self.search_product_button.click()

    def add_to_cart_by_name(self, name: str) -> None:
        """Hover over a product card and click 'Add to cart'."""
        logger.info("Adding to cart: %s", name)
        card = self.product_cards.filter(has_text=name).first
        card.hover()
        card.locator(".overlay-content a.add-to-cart").click()

    def continue_shopping(self) -> None:
        """Click 'Continue Shopping' in the modal."""
        self.continue_shopping_btn.click()

    def open_cart(self) -> CartPage:
        """Navigate to Cart page from the top nav."""
        logger.info("Opening cart")
        self.view_cart_top.click()
        return CartPage(self.page)

    def get_search_value(self) -> str:
        """Return the current value in the search input."""
        return self.search_product.input_value()
