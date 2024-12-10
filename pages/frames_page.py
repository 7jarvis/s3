from selenium.webdriver.common.by import By
from elements.web_element import WebElement
from .base_page import BasePage
from elements.iframe import IFrame


class FramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(@class, 'text-center')]")
    BIG_IFRAME_LOC = (By.XPATH, "//iframe[@id='frame1']")
    SMALL_IFRAME_LOC = (By.XPATH, "//iframe[@id='frame2']")
    TEXT_LOC = (By.ID, 'sampleHeading')

    def __init__(self, browser):
        super().__init__(browser)
        self.text = WebElement(browser.driver, self.TEXT_LOC, description='Text inside of IFrame')
        self.big = IFrame(browser.driver, self.BIG_IFRAME_LOC, description='Big IFrame')
        self.small = IFrame(browser.driver, self.SMALL_IFRAME_LOC, description='Small IFrame')
        self.unique_element = WebElement(browser.driver, self.UNIQUE_ELEMENT_LOC,
                                         description='Main page -> Unique element')

    def get_iframe_text(self):
        text = self.text.get_text()
        return text
