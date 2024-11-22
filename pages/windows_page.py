from selenium.webdriver.common.by import By
from .base_page import BasePage
from elements.p import P


class WindowsPage(BasePage):
    url = 'http://the-internet.herokuapp.com/windows'
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'Click')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Windows page"
        self.unique_element = P(browser.driver, self.UNIQUE_ELEMENT_LOC, description="Main Page -> Click on 'Click here'")

    def click(self):
        element = self.unique_element.presence_of_element()
        super().wait_for_open()
        self.unique_element.click(element)
