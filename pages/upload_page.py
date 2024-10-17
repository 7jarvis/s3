from selenium.webdriver.common.by import By

from .base_page import BasePage
from utilites.file_upload_robot import FileUploadRobot
from elements.input import Input
from elements.div import Div


class UploadPage(BasePage):
    url = 'http://the-internet.herokuapp.com/upload'
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'File Uploader')]")
    FILE_NAME = 'test.txt'
    UPLOAD_FILE_LOC = (By.XPATH, "//*[@id='file-upload']")
    SUBMIT_BUTTON_LOC = (By.XPATH, "//*[@id='file-submit']")
    rb = FileUploadRobot()
    FILE_PATH = "D:/s3/data/test.txt"
    FILE_UPLOADED_LOC = (By.XPATH, "//*[contains(text(), 'File Uploaded')]")
    FILE_NAME_UPLOADED_LOC = (By.XPATH, "//*[@id='uploaded-files']")
    UPLOAD_SECTION_LOC = (By.XPATH, "//*[@id='drag-drop-upload']")

    def __init__(self, browser):
        super().__init__(browser)
        self.submit = Input(self.driver, self.SUBMIT_BUTTON_LOC, description='Main Page -> Submit File')
        self.upload = Input(self.driver, self.UPLOAD_FILE_LOC, description='Main Page -> Upload File')
        self.uploaded = Div(self.driver, self.FILE_UPLOADED_LOC, description='File uploaded message')
        self.file_name = Div(self.driver, self.FILE_NAME_UPLOADED_LOC, description='Uploaded file`s name')
        self.upload_section = Div(self.driver, self.UPLOAD_SECTION_LOC, description='Main Page -> Upload section')

    def is_page_opened(self):
        super().wait_for_open()
        return True

    def upload_file(self):
        file_input = self.upload.presence_of_element()
        self.rb.upload_file(file_input, self.FILE_PATH)

    def submit_button(self):
        submit_button = self.submit.presence_of_element()
        self.rb.submit_upload(submit_button)

    def check_text(self):
        self.uploaded.presence_of_element()
        file_name = self.file_name.presence_of_element()
        text = file_name.text
        return True if self.FILE_NAME == text else False

    def click_on_upload_section(self):
        section = self.upload_section.presence_of_element()
        self.rb.click_on_upload_section(section)
