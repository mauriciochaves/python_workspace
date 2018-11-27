from selenium import webdriver
import unittest
import pages
from config import BaseSetup

class NewTest(unittest.TestCase):

    def setUp(self):
        self.driver = BaseSetup.setUp(self,'chrome')
        self.driver.get(BaseSetup.url)

    def tearDown(self):
        BaseSetup.tearDown(self)

    def testPageAutomobile(self):
        driver = self.driver
        home_page = pages.HomePage()
        auto_mobile = pages.AutoMobilePage()

        home_page.click_auto_mobile(driver)
        self.assertTrue(auto_mobile.is_title_matches(driver))
        
if __name__=='__main__':
    unittest.main()
