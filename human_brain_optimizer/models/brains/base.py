from abc import ABC, abstractmethod

from human_brain_optimizer.models.actions.base import BaseAction


class BaseBrain(ABC):
    @abstractmethod
    def finesse(self, action: BaseAction) -> int:
        pass
