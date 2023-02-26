import sys
sys.path.append('../')
import logging

class LoggerService:
    def __init__(self):
       
        self.logger = logging.getLogger('app_production')
        self.logger.setLevel('INFO')
        # define handlers
        handler = logging.StreamHandler() # handler para consola
        handler.setLevel('INFO')
        logger_format = logging.Formatter("%(asctime)s - %(name)s - %(process)s - %(levelname)s - %(message)s")
        handler.setFormatter(logger_format)

        self.logger.addHandler(handler)

    def error(self, message):
        self.logger.error(message)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def critical(self, message):
        self.logger.critical(message)

loggerService = LoggerService()


