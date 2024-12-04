from pages.basic_auth import BasicAuth


def test_basic_auth(browser, config):
    basic = BasicAuth(browser)
    browser.get(config.return_value("test1_url"))
    basic.wait_for_open()
