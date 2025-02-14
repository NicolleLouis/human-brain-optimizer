import random

from human_brain_optimizer.models.actions.base import BaseAction
from human_brain_optimizer.models.brains.specific.base import BaseBrain


class RandomSpecificBrain(BaseBrain):
    def finesse(self, action: BaseAction) -> int:
        return random.randint(0, 99)
