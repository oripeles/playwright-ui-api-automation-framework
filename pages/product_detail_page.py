from pages.base_page import BasePage, logger
from playwright.sync_api import Page


class ProductsDetailPage(BasePage):
    """Single product detail page with quantity and add-to-cart."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.quantity_input = page.locator("#quantity")
        self.add_to_cart = page.get_by_role("button", name="Add to cart")
        self.continue_shopping = page.get_by_role("button", name="Continue Shopping")

    def set_quantity(self, amount: int) -> None:
        """Set the product quantity."""
        logger.info("Setting quantity to %d", amount)
        self.quantity_input.fill(str(amount))

    def click_add_to_cart(self) -> None:
        """Click the 'Add to cart' button."""
        logger.info("Adding product to cart")
        self.add_to_cart.click()

    def click_continue_shopping(self) -> None:
        """Click 'Continue Shopping' in the modal."""
        self.continue_shopping.click()
