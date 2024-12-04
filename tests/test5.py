from pages.slider_page import SliderPage
from utilites.get_random_number import get_random_num
from custom_elements.input_slider import SliderElement

START_VALUE_FOR_SLIDER = 1
STOP_VALUE_FOR_SLIDER = 9


def test_actions(browser, config):
    target_value = get_random_num(START_VALUE_FOR_SLIDER, STOP_VALUE_FOR_SLIDER) * SliderElement.STEP
    slider = SliderPage(browser)
    browser.get(config.return_value("test5_url"))
    slider.wait_for_open()
    slider.move_slider(target_value)
    assert target_value == slider.get_range_num(), "Expected result: The displayed number is correct\n Actual result: The displayed number is not correct"
