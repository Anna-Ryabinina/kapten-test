from selenium.webdriver.support.select import By

from src.BasePage import BasePage


class SignInPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):
        self.driver.find_element(By.CSS_SELECTOR, 'input[type="email"][data-testid="input"]').send_keys(email)
        return self

    def enter_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, 'input[type="password"][data-testid="input"]').send_keys(password)
        return self

    def click_continue(self):
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        return self

    def is_error_message_displayed(self):
        return self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/form/div[1]').is_displayed()

