from selenium.webdriver.common.by import By

from .base_page import BasePage
from elements.a import a


class WindowsPage(BasePage):
    url = 'http://the-internet.herokuapp.com/windows'
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'Click')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Windows page"
        self.click_here = a(self.driver, self.UNIQUE_ELEMENT_LOC, description="Main Page -> Click on 'Click here'")

    def is_page_opened(self):
        super().wait_for_open()
        return True

    def click(self):
        self.click_here.click()
