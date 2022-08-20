from selenium.webdriver.common.by import By
from utils.config.env import *


class SearchResultPageLocators:
    URL = URL
    ITEM_NAME = (By.XPATH, ITEM_XPATH)
    ITEM_PRICE = (By.XPATH, PRICE_XPATH)
    NEXT_PAGE_BUTTON = (By.XPATH, NEXT_PAGE_XPATH)
    TOTAL_RESULT_FOUND = (By.XPATH, TOTAL_RESULT_FOUND_XPATH)
    ITEM_BOX = (By.XPATH, ITEM_BOX_XPATH)
