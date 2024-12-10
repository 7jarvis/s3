from utilites.random_utils import RandomUtils
from pages.alert_page import AlertPage


def test_alert_js(browser, config):
    alert = AlertPage(browser)
    browser.get(config.get_value("test2_url"))
    alert.wait_for_open()
    alert.click_on_alert()
    assert alert.get_alert_text() == 'I am a JS Alert', f'Expected result: "I am a JS alert" text is displayed \n Actual result: {alert.get_alert_text()}  is displayed'
    browser.close_alert()
    assert alert.confirm_js_click() == 'I am a JS Confirm', 'Expected result: "I am a JS Confirm" text is displayed \n Actual result: Text is not displayed'
    browser.close_alert()
    assert alert.prompt_js_click() == 'I am a JS prompt', 'Expected result: "I am a JS Prompt" text is displayed \n Actual result: Text is not displayed'
    alert.send_text(RandomUtils.get_random_text())
    browser.close_alert()
