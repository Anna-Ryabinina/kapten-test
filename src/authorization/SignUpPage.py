from selenium.webdriver.common.by import *

from src.BasePage import BasePage


class SignUpPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):
        self.driver.find_element(By.NAME, "email").send_keys(email)
        return self

    def enter_password(self, password):
        self.driver.find_element(By.NAME, "password").send_keys(password)
        return self

    def click_signup(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[data-testid='signin_link'] + button[type='submit']").click()
        return self






