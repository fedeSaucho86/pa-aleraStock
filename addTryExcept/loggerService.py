import sys
sys.path.append('../')
import logging

class LoggerService:
    def __init__(self,) -> None:   
        self.logger = logging.getLogger('app_production')
        self.logger.setLevel('INFO')
        # define handlers
        handler = logging.StreamHandler() # handler para consola
        handler.setLevel('INFO')
        logger_format = logging.Formatter("%(asctime)s - %(name)s - %(process)s - %(levelname)s - %(message)s")
        handler.setFormatter(logger_format)

        self.logger.addHandler(handler)

    def error(self, message:str) -> None:
        """
        Error level of logging

        Args:
            message (str): error from console
        """
        self.logger.error(message)

    def info(self, message:str) -> None:
        """
        Error level of logginf

        Args:
            message (str): error from console
        """
        self.logger.info(message)

    def debug(self, message:str) -> None:
        """
        Error level of logginf

        Args:
            message (str): error from console
        """
        self.logger.debug(message)

    def warning(self, message:str) -> None:
        """
        Error level of logginf

        Args:
            message (str): error from console
        """
        self.logger.warning(message)

    def critical(self, message:str) -> None:
        """
        Error level of logginf

        Args:
            message (str): error from console
        """
        self.logger.critical(message)

loggerService = LoggerService()


