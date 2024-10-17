from selenium.webdriver.common.by import By

from .base_page import BasePage


class AlertsWindowsPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'Please select an item')]")

    def is_page_opened(self):
        super().wait_for_open()
        return True
