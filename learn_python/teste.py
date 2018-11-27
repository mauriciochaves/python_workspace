from selenium import webdriver
import unittest
import pages
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NewTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('..\\python_workspace\\learn_python\\drivers\\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.get('http://sampleapp.tricentis.com/101/index.php')
        self.driver.maximize_window()
        

    def tearDown(self):
        self.driver.close()

    def testPageAutomobile(self):
        driver = self.driver
        home_page = pages.HomePage()
        auto_mobile = pages.AutoMobilePage()

        home_page.click_auto_mobile(driver)
        self.assertTrue(auto_mobile.is_title_matches(driver))
        
if __name__=='__main__':
    unittest.main()
