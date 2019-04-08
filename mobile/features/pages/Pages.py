from selenium.webdriver.common.by import By
   
class HomePage:

    USER = (By.ID, "")
    PASSWORD = (By.ID, "")
    LOGIN = (By.ID, "")
    FORGOT_MY_PASSWORD = (By.ID, "")
    ERROR_ID = ""
    
class ForgotPasswordPage:

    TITLE_PAGE = (By.CLASS_NAME, "")
    HELP_PAGE = (By.ID, "")
    USER = (By.ID, "")
    SEND_BUTTON = (By.ID, "")
    ERROR_USER = (By.ID, "")