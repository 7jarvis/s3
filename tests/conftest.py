import pytest
from browser.browser import Browser
from utilites.config_reader import ConfigReader
from browser.browser_factory import BrowserFactory
from browser.browser_type import BrowserType
@pytest.fixture
def browser():
    browser_instance = Browser(BrowserFactory.get_remote_driver(BrowserType.CHROME))
    yield browser_instance
    browser_instance.quit()


@pytest.fixture
def config():
    return ConfigReader()
