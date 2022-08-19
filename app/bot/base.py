from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_elements(self, *by):
        sleep(1)
        elements = WebDriverWait(self.driver, 30).until(
            lambda driver: self.driver.find_elements(*by))
        return elements

    def get_element(self, *by):
        sleep(1)
        element = WebDriverWait(self.driver, 30).until(
            lambda driver: self.driver.find_element(*by))
        return element

    def scroll_down(self):
        self.driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight)/2")
