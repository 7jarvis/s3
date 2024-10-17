from selenium.webdriver.common.by import By

from .base_page import BasePage
from elements.img import Img

class DynamicContent(BasePage):
    url = 'http://the-internet.herokuapp.com/dynamic_content'
    IMG_LOC = (By.XPATH, "//img[contains(@src,'avatars')]")
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'Dynamic Content')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = 'Dynamic content'
        self.images = Img(self.driver, self.IMG_LOC, description='Main page -> Images on the page')

    def is_page_opened(self):
        super().wait_for_open()
        return True

    def presence_of_all_elements_located(self):
        images = self.images.presence_of_all_elements()
        return images

    def get_attributes(self):
        images = self.presence_of_all_elements_located()
        return self.images.get_attribute(images, self.IMG_LOC)

    def compare_srcs(self):
        srcs = self.get_attributes()
        if srcs[0] == (srcs[1] or srcs[2]) or srcs[1] == srcs[2]:
            return True
        else:
            return False


