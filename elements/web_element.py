import logging

from selenium.common import TimeoutException

from .base_element import BaseElement


class WebElement(BaseElement):
    def is_exists(self):
        try:
            self.presence_of_element()
            return True
        except TimeoutException:
            return False
