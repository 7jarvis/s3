from selenium.webdriver.common.by import By
from elements.iframe import IFrame
from elements.li import Li

from .base_page import BasePage


class NestedFramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'Nested Frames')]")
    PARENT_FRAME_LOC = (By.XPATH, "//*[@id='frame1']")
    CHILD_FRAME_LOC = (By.XPATH, "//iframe[contains(@srcdoc, 'Child Iframe')]")
    FRAMES_SECTION_LOC = (By.XPATH, "//*[@id='item-2' and contains(.//span, 'Frames')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.child = IFrame(self.driver, self.CHILD_FRAME_LOC, description='Child IFrame element')
        self.parent = IFrame(self.driver, self.PARENT_FRAME_LOC, description='Parent IFrame element')
        self.section = Li(self.driver, self.FRAMES_SECTION_LOC, description='Frames section')

    def is_page_opened(self):
        super().wait_for_open()
        return True

    def presence_of_parent_iframe_element(self):
        self.parent.presence_of_element()
        return True

    def presence_of_child_iframe_element(self):
        self.child.presence_of_element()
        return True

    def click_on_section(self):
        self.section.presence_of_element()
        self.section.click()
