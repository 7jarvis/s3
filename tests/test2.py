from pages.alert_page import AlertPage
from utilites.random_utils import RandomUtils


def test_alert(browser, config):
    browser.get(config.get_value("test2_url"))
    alert = AlertPage(browser)
    alert.wait_for_open()
    alert.click_on_alert()
    assert alert.get_alert_text() == 'I am a JS Alert', f'Expected result: "I am a JS Alert" text is displayed \n Actual result: {alert.get_alert_text()} is displayed'
    browser.close_alert(
    )
    assert browser.is_alert_closed(), 'Expected result: Alert was closed \n Actual result: Alert wasn`t closed'
    assert alert.confirm_click() == 'I am a JS Confirm', f'Expected result: "I am a JS Confirm" text is displayed \n Actual result: {alert.get_alert_text()} is displayed'
    browser.close_alert()
    assert browser.is_alert_closed(), 'Expected result: Alert was closed \n Actual result: Alert wasn`t closed'
    assert alert.prompt_click() == 'I am a JS prompt', f'Expected result: JS prompt windows is opened \n Actual result: JS prompt windows was not opened'
    text = RandomUtils.random_text
    browser.send_alert_text(text)
    browser.close_alert()
    assert alert.get_result_text() == f'You entered: {text.replace("\n", " ")}', f'Expected result: "{text}" text is displayed \n Actual result: {alert.get_alert_text()} is displayed'
