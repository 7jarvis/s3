from pages.dynamic_content_page import DynamicContent


def test_dynamic_content(browser, config):
    dynamic = DynamicContent(browser)
    browser.get(config.return_value("test10_url"))
    dynamic.wait_for_open()
    while dynamic.compare_images(3) > 2:
        browser.refresh()
