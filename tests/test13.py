from browser.browser import Browser
from pages.upload_page import UploadPage


def test_13():
    upload = UploadPage(Browser.driver())
    Browser.driver().get(upload.url)
    assert upload.is_page_opened(), "Expected result: Page was opened\n Actual result: Page wasn`t opened"
    assert upload.click_on_upload_section()
    assert upload.upload_file()
