import random

from human_brain_optimizer.models.actions.base import BaseAction
from human_brain_optimizer.models.brains.specific.base import BaseBrain


class EatBrain(BaseBrain):
    def finesse(self, action: BaseAction) -> int:
        if len(self.human.inventory) == 0:
            return 0
        return random.randint(0, 99)
