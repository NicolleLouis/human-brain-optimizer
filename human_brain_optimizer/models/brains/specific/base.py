from abc import ABC, abstractmethod

from human_brain_optimizer.models.actions.base import BaseAction


class BaseBrain(ABC):
    def __init__(self, human):
        self.human = human

    @abstractmethod
    def finesse(self, action: BaseAction) -> int:
        pass
