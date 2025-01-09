from selenium.webdriver.common.by import By
from elements.web_element import WebElement
from .base_page import BasePage


class NewWindowPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'New Window')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = WebElement(browser.driver, self.UNIQUE_ELEMENT_LOC,
                                         description='Main page ->"New window text"')
        self.page_name = "New window"
