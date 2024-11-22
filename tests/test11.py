from pages.infinity_scroll_page import InfinityScroll


def test_infinity_scroll(browser, config):
    infinity = InfinityScroll(browser)
    browser.driver.get(config.return_value("test11_url"))
    assert infinity.count_paragraphs(browser, config.return_value("AGE")), (
        "Expected result: Number of paragraphs is equal to the age of engineer\n Actual "
        "result: Number of paragraphs isn`t equal to the age of engineer")
