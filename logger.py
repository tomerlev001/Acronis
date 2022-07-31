import logging
from datetime import datetime
from enum import Enum


FORMATTER = "%(asctime)s_%(levelname)s_%(filename)s_:%(message)s"
PATH = rf".\Logs\{datetime.utcnow().now().date()}.log"


class DebugLevel(Enum):
    DEBUG = 'DEBUG',
    INFO = 'INFO',
    WARNING = 'WARNING',
    ERROR = 'ERROR',
    CRITICAL = 'CRITICAL'


class Logger:

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.__logger = logging.getLogger(self.file_name)
        self.__formatter = logging.Formatter(FORMATTER)

    def get_logger(self, debug_level: DebugLevel = DebugLevel.DEBUG) -> logging:
        self.__logger.setLevel(debug_level.name)
        self.__add_file_handler()
        self.__add_stream_handler()

        return self.__logger

    def __add_file_handler(self) -> None:
        file_handler = logging.FileHandler(PATH)
        file_handler.setFormatter(self.__formatter)
        self.__logger.addHandler(file_handler)

    def __add_stream_handler(self) -> None:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(self.__formatter)
        self.__logger.addHandler(stream_handler)
