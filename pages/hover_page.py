import logging

import requests
from bs4 import BeautifulSoup
from .base_page import BasePage
from selenium.webdriver.common.by import By
from elements.img import Img
from elements.multiweb_element import MultiWebElement
from selenium.webdriver import ActionChains


class HoverPage(BasePage):
    url = 'https://the-internet.herokuapp.com/hovers'
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'Hover over')]")
    IMAGE_LOC = "img[alt='User Avatar']"
    SEL_IMAGE_LOC = lambda x: f"(//img[@alt='User Avatar'])[{x}]"
    SEL_USERNAME_LOC = (By.XPATH, "//*[contains(text(), 'name: ')]")
    USERNAME_LOC = "//*[contains(text(), 'name: ')]"
    PROFILE_LINK_LOC = (By.XPATH, "//*[contains(text(), 'View')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Hover page"
        self.unique_element = Img(browser.driver, self.UNIQUE_ELEMENT_LOC, description="Main Page -> Header")
        self.image = Img(browser.driver, self.IMAGE_LOC, description="Main Page -> Hover over IMG")
        self.multi_image = MultiWebElement(browser.driver, lambda x: (By.XPATH, f"(//img[@alt='User Avatar'])[{x}]"),
                                           description="Main page ->Profile Image")
        self.multi_username = MultiWebElement(browser.driver,
                                              lambda x: (By.XPATH, f"(//*[contains(text(), 'name: ')])[{x}]"),
                                              description="Main page ->Profile Image")
        self.username_element = Img(browser.driver, self.USERNAME_LOC,
                                    description="Main Page -> Username")
        self.multi_link_element = MultiWebElement(browser.driver,
                                                  lambda x: (By.XPATH, f"(//*[contains(text(), 'View')])[{x}]"),
                                                  description="Main Page -> View profile")

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

    def count_users(self):
        return len(self.parse_elements(self.IMAGE_LOC, url='https://the-internet.herokuapp.com/hovers'))

    def select_user(self):
        try:
            image = next(self.multi_image)
            image_element = image.presence_of_element()
            actions = ActionChains(self.browser.driver)
            actions.move_to_element(image_element).perform()
        except StopIteration:
            print("Reached end of available elements.")
            return None

    def check_username(self):
        try:
            username = next(self.multi_username)
            text_value = username.presence_of_element().text
            return text_value
        except StopIteration:
            print("Reached end of available elements.")
            return None

    def open_profile_page(self):
        try:
            link = next(self.multi_link_element)
            link_text = link.presence_of_element().get_attribute("href")
            self.browser.driver.get(link_text)
        except StopIteration:
            print("Reached end of available elements.")
            return None

    def check_link(self, n):
        expected = f'users/{n + 1}'
        if expected in self.browser.get_current_url():
            self.browser.go_back()
            return True
        else:
            return False
