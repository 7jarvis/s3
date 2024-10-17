from utilites.browser_factory import BrowserFactory
import logging
from elements.iframe import IFrame


class Browser:
    def __init__(self, browser_type="chrome"):
        factory = BrowserFactory()
        self._driver = factory.get_remote_driver(browser_type)

    def driver(self):
        return self._driver

    def quit(self):
        self._driver.quit()

    def refresh(self):
        logging.info("Refreshing the current page")
        self.driver().refresh()

    def scroll_to_bottom(self):
        self.driver().execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def save_current_window(self):
        original_window = self.driver().current_window_handle
        return original_window

    def switch_to_the_main_page(self, original_window):
        logging.info("Switching to the main page")
        self.driver().switch_to.window(original_window)

    def switch_to_the_new_window(self):
        logging.info("Switching to the new window")
        new_window = self.driver().window_handles[-1]
        self.driver().switch_to.window(new_window)

    def close_all_other_windows(self, original_window):
        all_windows = self.driver().window_handles
        logging.info("Closing all the other windows")
        for window in all_windows:
            if window != original_window:
                self.driver().switch_to.window(window)
                self.driver().close()

        self.driver().switch_to.window(original_window)

    def switch_to_iframe(self, locator):
        driver = self.driver()
        iframe = IFrame(driver, locator, description="Switching to IFrame")
        iframe_element = iframe.presence_of_element()
        self.driver().switch_to.frame(iframe_element)

    def switch_to_default(self):
        self.driver().switch_to.default_content()


