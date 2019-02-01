from selenium import webdriver

def before_feature(context, feature):
    context.driver = webdriver.Chrome('..\\python_workspace\\drivers\\chromedriver.exe')
    context.driver.implicitly_wait(10)
    context.driver.delete_all_cookies()
    context.driver.maximize_window()

def after_feature(context, feature):
    context.driver.quit()
