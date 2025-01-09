from pages.upload_page import UploadPage
from pathlib import Path


def test_upload_image(browser, config):
    file_path = config.get_value(
        "test_12_file_path")
    file_name = Path(file_path).name
    browser.get(config.get_value("test12_url"))
    upload = UploadPage(browser, file_name)
    upload.wait_for_open()
    upload.upload_file(upload.get_absolute_path(file_path))
    upload.click_submit()
    assert upload.get_uploaded_file_text() == file_name, f"Expected result: '{file_name}' message appeared\n Actual result: {upload.get_uploaded_file_text()}"
