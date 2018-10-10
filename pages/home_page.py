from base.base_setup import BaseSetup
from base.webdriver_custom_class import WebDriverCustomClass
from utilities.ui_map import home_page


class HomePage(BaseSetup, WebDriverCustomClass):

    def search_product(self, searched_product):
        self.send_keys_to(home_page.get("searchFieldByID"), searched_product)

    def search_button(self):
        self.click_on_element(home_page.get("searchButtonByName"), "name")

    def cart_button(self):
        self.click_on_element(home_page.get("cartButtonCSSSelector"), "css")

    def dresses_button_click_on(self):
        self.click_on_element(home_page.get("dressesButtonByXpath"), "xpath")

    def dresses_summer_dresses_click_on(self):
        pass
