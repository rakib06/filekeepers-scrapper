from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from utils.config.env import *
driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get(URL)
driver.maximize_window()

item_name_list = driver.find_elements(By.XPATH, ITEM_XPATH)

# print(item_name_list, type(item_name_list))
i = 1

price_list = driver.find_elements(By.XPATH, PRICE_XPATH)
# print(price_list, type(price_list))
for item in zip(item_name_list, price_list):
    # print(item.text, type(item))
    with open('items__.txt', 'a+') as f:
        try:
            x = str(i) + ". " + item[0].text + \
                ": Price = " + item[1].text + "\n"
            x = x.encode("ascii", "ignore")
            x = x.decode()
            # print(x, type(x))
            f.write(x)

        except Exception as e:
            print(e)
        i += 1
# time.sleep(5)

driver.quit()
