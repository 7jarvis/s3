from .base_page import BasePage
from selenium.webdriver.common.by import By
from elements.img import Img
from elements.a import a

class HoverPage(BasePage):
    url = 'https://the-internet.herokuapp.com/hovers'
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'Hover over')]")
    IMAGE_LOC = (By.XPATH, "//img[@alt='User Avatar']")
    USERNAME_LOC = (By.XPATH, "//*[contains(text(), 'name: ')]")
    PROFILE_LINK_LOC = (By.XPATH, "//*[contains(text(), 'View')]")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Hover page"
        self.image = Img(self.driver, self.IMAGE_LOC, description="Main Page -> Hover over IMG")
        self.username_element = Img(self.driver, self.USERNAME_LOC, description="Main Page -> Username") #поменять элемент
        self.link_element = a(self.driver, self.PROFILE_LINK_LOC, description="Main Page -> Username")

    def is_page_opened(self):
        super().wait_for_open()
        return True

    def count_users(self):
        return len(self.image.presence_of_all_elements())

    def select_user(self, n):
        self.image.hover_over_element(n)

    def check_username(self, n):
        users = self.username_element.presence_of_all_elements()
        text_value = users[n].text
        expected = f'user{n + 1}'
        if expected in text_value:
            return True
        else:
            return False

    def is_link_present(self):
        self.link_element.presence_of_element()
        return True

    def open_profile_page(self, n):
        link = self.link_element.get_link(n)
        self.link_element.open_link(link)

    def check_link(self, n):
        expected = f'users/{n+1}'
        if expected in self.link_element.get_current_url():
            self.link_element.go_back()
            return True
        else:
            return False


