from pages.base_page import BasePage
from pages.cart_page import CartPage
from playwright.sync_api import Page, Locator

class ProductsPage(BasePage):
    def __init__(self, page):
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



    def click_product_view(self):
        self.view_product_first_button.click()

    def search_product_fill(self, product):
        self.search_product.fill(product)

    def search_product_click(self):
        self.search_product_button.click()

    def add_to_cart_by_name(self, name):
        card = self.product_cards.filter(has_text=name).first
        card.hover()
        card.locator(".overlay-content a.add-to-cart").click()

    def continue_shopping(self):
        self.continue_shopping_btn.click()

    def open_cart(self):
        self.view_cart_top.click()
        return CartPage(self.page)

    def get_search_value(self) :
        return self.search_product.input_value()





