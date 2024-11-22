from selenium.common import TimeoutException
import logging


class BasePage:
    UNIQUE_ELEMENT_LOC = None

    def __init__(self, browser):
        self.unique_element = None
        self.browser = browser
        self.page_name = None
        self.element = None

    def wait_for_open(self):
        logging.info("Open page")
        try:
            self.unique_element.presence_of_element()
        except TimeoutException:
            raise TimeoutException




