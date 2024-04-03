from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    MAIN_PICTURE = (By.XPATH, "//body/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]")
    BUTTON_FAVORITE = (By.XPATH, "//body/main[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/button[1]")
    BUTTON_BUY = (By.CSS_SELECTOR, "#button-cart")
    BUTTON_NEXT_REVIEW = (By.CSS_SELECTOR, "#button-review")
    INPUT_COUNT = (By.CSS_SELECTOR, "#input-quantity")
    BUTTON_DESCRIPTION = (By.LINK_TEXT, "Description")
    BUTTON_CHARACTERISTICS = (By.LINK_TEXT, "Specification")
    BUTTON_REVIEW = (By.PARTIAL_LINK_TEXT, "Reviews (")
    INPUT_NAME_REVIEW = (By.CSS_SELECTOR, "#input-name")
    INPUT_REVIEW = (By.CSS_SELECTOR, "#input-text")
    INPUT_KEYWORD = (By.CSS_SELECTOR, "#input-keyword-0-1")
    SELECT_COLOR = (By.CSS_SELECTOR, "#input-option-226")
    SELECT_OPTION_COLOR = (By.CSS_SELECTOR, "div.container:nth-child(2) div.row div.col div.row.mb-3 div.col-sm:nth-child(2) form:nth-child(1) div:nth-child(3) div.mb-3.required:nth-child(1) select.form-select > option:nth-child(3)")

    def click_main_picture(self):
        self.click(self.MAIN_PICTURE)
        return self

    def click_review_mark(self, index: int):
        self.click((By.CSS_SELECTOR, f'input.form-check-input:nth-child({index})'))
        return self

    def right_arrow(self, count: int):
        if count <= 1:
            self.rightArrow()
        else:
            for _ in range(count):
                self.rightArrow()

        return self