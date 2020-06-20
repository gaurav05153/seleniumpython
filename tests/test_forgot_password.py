from pabeobjects.ForgotPasswordPage import ForgotPasswordPage
from pabeobjects.LoginPage import LoginPage
from utilities.WebValidation import WebValidation

"""
How to run this test case in cmd or terminal
C:\Frameworks\Python\myseleniumpythonproject\tests>py.test test_forgot_password.py -v -s
"""

class TestForgotPassword(WebValidation):

    def test_navigation_to_forgot_password_screen(self):
        global login_page,forgot_password_page,log
        login_page = LoginPage(self.driver)
        log = self.getLogger()
        forgot_password_page = ForgotPasswordPage(self.driver)
        self.navigation_from_landing_page_to_login_page()
        self.click(login_page.get_forgot_password_link())
        assert "Forgot your password" in self.driver.title
        log.info("Navigated to Forgot Password Page")

    def test_validate_presence_of_expected_fields_in_forgot_password_screen(self):
        self.validate_element_to_be_displayed(forgot_password_page.get_sub_heading_of_forgot_password_page())
        self.validate_element_to_be_displayed(forgot_password_page.get_email_address_label())
        self.validate_element_to_be_displayed(forgot_password_page.get_email_address_textbox())
        self.validate_element_to_be_displayed(forgot_password_page.get_retrieve_password_button())
        expected_sub_heading_of_forgot_password_page= "FORGOT YOUR PASSWORD?"
        self.validate_text_value_of_element(forgot_password_page.get_sub_heading_of_forgot_password_page(), expected_sub_heading_of_forgot_password_page)


