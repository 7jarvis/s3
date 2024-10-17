from elements.base_element import BaseElement
import logging


class BasePage:
    UNIQUE_ELEMENT_LOC = None
    url = None

    def __init__(self, browser):
        self.unique_element = None
        self.driver = browser
        self.page_name = None
        self.element = None
        self.base = BaseElement(self.driver, self.UNIQUE_ELEMENT_LOC)

    def wait_for_open(self):
        logging.info("Opening page")
        self.base.presence_of_element()

    def check_text(self):
        self.base.presence_of_element()

    def click(self):
        self.base.click()

    def get_title(self):
        title = self.driver.title
        return title


