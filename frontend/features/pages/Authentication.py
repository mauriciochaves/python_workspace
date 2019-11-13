from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage

EMAIL_REGISTERED = (By.ID, "email")
EMAIL_CREATE_ACCOUNT = (By.NAME,"email_create")
SIGN_IN_REGISTERED = (By.ID, "SubmitLogin")
REGISTER_BT = (By.ID,"submitAccount")
CREATE_ACCOUNT_BT = (By.ID,"SubmitCreate")
ALERT = (By.CSS_SELECTOR, "ol")
PERSONAL_INFORMATION = (By.XPATH,'//*[@id="account-creation_form"]/div[1]/h3')
MR_TITLE_RB = (By.ID,"id_gender1")
FIRST_NAME = (By.ID,"customer_firstname")
LAST_NAME = (By.ID,"customer_lastname")
PASSWORD = (By.ID,"passwd")
ADDRESS_FIRST_NAME = (By.ID,"firstname")
ADDRESS_LAST_NAME = (By.ID,"lastname")
ADDRESS = (By.ID,"address1")
CITY = (By.ID,"city")
STATE = (By.ID,"id_state")

class AuthenticationActions(BasePage):
    def email_in (self, text):
        super().type_in(EMAIL_REGISTERED, text)

    def email_in_create_account(self,text):
        super().type_in(EMAIL_CREATE_ACCOUNT, text)

    def click_on_sign_in (self):
        super().click(EC.visibility_of_element_located(SIGN_IN_REGISTERED))

    def click_on_register (self):
        super().click(REGISTER_BT)

    def click_on_create_account (self):
        super().click(CREATE_ACCOUNT_BT)

    def click_on_mr_title (self):
        super().click(EC.visibility_of_element_located(MR_TITLE_RB))

    def type_in_first_name (self,text):
        super().type_in(FIRST_NAME, text)

    def type_in_last_name (self,text):
        super().type_in(LAST_NAME, text)
    
    def type_in_password (self,text):
        super().type_in(PASSWORD, text)
    
    def type_in_address_first_name (self,text):
        super().type_in(ADDRESS_FIRST_NAME, text)

    def type_in_address_last_name (self,text):
        super().type_in(ADDRESS_LAST_NAME, text)

    def type_in_address (self,text):
        super().type_in(ADDRESS, text)

    def type_in_city (self,text):
        super().type_in(CITY, text)

    def select_in_combo_box(self,text):
        super().type_in(STATE,text,False)

    def get_alert (self):
       element = super().find(ALERT)
       return element.text
    
    def get_personal_info (self):
       element = super().find(PERSONAL_INFORMATION)
       return element.text 