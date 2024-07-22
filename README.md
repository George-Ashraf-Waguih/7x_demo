# 7x_demo

# Automation Framework for Multi-Browser Testing

This framework is designed for automated testing using Selenium WebDriver, supporting multiple browsers (Chrome and Firefox). It utilizes the Page Object Model (POM) design pattern and Pytest for test execution. The framework also supports parallel test execution using `pytest-xdist`.



## Prerequisites

- Python 3.7+
- Chrome and/or Firefox browsers
- Install the required Python packages:
pip install selenium webdriver-manager pytest pytest-xdist


## Running Tests
To run tests on different browsers, use the --browser option with pytest:

Run Tests on Chrome
pytest --browser=chrome tests/

Run Tests on Firefox
pytest --browser=firefox tests/

Run Tests on Both Browsers in Parallel
Ensure you have pytest-xdist installed for parallel execution:
pip install selenium webdriver-manager pytest pytest-xdist





