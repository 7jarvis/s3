from selenium.webdriver.common.by import By
from pathlib import Path
from .base_page import BasePage
from utilites.file_upload_robot import FileUploadRobot
from elements.input import Input
from elements.p import P


class UploadPage(BasePage):
    url = 'http://the-internet.herokuapp.com/upload'
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'File Uploader')]")
    UPLOAD_FILE_LOC = (By.ID, 'file-upload')
    SUBMIT_BUTTON_LOC = (By.ID, 'file-submit')
    FILE_PATH = "../data/test.txt"
    FILE_UPLOADED_LOC = (By.XPATH, "//*[contains(text(), 'File Uploaded')]")
    FILE_NAME_UPLOADED_LOC = (By.XPATH, "//*[@id='uploaded-files']")
    UPLOAD_SECTION_LOC = (By.XPATH, "//*[@id='drag-drop-upload']")
    FILE_NAME = (By.XPATH, "//*[@class='dz-filename']//span")

    def __init__(self, browser):
        super().__init__(browser)
        self.submit = Input(browser.driver, self.SUBMIT_BUTTON_LOC, description='Main Page -> Submit File')
        self.upload = Input(browser.driver, self.UPLOAD_FILE_LOC, description='Main Page -> Upload File')
        self.uploaded = P(browser.driver, self.FILE_UPLOADED_LOC, description='File uploaded message')
        self.file_name = P(browser.driver, self.FILE_NAME_UPLOADED_LOC, description='Uploaded file`s name')
        self.upload_section = P(browser.driver, self.UPLOAD_SECTION_LOC, description='Main Page -> Upload section')
        self.unique_element = P(browser.driver, self.UNIQUE_ELEMENT_LOC,
                                  description='Main Page -> "File uploader" text')
        self.file = P(browser.driver, self.FILE_NAME, description='')

    def upload_file(self):
        absolute_file_path = str(Path(self.FILE_PATH).resolve())
        file_input = self.upload.presence_of_element()
        FileUploadRobot.upload_file(file_input, absolute_file_path)

    def click_submit(self):
        submit_button = self.submit.presence_of_element()
        FileUploadRobot.submit_upload(submit_button)

    def check_text(self):
        self.uploaded.presence_of_element()
        file_name = self.file_name.presence_of_element()
        text = file_name.text
        return text

    def check_text_area(self):
        file_name = self.file.visibility_of_element()
        text = file_name.text
        return text

    def click_on_upload_section(self):
        super().wait_for_open()
        section = self.upload_section.presence_of_element()
        section.click()

    def upload_file_gui(self, FILE_NAME):
        FileUploadRobot.upload_file_gui(FILE_NAME)
