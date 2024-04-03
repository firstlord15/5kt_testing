import time
from conftest import *
from config import *
from page_objects.MainPage import MainPage
from pages_admin.AdminProductPage import AdminProductPage
from pages_admin.LoginPage import LoginPage
from pages_admin.AdminPage import AdminPage
from pages_admin.AdminCategoriesPage import AdminCategoriesPage


@allure.feature("Create Categories")
@allure.title("Creating new categories 'Devices'")
def test_admin_first_task(driver):
    driver.get("http:/localhost/administration/")
    LoginPage(driver).login()
    AdminPage(driver).click(AdminPage.MENU_CATALOG)
    AdminPage(driver).click(AdminPage.LI_CATEGORIES)
    time.sleep(0.5)

    categories_page = AdminCategoriesPage(driver)
    categories_page.create_categories(new_categories, META_TAG_TITLE, META_TAG_DESCRIPTION, META_TAG_KEYWORDS)

    categories_page.create_categories(
        mouse_categories, META_TAG_TITLE, META_TAG_DESCRIPTION, META_TAG_KEYWORDS, new_categories
    )
    categories_page.create_categories(
        keyboard_categories, META_TAG_TITLE, META_TAG_DESCRIPTION, META_TAG_KEYWORDS, new_categories
    )


@allure.feature("Add products")
@allure.title("Creating 4 new products in 'Devices'")
def test_admin_second_task(driver):
    driver.get(admin_page)
    LoginPage(driver).login()
    time.sleep(0.5)

    AdminProductPage(driver).add_product(input_products)


@allure.feature("Checking products")
@allure.title("Checking all products in main page")
def test_admin_third_task(driver):
    driver.get(main_page)
    MainPage(driver).find_list(input_products)
    MainPage(driver).enter()
    time.sleep(2)


@allure.feature("Delete products")
@allure.title("Deleting 2 products")
def test_admin_fourth_task(driver):
    driver.get(admin_page)
    LoginPage(driver).login()
    time.sleep(0.5)

    AdminProductPage(driver).delete_product(input_products[0])
    AdminProductPage(driver).delete_product(input_products[1])
    time.sleep(2)


@allure.feature("Checking products")
@allure.title("Checking all products in main page")
def test_admin_third_task(driver):
    driver.get(main_page)
    MainPage(driver).input_search("Dark project")
    MainPage(driver).enter()
    time.sleep(1)
    MainPage(driver).input_search("Delux")
    MainPage(driver).enter()
    time.sleep(2)
