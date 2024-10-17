from browser.browser import Browser
from pages.infinity_scroll_page import InfinityScroll


def test_11():
    browser_instance = Browser()
    infinity = InfinityScroll(browser_instance.driver())
    browser_instance.driver().get(infinity.url)
    assert infinity.is_page_opened(), "Expected result: Page was opened\n Actual result: Page wasn`t opened"
    assert infinity.count_paragraphs(browser_instance), ("Expected result: Number of paragraphs is equal to the age of engineer\n Actual "
                                       "result: Number of paragraphs isn`t equal to the age of engineer")
