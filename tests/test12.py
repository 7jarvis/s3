from pages.upload_page import UploadPage



def test_upload_image(browser, config):
    upload = UploadPage(browser)
    browser.driver.get(config.return_value("test12_url"))
    upload.upload_file()
    upload.click_submit()
    assert upload.check_text() == config.return_value("test_12_file_name"), "Expected result: 'File Uploaded!' message appeared\n Actual result: Message didn`t appear"
