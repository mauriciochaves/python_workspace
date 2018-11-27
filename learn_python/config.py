from selenium import webdriver

class BaseSetup:

    url = 'http://sampleapp.tricentis.com/101/index.php'

    def setUp(self, browser):
        
        if browser == "chrome":
            self.driver = webdriver.Chrome('..\\python_workspace\\learn_python\\drivers\\chromedriver.exe')
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            raise Exception("Selected browser not supported")
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        return self.driver
    
    def tearDown(self):
        self.driver.quit()