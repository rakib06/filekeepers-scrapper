from utils.config.env import SCREENSHOT_DIR

import time
from bot.SearchPage import SearchPage
from bot import driver_setup

driver = driver_setup.docker_remote()

x = SearchPage(driver)
# driver.maximize_window()

page_count = 1
max_page_count = 10

while (x.is_next_page_button_found() and page_count < max_page_count):
    # x.driver.save_screenshot(
    #     SCREENSHOT_DIR + datetime.today().strftime('%H_%M_%S')+'test_screenshot.png')
    print(f"Page {page_count} started")
    if x.is_item_price_pair_matched():
        print(f"Page {page_count} item -price pair matched ")
        x.save_item_price_pair(filename="remote.txt")

    x.click_next_page()
    page_count += 1

time.sleep(5)
driver.quit()
