from browser.browser import Browser
from pages.dynamic_content_page import DynamicContent


def test_10():
    browser_instance = Browser()
    dynamic = DynamicContent(browser_instance.driver())
    browser_instance.driver().get(dynamic.url)
    assert dynamic.is_page_opened(), "Expected result: Page was opened\n Actual result: Page wasn`t opened"
    while not dynamic.compare_srcs():
        browser_instance.refresh()

