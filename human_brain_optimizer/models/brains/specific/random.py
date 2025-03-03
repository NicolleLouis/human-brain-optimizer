import random

from human_brain_optimizer.models.brains.specific.base import BaseBrain


class RandomSpecificBrain(BaseBrain):
    def finesse(self) -> int:
        return random.randint(0, self.MAX_FINESSE)

    def set_config(self, config_type: str, config_value: int):
        pass # pragma: no cover
