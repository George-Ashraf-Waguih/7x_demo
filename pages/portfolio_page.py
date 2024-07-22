from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage


class PortfolioPage(BasePage):
    PORTFOLIO_LINK = (By.XPATH, "//a[@href='/portfolio']")
    EMIRATES_POST_LINK = (By.XPATH, "//a[@href='/portfolio#emiratespost']")

    def hover_and_click_emirates_post(self):
        portfolio_menu = self.wait_for_element(*self.PORTFOLIO_LINK)
        actions = ActionChains(self.driver)
        actions.move_to_element(portfolio_menu).perform()
        self.wait_for_element(*self.EMIRATES_POST_LINK).click()
