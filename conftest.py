import pytest
from utils.driver_setup import get_driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to run tests (chrome, firefox)"
    )


@pytest.fixture(scope="module")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="module")
def driver(browser):
    driver = get_driver(browser)
    yield driver
    driver.quit()
