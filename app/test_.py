from utils.db.select import select
from utils.config.env import *
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import sys


def test_browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(URL)
    driver.maximize_window()

    # item_name_list = driver.find_elements(By.XPATH, ITEM_XPATH)

    # print(item_name_list, type(item_name_list))
    i = 1

    ITEM_BOX_XPATH = "*//div[@class='s-item__wrapper clearfix']"

    # If you start an XPath expression with //, it begins searching from the root of document. To search relative to a particular element, you should prepend the expression with . instead:

    item_box = driver.find_elements(By.XPATH, ITEM_BOX_XPATH)

    for item in item_box:
        item_name = print(item.find_element(By.XPATH, ITEM_XPATH).text)
        item_price = print(item.find_element(By.XPATH, PRICE_XPATH).text)
    print(len(item_box))

    driver.quit()


def test_mongo_db():
    ...


# test_mongo_db()

if __name__ == '__main__':
    import sys
    from utils.config.env import SITE_NAME
    if sys.argv[1] == 'mongo' and len(sys.argv[1:]) == 1:

        select(query={"site": SITE_NAME})
