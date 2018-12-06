from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class HomePage(BasePage):
    URL ='http://automationpractice.com/index.php'
    SIGN_IN = (By.CLASS_NAME, "login")

class AuthenticationPage(BasePage):
    EMAIL_REGISTERED = (By.ID, "email")
    SIGN_IN_REGISTERED = (By.ID, "SubmitLogin")
    ALERT = (By.CSS_SELECTOR, "ol")

