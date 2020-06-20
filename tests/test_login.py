from pabeobjects.HomePage import HomePage
from pabeobjects.LandingPage import LandingPage
from pabeobjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


'''
How to run this test case in cmd or terminal
C:\Frameworks\Python\myseleniumpythonproject\tests>py.test test_login.py -v -s
'''

class TestLogin(BaseClass):

    def setup(self):
        self.landingpage = LandingPage(self.driver)
        self.loginpage = LoginPage(self.driver)
        self.homepage = HomePage(self.driver)


    def test_login_for_registered_user(self):
        #landingpage = LandingPage(self.driver)
        self.landingpage.get_signin_link().click()
        print(self.driver.title)
        assert self.driver.title == "Login - My Store"

    def test_login_by_passing_correct_user_credentials(self):
        self.test_login_for_registered_user()
        #loginpage = LoginPage(self.driver)
        self.loginpage.get_email_address_textbox().send_keys("gaurav05153@gmail.com")
        self.loginpage.get_password_textbox().send_keys("admin")
        self.loginpage.get_sign_in_button().click()
        print(self.driver.title)
        assert self.driver.title  == "My account - My Store"
        self.homepage.get_sign_out_link().click()


    def test_login_unsuccessful_message_by_passing_correct_user_credentials(self):
        self.test_login_for_registered_user()
        #loginpage = LoginPage(self.driver)
        self.loginpage.get_email_address_textbox().send_keys("gaurav0505153@gmail.com")
        self.loginpage.get_password_textbox().send_keys("admin")
        self.loginpage.get_sign_in_button().click()
        actual_error_message = self.loginpage.get_authentication_error_message().text
        expected_error_message = "Authentication failed."
        assert expected_error_message == actual_error_message
