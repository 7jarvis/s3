from selenium import webdriver
import logging

from selenium.common import TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from utilites.browser_factory import BrowserFactory


class Browser:
    CHROME = 'chrome'
    ALERT_TIMEOUT = 10  # MOVE TO CFG

    def __init__(self, browser_type=CHROME):
        self.driver = BrowserFactory.get_remote_driver(browser_type)

    @staticmethod
    def get_remote_driver(browser_name):
        if browser_name == "chrome":
            return webdriver.Chrome()
        elif browser_name == "firefox":
            return webdriver.Firefox()

    def quit(self):
        logging.info("Quit the browser")
        self.driver.quit()

    def execute(self, command, params=None):
        return self.driver.execute(command, params)

    def close(self):
        try:
            logging.info("Close the current window")
            self.driver.close()
        except Exception as e:
            logging.error(f"Failed to close the window: {e}")
            raise

    def refresh(self):
        logging.info("Refresh the current page")
        self.driver.refresh()

    def go_back(self):
        logging.info("Return to the previous page")
        self.driver.back()

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def switch_to_window(self, window_name):
        try:
            logging.info(f"Switching to window: {window_name}")
            self.driver.switch_to.window(window_name)
        except Exception as e:
            logging.error(f"Failed to switch to window {window_name}: {e}")
            raise

    def save_current_window(self):
        self._original_window = self.driver.current_window_handle
        logging.info(f"Saved current window: {self._original_window}")

    def switch_to_the_main_page(self):
        new_window = [window for window in self.driver.window_handles if window != self._original_window]
        if not new_window:
            raise Exception("No new window found to switch.")
        self.driver.switch_to.window(new_window[0])
        logging.info(f"Switched to new window: {new_window[0]}")

    def switch_to_the_new_window(self):
        logging.info("Switching to the new window")
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)

    def close_all_other_windows(self):
        for handle in self.driver.window_handles:
            if handle != self._original_window:
                self.driver.switch_to.window(handle)
                self.driver.close()
                logging.info(f"Closed window: {handle}")
        self.switch_to_main_window()

    def switch_to_main_window(self):
        if self._original_window:
            self.driver.switch_to.window(self._original_window)
            logging.info("Switched back to the main window.")
        else:
            raise Exception("Original window handle is not saved.")

    def switch_to_iframe(self, iframe):
        iframe_element = iframe.presence_of_element()
        logging.info("Switch to IFrame")
        self.driver.switch_to.frame(iframe_element)

    def switch_to_default(self):
        logging.info("Switch to Default content")
        self.driver.switch_to.default_content()

    def get_title(self):
        title = self.driver.title
        return title

    def get_alert_text(self):
        WebDriverWait(self.driver, self.ALERT_TIMEOUT).until(ec.alert_is_present())
        alert = Alert(self.driver)
        alert_text = alert.text
        return alert_text

    def close_alert(self):
        WebDriverWait(self.driver, self.ALERT_TIMEOUT).until(ec.alert_is_present())
        alert = Alert(self.driver)
        alert.accept()
        return True

    def is_alert_closed(self):
        try:
            WebDriverWait(self.driver, self.ALERT_TIMEOUT).until_not(ec.alert_is_present())
            return True
        except TimeoutException:
            return False

    def send_alert_text(self, text):
        alert = Alert(self.driver)
        alert.send_keys(text)
