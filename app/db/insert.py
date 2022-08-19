
from db.conn import *
import random

myclient, mydb, mycol = connection()


def insert_test():
    mobile = random.randint(1000000, 9000000)

    mydict = [
        {"name": "John", "address": "Highway 37", "mobile": mobile},
    ]
    x = mycol.insert_many(mydict)
    with open('data/insert.txt', 'w+') as f:
        f.write(f"inserted_ids= {x.inserted_ids}")
