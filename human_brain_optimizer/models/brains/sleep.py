import random

from human_brain_optimizer.models.actions.base import BaseAction
from human_brain_optimizer.models.brains.base import BaseBrain


class SleepBrain(BaseBrain):
    def finesse(self, action: BaseAction) -> int:
        return random.randint(0, 100)
