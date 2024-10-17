from .base_element import BaseElement
from selenium.webdriver import ActionChains


class Img(BaseElement):
    def hover_over_element(self, n):
        elements = self.presence_of_all_elements()
        element = elements[n]
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def get_attribute(self, elements, attribute):
        attributes = super().get_attribute(elements, attribute)
        return attributes
