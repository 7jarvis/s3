import logging

from selenium.webdriver.common.by import By

from .base_page import BasePage
from elements.input import Input


class BasicAuth(BasePage):
    url = 'http://admin:admin@the-internet.herokuapp.com/basic_auth'
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'Congratulations!')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Basic auth page"
        self.input = Input(self.driver, self.UNIQUE_ELEMENT_LOC,
                           description="Login page -> Username and password input")
        self.unique_element = (By.XPATH, "//p[contains(text(), 'Congratulations!')]")

    def log_in(self):
        logging.info(f"{self.page_name}: logging in")
        self.driver.get(self.url)

    def wait_for_open(self):
        super().wait_for_open()
        return True

    def check_text(self):
        super().check_text()
        return True



