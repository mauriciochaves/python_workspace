import os
from appium import webdriver

desired_caps = {}
desired_caps['platformName']='Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'apks/(name_apk)'))

def before_feature(context, feature):
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
 

def after_feature(context, feature):
    context.driver.quit()