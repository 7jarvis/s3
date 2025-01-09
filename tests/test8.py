from pages.iframe_page import IFramePage
from pages.nested_frames_page import NestedFramesPage
from pages.frames_page import FramesPage


def test_iframe(browser, config):
    browser.get(config.get_value("test8_url"))
    iframe = IFramePage(browser)
    iframe.wait_for_open()
    iframe.click_on_section()
    iframe.click_on_page()
    nestedFrame = NestedFramesPage(browser)
    nestedFrame.wait_for_open()
    nestedFrame.presence_of_parent_iframe_element()
    browser.switch_to_iframe(nestedFrame.parent)
    nestedFrame.presence_of_child_iframe_element()
    browser.switch_to_default()
    nestedFrame.click_on_section()
    frame = FramesPage(browser)
    frame.wait_for_open()
    browser.switch_to_iframe(frame.big_iframe)
    text1 = frame.get_iframe_text()
    browser.switch_to_default()
    browser.switch_to_iframe(frame.small_iframe)
    text2 = frame.get_iframe_text()
    assert text1 == text2, f"Expected result: Texts inside the IFrames are equal: {text1} == {text2}\n Actual result: Texts inside the IFrames are not equal {text1} != {text2}"
