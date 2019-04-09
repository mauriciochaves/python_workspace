from pages.BasePage import BasePage
from pages.Pages import HomePage
from pages.Pages import AuthenticationPage


class HomeActions(BasePage):
 
    def open_application (self):
        super().open_url(HomePage.URL)
    

    def get_page_title(self):
        return super().get_title()


    def click_on_sign_in (self):
        super().click(HomePage.SIGN_IN)

class AuthenticationActions(BasePage):
    def email_in (self, text):
        super().type_in(AuthenticationPage.EMAIL_REGISTERED, text)


    def click_on_sign_in (self):
        super().click(AuthenticationPage.SIGN_IN_REGISTERED)


    def get_alert (self):
       element = super().find(AuthenticationPage.ALERT )
       return element.text