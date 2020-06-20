from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.CommonMethods import CommonMethods


class WebValidation(CommonMethods):

    def validate_element_to_be_displayed(self, element):
        global log
        log = self.getLogger()
        try:
            test_element = WebDriverWait(self.driver, 10, poll_frequency=2).until(EC.visibility_of(element))
            test_element.is_displayed()
            log.info("Element {0} is visible".format(test_element))
        except:
            raise Exception("Element {0} is not visible".format(element))

    def validate_element_not_to_be_displayed(self, element):
        assert not element.is_displayed()
        log.info("Element is not displayed")

    def validate_text_value_of_element(self, element_to_check, expected_text):
        actual_text = element_to_check.text
        assert expected_text == actual_text
        log.info("Expected Message {} is present".format(expected_text))
