import logging
#wrote this comment to add to git

class BasePage:
    UNIQUE_ELEMENT_LOC = None

    def __init__(self, browser):
        self.unique_element = None
        self.browser = browser
        self.page_name = None

    def wait_for_open(self):
        logging.info("Open page")
        self.unique_element.presence_of_element()
