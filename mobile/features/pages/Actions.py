from pages.BasePage import BasePage
from pages.Pages import *
  
class HomeActions(BasePage):
 
    def click_on_login (self):
        super().click(HomePage.LOGIN)

    def click_on_forgot_password (self):
        super().click(HomePage.FORGOT_MY_PASSWORD)

    def get_error_user (self):
        element = super().elements_by_id(HomePage.ERROR_ID)[0]
        return element.text

    def get_error_password (self):
        element = super().elements_by_id(HomePage.ERROR_ID)[1]
        return element.text

class ForgotPasswordActions(BasePage):

    def click_on_send_button (self):
        super().click(ForgotPasswordPage.SEND_BUTTON)

    def get_error_user (self):
       element = super().find(ForgotPasswordPage.ERROR_USER)
       return element.text

    def get_title(self):
        element = super().find(ForgotPasswordPage.TITLE_PAGE)
        return element.text

    def get_help_mensage(self):
        element = super().find(ForgotPasswordPage.HELP_PAGE)
        return element.text
