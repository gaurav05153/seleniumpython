from selenium.webdriver.common.by import By

from pabeobjects.LoginPage import LoginPage


class ForgotPasswordPage:

    def __init__(self, driver):
        self.driver = driver

    sub_heading_of_forgot_password_page = (By.XPATH, "//*[@id='center_column']/div/h1[text()='Forgot your password?']")
    email_address_label = (By.XPATH, "//form[@id='form_forgotpassword']/fieldset/div/label[text()='Email address']")
    email_address_textbox = (By.CSS_SELECTOR, "input#email")
    retrieve_password_button = (By.XPATH,"//button[@type='submit']")



    def get_sub_heading_of_forgot_password_page(self):
        return self.driver.find_element(*ForgotPasswordPage.sub_heading_of_forgot_password_page)

    def get_email_address_label(self):
        return self.driver.find_element(*ForgotPasswordPage.email_address_label)

    def get_email_address_textbox(self):
        return self.driver.find_element(*ForgotPasswordPage.email_address_textbox)

    def get_retrieve_password_button(self):
        return self.driver.find_element(*ForgotPasswordPage.retrieve_password_button )




