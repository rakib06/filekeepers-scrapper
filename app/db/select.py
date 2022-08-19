
from db import conn

myclient, mydb, mycol = conn.connection()


def test_query():
    myquery = {"address": "Highway 37"}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        with open('data/test_query.txt', 'w+') as f:
            f.write(f"result = {str(x)}")
