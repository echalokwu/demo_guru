from selenium.webdriver.common.by import By

from locators.locators import Locators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.url = "http://automationpractice.com/index.php"
        self.signIn_link_xpath = Locators.signIn_link_xpath
        self.signIn_button_xpath = Locators.signIn_button_xpath
        self.login_textBox_id = Locators.login_textBox_id
        self.passWord_textBox_id = Locators.passWord_textBox_id

    def load(self):
        self.driver.get(self.url)

    def click_signIn_link(self):
        self.driver.find_element(By.XPATH, Locators.signIn_link_xpath).click()

    def enter_email(self, email):
        self.driver.find_element(By.ID, Locators.login_textBox_id).clear()
        self.driver.find_element(By.ID, Locators.login_textBox_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, Locators.passWord_textBox_id).clear()
        self.driver.find_element(By.ID, Locators.passWord_textBox_id).send_keys(password)

    def click_signIn_button(self):
        self.driver.find_element(By.XPATH, Locators.signIn_button_xpath).click()



