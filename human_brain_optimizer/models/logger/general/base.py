from abc import ABC

from human_brain_optimizer.exceptions.models.logger import UnknownLoggerNameException
from human_brain_optimizer.models.logger.ability import AbilityLogger
from human_brain_optimizer.models.logger.action import ActionLogger
from human_brain_optimizer.models.logger.base import BaseLogger
from human_brain_optimizer.models.logger.inventory import InventoryLogger
from human_brain_optimizer.models.logger.lifespan import LifespanLogger


class GlobalLogger(ABC):
    CONFIG = {
            'ability': AbilityLogger,
            'action': ActionLogger,
            'inventory': InventoryLogger,
            'lifespan': LifespanLogger,
        }

    def __init__(self):
        self.config = {}
        for logger_name, logger_class in self.CONFIG.items():
            self.config[logger_name] = logger_class()

    def receive_message(self, logger_name: str, **kwargs) -> None:
        logger = self.get_logger(logger_name)
        logger.log(**kwargs)

    def merge_logger(self, logger_name: str, other_logger: BaseLogger) -> None:
        logger = self.get_logger(logger_name)
        logger.merge_logger(other_logger)

    def get_logger(self, logger_name: str) -> BaseLogger:
        if logger_name not in self.config:
            raise UnknownLoggerNameException(logger_name)

        return self.config[logger_name]

    def save(self, logger_names: [str] = None):
        if logger_names is None:
            for logger in self.config.values():
                logger.save()
        else:
            for logger_name in logger_names:
                self.get_logger(logger_name).save()

    def reset(self, logger_names: [str] = None):
        if logger_names is None:
            for _logger_name, logger in self.config.items():
                logger.reset()
        else:
            for logger_name in logger_names:
                self.get_logger(logger_name).reset()
