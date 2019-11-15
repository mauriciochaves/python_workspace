from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

ADD_TO_CARD = (By.XPATH,'//*[@id="add_to_cart"]/button')
PROCEED_TO_CHECKOUT = (By.XPATH,'//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a')
class ProductPageActions(BasePage):
 
    def click_on_add_to_cart (self):
        super().click(ADD_TO_CARD)

    def click_on_proceed_to_checkout(self):
        super().click(PROCEED_TO_CHECKOUT)

