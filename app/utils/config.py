import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv('URL')
USE_DOCKER = bool(os.getenv('USE_DOCKER'))

# print(URL, type(URL), USE_DOCKER, type(USE_DOCKER))
