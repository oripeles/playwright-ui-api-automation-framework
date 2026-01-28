from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.cases_title = page.get_by_role("heading", name="All Products")
        self.view_product = page.locator("a[href^='/product_details/']")
        self.view_product_first_button = page.locator("a[href='/product_details/1']")
        self.search_product = page.locator("#search_product")
        self.view_product_result = page.locator(".productinfo.text-center p")
        self.continue_shopping_btn = page.get_by_role("button", name="Continue Shopping")
        self.view_cart_top = page.get_by_role("link", name="Cart")
        self.product_cards = page.locator(".product-image-wrapper")
        self.add_to_cart_buttons = page.locator(".add-to-cart")










