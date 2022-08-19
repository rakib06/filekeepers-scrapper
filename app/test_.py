from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get(
    "https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067?_dmd")
driver.maximize_window()

item_name_list = driver.find_elements(By.XPATH,
                                      "*//h3[@class= 's-item__title s-item__title--has-tags' or @class= 's-item__title']")

# print(item_name_list, type(item_name_list))
i = 1

price_list = driver.find_elements(By.XPATH, "*//span[@class='s-item__price']")
# print(price_list, type(price_list))
for item in zip(item_name_list, price_list):
    # print(item.text, type(item))
    with open('item.txt', 'a+') as f:
        f.write(f"{i}. {item[0].text}; Price = {item[1].text} \n")
        i += 1
# time.sleep(5)

driver.quit()
