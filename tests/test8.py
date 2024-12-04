from pages.iframe_page import IFramePage
from pages.nested_frames_page import NestedFramesPage
from pages.frames_page import FramesPage


def test_iframe(browser, config):
    iframe = IFramePage(browser)
    nestedFrame = NestedFramesPage(browser)
    frame = FramesPage(browser)
    browser.get(config.return_value("test8_url"))
    iframe.wait_for_open()
    iframe.click_on_section()
    iframe.click_on_page()
    nestedFrame.wait_for_open()
    assert nestedFrame.presence_of_parent_iframe_element(), "Expected result: Parent IFrame elemenet is present\n Actual result: Parent IFrame element isn`t present"
    browser.switch_to_iframe(nestedFrame.parent)
    assert nestedFrame.presence_of_child_iframe_element(), "Expected result: Child IFrame elemenet is present\n Actual result: Child IFrame element isn`t present"
    browser.switch_to_default()
    nestedFrame.click_on_section()
    frame.wait_for_open()
    browser.switch_to_iframe(frame.big)
    text1 = frame.get_iframe_text()
    browser.switch_to_default()
    browser.switch_to_iframe(frame.small)
    text2 = frame.get_iframe_text()
    assert text1 == text2, f"Expected result: Texts inside the IFrames are equal: {text1} == {text2}\n Actual result: Texts inside the IFrames are not equal {text1} != {text2}"
