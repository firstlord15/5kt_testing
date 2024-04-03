from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
from config import *
import time


class AdminCategoriesPage(BasePage):
    Main_Page = (By.LINK_TEXT, "Categories")

    # GENERAL
    LI_GENERAL = (By.LINK_TEXT, "General")
    BUTTON_ADD_NEW_CATEGORIES = (By.CSS_SELECTOR, "a.btn.btn-primary:nth-child(2)")
    INPUT_CATEGORY_NAME = (By.CSS_SELECTOR, "#input-name-1")
    INPUT_META_TAG_TITLE = (By.CSS_SELECTOR, "#input-meta-title-1")
    INPUT_META_TAG_DESCRIPTION = (By.CSS_SELECTOR, "#input-meta-description-1")
    INPUT_META_TAG_KEYWORDS = (By.CSS_SELECTOR, "#input-meta-keyword-1")
    BUTTON_SAVE_CATEGORY = (By.CSS_SELECTOR, "button.btn.btn-primary:nth-child(1)")

    # _DATA
    SELECT_PARENT = (By.CSS_SELECTOR, "#input-parent")
    OPTION_PARENT = (By.PARTIAL_LINK_TEXT, "--- None -")
    INPUT_FILTER = (By.CSS_SELECTOR, "#input-filter")
    INPUT_COLUMNS = (By.CSS_SELECTOR, "#input-column")
    INPUT_SORT_ORDER = (By.CSS_SELECTOR, "#input-sort-order")
    INPUT_STATUS = (By.CSS_SELECTOR, "#input-status")

    # _DESIGN
    LI_DESIGN = (
        By.XPATH, "//body/div[@id='container']/div[@id='content']/div[2]/div[1]/div[2]/form[1]/ul[1]/li[4]/a[1]")
    SELECT_LAYOUT_OVERRIDE = (By.XPATH, "//tbody/tr[1]/td[2]/select[1]")

    # _DATA
    LI_DATA = (By.LINK_TEXT, "Data")

    # _SEO
    LI_SEO = (By.LINK_TEXT, "SEO")
    INPUT_KEYWORD = (By.CSS_SELECTOR, "#input-keyword-0-1")

    def arrow_down(self, count: int):
        if count > 0:
            for _ in range(count):
                self.downArrow()
        else:
            self.downArrow()
        return self

    def create_categories(self, name: str, mtt: str, mtd: str, mtk: str, parent=None):
        self.click(self.BUTTON_ADD_NEW_CATEGORIES)

        self._input(self.INPUT_CATEGORY_NAME, name)
        self._input(self.INPUT_META_TAG_TITLE, mtt+name)
        self._input(self.INPUT_META_TAG_DESCRIPTION, mtd+name)
        self._input(self.INPUT_META_TAG_KEYWORDS, mtk+name)
        time.sleep(0.5)

        self.click(self.LI_DATA)

        if parent is not None:
            self._input(self.SELECT_PARENT, parent)
            time.sleep(0.5)
            self.click((By.LINK_TEXT, parent))
        else:
            self.click(self.SELECT_PARENT)
            self.click(self.OPTION_PARENT)

        time.sleep(0.5)

        self.click(self.LI_SEO)
        self._input(self.INPUT_KEYWORD, name.lower()+"test")
        time.sleep(0.5)

        self.click(self.LI_DESIGN)
        self.click(self.SELECT_LAYOUT_OVERRIDE)
        self.arrow_down(7)
        time.sleep(0.5)

        self.click(self.BUTTON_SAVE_CATEGORY)
        time.sleep(3)
        self.click(self.Main_Page)
