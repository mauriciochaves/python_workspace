from base.base_setup import BaseSetup
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.dresses_page import DressesPage
from pages.shopping_cart_page import ShoppingCartPage
from pages.sign_in_page import SignInPage
from utilities import data_provider
import unittest


class BuyingProducts(BaseSetup, unittest.TestCase):

    def setUp(self):
        super(BuyingProducts, self).setUp()
        self.home_page = HomePage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.shopping_cart_page = ShoppingCartPage(self.driver)
        self.dresses_page = DressesPage(self.driver)
        self.data = data_provider.test_data_provider()
        self.sign_in_page = SignInPage(self.driver)

    def test_check_if_product_was_added_th_the_cart(self):
        self.home_page.dresses_button_click_on()
        self.dresses_page.summer_dresses_image_click_on()
        self.dresses_page.add_to_the_cart_all_products_in_the_category()
        self.home_page.cart_button()
        self.shopping_cart_page.proceed_to_checkout_summary_button_click_on()

        #sign
        self.sign_in_page.email_address(self.data.get("email"))
        self.sign_in_page.password_address(self.data.get("password"))
        self.sign_in_page.sign_click_on()

        #address
        self.shopping_cart_page.purchase_comments(self.data.get("menssage"))
        self.shopping_cart_page.proceed_to_checkout_address_button_click_on()






    def tearDown(self):
        super(BuyingProducts, self).tearDown()


if __name__ == '__main__':
    unittest.main()
