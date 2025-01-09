from pages.windows_page import WindowsPage
from pages.new_window_page import NewWindowPage


def test_handlers(browser, config):
    browser.get(config.get_value("test7_url"))
    windows = WindowsPage(browser)

    windows.wait_for_open()

    main_window = browser.save_main_window()
    windows.click_on_click_here()
    browser.switch_to_the_new_window()
    new_windows = NewWindowPage(browser)
    new_windows.wait_for_open()
    assert browser.get_title() == 'New Window', f"Expected title 'New Window', but got a {browser.get_title()}."

    browser.switch_to_main_window(main_window)
    windows.click_on_click_here()
    browser.switch_to_the_new_window()
    new_windows.wait_for_open()
    assert browser.get_title() == 'New Window', f"Expected title 'New Window', but got {browser.get_title()}."

    browser.switch_to_main_window(main_window)
    browser.close_all_other_windows(main_window)
