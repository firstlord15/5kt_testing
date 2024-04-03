from page_objects.BasePage import BasePage
from pages_admin.AdminPage import AdminPage
from selenium.webdriver.common.by import By
from config import *
import time


class LoginPage(BasePage):
    INPUT_LOGIN = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    NEXT = (By.XPATH, "//body/div[@id='container']/div[@id='content']/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[3]/button[1]")

    def login(self):
        self._input(LoginPage.INPUT_LOGIN, admin_login_text)
        self._input(LoginPage.INPUT_PASSWORD, admin_password_text)
        self.click(LoginPage.NEXT)
        self.logger.info("ADMIN: FINISH LOGGING")
        self.click(AdminPage.MENU_CATALOG)
        self.click(AdminPage.LI_PRODUCTS)
