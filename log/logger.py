import logging
import os
from datetime import datetime
dir_path = os.path.dirname(__file__) + '/'
filename = "{:%Y-%m-%d}".format(datetime.now()) + '.log'  # 設定檔名


def create_logger(log_folder):
    #  config
    logging.captureWarnings(True)  # 捕捉 py waring message
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    my_logger = logging.getLogger('py.warnings')  # 捕捉 py waring message
    my_logger.setLevel(logging.INFO)
    if not os.path.exists(dir_path + log_folder):
        os.makedirs(dir_path + log_folder)

    # file handler
    fileHandler = logging.FileHandler(dir_path + log_folder + '/' + filename, 'a', 'utf-8')
    fileHandler.setFormatter(formatter)
    my_logger.addHandler(fileHandler)

    # console handler
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.DEBUG)
    consoleHandler.setFormatter(formatter)
    my_logger.addHandler(consoleHandler)

    return my_logger
