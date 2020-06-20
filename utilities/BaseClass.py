import inspect
import logging
import time

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('C:\Frameworks\Python\myseleniumpythonproject\logs\logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def select_drop_down_value(self, locator, text):
        try:
            sel = Select(locator)
            sel.select_by_value(text)
        except:
            raise Exception("Dropdown value {0} is not present".format(text))

    def select_drop_down_value_by_text(self, locator, text):
        try:
            sel = Select(locator)
            sel.select_by_visible_text(text)
        except:
            raise Exception("Dropdown value with text {0} is not present".format(text))

    def select_drop_down_value_by_index(self, locator, index):
        try:
            sel = Select(locator)
            sel.select_by_index(index)
        except:
            raise Exception("Dropdown index {0} is not present".format(index))

    def move_to_element(self, element):
        try:
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
        except:
            raise Exception("Move to element didn't work")

    def move_to_element_and_click(self, element):
        try:
            action = ActionChains(self.driver)
            action.move_to_element(element).click().perform()
        except:
            raise Exception("Move to element and click didn't work")

    def send_value_to_text_box(self, element, text):
        try:
            test_element = WebDriverWait(self.driver, 10).until(EC.visibility_of(element))
            test_element.clear()
            test_element.send_keys(text)
        except:
            raise Exception("Send value to text box didn't work")

    def scroll_down_to_element(self, element):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of(element))
            self.driver.execute_script(" return arguments[0].scrollIntoView();", element)
        except:
            raise Exception("Scroll down to element didn't work")

    def scroll_till_end_of_the_page(self):
        try:
            self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        except:
            raise Exception("Scroll to end of the page didn't work")

    def scroll_down_by_pixel(self, pixel):
        try:
            self.driver.execute_script("window.scrollBy(0,"+ str(pixel)+")", "")
        except:
            raise Exception("Scroll down by pixel {0} didn't work".format(pixel))

    def click(self, element):
        try:
            test_element = WebDriverWait(self.driver, 10).until(EC.visibility_of(element))
            test_element.click()
        except NoSuchElementException as exception:
            #raise Exception("Click on the element {0} didn't work".format(element))
            pass

    def double_click(self, element):
        try:
            test_element = WebDriverWait(self.driver, 10).until(EC.visibility_of(element))
            actions = ActionChains(self.driver)
            actions.double_click(test_element).perform()
        except:
            raise Exception("Double click didn't work properly")

    def right_click(self, element):
        try:
            test_element = WebDriverWait(self.driver, 10).until(EC.visibility_of(element))
            actions = ActionChains(self.driver)
            actions.context_click(test_element).perform()
        except:
            raise Exception("Right click didn't work properly")

    def drag_and_drop(self, source_element, target_element):
        try:
            test_source_element = WebDriverWait(self.driver, 10, poll_frequency=2).until(EC.visibility_of(source_element))
            test_target_element = WebDriverWait(self.driver, 10, poll_frequency=2).until(EC.visibility_of(target_element))
            actions = ActionChains(self.driver)
            actions.drag_and_drop(test_source_element, test_target_element).perform()
        except:
            raise Exception("Drag and drop didn't work properly")
