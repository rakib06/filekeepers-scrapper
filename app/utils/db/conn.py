import pymongo
from utils.log import log_manager
from utils.config.env import MONGO_DB_NAME, MONGO_COLLECTION_NAME, USING_DOCKER

logger = log_manager.db_logger()


def connection():
    if USING_DOCKER.upper() == "YES":
        client = pymongo.MongoClient("mongodb://mongo:27017/")
    else:
        client = pymongo.MongoClient("mongodb://localhost:27017/")

    db = client[MONGO_DB_NAME]
    col = db[MONGO_COLLECTION_NAME]
    return client, db, col
