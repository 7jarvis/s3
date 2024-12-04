from pages.upload_page import UploadPage
from utilites.file_upload_robot import FileUploadRobot


def test_upload_image(browser, config):
    upload = UploadPage(browser, config.return_value("test_12_file_name"))
    browser.get(config.return_value("test12_url"))
    upload.wait_for_open()
    FileUploadRobot.upload_file(upload.get_file_input(), upload.get_absolute_path())
    upload.click_submit()
    assert upload.check_text() == config.return_value(
        "test_12_file_name"), "Expected result: 'File Uploaded!' message appeared\n Actual result: Message didn`t appear"
