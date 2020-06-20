from logging import getLogger

import pytest

from pabeobjects.HomePage import HomePage
from pabeobjects.LandingPage import LandingPage
from pabeobjects.LoginPage import LoginPage
from testdata.LoginPageData import LoginPageData
from utilities.BaseClass import BaseClass

'''
How to run this test case in cmd or terminal
Path of test case folder>py.test test_login_with_test_data_management.py -v -s
Path of test case folder>py.test test_login_with_test_data_management.py --html=reports/report.html  
'''

class TestLoginWithTestData(BaseClass):

    def test_login(self):
        log = self.getLogger()
        landingpage = LandingPage(self.driver)
        landingpage.get_signin_link().click()
        log.info("Clicked on the SIgn in link of Landing page")
        assert self.driver.title == "Login - My Store"
        log.info("Navigated to Login Page")

    def test_login_by_passing_correct_user_credentials(self, get_correct_creds):
        loginpage = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        log = self.getLogger()
        self.test_login()
        loginpage.get_email_address_textbox().send_keys(get_correct_creds["email_id"])
        log.info("Email id {} is entered".format(get_correct_creds["email_id"]))
        loginpage.get_password_textbox().send_keys(get_correct_creds["password"])
        log.info("Password {} is entered".format(get_correct_creds["password"]))
        loginpage.get_sign_in_button().click()
        log.info("Clicked on Sign in button of Login Page")
        assert self.driver.title == "My account - My Store"
        log.info("Navigated to Home Page")
        homepage.get_sign_out_link().click()
        log.info("Clicked on Sign out")

    def test_login_unsuccessful_message_by_passing_incorrect_user_credentials(self, get_wrong_creds):
        loginpage = LoginPage(self.driver)
        log = self.getLogger()
        self.test_login()
        loginpage.get_email_address_textbox().send_keys(get_wrong_creds["email_id"])
        log.info("Email id {} is entered".format(get_wrong_creds["email_id"]))
        loginpage.get_password_textbox().send_keys(get_wrong_creds["password"])
        log.info("Password {} is entered".format(get_wrong_creds["password"]))
        loginpage.get_sign_in_button().click()
        log.info("Clicked on Sign in button of Login Page")
        actual_error_message = loginpage.get_authentication_error_message().text
        expected_error_message = "Authentication failed."
        assert expected_error_message == actual_error_message
        log.info("Validated the error message due to wrong credentials entered")

    @pytest.fixture(params=LoginPageData.test_LoginPage_wrong_credentials_data)
    def get_wrong_creds(self, request):
        return request.param


