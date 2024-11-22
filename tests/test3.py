from utilites.generate_text import get_random_text
from pages.alert_page import AlertPage


def test_alert_js(browser, config):
    alert = AlertPage(browser)
    browser.driver.get(config.return_value("test2_url"))
    assert alert.alert_click() == 'I am a JS Alert', 'Expected result: "I am a JS alert" text is displayed \n Actual result: Text is not displayed'  # можно вынести в test2_data
    assert browser.close_alert(), 'Expected result: "You successfully clicked an Alert text is displayed"\n Actual result: Text is not displayed'
    assert alert.confirm_js_click() == 'I am a JS Confirm', 'Expected result: "I am a JS Confirm" text is displayed \n Actual result: Text is not displayed'
    assert browser.close_alert(), 'Expected result: "You clicked : OK" text is displayed\n Actual result: Text is not displayed'
    assert alert.prompt_js_click() == 'I am a JS prompt', 'Expected result: "I am a JS Prompt" text is displayed \n Actual result: Text is not displayed'
    alert.send_text(get_random_text())
    assert browser.close_alert()

