from selenium.webdriver.common.by import By
from elements.p import P
from .base_page import BasePage
from elements.input import Input


class BasicAuth(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'Congratulations!')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Basic auth page"
        self.input = Input(browser.driver, self.UNIQUE_ELEMENT_LOC,
                           description="Login page -> Username and password input")
        self.unique_element = P(browser.driver, self.UNIQUE_ELEMENT_LOC,
                                description='Main Page -> "Congratulations!" text')

    def wait_for_open(self):
        super().wait_for_open()
