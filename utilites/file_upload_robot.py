import pyautogui


class FileUploadRobot:

    @staticmethod
    def upload_file(file_input, file_path):
        file_input.send_keys(file_path)

    @staticmethod
    def upload_file_gui(file_path):
        pyautogui.sleep(3)
        pyautogui.write(file_path)
        pyautogui.sleep(3)
        pyautogui.press('enter')

    @staticmethod
    def submit_upload(submit_button):
        submit_button.click()
