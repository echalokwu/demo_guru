from utils import utils as utils
from pages.registration import RegistrationPage


def test_verify_user_can_register(browser):
    register = RegistrationPage(browser)

    register.load()
    register.enter_create_account_email(utils.email)
    register.click_create_account_button()
    register.select_title()
    register.enter_customer_firstName(utils.firstName)
    register.enter_customer_lastName(utils.lastName)
    register.enter_create_account_password(utils.password)
    register.select_title()
    register.select_dob_day().select_by_value("24")
    register.select_dob_month().select_by_value("11")
    register.select_dob_year().select_by_value("1970")
    register.enter_shipping_firstName("iwe")
    register.enter_shipping_lastName("iwe")
    register.enter_address("34 zeus dr")
    register.enter_city("Orange")
    register.select_state().select_by_visible_text("New Jersey")
    register.enter_zipCode("07502")
    register.select_country().select_by_visible_text("United States")
    register.enter_mobile("4586996666")
    register.enter_address_alia("My address")
    register.click_register_button()
