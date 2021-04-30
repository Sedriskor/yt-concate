import logging
from datetime import datetime
from yt_concate.settings import LOG_DIR


# filename = "{:%Y-%m-%d}".format(datetime.name()) + '.log'

class MyLog:
    def __init__(self, __name__):
        # logging.basicConfig(level=logging.DEBUG,
        #                     format=LOGGING_FORMAT,
        #                     datefmt=DATE_FORMAT)

        # config
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        logging.captureWarnings(True)
        formatter = logging.Formatter('%(asctime)s : %(name)s - %(levelname)s: %(message)s')

        # file handler
        log_filename = datetime.now().strftime("%Y-%m-%d.log")
        file_fandler = logging.FileHandler(LOG_DIR + '/' + log_filename, 'a', 'utf-8')
        file_fandler.setLevel(logging.DEBUG)
        file_fandler.setFormatter(formatter)
        self.logger.addFilter(file_fandler)

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
