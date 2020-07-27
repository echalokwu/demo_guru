"""
This module contains shared fixtures.
"""

import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    # Initialize the ChromeDriver instance
    b = webdriver.Chrome()

    # Makes it calls wait up to seconds for elements to appear
    b.implicitly_wait(10)

    # Maximizes browser
    b.maximize_window()

    # Return the WebDriver instance for the setup
    yield b

    # Quite the WebDriver instance for the cleanup
    b.quit()
