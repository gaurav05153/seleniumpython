from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email_address_textbox = (By.ID, "email")
    password_textbox = (By.ID, "passwd")
    sign_in_button = (By.ID, "SubmitLogin")
    forgot_password_link = (By.LINK_TEXT, "Forgot your password?")
    authentication_error_message = (By.XPATH, "//div[@id='center_column']//ol/li")
    create_account_email_address_textbox = (By.ID, "email_create")
    create_an_account_submit_button = (By.ID, "SubmitCreate")

    def get_email_address_textbox(self):
        return self.driver.find_element(*LoginPage.email_address_textbox)

    def get_password_textbox(self):
        return self.driver.find_element(*LoginPage.password_textbox)

    def get_sign_in_button(self):
        return self.driver.find_element(*LoginPage.sign_in_button)

    def get_forgot_password_link(self):
        return self.driver.find_element(*LoginPage.forgot_password_link)

    def get_authentication_error_message(self):
        return self.driver.find_element(*LoginPage.authentication_error_message)

    def get_create_account_email_address_textbox(self):
        return self.driver.find_element(*LoginPage.create_account_email_address_textbox)

    def get_create_an_account_submit_button(self):
        return self.driver.find_element(*LoginPage.create_an_account_submit_button)
