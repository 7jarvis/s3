import logging
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utilites.config_reader import ConfigReader


class Browser:
    cfg = ConfigReader()
    ALERT_TIMEOUT = cfg.get_value("TIMEOUT")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, self.ALERT_TIMEOUT)
        self.action_chains = ActionChains(driver)

    def get(self, url):
        logging.info(f"Navigating to: {url}")
        self.driver.get(url)

    def quit(self):
        logging.info("Quit the browser")
        self.driver.quit()

    def execute_script(self, script, *args):
        logging.info(f"Excecute script: {script}")
        return self.driver.execute_script(script, *args)

    def close(self):
        logging.info("Close the current window")
        self.driver.close()

    def refresh(self):
        logging.info("Refresh the current page")
        self.driver.refresh()

    def go_back(self):
        logging.info("Return to the previous page")
        self.driver.back()

    def get_current_url(self):
        logging.info("Get current url")
        current_url = self.driver.current_url
        return current_url

    def check_link_and_return(self, expected_text):
        if expected_text in self.get_current_url():
            self.go_back()
            return True
        self.go_back()
        return False

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def switch_to_window(self, window_name):
        logging.info(f"Switch to window: {window_name}")
        self.driver.switch_to.window(window_name)

    def save_main_window(self):
        logging.info("Saved main window")
        return self.driver.current_window_handle

    def switch_to_the_new_window(self):
        logging.info("Switching to the new window")
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)

    def close_all_other_windows(self, main_window):
        for handle in self.driver.window_handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)
                self.driver.close()
                logging.info(f"Closed window: {handle}")
        self.switch_to_main_window(main_window)

    def switch_to_main_window(self, main_window):
        logging.info("Switched back to the main window.")
        self.driver.switch_to.window(main_window)

    def switch_to_iframe(self, iframe):
        iframe_element = iframe.presence_of_element()
        logging.info("Switch to IFrame")
        self.driver.switch_to.frame(iframe_element)

    def switch_to_default(self):
        logging.info("Switch to Default content")
        self.driver.switch_to.default_content()

    def get_title(self):
        logging.info("Get title of the text")
        title = self.driver.title
        return title

    def get_alert_text(self):
        self.wait.until(ec.alert_is_present())
        alert = Alert(self.driver)
        logging.info("Get the alert text")
        alert_text = alert.text
        return alert_text

    def wait_for_alert_to_be_present(self):
        logging.info("Wait for alert to be present")
        self.wait.until(ec.alert_is_present())

    def close_alert(self):
        self.wait_for_alert_to_be_present()
        alert = Alert(self.driver)
        logging.info("Close alert.")
        alert.accept()

    def is_alert_closed(self):
        logging.info("Check if alert was closed")
        try:
            self.wait.until_not(ec.alert_is_present())
            return True
        except TimeoutException:
            return False

    def send_alert_text(self, text):
        self.wait.until(ec.alert_is_present())
        alert = Alert(self.driver)
        logging.info("Send text to Alert")
        alert.send_keys(text)
