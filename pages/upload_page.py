from selenium.webdriver.common.by import By
from pathlib import Path
from .base_page import BasePage
from elements.input import Input
from elements.web_element import WebElement


class UploadPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(text(), 'File Uploader')]")
    UPLOAD_FILE_LOC = (By.ID, 'file-upload')
    SUBMIT_BUTTON_LOC = (By.ID, 'file-submit')
    FILE_UPLOADED_LOC = (By.XPATH, "//*[contains(text(), 'File Uploaded')]")
    FILE_NAME_UPLOADED_LOC = (By.ID, 'uploaded-files')
    UPLOAD_SECTION_LOC = (By.ID, 'drag-drop-upload')
    SUCCESS_MARK = (By.XPATH, "//div[@class='dz-success-mark']")
    TEXT_NAME_LOC = "//span[contains(text(), '{}')]"

    def __init__(self, browser, file_name):
        super().__init__(browser)
        self.submit = Input(browser.driver, self.SUBMIT_BUTTON_LOC, description='Main Page -> Submit File')
        self.upload = Input(browser.driver, self.UPLOAD_FILE_LOC, description='Main Page -> Upload File')
        self.uploaded_file_name = WebElement(browser.driver, self.FILE_NAME_UPLOADED_LOC,
                                             description='Uploaded file`s name')
        self.upload_section = WebElement(browser.driver, self.UPLOAD_SECTION_LOC,
                                         description='Main Page -> Upload section')
        self.unique_element = WebElement(browser.driver, self.UNIQUE_ELEMENT_LOC,
                                         description='Main Page -> unique text on the main page')
        self.file_name = file_name
        self.file = WebElement(browser.driver, (By.XPATH, self.TEXT_NAME_LOC.format(file_name)),
                               description=f"Main Page -> Name of the file: {self.file_name}")
        self.mark = WebElement(browser.driver, self.SUCCESS_MARK, description='Main Page -> Success mark')

    def get_absolute_path(self, file_path):
        absolute_file_path = str(Path(file_path).resolve())
        return absolute_file_path

    def upload_file(self, file_path):
        self.upload.send_keys(file_path)

    def click_submit(self):
        submit_button = self.submit.presence_of_element()
        submit_button.click()

    def wait_for_mark(self):
        self.mark.presence_of_element()

    def get_uploaded_file_text(self):
        text = self.uploaded_file_name.get_text()
        return text

    def get_text_area(self):
        text = self.file.get_text()
        return text

    def click_on_upload_section(self):
        section = self.upload_section.presence_of_element()
        section.click()
