from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

SIGN_IN = (By.CLASS_NAME, "login")
BLOUSE = (By.XPATH,'//*[@id="homefeatured"]/li[2]/div/div[2]/h5/a')

class HomeActions(BasePage):
 
    def open_application (self, url):
        super().open_url(url)
    

    def get_page_title(self):
        return super().get_title()


    def click_on_sign_in (self):
        super().click(SIGN_IN)

    def click_on_blouse(self):
        super().click(BLOUSE)