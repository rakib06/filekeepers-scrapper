
from utils.config.env import *
from utils.db import conn

myclient, mydb, mycol = conn.connection()


def test_query():
    myquery = {"address": "Highway 37"}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        with open(DATA_DIR+'test_query.txt', 'w+') as f:
            f.write(f"result = {str(x)}")
