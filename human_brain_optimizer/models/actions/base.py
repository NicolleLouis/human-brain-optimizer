from abc import ABC, abstractmethod

from human_brain_optimizer.exceptions.models.action import ActionMissingImplementation


class BaseAction(ABC):
    ACTION_NAME = None

    def __init__(self):
        self.sanitize()

    def sanitize(self):
        if self.ACTION_NAME is None:
            raise ActionMissingImplementation

    @classmethod
    def use(cls, human):
        log_requests = cls.run(human)
        human.last_action = cls.ACTION_NAME
        return log_requests

    @staticmethod
    @abstractmethod
    def run(human):
        pass
