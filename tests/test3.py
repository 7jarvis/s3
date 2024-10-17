from browser.browser import Browser
from pages.alert_page import AlertPage


def test_3():
    browser_instance = Browser()
    alert = AlertPage(browser_instance.driver())
    browser_instance.driver().get(alert.url)
    assert alert.wait_for_open(), "Expected result: Page was opened\n Actual result: Page wasn`t opened"
    assert alert.alert_click() == 'I am a JS Alert', 'Expected result: "I am a JS alert" text is displayed \n Actual result: Text is not displayed'  # можно вынести в test2_data
    assert alert.close_alert(), 'Expected result: "You successfully clicked an Alert text is displayed"\n Actual result: Text is not displayed'
    assert alert.confirm_js_click() == 'I am a JS Confirm', 'Expected result: "I am a JS Confirm" text is displayed \n Actual result: Text is not displayed'
    assert alert.close_alert(), 'Expected result: "You clicked : OK" text is displayed\n Actual result: Text is not displayed'
    assert alert.prompt_js_click() == 'I am a JS prompt', 'Expected result: "I am a JS Prompt" text is displayed \n Actual result: Text is not displayed'
    alert.send_text()
    assert alert.close_alert()
    browser_instance.quit()
