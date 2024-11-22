from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from elements.button import Button
import logging
from elements.p import P


class AlertPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'JavaScript')]")
    ALERT_BUTTON_LOC = (By.XPATH, "//button[@onclick='jsAlert()']")
    RESULT_LOC = (By.XPATH, "//*[@id='result']")
    JS_CONFIRM_LOC = (By.XPATH, "//button[@onclick='jsConfirm()']")
    JS_PROMPT_LOC = (By.XPATH, "//button[@onclick='jsPrompt()']")

    def __init__(self, browser):
        super().__init__(browser)
        self.alert_button = Button(browser.driver, self.ALERT_BUTTON_LOC, description="Main Page -> Click for JS alert")
        self.confirm_button = Button(browser.driver, self.JS_CONFIRM_LOC, description="Main Page -> Click for JS Confirm")
        self.prompt_button = Button(browser.driver, self.JS_PROMPT_LOC, description="Main Page -> Click for JS Prompt")
        self.unique_element = P(browser.driver, self.UNIQUE_ELEMENT_LOC, description="Main Page -> Unique Text")
        self.page_name = "Alert test page"

    def alert_click(self):
        super().wait_for_open()
        logging.info("Clicking alert")
        element = self.alert_button.presence_of_element()
        self.alert_button.click(element)
        text = self.browser.get_alert_text()
        return text

    def js_click(self):
        logging.info("Clicking JS alert")
        self.alert_button.js_click()
        text = self.browser.get_alert_text()
        return text

    def confirm_click(self):
        element = self.confirm_button.presence_of_element()
        self.confirm_button.click(element)
        text = self.browser.get_alert_text()
        return text

    def confirm_js_click(self):
        self.confirm_button.js_click()
        text = self.browser.get_alert_text()
        return text

    def prompt_click(self):
        element = self.prompt_button.presence_of_element()
        self.prompt_button.click(element)
        text = self.browser.get_alert_text()
        return text

    def prompt_js_click(self):
        self.prompt_button.js_click()
        text = self.browser.get_alert_text()
        return text

    def send_text(self, text):
        self.browser.send_alert_text(text)
