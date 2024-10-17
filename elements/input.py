from selenium.webdriver import ActionChains, Keys
from .base_element import BaseElement
from utilites.get_random_number import get_random_num


class Input(BaseElement):
    STEP = 0.5

    def send_keys(self, credentials):
        self.element.send_keys(credentials)

    def move_slider(self):
        slider = self.presence_of_element()
        self.driver.execute_script("arguments[0].focus();", slider)
        actions = ActionChains(self.driver)
        number = get_random_num()
        for _ in range(number):
            actions.send_keys(Keys.ARROW_UP)
        actions.perform()
        return number
