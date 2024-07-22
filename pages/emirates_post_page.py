from selenium.webdriver.common.by import By
from .base_page import BasePage


class EmiratesPostPage(BasePage):
    EMIRATES_POST_LINK = (By.XPATH, "//a[@href='https://www.emiratespost.ae/']")
    CLOSE_BANNER_BUTTON = (By.XPATH, "//button[@aria-label='Close']")

    def click_emirates_post(self):
        self.wait_for_element(*self.EMIRATES_POST_LINK).click()

    def close_banner(self):
        self.wait_for_element(*self.CLOSE_BANNER_BUTTON).click()
