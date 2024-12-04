from pages.hover_page import HoverPage


def test_hover(browser, config):
    hover = HoverPage(browser)
    browser.get(config.return_value("test6_url"))
    hover.is_page_opened()
    for i in range(3):
        hover.select_user()
        expected = f'user{i + 1}'
        assert expected in hover.check_username(), "Expected result: Correct username is displayed\n Actual result: The displayed username is incorrect"
        browser.get(hover.get_link())
        assert browser.check_link(hover.get_expected_text(
            i)), "Expected result: Correct profile page was opened\n Actual result: Correct profile page wasn`t opened"

    hover.is_page_opened()
