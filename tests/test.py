from pages.basic_auth import BasicAuth
from browser.browser import Browser


def test_1():
    browser_instance = Browser()
    basic = BasicAuth(browser_instance.driver())
    basic.log_in()
    assert basic.wait_for_open(), "Expected result: Page was opened\n Actual result: Page wasn`t opened"
    assert basic.check_text(), "Expected result: Text is displayed on the page\n Actual result: Text is not displayed"
    browser_instance.quit()
