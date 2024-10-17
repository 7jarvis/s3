from selenium.webdriver.common.by import By
from elements.a import a

from .base_page import BasePage


class NewWindowPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//div//*[contains(text(), 'New Window')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "New window"

    def is_page_opened(self):
        super().wait_for_open()
        return True

    def save_current_window(self):
        current_window = self.driver.current_window_handle
        return current_window

    def get_title(self):
        return super().get_title()
