from pages.base_page import BasePage

class ProductsDetailPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.quantity_input = page.locator("#quantity")
        self.add_to_cart = page.get_by_role("button", name="Add to cart")
        self.continue_shopping = page.get_by_role("button", name="Continue Shopping")


    def set_quantity(self, amount):
        self.quantity_input.fill(str(amount))

    def click_add_to_cart(self):
        self.add_to_cart.click()

    def click_continue_shopping(self):
        self.continue_shopping.click()
