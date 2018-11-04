from base.base_setup import BaseSetup
from base.webdriver_custom_class import WebDriverCustomClass
from utilities.ui_map import product_page


class ProductPage(BaseSetup, WebDriverCustomClass):

    def select_product(self):
        self.scroll_into_view(product_page.get("selectProductByClassName"), "class")
        self.hover_over_an_element_and_click_on(product_page.get("hoverOverProductBoxByClassName"), "class")
        self.click_on_element(product_page.get("productAddButtonByXpath"), "xpath")

    def continue_shopping_button(self):
        element = self.is_element_visible(product_page.get("modalWindowByXpath"), "xpath")
        self.click_on_returned_element(element)
