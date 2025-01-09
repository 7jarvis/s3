from pages.context_menu import ContextMenu


def test_alert_context(browser, config):
    browser.get(config.get_value("test4_url"))
    context = ContextMenu(browser)
    context.wait_for_open()
    context.click_on_context_menu()
    assert context.get_alert_text() == 'You selected a context menu', "Expected result: You selected a context menu' text was displayed\n Actual result: Text wasn`t displayed"
    browser.close_alert()
    assert browser.is_alert_closed(), "Expected result: Alert was closed \n Actual result: Alert wasn`t closed"
