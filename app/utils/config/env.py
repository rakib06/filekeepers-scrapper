import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv('URL')
USE_DOCKER = bool(os.getenv('USE_DOCKER'))
SCREENSHOT_DIR = os.getenv('SCREENSHOT_DIR')
LOGS_DIR = os.getenv('LOGS_DIR')
DATA_DIR = os.getenv('DATA_DIR')
ITEM_XPATH = os.getenv('ITEM_XPATH')
PRICE_XPATH = os.getenv('PRICE_XPATH')
NEXT_PAGE_XPATH = os.getenv('NEXT_PAGE_XPATH')
TOTAL_RESULT_FOUND_XPATH = os.getenv('TOTAL_RESULT_FOUND_XPATH')
ITEM_BOX_XPATH = os.getenv('ITEM_BOX_XPATH')

# print(URL, type(URL), USE_DOCKER, type(USE_DOCKER))
# print(ITEM_XPATH, PRICE_XPATH, NEXT_PAGE_XPATH)
