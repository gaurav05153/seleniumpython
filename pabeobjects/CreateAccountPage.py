from selenium.webdriver.common.by import By

from pabeobjects.LoginPage import LoginPage


class CreateAccountPage:

    def __init__(self, driver):
        self.driver = driver

    page_heading = (By.XPATH, "//*[@id='noSlide']/h1[text()='Create an account']")
    personal_info_page_subheading = (
    By.XPATH, "//*[@id='account-creation_form']/div/h3[text()='Your personal information']")
    title_label = (By.XPATH, "//*[@id='account-creation_form']/div/div/label[text()='Title']")
    mr_title_radio_button_label = (By.XPATH, "//label[@for='id_gender1' and contains(string(),'Mr.')]")
    mr_title_radio_button = (By.ID, "uniform-id_gender1")
    mrs_title_radio_button_label = (By.XPATH, "//label[@for='id_gender2' and contains(string(),'Mrs.')]")
    mrs_title_radio_button = (By.ID, "uniform-id_gender2")
    first_name_label = (By.XPATH, "//label[@for='customer_firstname' and text()='First name ']")
    first_name_text_box = (By.ID, "customer_firstname")
    last_name_label = (By.XPATH, "//label[@for='customer_lastname' and text()='Last name ']")
    last_name_text_box = (By.NAME, "customer_lastname")
    email_label = (By.XPATH, "//label[@for='email' and text()='Email ']")
    email_text_box = (By.ID, "email")
    password_label = (By.XPATH, "//label[@for='passwd' and text()='Password ']")
    password_text_box = (By.ID, "passwd")
    date_of_birth_label = (By.XPATH, "//label[text()='Date of Birth']")
    date_dropdown = (By.ID, "days")
    month_dropdown = (By.ID, "months")
    year_dropdown = (By.ID, "years")
    sign_up_for_our_newsletter_check_box = (By.ID, "newsletter")
    receive_special_offers_check_box = (By.ID, "optin")

    address_page_subheading = (By.XPATH, "//*[@id='account-creation_form']/div[2]/h3[text()='Your address']")
    address_first_name_label = (By.XPATH, "//label[@for='firstname' and text()='First name ']")
    address_first_name_text_box = (By.ID, "firstname")
    address_last_name_label = (By.XPATH, "//label[@for='lastname' and text()='Last name ']")
    address_last_name_text_box = (By.NAME, "lastname")
    address_company_label = (By.XPATH, "//label[@for='company' and text()='Company']")
    address_company_text_box = (By.CSS_SELECTOR, "#company")
    address_label = (By.XPATH, "//label[@for='address1' and text()='Address ']")
    address_text_box = (By.CSS_SELECTOR, "#address1")
    address_line2_label = (By.XPATH, "//label[@for='address2' and text()='Address (Line 2)']")
    address_line2_text_box = (By.CSS_SELECTOR, "#address2")
    address_city_label = (By.XPATH, "//label[@for='city' and text()='City ']")
    address_city_text_box = (By.ID, "city")
    address_state_label = (By.XPATH, "//label[@for='id_state' and text()='State ']")
    address_state_drop_down = (By.ID, "id_state")
    address_zip_code_label = (By.XPATH, "//label[@for='postcode' and text()='Zip/Postal Code ']")
    address_zip_code_text_box = (By.ID, "postcode")
    address_country_label = (By.XPATH, "//label[@for='id_country' and text()='Country ']")
    address_country_drop_down = (By.ID, "id_country")
    address_additional_information_label = (By.XPATH, "//label[@for='other' and text()='Additional information']")
    address_additional_information_text_box = (By.ID, "other")
    address_home_phone_label = (By.XPATH, "//label[@for='phone' and text()='Home phone']")
    address_home_phone_text_box = (By.ID, "phone")
    address_mobile_phone_label = (By.XPATH, "//label[@for='phone_mobile' and text()='Mobile phone ']")
    address_mobile_phone_text_box = (By.ID, "phone_mobile")
    address_alias_label = (
    By.XPATH, "//label[@for='alias' and text()='Assign an address alias for future reference. ']")
    address_alias_text_box = (By.ID, "alias")

    def get_page_heading(self):
        return self.driver.find_element(*CreateAccountPage.page_heading)

    def get_personal_info_page_subheading(self):
        return self.driver.find_element(*CreateAccountPage.personal_info_page_subheading)

    def get_title_label(self):
        return self.driver.find_element(*CreateAccountPage.title_label)

    def get_mr_title_radio_button_label(self):
        return self.driver.find_element(*CreateAccountPage.mr_title_radio_button_label)

    def get_mr_title_radio_button(self):
        return self.driver.find_element(*CreateAccountPage.mr_title_radio_button)

    def get_mrs_title_radio_button_label(self):
        return self.driver.find_element(*CreateAccountPage.mrs_title_radio_button_label)

    def get_mrs_title_radio_button(self):
        return self.driver.find_element(*CreateAccountPage.mrs_title_radio_button)

    def get_first_name_label(self):
        return self.driver.find_element(*CreateAccountPage.first_name_label)

    def get_first_name_text_box(self):
        return self.driver.find_element(*CreateAccountPage.first_name_text_box)

    def get_last_name_label(self):
        return self.driver.find_element(*CreateAccountPage.last_name_label)

    def get_last_name_text_box(self):
        return self.driver.find_element(*CreateAccountPage.last_name_text_box)

    def get_email_label(self):
        return self.driver.find_element(*CreateAccountPage.email_label)

    def get_email_text_box(self):
        return self.driver.find_element(*CreateAccountPage.email_text_box)

    def get_password_label(self):
        return self.driver.find_element(*CreateAccountPage.password_label)

    def get_password_text_box(self):
        return self.driver.find_element(*CreateAccountPage.password_text_box)

    def get_date_of_birth_label(self):
        return self.driver.find_element(*CreateAccountPage.date_of_birth_label)

    def get_date_from_date_of_birth_drop_down(self):
        return self.driver.find_element(*CreateAccountPage.date_dropdown)

    def get_month_from_date_of_birth_drop_down(self):
        return self.driver.find_element(*CreateAccountPage.month_dropdown)

    def get_year_from_date_of_birth_drop_down(self):
        return self.driver.find_element(*CreateAccountPage.year_dropdown)

    def get_sign_up_for_our_newsletter_check_box(self):
        return self.driver.find_element(*CreateAccountPage.sign_up_for_our_newsletter_check_box)

    def get_receive_special_offers_check_box(self):
        return self.driver.find_element(*CreateAccountPage.receive_special_offers_check_box)

    """Start of address section methods"""

    def get_address_page_subheading(self):
        return self.driver.find_element(*CreateAccountPage.address_page_subheading)

    def get_address_first_name_label(self):
        return self.driver.find_element(*CreateAccountPage.address_first_name_label)

    def get_address_first_name_text_box(self):
        return self.driver.find_element(*CreateAccountPage.address_first_name_text_box)

    def get_address_last_name_label(self):
        return self.driver.find_element(*CreateAccountPage.address_last_name_label)

    def get_address_last_name_text_box(self):
        return self.driver.find_element(*CreateAccountPage.address_last_name_text_box)

    def get_address_company_label(self):
        return self.driver.find_element(*CreateAccountPage.address_company_label)

    def get_address_company_text_box(self):
        return self.driver.find_element(*CreateAccountPage.address_company_text_box)

    def get_address_label(self):
        return self.driver.find_element(*CreateAccountPage.address_label)

    def get_address_text_box(self):
        return self.driver.find_element(*CreateAccountPage.address_text_box)

    def get_address_line2_label(self):
        return self.driver.find_element(*CreateAccountPage.address_line2_label)

    def get_address_line2_text_box(self):
        return self.driver.find_element(*CreateAccountPage.address_line2_text_box)

    def get_address_city_label(self):
        return self.driver.find_element(*CreateAccountPage.address_city_label)

    def get_address_city_text_box(self):
        return self.driver.find_element(*CreateAccountPage.address_city_text_box)

    def get_address_state_label(self):
        return self.driver.find_element(*CreateAccountPage.address_state_label)

    def get_address_state_drop_down(self):
        return self.driver.find_element(*CreateAccountPage.address_state_drop_down)

    def get_address_zip_code_label(self):
        return self.driver.find_element(*CreateAccountPage.address_zip_code_label)

    def get_address_zip_code_text_box(self):
        return self.driver.find_element(*CreateAccountPage.address_zip_code_text_box)

    def get_address_country_label(self):
        return self.driver.find_element(*CreateAccountPage.address_country_label)

    def get_address_country_drop_down(self):
        return self.driver.find_element(*CreateAccountPage.address_country_drop_down)

    def get_address_additional_information_label(self):
        return self.driver.find_element(*CreateAccountPage.address_additional_information_label)

    def get_address_additional_information_text_box(self):
        return self.driver.find_element(*CreateAccountPage.address_additional_information_text_box)

    def get_address_home_phone_label(self):
        return self.driver.find_element(*CreateAccountPage.address_home_phone_label)

    def get_address_home_phone_text_box(self):
        return self.driver.find_element(*CreateAccountPage.address_home_phone_text_box)

    def get_address_mobile_phone_label(self):
        return self.driver.find_element(*CreateAccountPage.address_mobile_phone_label)

    def get_address_mobile_phone_text_box(self):
        return self.driver.find_element(*CreateAccountPage.address_mobile_phone_text_box)

    def get_address_alias_label(self):
        return self.driver.find_element(*CreateAccountPage.address_alias_label)

    def get_address_alias_text_box(self):
        return self.driver.find_element(*CreateAccountPage.address_alias_text_box)
