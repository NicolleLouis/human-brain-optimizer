from human_brain_optimizer.exceptions.models.brain import UnknownConfigTypeException
from human_brain_optimizer.models.actions.base import BaseAction
from human_brain_optimizer.models.brains.specific.base import BaseBrain


class EatBrain(BaseBrain):
    FLAT_AMOUNT = 0
    RATIO_AMOUNT = 25

    def __init__(self, human):
        super().__init__(human)
        self.flat_amount = self.FLAT_AMOUNT
        self.ratio_amount = self.RATIO_AMOUNT

    def finesse(self, action: BaseAction) -> int:
        if len(self.human.inventory) == 0:
            return 0
        return self.flat_amount + self.ratio_amount * self.hunger()

    def hunger(self):
        return self.human.MAXIMUM_INDICATOR_LEVEL - self.human.food_level

    def set_config(self, config_type: str, config_value: int):
        if config_type == 'flat_amount':
            self.flat_amount = config_value
        elif config_type == 'ratio_amount':
            self.ratio_amount = config_value
        else:
            raise UnknownConfigTypeException(config_type)
