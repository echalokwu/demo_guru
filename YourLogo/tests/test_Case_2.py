from utils import utils as utils
from pages.loginPage import LoginPage
import time


def test_verify_login_with_valid_details(browser):
    login = LoginPage(browser)

    login.load()
    login.click_signIn_link()
    login.enter_email(utils.email)
    login.enter_password(utils.password)
    login.click_signIn_button()
