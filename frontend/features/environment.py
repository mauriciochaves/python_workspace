from selenium import webdriver

def before_feature(context, feature):
    context.driver = webdriver.Chrome('..\\drivers\\chromedriver.exe')
    context.driver.delete_all_cookies()
    context.driver.maximize_window()


def after_feature(context, feature):
    pass