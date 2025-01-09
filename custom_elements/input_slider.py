import logging
from selenium.webdriver import ActionChains, Keys
from elements.input import Input


class SliderElement(Input):

    def move_slider(self, target_value, current_value, step):
        actions = ActionChains(self.driver)
        if target_value < current_value:
            while current_value != target_value:
                actions.send_keys(Keys.ARROW_DOWN)
                current_value -= step
            actions.perform()
        else:
            while current_value != target_value:
                actions.send_keys(Keys.ARROW_UP)
                current_value += step
            actions.perform()
