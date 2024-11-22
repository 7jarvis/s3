from .base_page import BasePage
from selenium.webdriver.common.by import By
from elements.p import P


class ContextMenu(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='hot-spot']")

    def __init__(self, browser):
        super().__init__(browser)
        self.context_menu = P(browser.driver, self.UNIQUE_ELEMENT_LOC,
                                description="Main Page -> Click on the context menu")
        self.page_name = "Context menu page"
        self.unique_element = P(browser.driver, self.UNIQUE_ELEMENT_LOC, description = "Main Page -> Unique element")

    def click_on_context_menu(self):
        super().wait_for_open()
        self.context_menu.context_click()
        text = self.get_text()
        return text

    def get_text(self):
        return self.browser.get_alert_text()
