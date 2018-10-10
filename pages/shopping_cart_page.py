from base.base_setup import BaseSetup
from base.webdriver_custom_class import WebDriverCustomClass
from utilities.ui_map import shopping_cart


class ShoppingCartPage(BaseSetup, WebDriverCustomClass):

    def cart_products(self, item):
        return self.get_elements(shopping_cart.get(item), "link")
