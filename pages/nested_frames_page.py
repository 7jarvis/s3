from selenium.webdriver.common.by import By
from elements.iframe import IFrame
from elements.web_element import WebElement

from .base_page import BasePage


class NestedFramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'Nested Frames')]")
    PARENT_FRAME_LOC = (By.XPATH, "//*[@id='frame1']")
    CHILD_FRAME_LOC = (By.XPATH, "//iframe[contains(@srcdoc, 'Child Iframe')]")
    FRAMES_SECTION_LOC = (By.XPATH, "//*[@id='item-2' and contains(.//span, 'Frames')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.child = IFrame(browser.driver, self.CHILD_FRAME_LOC, description='Child IFrame element')
        self.parent = IFrame(browser.driver, self.PARENT_FRAME_LOC, description='Parent IFrame element')
        self.section = WebElement(browser.driver, self.FRAMES_SECTION_LOC, description='Frames section')
        self.unique_element = WebElement(browser.driver, self.UNIQUE_ELEMENT_LOC,
                                         description='Main page -> Unique element')

    def wait_for_open(self):
        super().wait_for_open()

    def presence_of_parent_iframe_element(self):
        self.parent.presence_of_element()
        return True

    def presence_of_child_iframe_element(self):
        self.child.presence_of_element()
        return True

    def click_on_section(self):
        self.section.click()
