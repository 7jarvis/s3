from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from elements.base_element import BaseElement
from utilites.generate_text import get_random_text


class Alerts(BaseElement):
    TIMEOUT = 10

    def get_text(self, driver):
        WebDriverWait(driver, self.TIMEOUT).until(ec.alert_is_present())
        alert = Alert(driver)
        alert_text = alert.text
        return alert_text

    def close_alert(self, driver):
        WebDriverWait(driver, self.TIMEOUT).until(ec.alert_is_present())
        alert = Alert(driver)
        alert.accept()

    def is_alert_closed(self, driver):
        WebDriverWait(driver, self.TIMEOUT).until_not(ec.alert_is_present())
        return True

    @staticmethod
    def send_text(driver):
        alert = Alert(driver)
        text = get_random_text()
        alert.send_keys(text)
        return text
