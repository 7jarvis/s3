from browser.browser import Browser
from pages.iframe_page import IFramePage
from pages.nested_frames_page import NestedFramesPage
from pages.frames_page import FramesPage


def test_8():
    browser_instance = Browser()
    iframe = IFramePage(browser_instance.driver())
    nestedFrame = NestedFramesPage(browser_instance.driver())
    frame = FramesPage(browser_instance.driver())
    browser_instance.driver().get(iframe.url)
    assert iframe.is_page_opened(), "Expected result: Page was opened\n Actual result: Page wasn`t opened"
    iframe.click_on_section()
    iframe.click_on_page()
    assert nestedFrame.is_page_opened(), "Expected result: Page was opened\n Actual result: Page wasn`t opened"
    assert nestedFrame.presence_of_parent_iframe_element(), "Expected result: Parent IFrame elemenet is present\n Actual result: Parent IFrame element isn`t present"
    browser_instance.switch_to_iframe(nestedFrame.PARENT_FRAME_LOC)
    assert nestedFrame.presence_of_child_iframe_element(), "Expected result: Child IFrame elemenet is present\n Actual result: Child IFrame element isn`t present"
    browser_instance.switch_to_default()
    nestedFrame.click_on_section()
    assert frame.is_page_opened(), "Expected result: Page was opened\n Actual result: Page wasn`t opened"
    browser_instance.switch_to_iframe(frame.BIG_IFRAME_LOC)
    text1 = frame.get_text()
    browser_instance.switch_to_default()
    browser_instance.switch_to_iframe(frame.SMALL_IFRAME_LOC)
    text2 = frame.get_text()
    assert text1 == text2, "Expected result: Texts inside the IFrames are equal\n Actual result: Texts inside the IFrames are not equal"
