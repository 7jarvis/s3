from selenium.webdriver.common.by import By
from .base_page import BasePage
from elements.web_element import WebElement
from elements.multiweb_element import MultiWebElement


class InfinityScroll(BasePage):
    PARAGRAPH_LOC = (By.XPATH, "//*[@class='jscroll-added']")
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'Infinite Scroll')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = 'Infinite scroll'
        self.unique_element = WebElement(browser.driver, self.UNIQUE_ELEMENT_LOC,
                                         description='Main page -> "Infinite Scroll" text')
        self.multi_paragraphs = MultiWebElement(browser.driver,
                                                lambda x: (By.XPATH, f"(//*[@class='jscroll-added'])[{x}]"),
                                                description='Main page -> Paragraph')

    def count_paragraphs(self, browser, age):
        elements = []
        while len(elements) != age:
            for paragraph in self.multi_paragraphs:
                elements.append(paragraph)
                if len(elements) == age:
                    return True
            browser.scroll_to_bottom()

        return True
