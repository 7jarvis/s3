from selenium.webdriver.common.by import By
from pathlib import Path
from .base_page import BasePage
from elements.input import Input
from elements.p import P


class UploadPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'File Uploader')]")
    UPLOAD_FILE_LOC = (By.ID, 'file-upload')
    SUBMIT_BUTTON_LOC = (By.ID, 'file-submit')
    FILE_PATH = "../data/test.txt"
    FILE_UPLOADED_LOC = (By.XPATH, "//*[contains(text(), 'File Uploaded')]")
    FILE_NAME_UPLOADED_LOC = (By.ID, 'uploaded-files')
    UPLOAD_SECTION_LOC = (By.ID, 'drag-drop-upload')
    SUCCESS_MARK = (By.XPATH, "//div[@class='dz-success-mark']")

    def __init__(self, browser, file_name):
        super().__init__(browser)
        self.submit = Input(browser.driver, self.SUBMIT_BUTTON_LOC, description='Main Page -> Submit File')
        self.upload = Input(browser.driver, self.UPLOAD_FILE_LOC, description='Main Page -> Upload File')
        self.uploaded_file_name = P(browser.driver, self.FILE_NAME_UPLOADED_LOC, description='Uploaded file`s name')
        self.upload_section = P(browser.driver, self.UPLOAD_SECTION_LOC, description='Main Page -> Upload section')
        self.unique_element = P(browser.driver, self.UNIQUE_ELEMENT_LOC,
                                description='Main Page -> "File uploader" text')
        self.file_name = file_name
        self.file = P(browser.driver, self.get_locator_for_text_check(file_name),
                      description='Main Page -> Name of the file')
        self.mark = P(browser.driver, self.SUCCESS_MARK, description='Main Page -> Success mark')

    def wait_for_open(self):
        super().wait_for_open()

    def get_absolute_path(self):
        absolute_file_path = str(Path(self.FILE_PATH).resolve())
        return absolute_file_path

    def get_file_input(self):
        file_input = self.upload.presence_of_element()
        return file_input

    def click_submit(self):
        submit_button = self.submit.presence_of_element()
        submit_button.click()

    @staticmethod
    def get_locator_for_text_check(file_name):
        return By.XPATH, f"//span[contains(text(), '{file_name}')]"

    def wait_for_mark(self):
        self.mark.presence_of_element()

    def check_text(self):
        text = self.uploaded_file_name.get_text()
        return text

    def get_text_area(self):
        text = self.file.get_text()
        return text

    def click_on_upload_section(self):
        section = self.upload_section.presence_of_element()
        section.click()
