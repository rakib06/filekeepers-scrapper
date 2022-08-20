from utils.config.env import SCREENSHOT_DIR
import time
from bot.SearchPage import SearchPage
from bot import driver_setup
from utils.folders import make_dir_if_not_exits
from utils.log import log_manager

logger = log_manager.app_logger()


make_dir_if_not_exits()
srart_msg = '\n'+'='*100 + '\nTest Execution Started\n' + '='*100

# print(srart_msg)
logger.info(srart_msg)


driver = driver_setup.docker_remote()

x = SearchPage(driver)
# driver.maximize_window()

page_count = 1
max_page_count = 10

total_result = x.get_total_results()

try:

    while (x.is_next_page_button_found() and page_count < max_page_count):
        print(f"Page {page_count} started")
        if x.is_item_price_pair_matched():
            print(f"Page {page_count} item -price pair matched ")
            # x.save_item_price_pair()
            x.insert_item_price_pair_into_mongo_db()

        x.click_next_page()
        page_count += 1

except Exception as e:
    logger.error(e)

finally:
    print('-'*100)
    summery = f"Items Extracted = {x.i}, Total Items Found = {total_result}, Remaining Items= {total_result-x.i}"
    print(summery)
    logger.info(summery)
    print('-'*100)
    print("Test Execution Finished")
    logger.info("Test Execution Finished")
    time.sleep(10)
    driver.quit()
