import time
from conftest import *
from config import *
from page_objects.MainPage import MainPage
from page_objects.ProductPage import ProductPage
from page_objects.RegistrationPage import RegistrationPage
from pages_admin.LoginPage import LoginPage
from pages_admin.AdminPage import AdminPage
from pages_admin.AdminCategoriesPage import AdminCategoriesPage
from pages_admin.AdminProductPage import AdminProductPage


def test(driver):
    driver.get(admin_page)
    LoginPage(driver).login()
    time.sleep(0.5)

    AdminProductPage(driver).delete_product(input_products[0])
    AdminProductPage(driver).delete_product(input_products[1])
    time.sleep(2)

