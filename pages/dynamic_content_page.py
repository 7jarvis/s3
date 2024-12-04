import logging
from selenium.webdriver.common.by import By
from elements.p import P
from .base_page import BasePage
from elements.web_element import WebElement
from elements.multiweb_element import MultiWebElement


class DynamicContent(BasePage):
    IMG_LOC = (By.XPATH, "//img[contains(@src,'avatars')]")
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'Dynamic Content')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.unique_element = P(browser.driver, self.UNIQUE_ELEMENT_LOC,
                                description='Main page -> "Dynamic Content" text')
        self.page_name = 'Dynamic content'
        self.images = WebElement(browser.driver, self.IMG_LOC, description='Main page -> Images on the page')
        self.multi_image = MultiWebElement(browser.driver,
                                           lambda x: (By.XPATH, f"(//img[contains(@src,'avatars')])[{x}]"),
                                           description='Main page -> Images on the page')

    def wait_for_open(self):
        super().wait_for_open()

    def parse_element_html(self, num_of_elems):
        attributes = []
        for i in range(num_of_elems):
            for image in self.multi_image:
                image_element = image.presence_of_element()
                attributes.append(image_element.get_attribute("outerHTML"))

                logging.info("Reached end of available elements.")
            return attributes

    def compare_images(self, num_of_elems):
        images = self.parse_element_html(num_of_elems)
        return len(set(images))
