import logging
from datetime import datetime
from yt_concate.settings import LOG_DIR


class MyLog:
    def __init__(self, __name__):
        # config
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        logging.captureWarnings(True)
        log_filename = datetime.now().strftime("%Y-%m-%d.log")
        formatter = logging.Formatter('%(asctime)s [%(name)s] <%(levelname)s> %(message)s')

        # file handler
        file_handler = logging.FileHandler(LOG_DIR + '/' + log_filename, 'a', 'utf-8')
        file_handler.setLevel(logging.WARNING)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        # stream handler
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

    def log(self, level, msg):
        self.logger.log(level, msg)

    def setLevel(self, level):
        self.logger.setLevel(level)

    def disable(self):
        logging.disable(50)
