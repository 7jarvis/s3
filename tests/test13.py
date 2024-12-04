from pages.upload_page import UploadPage
from utilites.file_upload_robot import FileUploadRobot


def test_upload_image_dialog(browser, config):
    upload = UploadPage(browser, config.return_value(
        "test_12_file_name"))
    browser.get(config.return_value("test12_url"))
    upload.wait_for_open()
    upload.click_on_upload_section()
    FileUploadRobot.upload_file_gui(upload.get_absolute_path())
    upload.wait_for_mark()
    assert upload.get_text_area() == config.return_value(
        "test_12_file_name"), "Expected result: Name of the file appeared\n Actual result: Name of the file didn`t appear"
