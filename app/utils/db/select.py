from utils.db.conn import connection, logger
from utils.config.env import OUTPUT_FILE_NAME, DATA_DIR

client, db, col = connection()  # Conn


def select(query={"site": "ebay"}):

    # logger.info("Mongo Select Query Execution Started")
    msg = "Verifying Mongo query..."
    logger.info("Mongo Select Query Execution Started")
    print(msg)

    doc = col.find(query)

    docs = []
    file = DATA_DIR + OUTPUT_FILE_NAME+'.txt'
    for x in doc:
        with open(file, 'a+') as f:
            msg = str(x)+'\n'
            docs.append(msg)
            f.write(f"{msg}")

    msg = f"{len(docs)} items found!"
    logger.info(msg)
    print(msg)
