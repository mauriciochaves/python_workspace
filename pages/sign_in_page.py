from base.base_setup import BaseSetup
from base.webdriver_custom_class import WebDriverCustomClass
from utilities.ui_map import sign_up_page


class SignInPage(BaseSetup, WebDriverCustomClass):

    def email_address(self, email):
        self.send_keys_to(sign_up_page.get("emailAddressByID"), email)
        #new
    def password_address(self, password):
        self.send_keys_to(sign_up_page.get("passwordByID"), password)

    def sign_click_on(self):
        self.click_on_element(sign_up_page.get("signinByID"), "id")
