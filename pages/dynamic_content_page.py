import logging

import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from elements.p import P
from .base_page import BasePage
from elements.img import Img
from elements.multiweb_element import MultiWebElement


class DynamicContent(BasePage):
    url = 'http://the-internet.herokuapp.com/dynamic_content'
    IMG_LOC = (By.XPATH, "//img[contains(@src,'avatars')]")
    STR_IMG_LOC = "img[src*='avatars']"
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'Dynamic Content')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = P(browser.driver, self.UNIQUE_ELEMENT_LOC,
                                description='Main page -> "Dynamic Content" text')
        self.page_name = 'Dynamic content'
        self.images = Img(browser.driver, self.IMG_LOC, description='Main page -> Images on the page')
        self.multi_image = MultiWebElement(browser.driver,
                                           lambda x: (By.XPATH, f"(//img[contains(@src,'avatars')])[{x}]"),
                                           description='Main page -> Images on the page')

    def is_page_opened(self):
        super().wait_for_open()
        return True

    @staticmethod
    def parse_elements(str_locator, url):
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        logging.info("Parse all elements")
        elements = soup.select(str_locator)
        return elements

    def get_attributes(self):
        images = self.parse_elements(self.STR_IMG_LOC, url='http://the-internet.herokuapp.com/dynamic_content')
        return images

    def compare_images(self):
        images = self.get_attributes()
        return True if len(set(images)) < 3 else False
