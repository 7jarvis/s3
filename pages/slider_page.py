from selenium.webdriver.common.by import By

from .base_page import BasePage
from elements.input import Input


class SliderPage(BasePage):
    url = "https://the-internet.herokuapp.com/horizontal_slider"
    RANGE_LOC = (By.XPATH, "//*[@id='range']")
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//input[@type='range']")

    def __init__(self, browser):
        super().__init__(browser)
        self.slide = Input(self.driver, self.UNIQUE_ELEMENT_LOC, description='Main page -> Moving slider')
        self.value = Input(self.driver, self.RANGE_LOC, description='Main page -> Value of slider')

    def is_page_opened(self):
        super().wait_for_open()
        return True

    def move_slider(self):
        n = self.slide.move_slider()
        return n

    def get_range_num(self):
        range_num = self.value.presence_of_element()
        text_value = range_num.text
        num_value = float(text_value)
        return num_value
