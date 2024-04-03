from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
from config import *
import time


class MainPage(BasePage):
    INPUT_SEARCH = (By.XPATH, "//header/div[1]/div[1]/div[2]/div[1]/input[1]")
    BUTTON_CART_TOTAL = (By.XPATH, "//body/nav[@id='top']/div[1]/div[2]/ul[1]/li[4]")
    BUTTON_CART = (By.CSS_SELECTOR, "#header-cart")
    BUTTON_REGLOG = (By.XPATH, "//body/nav[@id='top']/div[1]/div[2]/ul[1]/li[2]")
    BUTTON_REGISTER = (By.LINK_TEXT, "Register")
    BUTTON_LOGIN = (By.LINK_TEXT, "Login")
    DROPDOWN_TABLET = (By.LINK_TEXT, "Tablets")
    PRODUCT_TABLET = (By.LINK_TEXT, "Samsung Galaxy Tab 10.1")
    DROPDOWN_TELEPHONES = (By.LINK_TEXT, "Phones & PDAs")
    PRODUCT_IPHONE = (By.LINK_TEXT, "iPhone")
    DROPDOWN_PC = (By.LINK_TEXT, "Desktops")
    LI_PC = (By.LINK_TEXT, "PC (0)")

    PRODUCTS = [
        (By.LINK_TEXT, "MacBook"),
        (By.LINK_TEXT, "iPhone"),
        (By.LINK_TEXT, 'Apple Cinema 30"'),
        (By.LINK_TEXT, "Canon EOS 5D"),
    ]

    PRODUCTS_BUTTON_BUY = [
        (By.XPATH, product.format(str(i), "1"))
        for i in range(1, 5)
    ]

    PRODUCTS_BUTTON_FAVORITE = [
        (By.XPATH, product.format(str(i), "2"))
        for i in range(1, 5)
    ]

    LAST_INDEX = PRODUCTS[len(PRODUCTS) - 1]

    def click_product(self, index: int):
        self.click(self.PRODUCTS[index])
        time.sleep(0.1)
        return self

    def click_products_buy(self, count):
        for i in count:
            self.click(self.PRODUCTS_BUTTON_BUY[i])
        time.sleep(0.1)
        return self

    def open_registration(self):
        self.click(self.BUTTON_REGLOG)
        self.click(self.BUTTON_REGISTER)
        return self

    def input_search(self, text: str):
        self._input(self.INPUT_SEARCH, text)
        self.enter()

    def find_list(self, arr):
        for element in arr:
            self.input_search(element[0] + " " + element[1])
            time.sleep(2)
