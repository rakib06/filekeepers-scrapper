
from db.conn import *

myclient, mydb, mycol = connection()


def insert_test():
    mydict = [{"name": "John", "address": "Highway 37"}, ]
    x = mycol.insert_many(mydict)
    with open('data/insert.txt', 'w+') as f:
        f.write(f"inserted_ids= {x.inserted_ids}")
