from pages.slider_page import SliderPage
from utilites.random_utils import RandomUtils


def test_actions(browser, config):
    browser.get(config.get_value("test5_url"))
    slider_page = SliderPage(browser)
    attributes = slider_page.get_slider_attributes()
    target_value = RandomUtils.get_random_num(attributes["min"], attributes["max"], attributes["step"])
    slider_page.wait_for_open()
    slider_page.move_slider(target_value, attributes["step"])
    assert target_value == slider_page.get_range_num(), f"Expected result: The displayed number is {target_value}\n Actual result: The displayed number is {slider.get_range_num()}"
