from human_brain_optimizer.exceptions.models.brain import UnknownConfigTypeException
from human_brain_optimizer.models.brains.specific.base import BaseBrain


class TrainBrain(BaseBrain):
    FLAT_AMOUNT = 500
    RATIO_AMOUNT = 0
    MAXIMUM_DEXTERITY = 20

    def __init__(self, human):
        super().__init__(human)
        self.flat_amount = self.FLAT_AMOUNT
        self.ratio_amount = self.RATIO_AMOUNT

    def finesse(self) -> int:
        if self.human.dexterity >= self.MAXIMUM_DEXTERITY:
            return 0
        return self.flat_amount + self.RATIO_AMOUNT * self.human.dexterity

    def set_config(self, config_type: str, config_value: int):
        if config_type == 'flat_amount':
            self.flat_amount = config_value
        elif config_type == 'ratio_amount':
            self.ratio_amount = config_value
        else:
            raise UnknownConfigTypeException(config_type)
