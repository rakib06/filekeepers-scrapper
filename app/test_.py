from utils.config.env import *
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "utils"))

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


# price_list = driver.find_elements(By.XPATH, PRICE_XPATH)
# # print(price_list, type(price_list))
# for item in zip(item_name_list, price_list):
#     # print(item.text, type(item))
#     with open('items__.txt', 'a+') as f:
#         try:
#             x = str(i) + ". " + item[0].text + \
#                 ": Price = " + item[1].text + "\n"
#             x = x.encode("ascii", "ignore")
#             x = x.decode()
#             # print(x, type(x))
#             f.write(x)

#         except Exception as e:
#             print(e)
#         i += 1
# time.sleep(5)

driver.quit()
