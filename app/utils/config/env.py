import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv('URL')
USE_DOCKER = bool(os.getenv('USE_DOCKER'))
SCREENSHOT_DIR = os.getenv('SCREENSHOT_DIR')
LOGS_DIR = os.getenv('LOGS_DIR')
DATA_DIR = os.getenv('DATA_DIR')

# print(URL, type(URL), USE_DOCKER, type(USE_DOCKER))
