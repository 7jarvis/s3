from robot.api.deco import keyword


class FileUploadRobot:
    # def __init__(self, driver):
    #     self.driver = driver

    # def open_browser(self, url):
    #     self.driver.get(url)

    @keyword
    def upload_file(self, file_input, file_path):
        file_input.send_keys(file_path)

    @keyword
    def hello_world(self):
        return "Hello, world!"

    @keyword
    def submit_upload(self, submit_button):
        submit_button.click()

    @keyword
    def click_on_upload_section(self, locator):
        locator.click()

    # def close_browser(self):
    #     self.driver.quit()
