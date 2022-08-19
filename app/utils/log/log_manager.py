from utils.log.logs import Log


def exception_manager_logger():
    logger = Log().get_logger(logger_name='exception',
                              level='WARNING', log_file_name='Exception')
    # file name : dd_MM_YYYY.log
    return logger


def main_logger():
    logger = Log().get_logger(logger_name='Main Program',
                              level='DEBUG', log_file_name="MAIN")
    # file name : dd_MM_YYYY.log
    return logger


def app_logger():
    logger = Log().get_logger(logger_name='app_logger', level='INFO')
    # file name : dd_MM_YYYY.log
    return logger