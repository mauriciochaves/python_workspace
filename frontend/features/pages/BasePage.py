from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def open_url(self, url):
        self.driver.get(url)


    def refresh(self):
        self.driver.refresh()


    def click(self, locator):
        self.wait(EC.element_to_be_clickable(locator)).click()


    def find(self, locator, seconds = 5):
        element = self.wait(EC.visibility_of_element_located(locator), seconds)
        return element
    

    def wait(self, condition, seconds = 5):
        return WebDriverWait(self.driver, seconds).until(condition)


    def type_in(self, locator, text, set_clear = True):
        element = self.find(locator)
        if set_clear:
            element.clear()
        element.send_keys(text)


    def select_in_combo_visible_text(self, locator, value):
        Select(self.wait(EC.visibility_of_element_located(locator))).select_by_visible_text(value)


    def select_in_combo_by_value(self, locator, value):
        Select(self.wait(EC.visibility_of_element_located(locator))).select_by_value(value)


    def switch_to_frame(self):
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name('iframe'))


    def switch_to_default_content(self):
        self.driver.switch_to.default_content()


    def is_display(self, locator, seconds = 10):
        return  self.find(locator, seconds).is_displayed()

    
    def is_not_displayed(self, locator, seconds = 10):
        visible = True
        time = 1
        while ( visible == True and time <= seconds):
            time+= 1
            try:
                visible = self.is_display(locator, 2)
            except:
                visible = False


    def is_enabled(self, locator):
        return  self.find(locator).is_enabled()