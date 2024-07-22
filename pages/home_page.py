from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    MENU_BUTTON = (By.XPATH, "//img[@alt='Open Menu']")

    def open_menu(self):
        self.wait_for_element(*self.MENU_BUTTON).click()
