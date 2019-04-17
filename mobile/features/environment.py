import os
import sys
from appium import webdriver
PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)
from util.utils import generate_report

def before_all(context):
    desired_caps = {}
    desired_caps['platformName']='Android'
    desired_caps['platformVersion'] = '7.0'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['appPackage'] = "com.android.chrome"
    desired_caps['appActivity'] = "com.google.android.apps.chrome.Main" 
    # desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'apks/(name_apk)'))
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def after_all(context):
    generate_report(context.config.userdata['SYSTEM'])