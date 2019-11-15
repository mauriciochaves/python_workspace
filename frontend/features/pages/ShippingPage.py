from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

CONFIRM_PROCEED_TO_CHECKOUT = (By.XPATH,'//*[@id="center_column"]/p[2]/a[1]')
PROCEED_TO_CHECKOUT_ADDRESS = (By.XPATH,'//*[@id="center_column"]/form/p/button')
PROCEED_TO_CHECKOUT_SHIPPING = (By.XPATH,'//*[@id="form"]/p/button')
TERMS_OF_SERVICE_RB = (By.XPATH,'//*[@id="cgv"]')

class ShippingPageActions(BasePage):
    def confirm_proceed_to_checkout(self):
        super().click(CONFIRM_PROCEED_TO_CHECKOUT)

    def proceed_to_checkout_address(self):
        super().click(PROCEED_TO_CHECKOUT_ADDRESS)

    def proceed_to_checkout_shipping(self):
        super().click(PROCEED_TO_CHECKOUT_SHIPPING)
    
    def click_on_terms_of_service(self):
        super().click(TERMS_OF_SERVICE_RB)