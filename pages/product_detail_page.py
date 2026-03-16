from pages.base_page import BasePage
from playwright.sync_api import Page


class ProductsDetailPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.quantity_input = page.locator("#quantity")
        self.add_to_cart = page.get_by_role("button", name="Add to cart")
        self.continue_shopping = page.get_by_role("button", name="Continue Shopping")

    def set_quantity(self, amount: int) -> None:
        self.quantity_input.fill(str(amount))

    def click_add_to_cart(self) -> None:
        self.add_to_cart.click()

    def click_continue_shopping(self) -> None:
        self.continue_shopping.click()
