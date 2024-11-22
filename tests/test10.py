from browser.browser import Browser
from pages.dynamic_content_page import DynamicContent


def test_dynamic_content(browser, config):
    dynamic = DynamicContent(browser)
    browser.driver.get(config.return_value("test10_url"))
    assert dynamic.is_page_opened(), "Expected result: Page was opened\n Actual result: Page wasn`t opened"
    while not dynamic.compare_images():
        browser.refresh()

