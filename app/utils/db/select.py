
from utils.config.env import *
from utils.db import conn
from utils.log import log_manager
import pymongo


myclient, mydb, mycol = conn.connection()


def test_query():
    myquery = {"address": "Highway 37"}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        with open(DATA_DIR+'test_query.txt', 'w+') as f:
            f.write(f"result = {str(x)}")


def query(q={"site": "ebay"}, db_name='ebay_db', collection_name='items'):
    logger = log_manager.app_logger()
    logger.info("Mongo Select Query Execution Started")
    db = myclient[db_name]
    collection = db[collection_name]
    doc = collection.find(myquery)

    docs = ''
    for x in doc:
        with open(DATA_DIR+'query.txt', 'w+') as f:
            msg = str(x)+'\n'
            docs.append(msg)
            f.write(f"{msg}")

    logger.info(f"Mongo Select Query: {docs}")
