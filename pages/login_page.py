from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    LOGIN_BUTTON = (By.LINK_TEXT, "Log in / Register")
    USERNAME_FIELD = (By.ID, "b4-Input_Username")
    PASSWORD_FIELD = (By.ID, "b4-Input_Password")
    LOGIN_SUBMIT_BUTTON = (By.ID, "b4-b12-Primary")
    ERROR_MESSAGE = (By.ID, "b4-b9-ErrorMessage")

    def login(self, username, password):
        self.wait_for_element(*self.LOGIN_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_for_element(*self.USERNAME_FIELD).send_keys(username)
        self.wait_for_element(*self.PASSWORD_FIELD).send_keys(password)
        self.wait_for_element(*self.LOGIN_SUBMIT_BUTTON).click()

    def get_error_message(self):
        return self.wait_for_element(*self.ERROR_MESSAGE).text
