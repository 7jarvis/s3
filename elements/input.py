from .base_element import BaseElement
import logging


class Input(BaseElement):
    def send_keys(self, credentials):
        logging.info(f"Send {credentials} to {self.description}")
        element = self.presence_of_element()
        element.send_keys(credentials)
        element.clear()
