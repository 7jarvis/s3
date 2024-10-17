from browser.browser import Browser
from pages.hover_page import HoverPage


def test_6():
    browser_instance = Browser()
    hover = HoverPage(browser_instance.driver())
    browser_instance.driver().get(hover.url)
    assert hover.is_page_opened(), "Expected result: Page was opened\n Actual result: Page wasn`t opened"
    n = hover.count_users()
    for i in range(n):
        hover.select_user(i)
        assert hover.check_username(
            i), "Expected result: Correct username is displayed\n Actual result: The displayed username is incorrect"
        assert hover.is_link_present(), "Expected result: link was displayed\n Actual result: link wasn`t displayed"
        hover.open_profile_page(i)
        assert hover.check_link(
            i), "Expected result: Correct profile page was opened\n Actual result: Correct profile page wasn`t opened"

        assert hover.is_page_opened(), "Expected result: Page was opened\n Actual result: Page wasn`t opened"
    browser_instance.quit()



