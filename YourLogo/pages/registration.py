from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from locators.locators import Locators


class RegistrationPage:
    def __init__(self, browser):
        self.driver = browser

        self.URL = "http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation"
        self.createAccount_textBox_id = Locators.createAccount_textBox_id
        self.createAccount_button_xpath = Locators.createAccount_button_xpath
        self.passWord_textBox_id = Locators.passWord_textBox_id
        self.titleMr_radioButton_id = Locators.titleMr_radioButton_id
        self.titleMrs_radioButton_id = Locators.titleMrs_radioButton_id
        self.customerFirstName_textBox_id = Locators.customerFirstName_textBox_id
        self.customerLastName_textBox_id = Locators.customerLastName_textBox_id
        self.dob_day_id = Locators.dob_day_id
        self.dob_month_id = Locators.dob_month_id
        self.dob_year_id = Locators.dob_year_id
        self.firstName_textBox_id = Locators.firstName_textBox_id
        self.lastName_textBox_id = Locators.lastName_textBox_id
        self.address_textBox_id = Locators.address_textBox_id
        self.city_textBox_id = Locators.city_textBox_id
        self.state_sel_id = Locators.state_sel_id
        self.zipCode_textBox_id = Locators.zipCode_textBox_id
        self.country_sel_id = Locators.country_sel_id
        self.mobile_textBox_id = Locators.mobile_textBox_id
        self.address_alias_id = Locators.address_alias_id
        self.register_button_xpath = Locators.register_button_xpath

    def load(self):
        self.driver.get(self.URL)

    def enter_create_account_email(self, email):
        self.driver.find_element(By.ID, Locators.createAccount_textBox_id).clear()
        self.driver.find_element(By.ID, Locators.createAccount_textBox_id).send_keys(email)

    def click_create_account_button(self):
        self.driver.find_element(By.XPATH, Locators.createAccount_button_xpath).click()

    def enter_create_account_password(self, password):
        self.driver.find_element(By.ID, Locators.passWord_textBox_id).clear()
        self.driver.find_element(By.ID, Locators.passWord_textBox_id).send_keys(password)

    def select_title(self):
        self.driver.find_element(By.ID, Locators.titleMr_radioButton_id).click()

    def enter_customer_firstName(self, firstName):
        self.driver.find_element(By.ID, Locators.customerFirstName_textBox_id).send_keys(firstName)

    def enter_customer_lastName(self, lastName):
        self.driver.find_element(By.ID, Locators.customerLastName_textBox_id).send_keys(lastName)

    def select_dob_day(self):
        return Select(self.driver.find_element(By.ID, Locators.dob_day_id))

    def select_dob_month(self):
        return Select(self.driver.find_element(By.ID, Locators.dob_month_id))

    def select_dob_year(self):
        return Select(self.driver.find_element(By.ID, Locators.dob_year_id))

    def enter_shipping_firstName(self, shippingFirstName):
        self.driver.find_element(By.ID, Locators.firstName_textBox_id).send_keys(shippingFirstName)

    def enter_shipping_lastName(self, shippingLastName):
        self.driver.find_element(By.ID, Locators.firstName_textBox_id).send_keys(shippingLastName)

    def enter_address(self, address):
        self.driver.find_element(By.ID, Locators.address_textBox_id).send_keys(address)

    def enter_city(self, city):
        self.driver.find_element(By.ID, Locators.city_textBox_id).send_keys(city)

    def select_state(self):
        return Select(self.driver.find_element(By.ID, Locators.state_sel_id))

    def enter_zipCode(self, zipCode):
        self.driver.find_element(By.ID, Locators.zipCode_textBox_id).send_keys(zipCode)

    def select_country(self):
        return Select(self.driver.find_element(By.ID, Locators.country_sel_id))

    def enter_mobile(self, mobile):
        self.driver.find_element(By.ID, Locators.mobile_textBox_id).send_keys(mobile)

    def enter_address_alia(self, alias):
        self.driver.find_element(By.ID, Locators.address_alias_id).clear()
        self.driver.find_element(By.ID, Locators.address_alias_id).send_keys(alias)

    def click_register_button(self):
        self.driver.find_element(By.XPATH, Locators.register_button_xpath).click()
