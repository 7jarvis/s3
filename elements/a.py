from .base_element import BaseElement
import logging


class a(BaseElement):

    def get_link(self, n):
        elements = self.presence_of_all_elements()
        link = elements[n].get_attribute("href")
        return link

    def open_link(self, link):
        logging.info("Opening link")
        self.driver.get(link)

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def go_back(self):
        logging.info("Returning to the previous page")
        self.driver.back()


