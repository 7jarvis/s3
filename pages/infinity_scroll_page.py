from selenium.webdriver.common.by import By
from .base_page import BasePage
from elements.div import Div


class InfinityScroll(BasePage):
    url = 'http://the-internet.herokuapp.com/infinite_scroll'
    COUNT = 23
    PARAGRAPH_LOC = (By.XPATH, "//*[@class='jscroll-added']")
    paragraphs_list = []
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'Infinite Scroll')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = 'Infinite scroll'
        self.paragraphs = Div(self.driver, self.PARAGRAPH_LOC, description='Main page -> Paragraph')

    def is_page_opened(self):
        super().wait_for_open()
        return True

    def count_paragraphs(self, browser):
        while True:
            elements = self.paragraphs.presence_of_all_elements()
            if len(elements) >= self.COUNT:
                return True
            browser.scroll_to_bottom()
