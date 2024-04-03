from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from random import randint
import allure
import time


class BasePage:
    def __init__(self, driver, wait=10):
        self.driver = driver
        self.logger = driver.logger
        self.wait = WebDriverWait(self.driver, wait)
        self.class_name = self.__class__.__name__

    def is_tuple(self, element_locator):
        if isinstance(element_locator, tuple):
            return self.driver.find_element(*element_locator)
        else:
            return self.driver.find_element(element_locator)

    @allure.step
    def escape(self):
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        self.logger.info("Press 'Escape'")
        time.sleep(1)
        return self

    @allure.step
    def enter(self):
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        self.logger.info("Press 'Enter'")
        time.sleep(1)
        return self
    
    @allure.step
    def tab(self):
        ActionChains(self.driver).send_keys(Keys.TAB).perform()
        self.logger.info("Press 'TAB'")
        time.sleep(1)
        return self
    
    @allure.step
    def rightArrow(self):
        ActionChains(self.driver).send_keys(Keys.CONTROL).send_keys(Keys.ARROW_RIGHT).perform()
        self.logger.info("Press 'Right'")
        time.sleep(1)
        return self
    
    @allure.step
    def downArrow(self):
        ActionChains(self.driver).send_keys(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).perform()
        self.logger.info("Press 'Down'")
        time.sleep(0.2)
        return self

    @staticmethod
    def random(arr):
        return randint(0, len(arr) - 1)

    @staticmethod
    def last(arr):
        return len(arr) - 1

    # метод для поиска названия поля в классе, по значению
    def element_name(self, element):
        for name, value in vars(self.__class__).items():
            if isinstance(value, (list, tuple)) and element in value:
                return f"{name}[{value.index(element)}]"
            elif value == element:
                return name
        return element
    
    def home(self):
        self.click('(By.CSS_SELECTOR, "#logo")')
    
    @allure.step
    def click(self, element_locator):
        try:
            time.sleep(1)
            element = self.is_tuple(element_locator)
            element_name = self.element_name(element_locator)
            ActionChains(self.driver).move_to_element(element).perform()
            self.wait.until(EC.element_to_be_clickable(element)).click()
            self.logger.info(f"{self.class_name}: Clicking element '{element_name}'")
            time.sleep(0.5)
        except Exception:
            allure.attach(name="screenshot", body=self.driver.get_screenshot_as_png())
            self.logger.error(f"{self.class_name}: Error when clicking element '{element_name}': {element_locator}")
            raise AssertionError(f"Ошибка при выполнении click")

        return self

    @allure.step
    def write(self, element_locator, value, clearing = True):
        try:
            element = self.is_tuple(element_locator)
            element_name = self.element_name(element_locator)
            
            if clearing:
                element.clear()
                self.logger.info(f"{self.class_name}: Clearing input '{element_name}'")

            result_text = value[randint(0, len(value) - 1)] if isinstance(value, list) else value

            for letter in result_text:
                time.sleep(randint(1, 3) / 50)
                element.send_keys(letter)
            self.logger.info(f"{self.class_name}: Writing '{
                result_text}' in input '{element_name}'")
        except Exception:
            allure.attach(name="screenshot", body=self.driver.get_screenshot_as_png())
            self.logger.error(f"{self.class_name}: Error when writing element '{element_name}': {element_locator}")
            raise AssertionError("Ошибка при выполнении write")

        return self

    def _input(self, element, value, clear = True, timing=0.1):
        self.click(element)
        time.sleep(timing)
        self.write(element, value, clearing=clear)
        time.sleep(0.5)

        return self
