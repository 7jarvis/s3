from selenium.webdriver.common.by import By
from elements.span import Span
from .base_page import BasePage
from elements.li import Li


class IFramePage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//img[@alt='Selenium Online Training']")
    url = 'https://demoqa.com'
    ALERTS_SECTION_LOC = (By.XPATH, "//*[contains(text(), 'Alerts, Frame & Windows')]")
    NESTED_FRAMES_LOC = (By.XPATH, "//*[contains(text(), 'Nested')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.nested = Li(self.driver, self.NESTED_FRAMES_LOC, description='Opened section -> Choose page')
        self.section = Span(self.driver, self.ALERTS_SECTION_LOC, description='Main page -> Open section')

    def is_page_opened(self):
        super().wait_for_open()
        return True

    def click_on_section(self):
        self.section.presence_of_element()
        self.section.click()

    def click_on_page(self):
        self.nested.visibility_of_element()
        self.nested.click()
