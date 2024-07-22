import pytest
from pages.home_page import HomePage
from pages.portfolio_page import PortfolioPage
from pages.emirates_post_page import EmiratesPostPage
from pages.login_page import LoginPage


def test_emirates_post_login(driver):
    home_page = HomePage(driver)
    portfolio_page = PortfolioPage(driver)
    emirates_post_page = EmiratesPostPage(driver)
    login_page = LoginPage(driver)

    home_page.open_menu()
    portfolio_page.hover_and_click_emirates_post()
    emirates_post_page.close_banner()
    login_page.login("Testuser1", "wrongpass")

    expected_error_message = "Invalid username or password."
    assert login_page.get_error_message() == expected_error_message, f"Expected: {expected_error_message}, but got {login_page.get_error_message()}"
