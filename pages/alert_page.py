from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from elements.button import Button
import logging
from elements.web_element import WebElement


class AlertPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'JavaScript')]")
    ALERT_BUTTON_LOC = (By.XPATH, "//button[@onclick='jsAlert()']")
    RESULT_LOC = (By.ID, 'result')
    JS_CONFIRM_LOC = (By.XPATH, "//button[@onclick='jsConfirm()']")
    JS_PROMPT_LOC = (By.XPATH, "//button[@onclick='jsPrompt()']")

    def __init__(self, browser):
        super().__init__(browser)
        self.alert_button = Button(browser.driver, self.ALERT_BUTTON_LOC, description="Main Page -> Click for JS alert")
        self.confirm_button = Button(browser.driver, self.JS_CONFIRM_LOC,
                                     description="Main Page -> Click for JS Confirm")
        self.prompt_button = Button(browser.driver, self.JS_PROMPT_LOC, description="Main Page -> Click for JS Prompt")
        self.unique_element = WebElement(browser.driver, self.UNIQUE_ELEMENT_LOC,
                                         description="Main Page -> Unique Text")
        self.result_text = WebElement(browser.driver, self.RESULT_LOC, description='Main Page -> Result text')
        self.page_name = "Alert test page"

    def get_result_text(self):
        text = self.result_text.get_text()
        return text

    def click_on_alert(self):
        logging.info("Click alert")
        self.alert_button.click()

    def get_alert_text(self):
        text = self.browser.get_alert_text()
        return text

    def confirm_click(self):
        self.confirm_button.click()
        text = self.browser.get_alert_text()
        return text

    def confirm_js_click(self):
        self.confirm_button.js_click()
        text = self.browser.get_alert_text()
        return text

    def prompt_click(self):
        self.prompt_button.click()
        text = self.browser.get_alert_text()
        return text

    def prompt_js_click(self):
        self.prompt_button.js_click()
        text = self.browser.get_alert_text()
        return text
