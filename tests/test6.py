from pages.hover_page import HoverPage


def test_hover(browser, config):
    hover = HoverPage(browser)
    browser.driver.get(config.return_value("test6_url"))
    assert hover.is_page_opened(), "Expected result: Page was opened\n Actual result: Page wasn`t opened"
    n = hover.count_users()
    for i in range(n):
        hover.select_user()
        expected = f'user{i + 1}'
        assert expected in hover.check_username(), "Expected result: Correct username is displayed\n Actual result: The displayed username is incorrect"
        hover.open_profile_page()
        assert hover.check_link(
            i), "Expected result: Correct profile page was opened\n Actual result: Correct profile page wasn`t opened"

    assert hover.is_page_opened(), "Expected result: Page was opened\n Actual result: Page wasn`t opened"