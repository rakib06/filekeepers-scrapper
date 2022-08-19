
from utils.config.env import *
from utils.db.conn import *

myclient, mydb, mycol = connection()


def insert_test():
    mydict = [{"name": "John", "address": "Highway 37"}, ]
    x = mycol.insert_many(mydict)
    with open(DATA_DIR+'insert.txt', 'w+') as f:
        f.write(f"inserted_ids= {x.inserted_ids}")
