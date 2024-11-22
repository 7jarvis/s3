from pages.slider_page import SliderPage


def test_actions(browser):
    slider = SliderPage(browser)
    browser.driver.get(slider.url)
    slider.move_slider()
    assert slider.target_value == slider.get_range_num(), "Expected result: The displayed number is correct\n Actual result: The displayed number is not correct"
