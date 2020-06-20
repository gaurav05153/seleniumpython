from pabeobjects.CreateAccountPage import CreateAccountPage
from pabeobjects.LoginPage import LoginPage
from testdata.CreateAccountPageData import CreateAccountPageData
from testdata.LoginPageData import LoginPageData
from utilities.WebValidation import WebValidation

'''
How to run this test case in cmd or terminal
C:\Frameworks\Python\myseleniumpythonproject\Tests>py.test test_create_account.py -v -s
C:\Frameworks\Python\myseleniumpythonproject\Tests>py.test  --html=reports/report.html

to run oly one test:
py.test test_create_account.py::TestCreateAccount::
test_validation_of_the_presence_all_the_fields_on_create_account_screen_basic_information_section
'''


class TestCreateAccount(WebValidation):

    def test_navigation_to_create_account_screen(self):
        global login_page, log, login_page_data, create_account_page
        login_page = LoginPage(self.driver)
        create_account_page = CreateAccountPage(self.driver)
        login_page_data = LoginPageData()
        log = self.getLogger()
        self.navigation_from_landing_page_to_login_page()
        email = login_page_data.test_create_account_data.get("email_id")
        self.send_value_to_text_box(login_page.get_create_account_email_address_textbox(), email)
        self.click(login_page.get_create_an_account_submit_button())
        assert "Login - My Store" in self.driver.title
        self.validate_element_to_be_displayed(create_account_page.get_page_heading())
        page_heading = create_account_page.get_page_heading().text
        assert page_heading == "CREATE AN ACCOUNT"
        log.info("Navigated to Create Account Page")

    def test_validation_of_the_presence_of_all_fields_label_on_create_account_screen(self):
        self.test_navigation_to_create_account_screen()
        self.validate_element_to_be_displayed(create_account_page.get_page_heading())
        self.validate_element_to_be_displayed(create_account_page.get_personal_info_page_subheading())
        self.validate_element_to_be_displayed(create_account_page.get_title_label())
        self.validate_element_to_be_displayed(create_account_page.get_mr_title_radio_button_label())
        self.validate_element_to_be_displayed(create_account_page.get_mrs_title_radio_button_label())
        self.validate_element_to_be_displayed(create_account_page.get_first_name_label())
        self.validate_element_to_be_displayed(create_account_page.get_last_name_label())
        self.validate_element_to_be_displayed(create_account_page.get_email_label())
        self.validate_element_to_be_displayed(create_account_page.get_password_label())
        self.scroll_down_by_pixel(100)
        self.validate_element_to_be_displayed(create_account_page.get_date_of_birth_label())

        self.validate_element_to_be_displayed(create_account_page.get_address_page_subheading())
        self.validate_element_to_be_displayed(create_account_page.get_address_first_name_label())
        self.validate_element_to_be_displayed(create_account_page.get_address_last_name_label())
        self.validate_element_to_be_displayed(create_account_page.get_address_company_label())
        self.validate_element_to_be_displayed(create_account_page.get_address_label())
        self.validate_element_to_be_displayed(create_account_page.get_address_line2_label())
        self.validate_element_to_be_displayed(create_account_page.get_address_city_label())
        self.validate_element_to_be_displayed(create_account_page.get_address_state_label())
        self.validate_element_to_be_displayed(create_account_page.get_address_zip_code_label())
        self.validate_element_to_be_displayed(create_account_page.get_address_country_label())
        self.validate_element_to_be_displayed(create_account_page.get_address_additional_information_label())
        self.validate_element_to_be_displayed(create_account_page.get_address_home_phone_label())
        self.validate_element_to_be_displayed(create_account_page.get_address_mobile_phone_label())
        self.validate_element_to_be_displayed(create_account_page.get_address_alias_label())

    def test_validation_of_the_presence_all_the_fields_on_create_account_screen_basic_information_section(self):
        self.test_navigation_to_create_account_screen()
        self.validate_element_to_be_displayed(create_account_page.get_page_heading())
        self.validate_element_to_be_displayed(create_account_page.get_personal_info_page_subheading())
        self.validate_element_to_be_displayed(create_account_page.get_mr_title_radio_button())
        self.validate_element_to_be_displayed(create_account_page.get_mrs_title_radio_button())
        self.validate_element_to_be_displayed(create_account_page.get_first_name_text_box())
        self.validate_element_to_be_displayed(create_account_page.get_last_name_text_box())
        self.validate_element_to_be_displayed(create_account_page.get_email_text_box())
        self.validate_element_to_be_displayed(create_account_page.get_password_text_box())
        # self.scroll_down_by_pixel(300)
        # self.validate_element_to_be_displayed(create_account_page.get_date_from_date_of_birth_drop_down())
        # create_account_page.get_date_from_date_of_birth_drop_down().is_present()
        # create_account_page.get_date_from_date_of_birth_drop_down().click()
        # self.validate_element_to_be_displayed(create_account_page.get_date_from_date_of_birth_drop_down())
        # self.validate_element_to_be_displayed(create_account_page.get_month_from_date_of_birth_drop_down())
        # self.validate_element_to_be_displayed(create_account_page.get_year_from_date_of_birth_drop_down())
        # self.driver.execute_script(" return arguments[0].scrollIntoView();", self.driver.find_element_by_id("newsletter"))
        # self.scroll_down_to_element(create_account_page.get_sign_up_for_our_newsletter_check_box())
        # self.validate_element_to_be_displayed(create_account_page.get_sign_up_for_our_newsletter_check_box())
        # self.validate_element_to_be_displayed(create_account_page.get_receive_special_offers_check_box())

    def test_validation_of_the_presence_all_the_fields_on_create_account_screen_address_section(self):
        self.test_navigation_to_create_account_screen()
        self.validate_element_to_be_displayed(create_account_page.get_address_page_subheading())
        self.validate_element_to_be_displayed(create_account_page.get_address_first_name_text_box())
        self.validate_element_to_be_displayed(create_account_page.get_address_last_name_text_box())
        self.validate_element_to_be_displayed(create_account_page.get_address_company_text_box())
        self.validate_element_to_be_displayed(create_account_page.get_address_text_box())
        self.validate_element_to_be_displayed(create_account_page.get_address_line2_text_box())
        self.validate_element_to_be_displayed(create_account_page.get_address_city_text_box())
        #self.validate_element_to_be_displayed(create_account_page.get_address_state_drop_down())
        self.validate_element_to_be_displayed(create_account_page.get_address_zip_code_text_box())
        # self.validate_element_to_be_displayed(create_account_page.get_address_country_drop_down())
        self.validate_element_to_be_displayed(create_account_page.get_address_additional_information_text_box())
        self.validate_element_to_be_displayed(create_account_page.get_address_home_phone_text_box())
        self.validate_element_to_be_displayed(create_account_page.get_address_mobile_phone_text_box())
        self.validate_element_to_be_displayed(create_account_page.get_address_alias_text_box())

    def test_validation_of_filling_the_create_account_form_on_create_account_screen(self):
        global create_account_page_data, create_account_page;
        create_account_page_data = CreateAccountPageData()
        create_account_page = CreateAccountPage(self.driver)
        self.test_navigation_to_create_account_screen()
        if create_account_page_data.test_create_account_page_correct_data.get("title") == "Mr":
            self.click(create_account_page.get_mr_title_radio_button())
        elif create_account_page_data.test_create_account_page_correct_data.get("title") == "Mrs":
            self.click(create_account_page.get_mrs_title_radio_button())
        self.send_value_to_text_box(create_account_page.get_first_name_text_box(),
                                    create_account_page_data.test_create_account_page_correct_data.get("first_name"))
        self.send_value_to_text_box(create_account_page.get_last_name_text_box(),
                                    create_account_page_data.test_create_account_page_correct_data.get("last_name"))
        self.send_value_to_text_box(create_account_page.get_email_text_box(),
                                    create_account_page_data.test_create_account_page_correct_data.get("email"))
        self.send_value_to_text_box(create_account_page.get_password_text_box(),
                                    create_account_page_data.test_create_account_page_correct_data.get("password"))
        self.select_drop_down_value(create_account_page.get_date_from_date_of_birth_drop_down(),
                                    create_account_page_data.test_create_account_page_correct_data.get("date_of_birth"))
        self.select_drop_down_value_by_index(create_account_page.get_month_from_date_of_birth_drop_down(),
                                             create_account_page_data.test_create_account_page_correct_data.get(
                                                 "month_of_birth"))
        self.select_drop_down_value(create_account_page.get_year_from_date_of_birth_drop_down(),
                                    create_account_page_data.test_create_account_page_correct_data.get("year_of_birth"))
        self.send_value_to_text_box(create_account_page.get_address_first_name_text_box(),
                                    create_account_page_data.test_create_account_page_correct_data.get("address_first_name"))
        self.send_value_to_text_box(create_account_page.get_address_last_name_text_box(),
                                    create_account_page_data.test_create_account_page_correct_data.get("address_last_name"))
        self.send_value_to_text_box(create_account_page.get_address_company_text_box(),
                                    create_account_page_data.test_create_account_page_correct_data.get("company_name"))
        self.send_value_to_text_box(create_account_page.get_address_text_box(),
                                    create_account_page_data.test_create_account_page_correct_data.get("address_line_1"))
        self.send_value_to_text_box(create_account_page.get_address_line2_text_box(),
                                    create_account_page_data.test_create_account_page_correct_data.get("address_line_2"))
        self.send_value_to_text_box(create_account_page.get_address_city_text_box(),
                                    create_account_page_data.test_create_account_page_correct_data.get("city"))
        self.select_drop_down_value_by_text(create_account_page.get_address_state_drop_down(),
                                    create_account_page_data.test_create_account_page_correct_data.get("state"))
        self.send_value_to_text_box(create_account_page.get_address_zip_code_text_box(),
                                    create_account_page_data.test_create_account_page_correct_data.get("zip_code"))
        self.select_drop_down_value_by_text(create_account_page.get_address_country_drop_down(),
                                    create_account_page_data.test_create_account_page_correct_data.get("country"))
        #self.click(self.driver.find_element_by_id("test"))

