from .base_page import BasePage
from selenium.webdriver.common.by import By
from elements.web_element import WebElement
from elements.multiweb_element import MultiWebElement
from selenium.webdriver import ActionChains


class HoverPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'Hover over')]")
    STRING_IMAGE_LOC = "img[alt='User Avatar']"
    SEL_USERNAME_LOC = (By.XPATH, "//*[contains(text(), 'name: ')]")
    STRING_USERNAME_LOC = "//*[contains(text(), 'name: ')]"
    PROFILE_LINK_LOC = (By.XPATH, "//*[contains(text(), 'View')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Hover page"
        self.unique_element = WebElement(browser.driver, self.UNIQUE_ELEMENT_LOC, description="Main Page -> Header")
        self.image = WebElement(browser.driver, self.STRING_IMAGE_LOC, description="Main Page -> Hover over IMG")
        self.multi_image = MultiWebElement(browser.driver, lambda x: (By.XPATH, f"(//img[@alt='User Avatar'])[{x}]"),
                                           description="Main page ->Profile Image")
        self.multi_username = MultiWebElement(browser.driver,
                                              lambda x: (By.XPATH, f"(//*[contains(text(), 'name: ')])[{x}]"),
                                              description="Main page ->Profile Image")
        self.username_element = WebElement(browser.driver, self.STRING_USERNAME_LOC,
                                           description="Main Page -> Username")
        self.multi_link_element = MultiWebElement(browser.driver,
                                                  lambda x: (By.XPATH, f"(//*[contains(text(), 'View')])[{x}]"),
                                                  description="Main Page -> View profile")

    def select_user(self, current_elem):
        images = []
        for element in self.multi_image:
            images.append(element.presence_of_element())
        
        actions = ActionChains(self.browser.driver)
        actions.move_to_element(images[current_elem]).perform()

    def check_username(self):
        usernames = []
        for element in self.multi_username:
            text_value = element.get_text()
            usernames.append(text_value)

        return usernames

    def get_link(self):
        links = []
        for element in self.multi_link_element:
            link_text = element.get_attribute("href")
            links.append(link_text)
        return links
