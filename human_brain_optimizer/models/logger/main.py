from human_brain_optimizer.exceptions.models.logger import UnknownLoggerNameException
from human_brain_optimizer.models.logger.lifespan import LifespanLogger


class MainLogger:
    def __init__(self):
        self.config = {
            'lifespan': LifespanLogger()
        }

    def receive_message(self, logger_name: str, message) -> None:
        if logger_name not in self.config:
            raise UnknownLoggerNameException(logger_name)

        logger = self.config[logger_name]
        logger.log(message)

    def save(self):
        for logger in self.config.values():
            logger.save()
