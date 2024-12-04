from .base_page import BasePage
from selenium.webdriver.common.by import By
from elements.web_element import WebElement
from elements.multiweb_element import MultiWebElement
from selenium.webdriver import ActionChains


class HoverPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'Hover over')]")
    IMAGE_LOC = "img[alt='User Avatar']"
    SEL_USERNAME_LOC = (By.XPATH, "//*[contains(text(), 'name: ')]")
    USERNAME_LOC = "//*[contains(text(), 'name: ')]"
    PROFILE_LINK_LOC = (By.XPATH, "//*[contains(text(), 'View')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Hover page"
        self.unique_element = WebElement(browser.driver, self.UNIQUE_ELEMENT_LOC, description="Main Page -> Header")
        self.image = WebElement(browser.driver, self.IMAGE_LOC, description="Main Page -> Hover over IMG")
        self.multi_image = MultiWebElement(browser.driver, lambda x: (By.XPATH, f"(//img[@alt='User Avatar'])[{x}]"),
                                           description="Main page ->Profile Image")
        self.multi_username = MultiWebElement(browser.driver,
                                              lambda x: (By.XPATH, f"(//*[contains(text(), 'name: ')])[{x}]"),
                                              description="Main page ->Profile Image")
        self.username_element = WebElement(browser.driver, self.USERNAME_LOC,
                                           description="Main Page -> Username")
        self.multi_link_element = MultiWebElement(browser.driver,
                                                  lambda x: (By.XPATH, f"(//*[contains(text(), 'View')])[{x}]"),
                                                  description="Main Page -> View profile")

    def is_page_opened(self):
        super().wait_for_open()

    def select_user(self):
        image = next(self.multi_image)
        image_element = image.presence_of_element()
        actions = ActionChains(self.browser.driver)
        actions.move_to_element(image_element).perform()

    def check_username(self):
        username = next(self.multi_username)
        text_value = username.get_text()
        return text_value

    def get_link(self):
        link = next(self.multi_link_element)
        link_text = link.get_attribute("href")
        return link_text

    def get_expected_text(self, n):
        expected = f'users/{n + 1}'
        return expected
