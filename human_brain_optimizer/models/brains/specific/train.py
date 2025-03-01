from human_brain_optimizer.exceptions.models.brain import UnknownConfigTypeException
from human_brain_optimizer.models.brains.specific.base import BaseBrain


class TrainBrain(BaseBrain):
    FLAT_AMOUNT = 480

    def __init__(self, human):
        super().__init__(human)
        self.flat_amount = self.FLAT_AMOUNT

    def finesse(self) -> int:
        if self.human.dexterity >= 5:
            return 0
        return self.flat_amount

    def set_config(self, config_type: str, config_value: int):
        if config_type == 'flat_amount':
            self.flat_amount = config_value
        else:
            raise UnknownConfigTypeException(config_type)
