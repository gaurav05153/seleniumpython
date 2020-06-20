from selenium.webdriver.common.by import By

from pabeobjects.LoginPage import LoginPage


class LandingPage:

    def __init__(self, driver):
        self.driver = driver

    sign_in_link = (By.LINK_TEXT, "Sign in")



    def get_signin_link(self):
        return self.driver.find_element(*LandingPage.sign_in_link)




