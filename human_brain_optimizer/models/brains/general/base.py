from abc import ABC

from human_brain_optimizer.exceptions.models.brain import UnknownActionNameException
from human_brain_optimizer.models.actions.base import BaseAction


class Brain(ABC):
    CONFIG = None

    def __init__(self, human):
        self.config = {}
        for action_name, brain_class in self.CONFIG.items():
            self.config[action_name] = brain_class(human)

    def finesse(self, action: BaseAction) -> int:
        action_name = action.ACTION_NAME
        if action_name not in self.CONFIG:
            raise UnknownActionNameException(action_name)

        brain = self.config[action_name]
        return brain.finesse(action)
