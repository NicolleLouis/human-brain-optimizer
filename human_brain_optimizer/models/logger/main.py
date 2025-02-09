from human_brain_optimizer.exceptions.models.logger import UnknownLoggerNameException
from human_brain_optimizer.models.logger.action import ActionLogger
from human_brain_optimizer.models.logger.base import BaseLogger
from human_brain_optimizer.models.logger.lifespan import LifespanLogger


class MainLogger:
    def __init__(self):
        self.config = {
            'lifespan': LifespanLogger(),
            'action': ActionLogger(),
        }

    def receive_message(self, logger_name: str, message) -> None:
        logger = self.get_logger(logger_name)
        logger.log(message)

    def merge_logger(self, logger_name: str, other_logger: BaseLogger) -> None:
        logger = self.get_logger(logger_name)
        logger.merge_logger(other_logger)

    def get_logger(self, logger_name: str) -> BaseLogger:
        if logger_name not in self.config:
            raise UnknownLoggerNameException(logger_name)

        return self.config[logger_name]

    def save(self):
        for logger in self.config.values():
            logger.save()
