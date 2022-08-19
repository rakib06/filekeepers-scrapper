from time import sleep

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from utils.config.env import *
from utils.db import insert, select
from utils.log import log_manager
from utils.folders import make_dir_if_not_exits
logger = log_manager.app_logger()


make_dir_if_not_exits()
sleep(5)
print("Test Execution Started")
logger.info("Test Execution Started")

driver = webdriver.Remote('http://selenium:4444/wd/hub',
                          desired_capabilities=DesiredCapabilities.CHROME,
                          )


driver.get(URL)
logger.info(f"Site Opened: {URL}")

driver.save_screenshot(SCREENSHOT_DIR+'test_screenshot.png')
insert.insert_test()
select.test_query()
