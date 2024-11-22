import pytest
from browser.browser import Browser
from utilites.config_reader import ConfigReader


@pytest.fixture
def browser():
    browser_instance = Browser()
    yield browser_instance
    browser_instance.quit()


@pytest.fixture
def config():
    return ConfigReader()
