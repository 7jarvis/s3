from pages.basic_auth import BasicAuth


def test_basic_auth(browser, config):
    basic = BasicAuth(browser)
    browser.driver.get(config.return_value("test1_url"))
    assert basic.wait_for_open(), "Expected result: Page was opened\n Actual result: Page wasn`t opened"
