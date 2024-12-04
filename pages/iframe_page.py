from selenium.webdriver.common.by import By
from elements.web_element import WebElement
from .base_page import BasePage


class IFramePage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//img[@alt='Selenium Online Training']")
    ALERTS_SECTION_LOC = (By.XPATH, "//*[contains(text(), 'Alerts, Frame & Windows')]")
    NESTED_FRAMES_LOC = (By.XPATH, "//*[contains(text(), 'Nested')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.nested = WebElement(browser.driver, self.NESTED_FRAMES_LOC, description='Opened section -> Choose page')
        self.section = WebElement(browser.driver, self.ALERTS_SECTION_LOC, description='Main page -> Open section')
        self.unique_element = WebElement(browser.driver, self.UNIQUE_ELEMENT_LOC,
                                         description='Main page -> Unique element')

    def wait_for_open(self):
        super().wait_for_open()

    def click_on_section(self):
        self.section.click()

    def click_on_page(self):
        self.nested.click()
