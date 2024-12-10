from pages.infinity_scroll_page import InfinityScroll

AGE = 23


def test_infinity_scroll(browser, config):
    browser.get(config.get_value("test11_url"))
    infinity = InfinityScroll(browser)
    infinity.wait_for_open()
    assert infinity.count_paragraphs(browser, AGE), (
        "Expected result: Number of paragraphs is equal to the age of engineer\n Actual "
        "result: Number of paragraphs isn`t equal to the age of engineer")
