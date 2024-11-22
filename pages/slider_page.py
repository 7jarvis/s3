from selenium.webdriver.common.by import By
from utilites.get_random_number import get_random_num
from .base_page import BasePage
from custom_elements.input_slider import Input


class SliderPage(BasePage):
    url = "https://the-internet.herokuapp.com/horizontal_slider"
    RANGE_LOC = (By.XPATH, "//*[@id='range']")
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//input[@type='range']")

    def __init__(self, browser):
        super().__init__(browser)
        self.slide = Input(browser.driver, self.UNIQUE_ELEMENT_LOC, description='Main page -> Moving slider')
        self.value = Input(browser.driver, self.RANGE_LOC, description='Main page -> Value of slider')
        self.target_value = None
        self.unique_element = Input(browser.driver, self.UNIQUE_ELEMENT_LOC, description="Main page -> Unique Element")

    def move_slider(self):
        super().wait_for_open()
        self.target_value = get_random_num() * Input.STEP
        self.slide.move_slider(self.target_value, self.get_range_num())

    def get_range_num(self):
        range_num = self.value.presence_of_element()
        text_value = range_num.text
        num_value = float(text_value)
        return num_value
