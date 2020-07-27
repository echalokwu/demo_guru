"""
Set of test scripts for testing Guru99 Bank
Test script is developed using selenium with pytest framework
"""
import sys;

print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/Users/echalo/Desktop/demo_guru'])
import pytest
from selenium.webdriver.common.by import By
from utils import utils as utils


def test_verify_login_section_1(browser):
    # Go to URL
    browser.get(utils.URL)

    # Enter valid UserID
    v1 = browser.find_element(By.XPATH, "//input[@name='uid']")
    v1.send_keys(utils.UserID)

    # Enter valid Password
    v2 = browser.find_element(By.XPATH, "//input[@name='password']")
    v2.send_keys(utils.Password)

    # Click Login Button
    v3 = browser.find_element(By.XPATH, "//input[@name='btnLogin']")
    v3.click()

    # Verify Login is Successful
    ActualTile = browser.title
    print(ActualTile)
    try:
        assert utils.ExpectedTitle == ActualTile
    except AssertionError:
        print("Login Not Successful")

    # Take screenshot
    browser.get_screenshot_as_file("/Users/echalo/Desktop/demo_guru/screenshots/output.png")


@pytest.mark.parametrize("input1, input2, output",
                         [
                             (utils.UserID, utils.Password, utils.ExpectedTitle),
                             (utils.InvalidID, utils.Password, utils.Expect_Error),
                             (utils.UserID, utils.InvalidPassword, utils.Expect_Error),
                             (utils.InvalidID, utils.InvalidPassword, utils.Expect_Error)
                         ])
def test_verify_login_section(browser, input1, input2, output):
    # Go to URL
    browser.get(utils.URL)

    # Enter valid UserID
    v1 = browser.find_element(By.XPATH, "//input[@name='uid']")
    v1.send_keys(input1)

    # Enter valid Password
    v2 = browser.find_element(By.XPATH, "//input[@name='password']")
    v2.send_keys(input2)

    # Click Login Button
    v3 = browser.find_element(By.XPATH, "//input[@name='btnLogin']")
    v3.click()

    # Verify Login is Successful
    ActualTile = browser.title
    print(ActualTile)
    try:
        assert utils.ExpectedTitle == ActualTile
    except AssertionError as msg:
        print(msg)
        print("Login Not Successful")

    # Take screenshot
    browser.get_screenshot_as_file("/Users/echalo/Desktop/demo_guru/screenshots/output2.png")
