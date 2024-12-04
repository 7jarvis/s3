from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import logging
from utilites.config_reader import ConfigReader


class BaseElement:
    cfg = ConfigReader()
    TIMEOUT = cfg.return_value("TIMEOUT")

    def __init__(self, browser, element, description=None, timeout=None):
        self.driver = browser
        self.element = element
        self.description = description
        self.timeout = self.TIMEOUT
        self.wait = WebDriverWait(self.driver, BaseElement.TIMEOUT)

    def presence_of_element(self, timeout=None):
        logging.info("Wait for element to be present")
        wait_time = timeout or self.timeout
        element = WebDriverWait(self.driver, wait_time).until(
            ec.presence_of_element_located(self.element)
        )
        return element

    def visibility_of_element(self):
        logging.info("Wait for element to be visible")
        element = self.wait.until(
            ec.visibility_of_element_located(self.element)
        )
        return element

    def element_to_be_clickable(self):
        logging.info("Wait for element to be clickable")
        element = self.wait.until(
            ec.element_to_be_clickable(self.element)
        )
        return element

    def is_exists(self):
        logging.info("Check if element exists")
        try:
            self.presence_of_element(0)
            return True
        except TimeoutException:
            return False

    def click(self):
        logging.info(f"Click on the {self.element}")
        element = self.presence_of_element()
        element.click()

    def js_click(self):
        web_element = self.wait.until(
            ec.presence_of_element_located(self.element)
        )
        logging.info(f"Click on the {self.element} using JavaScript")
        self.driver.execute_script("arguments[0].click();", web_element)

    def context_click(self):
        element = self.wait.until(
            ec.element_to_be_clickable(self.element)
        )
        logging.info(f"Perform right-click on the {self.element}")

        actions = ActionChains(self.driver)

        actions.context_click(element).perform()

    def get_attribute(self, attribute_name):
        logging.info(f"Retreive attribute '{attribute_name}' of element.")
        attribute_value = self.presence_of_element().get_attribute(attribute_name)
        return attribute_value

    def get_text(self):
        logging.info("Get text of the element")
        return self.presence_of_element().text
