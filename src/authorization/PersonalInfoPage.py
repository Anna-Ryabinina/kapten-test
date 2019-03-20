from selenium.webdriver.support.select import By

from src.BasePage import BasePage


class PersonalInfoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def enter_first_name(self, name):
        first_name_textbox = self.driver.find_element(By.NAME, 'first_name')
        first_name_textbox.clear()
        first_name_textbox.send_keys(name)
        return self

    def enter_last_name(self, name):
        last_name_textbox = self.driver.find_element(By.NAME, 'last_name')
        last_name_textbox.clear()
        last_name_textbox.send_keys(name)
        return self

    def enter_phone_number(self, number):
        phone_textbox = self.driver.find_element(By.NAME, 'phone_data')
        phone_textbox.clear()
        phone_textbox.send_keys(number)
        return self

    def click_signup(self):
        signup_button = self.driver.find_element(By.CSS_SELECTOR,
                                                 "button[data-testid='promocode_link'] + div button[type='submit']")

        signup_button.click()
        return self


