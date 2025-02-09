from abc import ABC

from human_brain_optimizer.exceptions.models.brain import UnknownActionNameException
from human_brain_optimizer.models.actions.base import BaseAction


class Brain(ABC):
    CONFIG = None

    @classmethod
    def finesse(cls, action: BaseAction) -> int:
        action_name = action.ACTION_NAME
        if action_name not in cls.CONFIG:
            raise UnknownActionNameException(action_name)

        brain = cls.CONFIG[action_name]
        return brain.finesse(action)
