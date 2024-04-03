from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
from config import *


class CartPage(BasePage):
    main = "//tbody/tr[1]/td[4]/form[1]/div[1]/{}"

    BUTTON_UPDATE = (By.XPATH, main.format("button[1]"))
    BUTTON_DELETE = (By.XPATH, main.format("button[2]"))
    BUTTON_PRODUCT = (By.XPATH, "//body[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[1]")
    INPUT_COUNT = (By.XPATH, main.format("input[1]"))

    BUTTON_NEXT = (By.LINK_TEXT, "Continue Shopping")
    BUTTON_MAKE_PURCHASES = (By.LINK_TEXT, "Checkout")

    BUTTON_OPEN_COUPON = (By.XPATH, "//button[contains(text(),'Use Coupon Code')]")
    BUTTON_CONFIRM_COUPON = (By.XPATH, "//button[contains(text(),'Apply Coupon')]")
    INPUT_COUPON = (By.CSS_SELECTOR, "#input-coupon")

    BUTTON_OPEN_VOUCHER = (By.XPATH, "//button[contains(text(),'Use Gift Certificate')]")
    BUTTON_CONFIRM_VOUCHER = (By.CSS_SELECTOR, "//button[contains(text(),'Apply Gift Certificate')]")
    INPUT_VOUCHER = (By.CSS_SELECTOR, "#input-voucher")
