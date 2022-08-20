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
MONGO_DB_NAME = os.getenv('MONGO_DB_NAME')
MONGO_COLLECTION_NAME = os.getenv('MONGO_COLLECTION_NAME')
USING_DOCKER = os.getenv('USING_DOCKER')
OUTPUT_FILE_NAME = os.getenv('OUTPUT_FILE_NAME')
SITE_NAME = os.getenv('SITE_NAME')
# print(URL, type(URL), USE_DOCKER, type(USE_DOCKER))
# print(ITEM_XPATH, PRICE_XPATH, NEXT_PAGE_XPATH)
