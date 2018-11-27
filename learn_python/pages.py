from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage (object):
    def click_auto_mobile(self, driver):
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((HomePageLocators.AUTOMOBILE))).click()

class AutoMobilePage (object):
    def is_title_matches(self, driver):
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.visibility_of_element_located((AutoMobileLocators.TITLE)))
        """Verifies that the hardcoded text "Automobile Insurance" appears in page title"""
        return "Automobile Insurance" in element.text
        
    
       
        



