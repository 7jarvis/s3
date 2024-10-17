from selenium.webdriver.common.by import By
from elements.p import P
from .base_page import BasePage


class FramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(@class, 'text-center')]")
    BIG_IFRAME_LOC = (By.XPATH, "//iframe[@id='frame1']")
    SMALL_IFRAME_LOC = (By.XPATH, "//iframe[@id='frame2']")
    TEXT_LOC = (By.XPATH, "//*[@id='sampleHeading']")

    def __init__(self, browser):
        super().__init__(browser)
        self.text = P(self.driver, self.TEXT_LOC, description='Text inside of IFrame')

    def is_page_opened(self):
        super().wait_for_open()
        return True

    def get_text(self):
        element = self.text.presence_of_element()
        text = element.text
        return text
