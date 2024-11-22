from typing import Callable, Optional
from typing_extensions import Self
from .web_element import WebElement


class MultiWebElement:
    """Class-wrapper for Selenium several elements"""

    DEFAULT_TIMEOUT = 10

    def __init__(
            self,
            driver,
            lambda_xpath_locator: Callable,
            description: Optional[str] = None,
            timeout: Optional[int] = None,
    ) -> None:
        """
        Initializer of MultiWebElement

        :param driver: instance of WebDriver wrapper
        :param lambda_xpath_locator: lambda function for generate indexed locator.
                                     Example: 'lambda x: "//*[id='text'][{x}]"'
        :param description: description of element
                            Recommended path to element like "Main page -> Navigation Form -> Home page button"
        :param timeout: Default timeout for explicit waits
        """
        self.index = 1
        self.driver = driver
        self.lambda_xpath_locator = lambda_xpath_locator
        self.timeout = timeout if timeout is not None else self.DEFAULT_TIMEOUT
        self.description = description if description else self.lambda_xpath_locator("'i'")

    def __iter__(self) -> Self:
        """
        Get object iterator

        :return: iterable object
        """
        self.index = 1
        return self

    def __next__(self):

        """
        Get next item from iterable object

        :return: WebElement instance
        :raises:
            StopIteration: if aren't any more elements
        """
        locator = self.lambda_xpath_locator(self.index)
        current_element = WebElement(
            self.driver,
            locator,
            f"{self.description}[{self.index}]",
            timeout=self.timeout,
        )

        if not current_element.is_exists():
            raise StopIteration
        else:
            self.index += 1
            return current_element

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.description}]"

    def __repr__(self) -> str:
        return str(self)
