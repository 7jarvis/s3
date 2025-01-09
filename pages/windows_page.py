from selenium.webdriver.common.by import By
from .base_page import BasePage
from elements.web_element import WebElement


class WindowsPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'Click')]")
    CLICK_TEXT_LOC = (By.XPATH, "//*[contains(text(), 'Click')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Windows page"
        self.unique_element = WebElement(browser.driver, self.UNIQUE_ELEMENT_LOC,
                                         description="Main Page -> 'Click here' text")
        self.click_element = WebElement(browser.driver, self.CLICK_TEXT_LOC,
                                        description="Main Page -> Click on 'Click here'")

    def click_on_click_here(self):
        self.click_element.click()
