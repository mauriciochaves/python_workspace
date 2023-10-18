from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait

AUTHENTICATION = (By.CLASS_NAME,'page-heading')
EMAIL_REGISTERED = (By.ID, "email")
EMAIL_CREATE_ACCOUNT = (By.NAME,"email_create")
SIGN_IN_REGISTERED = (By.ID, "SubmitLogin")
REGISTER_BT = (By.ID,"submitAccount")
CREATE_ACCOUNT_BT = (By.ID,"SubmitCreate")
ALERT = (By.CSS_SELECTOR, "ol")
PERSONAL_INFORMATION = (By.XPATH,'//*[@id="account-creation_form"]/div[1]/h3')
MR_TITLE_RB = (By.CSS_SELECTOR,'input#id_gender1')
FIRST_NAME = (By.ID,"customer_firstname")
LAST_NAME = (By.ID,"customer_lastname")
PASSWORD = (By.ID,"passwd")
ADDRESS_FIRST_NAME = (By.ID,"firstname")
ADDRESS_LAST_NAME = (By.ID,"lastname")
ADDRESS = (By.ID,"address1")
CITY = (By.ID,"city")
STATE = (By.ID,"id_state")
ZIP_CODE = (By.ID,"postcode")
MOBILE_PHONE = (By.ID,"phone_mobile")
ADDRESS_ALIAS = (By.ID,"alias")
MY_ACCOUNT = (By.XPATH,'//*[@id="center_column"]/h1')
SIGN_OUT = (By.CLASS_NAME, "logout")

class AuthenticationActions(BasePage):
    def email_in (self, text):
        super().type_in(EC.visibility_of_element_located(EMAIL_REGISTERED), text)

    def email_in_create_account(self,text):
        super().type_in(EC.visibility_of_element_located(EMAIL_CREATE_ACCOUNT), text)

    def click_on_sign_in (self):
        super().click(SIGN_IN_REGISTERED)

    def click_on_register (self):
        super().click(REGISTER_BT)

    def click_on_create_account (self):
        super().click(CREATE_ACCOUNT_BT)

    def click_on_mr_title (self):
        super().click(MR_TITLE_RB)

    def type_in_mobile_phone (self,text):
        super().type_in(EC.visibility_of_element_located(MOBILE_PHONE), text)

    def type_in_zip_code (self,text):
        super().type_in(EC.visibility_of_element_located(ZIP_CODE), text)

    def type_in_first_name (self,text):
        super().type_in(EC.visibility_of_element_located(FIRST_NAME), text)

    def type_in_last_name (self,text):
        super().type_in(EC.visibility_of_element_located(LAST_NAME), text)
    
    def type_in_password (self,text):
        super().type_in(EC.visibility_of_element_located(PASSWORD), text)
    
    def type_in_address_first_name (self,text):
        super().type_in(EC.visibility_of_element_located(ADDRESS_FIRST_NAME), text)

    def type_in_address_last_name (self,text):
        super().type_in(EC.visibility_of_element_located(ADDRESS_LAST_NAME), text)

    def type_in_address (self,text):
        super().type_in(EC.visibility_of_element_located(ADDRESS), text)

    def type_in_address_alias (self,text):
        super().type_in(EC.visibility_of_element_located(ADDRESS_ALIAS), text)

    def type_in_city (self,text):
        super().type_in(EC.visibility_of_element_located(CITY), text)

    def select_in_combo_box(self,text):
        super().type_in(EC.presence_of_element_located(STATE), text, set_clear=False)

    def get_alert (self):
       element = super().find(EC.visibility_of_element_located(ALERT))
       return element.text
    
    def get_personal_info (self):
       element = super().find(EC.visibility_of_element_located(PERSONAL_INFORMATION))
       return element.text

    def get_my_account_info (self):
       element = super().find(EC.visibility_of_element_located(MY_ACCOUNT))
       return element.text

    def click_on_sign_out (self):
        super().click(SIGN_OUT)
    
    def get_authentication_text(self):
        element = super().find(EC.visibility_of_element_located(AUTHENTICATION))
        return element.text