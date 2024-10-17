from browser.browser import Browser
from pages.slider_page import SliderPage
from elements.input import Input


def test_5():
    browser_instance = Browser()
    slider = SliderPage(browser_instance.driver())
    browser_instance.driver().get(slider.url)
    assert slider.is_page_opened(), "Expected result: Page was opened\n Actual result: Page wasn`t opened"
    assert (slider.move_slider() * Input.STEP) == slider.get_range_num(), "Expected result: The displayed number is correct\n Actual result: The displayed number is not correct"
    browser_instance.quit()
