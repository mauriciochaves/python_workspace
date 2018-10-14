from base.base_setup import BaseSetup
from base.webdriver_custom_class import WebDriverCustomClass
from utilities.ui_map import shopping_cart


class ShoppingCartPage(BaseSetup, WebDriverCustomClass):

    def cart_products(self, item):
        return self.get_elements(shopping_cart.get(item), "link")

    def checkout_cart_products(self, item):
        return self.get_elements(shopping_cart.get(item), "id")

    def proceed_to_checkout_summary_button_click_on(self):
        self.click_on_element(shopping_cart.get("proceedToCheckoutSummaryByXpath"), "xpath")
        #new
    def proceed_to_checkout_address_button_click_on(self):
        self.click_on_element(shopping_cart.get("proceedToCheckoutAddressByName"), "name")

    def purchase_comments(self, comments):
        self.send_keys_to(shopping_cart.get("commentsPurchaseShoppingCardByName"), comments, "name")
