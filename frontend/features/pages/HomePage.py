from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

SIGN_IN = (By.CLASS_NAME, "login")

class HomeActions(BasePage):
 
    def open_application (self, url):
        super().open_url(url)
    

    def get_page_title(self):
        return super().get_title()


    def click_on_sign_in (self):
        super().click(SIGN_IN)