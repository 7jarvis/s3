from browser.browser import Browser
from pages.windows_page import WindowsPage
from pages.new_window_page import NewWindowPage


def test_7():
    browser_instance = Browser()
    windows = WindowsPage(browser_instance.driver())
    newWindows = NewWindowPage(browser_instance.driver())
    browser_instance.driver().get(windows.url)
    assert windows.is_page_opened(), "Expected result: Page was opened\n Actual result: Page wasn`t opened"
    main_window = browser_instance.save_current_window()
    windows.click()
    browser_instance.switch_to_the_new_window()
    assert newWindows.is_page_opened(), "Expected result: Page was opened\n Actual result: Page wasn`t opened"
    assert newWindows.get_title() == 'New Window', "Expected result: New window`s title is 'New Window'\n Actual result: New Window`s title is different"
    browser_instance.switch_to_the_main_page(main_window)
    assert windows.is_page_opened(), "Expected result: Page was opened. 'New window' text was displayed\n Actual result: Page wasn`t opened. Text wasn`t displayed."
    windows.click()
    browser_instance.switch_to_the_new_window()
    assert newWindows.is_page_opened(), "Expected result: Page was opened\n Actual result: Page wasn`t opened"
    assert newWindows.get_title() == 'New Window', "Expected result: New window`s title is 'New Window'\n Actual result: New Window`s title is different"
    browser_instance.switch_to_the_main_page(main_window)
    assert windows.is_page_opened(), "Expected result: Page was opened.\n Actual result: Page wasn`t opened."
    browser_instance.close_all_other_windows(main_window)
    browser_instance.driver().quit()
