from .base_page import BasePage
from selenium.webdriver.common.by import By
from elements.web_element import WebElement


class ContextMenu(BasePage):
    UNIQUE_ELEMENT_LOC = (By.ID, "hot-spot")

    def __init__(self, browser):
        super().__init__(browser)
        self.context_menu = WebElement(browser.driver, self.UNIQUE_ELEMENT_LOC,
                                       description="Main Page -> Click on the context menu")
        self.page_name = "Context menu page"
        self.unique_element = WebElement(browser.driver, self.UNIQUE_ELEMENT_LOC,
                                         description="Main Page -> Unique element")

    def click_on_context_menu(self):
        self.context_menu.context_click()

    def get_alert_text(self):
        text = self.browser.get_alert_text()
        return text
