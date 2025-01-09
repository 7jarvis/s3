from pages.upload_page import UploadPage
from utilites.file_upload_robot import FileUploadRobot
from pathlib import Path


def test_upload_image_dialog(browser, config):
    file_path = config.get_value(
        "test_13_file_path")
    file_name = Path(file_path).name
    browser.get(config.get_value("test12_url"))
    upload = UploadPage(browser, file_name)
    upload.wait_for_open()
    upload.click_on_upload_section()
    FileUploadRobot.upload_file_gui(upload.get_absolute_path(file_path))
    upload.wait_for_mark()
    assert upload.get_text_area() == file_name, f"Expected result: {file_name} appeared\n Actual result: {upload.get_text_area()} appeaed"
