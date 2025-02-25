import random
from abc import ABC, abstractmethod

from human_brain_optimizer.models.actions.base import BaseAction


class BaseBrain(ABC):
    MAX_FINESSE = 1000

    def __init__(self, human):
        self.human = human

    @abstractmethod
    def finesse(self) -> int:
        pass

    def score(self):
        score = self.finesse()
        score = min(self.MAX_FINESSE, score)

        # Adding some chaos to avoid deterministic behaviour
        score += random.randint(-10, 10)
        return score

    @abstractmethod
    def set_config(self, config_type: str, config_value: int):
        pass
