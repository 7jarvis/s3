import pytest
from browser.browser import Browser
from utilites.config_reader import ConfigReader
from browser.browser_factory import BrowserFactory


@pytest.fixture
def browser():
    browser_instance = Browser(BrowserFactory.get_remote_driver(ConfigReader().get_value("browser_type")))
    yield browser_instance
    browser_instance.quit()


@pytest.fixture(scope='session')
def config():
    return ConfigReader()
