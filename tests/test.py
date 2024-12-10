from pages.basic_auth import BasicAuth


def test_basic_auth(browser, config):
    browser.get(config.get_value("test1_url"))
    basic = BasicAuth(browser)
    basic.wait_for_open()
    assert True  # test passed
