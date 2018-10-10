from automation_test.base.base_setup import BaseSetup
from automation_test.base.webdriver_custom_class import WebDriverCustomClass
from automation_test.utilities.ui_map import shopping_cart


class ShoppingCartPage(BaseSetup, WebDriverCustomClass):

    def cart_products(self, item):
        return self.get_elements(shopping_cart.get(item), "link")
