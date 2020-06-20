from pabeobjects.HomePage import HomePage
from pabeobjects.ShoppingCartPage import ShoppingCartPage
from utilities.CommonMethods import CommonMethods

'''
1) try py.test --collect-only test_e2e.py to see how many test cases it will pick
2) Do not keep unnecessary imports. It works not like java. It will pick import functions and 
   create modules to run the unnecessary test cases picked from imports
3) Run with
   C:\Frameworks\Python\myseleniumpythonproject\tests> py.test test_e2e.py -v -s
   C:\Frameworks\Python\myseleniumpythonproject\tests> py.test test_e2e.py -v -s  --html=reports/report.html 
'''


class Test_e2e_shopping(CommonMethods):

    def test_e2e_tshirt_shopping(self):
        global homepage, cartpage, log
        homepage = HomePage(self.driver)
        cartpage = ShoppingCartPage(self.driver)
        log = self.getLogger()
        self.navigation_from_landing_page_to_login_page()
        self.login_by_passing_correct_user_credentials()

        self.select_dress("Tshirt")

        self.add_selected_dress_to_cart(homepage.get_add_to_cart())

        self.proceed_to_checkout(homepage.get_proceed_to_checkout_button())

        self.scroll_down_to_element(cartpage.get_summary_tab_proceed_to_checkout_button())
        self.click(cartpage.get_summary_tab_proceed_to_checkout_button())

        self.scroll_down_to_element(cartpage.get_address_tab_proceed_to_checkout_button())
        self.click(cartpage.get_address_tab_proceed_to_checkout_button())

        self.scroll_down_to_element(cartpage.get_shipping_tab_terms_of_service_text())
        cartpage.get_shipping_tab_terms_of_service_checkbox().click()

        self.click(cartpage.get_shipping_tab_proceed_to_checkout_button())

        self.scroll_down_to_element(cartpage.get_payment_tab_pay_by_bank_wire())
        self.click(cartpage.get_payment_tab_pay_by_bank_wire())
        log.info("Pay by Bank Wire is choosed by customer to payment")
        self.scroll_down_to_element(cartpage.get_payment_tab_I_Confirm_my_order_button())
        self.click(cartpage.get_payment_tab_I_Confirm_my_order_button())
        order_message = cartpage.get_payment_tab_order_complete_message().text
        assert order_message in "Your order on My Store is complete."
        log.info("T-shirt is found, shopped and ordered successfully")
        self.click(homepage.get_sign_out_link())
        log.info("Clicked on Sign out")

    def test_e2e_blouse_shopping(self):
        global homepage, cartpage, log
        homepage = HomePage(self.driver)
        cartpage = ShoppingCartPage(self.driver)
        log = self.getLogger()
        self.navigation_from_landing_page_to_login_page()
        self.login_by_passing_correct_user_credentials()

        self.select_dress("Blouse")

        self.add_selected_dress_to_cart(homepage.get_add_to_cart())

        self.proceed_to_checkout(homepage.get_proceed_to_checkout_button())

        self.scroll_down_to_element(cartpage.get_summary_tab_proceed_to_checkout_button())
        self.click(cartpage.get_summary_tab_proceed_to_checkout_button())

        self.scroll_down_to_element(cartpage.get_address_tab_proceed_to_checkout_button())
        self.click(cartpage.get_address_tab_proceed_to_checkout_button())

        self.scroll_down_to_element(cartpage.get_shipping_tab_terms_of_service_text())
        cartpage.get_shipping_tab_terms_of_service_checkbox().click()

        self.click(cartpage.get_shipping_tab_proceed_to_checkout_button())

        self.scroll_down_to_element(cartpage.get_payment_tab_pay_by_bank_wire())
        self.click(cartpage.get_payment_tab_pay_by_bank_wire())
        log.info("Pay by Bank Wire is choosed by customer to payment")
        self.scroll_down_to_element(cartpage.get_payment_tab_I_Confirm_my_order_button())
        self.click(cartpage.get_payment_tab_I_Confirm_my_order_button())
        order_message = cartpage.get_payment_tab_order_complete_message().text
        assert order_message in "Your order on My Store is complete."
        log.info("T-shirt is found, shopped and ordered successfully")
        self.click(homepage.get_sign_out_link())
        log.info("Clicked on Sign out")
