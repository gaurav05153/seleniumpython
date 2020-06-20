from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    sign_out_link = (By.LINK_TEXT, "Sign out")
    women_tab = (By.XPATH, "//a[@title='Women']")
    women_tshirts = (By.XPATH, "//a[@title='T-shirts']")
    women_blouses = (By.XPATH, "//a[@title='Blouses']")
    women_tshirt_first_option = (By.XPATH, "//a[@title='Faded Short Sleeve T-shirts']/img")
    women_blouse_first_option = (By.XPATH, "//a[@title='Blouse']/img")
    add_to_cart_button = (By.XPATH, "//a[@title='Add to cart']")
    continue_shopping_button = (By.XPATH, "//span[@title='Continue shopping']")
    proceed_to_checkout_button = (By.XPATH, "//a[@title='Proceed to checkout']")


    def get_sign_out_link(self):
        return self.driver.find_element(*HomePage.sign_out_link)

    def get_women_tab(self):
        return self.driver.find_element(*HomePage.women_tab)

    def get_women_tshirts(self):
        return self.driver.find_element(*HomePage.women_tshirts)

    def get_women_blouses(self):
        return self.driver.find_element(*HomePage.women_blouses)

    def get_women_tshirt_first_option(self):
        return self.driver.find_element(*HomePage.women_tshirt_first_option)

    def get_women_blouse_first_option(self):
        return self.driver.find_element(*HomePage.women_blouse_first_option)

    def get_add_to_cart(self):
        return self.driver.find_element(*HomePage.add_to_cart_button)

    def get_continue_shopping_button(self):
        return self.driver.find_element(*HomePage.continue_shopping_button)

    def get_proceed_to_checkout_button(self):
        return self.driver.find_element(*HomePage.proceed_to_checkout_button)
