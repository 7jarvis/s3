from pages.upload_page import UploadPage

#FILE_PATH = "../data/test.txt" #move to cfg
FILE_NAME = 'test.txt'


def test_upload_image_dialog(browser, config):
    upload = UploadPage(browser)
    browser.driver.get(config.return_value("test12_url"))
    upload.click_on_upload_section()
    upload.upload_file_gui(config.return_value("test_12_file_name"))
    assert upload.check_text_area() == config.return_value("test_12_file_name"), "Expected result: Name of the file appeared\n Actual result: Name of the file didn`t appear"
