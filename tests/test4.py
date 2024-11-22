from pages.context_menu import ContextMenu


def test_alert_context(browser, config):
    context = ContextMenu(browser)
    browser.driver.get(config.return_value("test4_url"))
    assert context.click_on_context_menu() == 'You selected a context menu', "Expected result: You selected a context menu' text was displayed\n Actual result: Text wasn`t displayed"
    browser.close_alert()
    assert browser.is_alert_closed(), "Expected result: Alert was closed \n Actual result: Alert wasn`t closed"

