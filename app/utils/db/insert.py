from utils.db.conn import connection, logger


client, db, col = connection()


def insert(data):

    # logger.info("Mongo Insert Execution Started")
    x = col.insert_many(data)

    msg = f"inserted_ids= {x.inserted_ids}\n"

    logger.info(f"Mongo Insert: {msg}")
