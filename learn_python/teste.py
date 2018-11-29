from selenium import webdriver
import unittest
import pages
from config import BaseSetup


class NewTest(unittest.TestCase):

    def setUp(self):
        self.driver = BaseSetup.setUp(self,"chrome")
        self.driver.get(BaseSetup.url)

    def tearDown(self):
        BaseSetup.tearDown(self)

    def testPageAutomobile(self):
        driver = self.driver
        home_page = pages.HomePage()
        auto_mobile = pages.AutoMobilePage()

        BaseSetup.printScr(self)
        home_page.click_auto_mobile(driver)
        BaseSetup.printScr(self)
        self.assertEqual(auto_mobile.is_title_matches(driver), "Automobile Insurance")
        BaseSetup.printScr(self)
        
if __name__=='__main__':
    unittest.main()
