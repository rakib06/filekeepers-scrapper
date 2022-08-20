from utils.config.env import SCREENSHOT_DIR, SITE_NAME
import time
from bot.SearchPage import SearchPage
from bot import driver_setup
from utils.folders import make_dir_if_not_exits
from utils.log import log_manager
from utils.db.select import select


logger = log_manager.app_logger()


make_dir_if_not_exits()
srart_msg = '\n'+'='*100 + '\nTest Execution Started\n' + '='*100

# print(srart_msg)
logger.info(srart_msg)


driver = driver_setup.docker_remote()

x = SearchPage(driver)
# driver.maximize_window()

page_count = 1
max_page_count = 2

total_result = x.get_total_results()

try:

    while (x.is_next_page_button_found() and page_count < max_page_count):
        scrap_msg = f"Page {page_count}: scraping started"
        logger.info(scrap_msg)
        x.insert_item_price_pair_into_mongo_db()
        scrap_msg_done = f"Page {page_count}: items = {x.count_item_box()}; upto {x.i} items scraped done!, "
        logger.info(scrap_msg_done)
        x.click_next_page()

        page_count += 1

except Exception as e:
    logger.error(e)
    driver.save_screenshot()

finally:
    print('-'*100)
    summery = f"Items Extracted = {x.i}, Total Items Found = {total_result}, Remaining Items= {total_result-x.i}"
    print(summery)
    logger.info(summery)
    print('-'*100)
    print("Test Execution Finished")
    logger.info("Test Execution Finished")
    # CHECK MONGO DB
    select(query={"site": SITE_NAME})
    time.sleep(10)
    driver.quit()
