from abc import ABC, abstractmethod

from human_brain_optimizer.models.actions.base import BaseAction


class BaseBrain(ABC):
    @staticmethod
    @abstractmethod
    def finesse(action: BaseAction) -> int:
        pass
