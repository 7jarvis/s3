from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import logging
from utilites.config_reader import ConfigReader


class BaseElement:
    cfg = ConfigReader()
    TIMEOUT = cfg.get_value("TIMEOUT")

    def __init__(self, browser, locator, description=None, timeout=None):
        self.driver = browser
        self.action_chains = ActionChains(browser)
        self.element = locator
        self.description = description
        self.timeout = self.TIMEOUT
        self.wait = WebDriverWait(self.driver, BaseElement.TIMEOUT)

    def presence_of_element(self, timeout=None):
        logging.info(f"Wait for element {self.description} to be present")
        wait_time = timeout or self.timeout
        element = WebDriverWait(self.driver, wait_time).until(
            ec.presence_of_element_located(self.element)
        )
        return element

    def visibility_of_element(self, timeout=None):
        logging.info(f"Wait for element {self.description} to be visible")
        wait_time = timeout or self.timeout
        element = WebDriverWait(self.driver, wait_time).until(
            ec.visibility_of_element_located(self.element)
        )
        return element

    def element_to_be_clickable(self, timeout=None):
        logging.info(f"Wait for element {self.description} to be clickable")
        wait_time = timeout or self.timeout
        element = WebDriverWait(self.driver, wait_time).until(
            ec.element_to_be_clickable(self.element)
        )
        return element

    def is_exists(self):
        logging.info(f"Check if element {self.description} exists")
        try:
            self.presence_of_element(0)
            return True
        except TimeoutException:
            return False

    def click(self):
        logging.info(f"Click on the {self.description}")
        element = self.element_to_be_clickable()
        element.click()

    def js_click(self, timeout=None):
        wait_time = timeout or self.timeout
        web_element = WebDriverWait(self.driver, wait_time).until(
            ec.presence_of_element_located(self.element)
        )

        logging.info(f"Click on the {self.description} using JavaScript")
        self.driver.execute_script("arguments[0].click();", web_element)

    def context_click(self, timeout=None):
        wait_time = timeout or self.timeout
        element = WebDriverWait(self.driver, wait_time).until(
            ec.element_to_be_clickable(self.element)
        )
        logging.info(f"Perform right-click on the {self.description}")

        actions = ActionChains(self.driver)

        actions.context_click(element).perform()

    def get_attribute(self, attribute_name):
        logging.info(f"Retreive attribute '{attribute_name}' of element.")
        attribute_value = self.presence_of_element().get_attribute(attribute_name)
        return attribute_value

    def get_text(self):
        logging.info("Get text of the element")
        return self.presence_of_element().text
