from pages.hover_page import HoverPage


def test_hover(browser, config):
    browser.get(config.get_value("test6_url"))
    hover = HoverPage(browser)
    hover.wait_for_open()
    for i in range(3):
        hover.select_user()
        expected = f'user{i + 1}'
        assert expected in hover.check_username(), f"Expected result: {expected} username is displayed\n Actual result: {hover.check_username()} is displayed"
        browser.get(hover.get_link())
        expected_url = f'users/{i + 1}'
        assert browser.check_link_and_return(
            expected_url), "Expected result: Correct profile page was opened\n Actual result: Correct profile page wasn`t opened"

    hover.wait_for_open()
