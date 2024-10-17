from browser.browser import Browser
from pages.context_menu import ContextMenu


def test_4():
    browser_instance = Browser()
    context = ContextMenu(browser_instance.driver())
    browser_instance.driver().get(context.url)
    assert context.is_page_opened(), "Expected result: Page was opened\n Actual result: Page wasn`t opened"
    assert context.click() == 'You selected a context menu', "Expected result: You selected a context menu' text was displayed\n Actual result: Text wasn`t displayed"
    context.close_alert()
    browser_instance.quit()
