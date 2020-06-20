import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pabeobjects.HomePage import HomePage
from pabeobjects.LandingPage import LandingPage
from pabeobjects.LoginPage import LoginPage
from pabeobjects.ShoppingCartPage import ShoppingCartPage
from testdata.LoginPageData import LoginPageData
from utilities.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions as EC


class CommonMethods(BaseClass):

    def navigation_from_landing_page_to_login_page(self):
        log = self.getLogger()
        landingpage = LandingPage(self.driver)
        landingpage.get_signin_link().click()
        log.info("Clicked on the Sign in link of Landing page")
        assert self.driver.title == "Login - My Store"
        log.info("Navigated to Login Page")

    def login_by_passing_correct_user_credentials(self):
        loginpage = LoginPage(self.driver)
        global homepage,log
        homepage = HomePage(self.driver)
        loginpagedata = LoginPageData()
        log = self.getLogger()

        email=loginpagedata.test_LoginPage_correct_credentials_data.get("email_id")
        password = loginpagedata.test_LoginPage_correct_credentials_data.get("password")

        loginpage.get_email_address_textbox().send_keys(email)
        log.info("Email id {} is entered".format(email))
        loginpage.get_password_textbox().send_keys(password)
        log.info("Password {} is entered".format(password))
        loginpage.get_sign_in_button().click()
        log.info("Clicked on Sign in button of Login Page")
        assert self.driver.title == "My account - My Store"
        log.info("Navigated to Home Page")

    def select_dress(self,dress_name):
        if(dress_name.casefold() == "tshirt".casefold()):
            self.move_to_element(homepage.get_women_tab())
            self.move_to_element_and_click(homepage.get_women_tshirts())
            self.scroll_down_to_element(homepage.get_women_tshirt_first_option())
            self.move_to_element(homepage.get_women_tshirt_first_option())
            log.info("T-shirt is found in dress collections")

        if(dress_name.casefold() == "blouse".casefold()):
            self.move_to_element(homepage.get_women_tab())
            self.move_to_element_and_click(homepage.get_women_blouses())
            self.scroll_down_to_element(homepage.get_women_blouse_first_option())
            self.move_to_element(homepage.get_women_blouse_first_option())
            log.info("Blouse is found in dress collections")

    def add_selected_dress_to_cart(self,element):
        self.click(element)
        log.info("Dress is selected")

    def continue_with_shopping(self):
        homepage.get_continue_shopping_button().click()

    def proceed_to_checkout(self,element):
        self.click(element)
        cartpage = ShoppingCartPage(self.driver)
        WebDriverWait(self.driver, 10).until(EC.visibility_of(cartpage.get_summary_tab()))
        assert "Order - My Store" == self.driver.title

