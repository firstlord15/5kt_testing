from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
from config import *


class RegistrationPage(BasePage):
    INPUT_FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    INPUT_LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    BUTTON_NEWSLETTER = (By.CSS_SELECTOR, "#input-newsletter")
    BUTTON_PRIVACY_POLICY = (By.XPATH, "//body/main[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/input[1]")
    BUTTON_NEXT = (By.XPATH, "//button[contains(text(),'Continue')]")
    BUTTON_FINISH_LOGIN = (By.XPATH, "//button[contains(text(),'Login')]")

    BUTTON_TRUE_SUBNEWS = (
        By.XPATH,
        "//body/div[@id='account-register']/div[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/label[1]/input[1]"
    )
    BUTTON_FALSE_SUBNEWS = (
        By.XPATH,
        "//body/div[@id='account-register']/div[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/label[2]/input[1]"
    )

    inputs = [
        INPUT_FIRSTNAME, INPUT_LASTNAME, INPUT_EMAIL, INPUT_PASSWORD
    ]

    def registration(self):
        for input_field, input_text in zip(self.inputs, input_texts):
            self._input(input_field, input_text)
        return self
    
    def finish_reg(self):
        self.click(self.BUTTON_NEWSLETTER)
        self.click(self.BUTTON_PRIVACY_POLICY)
        self.click(self.BUTTON_NEXT)
        return self

    def login(self):
        for input_field, input_text in zip([self.INPUT_EMAIL, self.INPUT_PASSWORD], [email_text, password_text]):
            self._input(input_field, input_text)
        return self

