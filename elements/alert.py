# from selenium.common import TimeoutException
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from elements.base_element import BaseElement
#
#
#
# class Alerts(BaseElement):
#     TIMEOUT = 10
#
#
#     def close_alert(self, driver):
#         WebDriverWait(driver, self.TIMEOUT).until(ec.alert_is_present())
#         alert = Alert(driver)
#         alert.accept()
#
#     def is_alert_closed(self, driver):
#         try:
#             WebDriverWait(driver, self.TIMEOUT).until_not(ec.alert_is_present())
#             return True
#         except TimeoutException:
#             return False
#
#     @staticmethod
#     def send_alert_text(driver, text):
#         alert = Alert(driver)
#         alert.send_keys(text)
