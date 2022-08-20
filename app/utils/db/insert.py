
from utils.config.env import *
from utils.db.conn import *
from utils.log import log_manager
import pymongo

myclient, mydb, mycol = connection()

logger = log_manager.db_logger()


def insert_test():
    mydict = [{"name": "John", "address": "Highway 37"}, ]
    x = mycol.insert_many(mydict)
    with open(DATA_DIR+'insert.txt', 'w+') as f:
        f.write(f"inserted_ids= {x.inserted_ids}")


def insert(data, db_name='ebay_db', collection_name='items'):

    # logger.info("Mongo Insert Execution Started")
    db = myclient[db_name]
    collection = db[collection_name]
    x = collection.insert_many(data)

    msg = f"inserted_ids= {x.inserted_ids}\n"
    # with open(DATA_DIR+'inserted_ids.txt', 'w+') as f:
    #     f.write(msg)

    logger.info(f"Mongo Insert: {msg}")
