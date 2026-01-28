from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.subscription_title = page.get_by_role("heading", name="Subscription")
        self.delete_product = page.locator("a.cart_quantity_delete")
        self.proceed_to_checkout = page.get_by_role("link",name="Proceed To Checkout")
        self.view_first_product = page.locator("a[href^='/product_details/']").first
        self.subscription_input = page.locator("#susbscribe_email")
        self.subscription_button = page.locator("#subscribe")
        self.cart_description = page.locator("td.cart_description")
        self.prices = page.locator("p.cart_total_price")
        self.quantities = page.locator("button.disabled")
        self.checkout_modal = page.locator("#checkoutModal")
        self.login_checkout = self.checkout_modal.get_by_role("link",name="Register / Login")
        self.empty_cart = page.locator("#empty_cart")












