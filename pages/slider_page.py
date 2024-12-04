from selenium.webdriver.common.by import By
from .base_page import BasePage
from custom_elements.input_slider import SliderElement


class SliderPage(BasePage):
    RANGE_LOC = (By.ID, 'range')
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//input[@type='range']")

    def __init__(self, browser):
        super().__init__(browser)
        self.slide = SliderElement(browser.driver, self.UNIQUE_ELEMENT_LOC, description='Main page -> Moving slider')
        self.value = SliderElement(browser.driver, self.RANGE_LOC, description='Main page -> Value of slider')
        self.unique_element = SliderElement(browser.driver, self.UNIQUE_ELEMENT_LOC,
                                            description="Main page -> Unique Element")

    def wait_for_open(self):
        super().wait_for_open()

    def move_slider(self, target_value):
        self.focus_on_slider()
        self.slide.move_slider(target_value, self.get_range_num())

    def focus_on_slider(self):
        slider = self.slide.presence_of_element()
        actions = self.browser.action_chains()
        actions.move_to_element(slider).click().perform()

    def get_range_num(self):
        range_num = self.value.presence_of_element()
        text_value = range_num.text
        num_value = float(text_value)
        return num_value
