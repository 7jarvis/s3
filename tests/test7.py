from pages.windows_page import WindowsPage
from pages.new_window_page import NewWindowPage


def test_handlers(browser, config):
    windows = WindowsPage(browser)
    new_windows = NewWindowPage(browser)
    browser.driver.get(config.return_value("test7_url"))

    browser.save_current_window()
    windows.click()
    browser.switch_to_the_new_window()
    assert new_windows.get_title() == 'New Window', "Expected title 'New Window', but got a different one."

    browser.switch_to_main_window()
    windows.click()
    browser.switch_to_the_new_window()
    assert new_windows.get_title() == 'New Window', "Expected title 'New Window', but got a different one."

    browser.switch_to_main_window()
    browser.close_all_other_windows()

