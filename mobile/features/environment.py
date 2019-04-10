import os
from appium import webdriver


def before_scenario(context, feature):
    desired_caps = {}
    desired_caps['platformName']='Android'
    desired_caps['platformVersion'] = '7.0'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['appPackage'] = "com.android.chrome"
    desired_caps['appActivity'] = "com.google.android.apps.chrome.Main" 
    # desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'apks/(name_apk)'))
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
