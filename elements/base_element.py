from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import logging


class BaseElement:
    TIMEOUT = 10

    def __init__(self, browser, element, description=None):
        self.driver = browser
        self.element = element
        self.description = description
        self.wait = WebDriverWait(self.driver, BaseElement.TIMEOUT)

    def presence_of_element(self):
        logging.info("Waiting for element to be present")
        element = self.wait.until(
            ec.presence_of_element_located(self.element)
        )
        return element

    def visibility_of_element(self):
        logging.info("Waiting for element to be visible")
        element = self.wait.until(
            ec.visibility_of_element_located(self.element)
        )
        return element

    def element_to_be_clickable(self):
        logging.info("Waiting for element to be visible")
        element = self.wait.until(
            ec.element_to_be_clickable(self.element)
        )
        return element

    def presence_of_all_elements(self):
        logging.info("Waiting for all elements to be present")
        elements = self.wait.until(
            ec.presence_of_all_elements_located(self.element)
        )
        return elements

    def click(self):
        web_element = self.wait.until(
            ec.presence_of_element_located(self.element)
        )
        logging.info(f"Clicking on the {self.element}")
        web_element.click()

    def click_with_js(self):
        web_element = self.wait.until(
            ec.presence_of_element_located(self.element)
        )
        logging.info(f"Clicking on the {self.element} using JavaScript")
        self.driver.execute_script("arguments[0].click();", web_element)

    def context_click(self):
        element = self.wait.until(
            ec.presence_of_element_located(self.element)
        )
        logging.info(f"Performing right-click on the {self.element}")

        actions = ActionChains(self.driver)

        actions.context_click(element).perform()

    def get_attribute(self, elements, attribute):
        attributes = []
        for elem in elements:
            attr_value = elem.get_attribute(f'{attribute}')
            attributes.append(attr_value)
        return attributes



