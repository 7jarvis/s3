import logging
from selenium.webdriver import ActionChains, Keys
from elements.base_element import BaseElement


class Input(BaseElement):
    STEP = 0.5

    def send_keys(self, credentials):
        logging.info("Send credentials")
        self.element.send_keys(credentials)

    def move_slider(self, target_value, current_value):
        slider = self.presence_of_element()

        self.driver.execute_script("arguments[0].focus();", slider)
        actions = ActionChains(self.driver)
        if target_value < current_value:
            while current_value != target_value:
                actions.send_keys(Keys.ARROW_DOWN)
                current_value -= self.STEP
            actions.perform()
            return target_value
        else:
            while current_value != target_value:
                actions.send_keys(Keys.ARROW_UP)
                current_value += self.STEP
            actions.perform()
            return target_value
