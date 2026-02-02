from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.subscription_title = page.get_by_role("heading", name="Subscription")
        self.delete_product = page.locator("a.cart_quantity_delete")
        self.proceed_to_checkout = page.get_by_text("Proceed To Checkout", exact=True)
        self.view_first_product = page.locator("[href^='/product_details/']").first
        self.subscription_input = page.locator("#susbscribe_email")
        self.subscription_button = page.locator("#subscribe")
        self.cart_description = page.locator("td.cart_description")
        self.prices = page.locator("p.cart_total_price")
        self.quantities = page.locator("button.disabled")
        self.checkout_modal = page.locator("#checkoutModal")
        self.login_checkout = self.checkout_modal.get_by_role("link",name="Register / Login")
        self.empty_cart = page.locator("#empty_cart")
        self.cart_rows = page.locator("tr[id^='product-']")
        self.register_login_message = page.get_by_text("Register / Login account to proceed on checkout.",exact=True)

    def scroll_down_to_footer(self):
        self.scroll_to_bottom()

    def subscribe(self, email):
        self.subscription_input.fill(email)
        self.subscription_button.click()

    def count_products(self):
        return self.cart_description.count()

    def row_by_product_name(self, name):
        return self.cart_rows.filter(
            has=self.page.locator(f"td.cart_description a:has-text('{name}')")
        ).first

    def price_by_product_name(self, name):
        row = self.row_by_product_name(name)
        return row.locator("td.cart_price p")

    def quantity_by_product_name(self, name):
        row = self.row_by_product_name(name)
        return row.locator("td.cart_quantity button.disabled")

    def click_checkout(self):
        self.proceed_to_checkout.click()

    def click_login(self):
        self.login_checkout.click()

    def click_delete(self,product_id):
        self.page.locator(
            f"a.cart_quantity_delete[data-product-id='{product_id}']"
        ).click()










