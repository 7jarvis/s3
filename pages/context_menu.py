from .base_page import BasePage
from selenium.webdriver.common.by import By
from elements.div import Div
from elements.alert import Alerts


class ContextMenu(BasePage):
    url = 'https://the-internet.herokuapp.com/context_menu'
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='hot-spot']")

    def __init__(self, browser):
        super().__init__(browser)
        self.context_menu = Div(self.driver, self.UNIQUE_ELEMENT_LOC,
                                description="Main Page -> Click on the context menu")
        self.page_name = "Context menu page"
        self.al = Alerts(self.driver, self.element)

    def is_page_opened(self):
        super().wait_for_open()
        return True

    def click(self):
        self.context_menu.context_click()
        text = self.get_text()
        return text

    def get_text(self):
        return self.al.get_text(self.driver)

    def close_alert(self):
        self.al.close_alert(self.driver)
        self.al.is_alert_closed(self.driver)
        return True
