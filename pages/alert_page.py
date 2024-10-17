from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from elements.button import Button
from elements.alert import Alerts
import logging


class AlertPage(BasePage):
    url = 'https://the-internet.herokuapp.com/javascript_alerts'
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'JavaScript')]")
    ALERT_BUTTON_LOC = (By.XPATH, "//button[@onclick='jsAlert()']")
    RESULT_LOC = (By.XPATH, "//*[@id='result']")
    JS_CONFIRM_LOC = (By.XPATH, "//button[@onclick='jsConfirm()']")
    JS_PROMPT_LOC = (By.XPATH, "//button[@onclick='jsPrompt()']")

    def __init__(self, browser):
        super().__init__(browser)
        self.alert_button = Button(self.driver, self.ALERT_BUTTON_LOC, description="Main Page -> Click for JS alert")
        self.confirm_button = Button(self.driver, self.JS_CONFIRM_LOC, description="Main Page -> Click for JS alert")
        self.prompt_button = Button(self.driver, self.JS_PROMPT_LOC, description="Main Page -> Click for JS alert")
        self.page_name = "Alert test page"
        self.al = Alerts(self.driver, self.element)

    def wait_for_open(self):
        super().wait_for_open()
        return True

    def alert_click(self):
        logging.info("Clicking alert")
        self.alert_button.click()
        text = self.get_text()
        return text

    def alert_js_click(self):
        logging.info("Clicking JS alert")
        self.alert_button.click_with_js()
        text = self.get_text()
        return text

    def confirm_click(self):
        self.confirm_button.click()
        text = self.get_text()
        return text

    def confirm_js_click(self):
        self.confirm_button.click_with_js()
        text = self.get_text()
        return text

    def prompt_click(self):
        self.prompt_button.click()
        text = self.get_text()
        return text

    def prompt_js_click(self):
        self.prompt_button.click_with_js()
        text = self.get_text()
        return text

    def get_text(self):
        return self.al.get_text(self.driver)

    def close_alert(self):
        self.al.close_alert(self.driver)
        self.al.is_alert_closed(self.driver)
        return True

    def send_text(self):
        self.al.send_text(self.driver)
