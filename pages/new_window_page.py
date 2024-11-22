from selenium.webdriver.common.by import By
from elements.p import P
from .base_page import BasePage


class NewWindowPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//div//*[contains(text(), 'New Window')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = P(browser.driver, self.UNIQUE_ELEMENT_LOC, description='Main page ->"New window text"')
        self.page_name = "New window"

    def get_title(self):
        super().wait_for_open()
        return self.browser.get_title()
