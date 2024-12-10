import pyautogui


class FileUploadRobot:

    @staticmethod
    def upload_file_gui(file_path):
        pyautogui.sleep(3)
        pyautogui.write(file_path)
        pyautogui.sleep(3)
        pyautogui.press('enter')
