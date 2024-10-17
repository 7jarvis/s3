from browser.browser import Browser
from pages.upload_page import UploadPage


def test_12():
    browser_instance = Browser()
    upload = UploadPage(browser_instance.driver())
    browser_instance.driver().get(upload.url)
    assert upload.is_page_opened(), "Expected result: Page was opened\n Actual result: Page wasn`t opened"
    upload.upload_file()
    upload.submit_button()
    assert upload.check_text(), "Expected result: 'File Uploaded!' message appeared\n Actual result: Message didn`t appear"
