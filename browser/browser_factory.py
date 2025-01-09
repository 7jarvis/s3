from selenium import webdriver
from .browser_type import BrowserType


class BrowserFactory:
    @staticmethod
    def get_remote_driver(browser_name):
        if browser_name == BrowserType.CHROME:
            return webdriver.Chrome()
        elif browser_name == BrowserType.FIREFOX:
            return webdriver.Firefox()
