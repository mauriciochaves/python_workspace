from base.base_setup import BaseSetup
from base.webdriver_custom_class import WebDriverCustomClass
from utilities.ui_map import dresses_page, product_page, home_page
from utilities.helpers import wait_and_click
import time


class DressesPage(BaseSetup, WebDriverCustomClass):

    def summer_dresses_image_click_on(self):
        self.hover_over_first_element_click_on_second(home_page.get("dressesButtonByXpath"), "xpath",
                                                      home_page.get("dressesButtonActivateByXpath"), "xpath",
                                                      home_page.get("dressesButtonCassualDressesByXpath"), "xpath")

    def add_to_the_cart_all_products_in_the_category(self):
        counter = 1
        self.scroll_into_view(dresses_page.get("scrollIntoViewByXpath"), "xpath")
        components = self.get_elements(dresses_page.get("hoverAllElementsByXpath"), "xpath")
        for element in components:
            time.sleep(.5)
            self.hover_over_an_element(element,
                                       dresses_page.get("locateSelectedElementsByXpath").format(counter), "xpath")
            wait_and_click(self, dresses_page.get("productAddButtonByXpath"), counter, "xpath")
            counter += 1
            wait_and_click(self, product_page.get("modalWindowByXpath"), counter, "xpath")
