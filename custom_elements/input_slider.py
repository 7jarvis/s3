import logging
from selenium.webdriver import ActionChains, Keys
from elements.input import Input


class SliderElement(Input):
    STEP = 0.5

    def __init__(self, browser, element, description=None, timeout=None):
        super().__init__(browser, element, description, timeout)
        self.browser = browser

    def send_keys(self, credentials):
        logging.info("Send credentials")
        self.element.send_keys(credentials)

    def move_slider(self, target_value, current_value):
        actions = ActionChains(self.browser)
        if target_value < current_value:
            while current_value != target_value:
                actions.send_keys(Keys.ARROW_DOWN)
                current_value -= self.STEP
            actions.perform()
        else:
            while current_value != target_value:
                actions.send_keys(Keys.ARROW_UP)
                current_value += self.STEP
            actions.perform()
