import pymongo


def connection():
    myclient = pymongo.MongoClient("mongodb://mongo:27017/")
    mydb = myclient["test_database"]
    mycol = mydb["customers"]
    return myclient, mydb, mycol
