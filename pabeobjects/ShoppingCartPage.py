from selenium.webdriver.common.by import By

from pabeobjects.LoginPage import LoginPage


class ShoppingCartPage:

    def __init__(self, driver):
        self.driver = driver

    summary_tab = (By.XPATH, "//*[@id = 'order_step']/li/span/em[text() = '01.']")
    summary_tab_proceed_to_checkout_button = (By.XPATH, "//a[@title='Continue shopping']/preceding-sibling::a/span")
    address_tab_proceed_to_checkout_button = (By.XPATH,"//button[@name='processAddress']/span")
    shipping_tab_term_of_service_text = (By.XPATH, "//*[@id='extra_carrier']/following-sibling::p[text()='Terms of service']")
    shipping_tab_terms_of_service_checkbox = (By.ID, "cgv")
    shipping_tab_proceed_to_checkout_button = (By.XPATH, "//button[@name='processCarrier']/span")
    payment_tab_pay_by_bank_wire = (By.XPATH, "//a[@title='Pay by bank wire']")
    payment_tab_I_Confirm_my_order_button = (By.XPATH, "//button[@type='submit']/span[text()='I confirm my order']")
    payment_tab_order_complete_message = (By.XPATH, "//p[@class='cheque-indent']/strong")



    def get_summary_tab(self):
        return self.driver.find_element(*ShoppingCartPage.summary_tab)

    def get_summary_tab_proceed_to_checkout_button(self):
        return self.driver.find_element(*ShoppingCartPage.summary_tab_proceed_to_checkout_button)

    def get_address_tab_proceed_to_checkout_button(self):
        return self.driver.find_element(*ShoppingCartPage.address_tab_proceed_to_checkout_button)

    def get_shipping_tab_terms_of_service_checkbox(self):
        return self.driver.find_element(*ShoppingCartPage.shipping_tab_terms_of_service_checkbox)

    def get_shipping_tab_terms_of_service_text(self):
        return self.driver.find_element(*ShoppingCartPage.shipping_tab_term_of_service_text)

    def get_shipping_tab_proceed_to_checkout_button(self):
        return self.driver.find_element(*ShoppingCartPage.shipping_tab_proceed_to_checkout_button)

    def get_payment_tab_pay_by_bank_wire(self):
        return self.driver.find_element(*ShoppingCartPage.payment_tab_pay_by_bank_wire)

    def get_payment_tab_I_Confirm_my_order_button(self):
        return self.driver.find_element(*ShoppingCartPage.payment_tab_I_Confirm_my_order_button)

    def get_payment_tab_order_complete_message(self):
        return self.driver.find_element(*ShoppingCartPage.payment_tab_order_complete_message)



