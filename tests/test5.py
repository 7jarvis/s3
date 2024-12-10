from pages.slider_page import SliderPage
from utilites.random_utils import RandomUtils


def test_actions(browser, config):
    browser.get(config.get_value("test5_url"))
    slider = SliderPage(browser)
    attributes = slider.get_slider_attributes()
    target_value = RandomUtils.get_random_num(attributes["min"], attributes["max"], attributes["step"])
    slider.wait_for_open()
    slider.move_slider(target_value, attributes["step"])
    assert target_value == slider.get_range_num(), f"Expected result: The displayed number is {target_value}\n Actual result: The displayed number is {slider.get_range_num()}"
