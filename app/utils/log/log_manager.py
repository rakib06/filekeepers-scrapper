from utils.log.logs import Log


def app_logger():
    logger = Log().get_logger(logger_name='app_logger', level='INFO')
    # file name : dd_MM_YYYY.log
    return logger


def db_logger():
    logger = Log().get_logger(log_file_name='mongo_db', logger_name='db_looger', level='INFO',
                              )
    # file name : dd_MM_YYYY.log
    return logger
