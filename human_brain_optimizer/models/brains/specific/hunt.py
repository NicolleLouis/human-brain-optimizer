from human_brain_optimizer.constants.food import Food
from human_brain_optimizer.exceptions.models.brain import UnknownConfigTypeException
from human_brain_optimizer.models.brains.specific.base import BaseBrain


class HuntBrain(BaseBrain):
    FLAT_AMOUNT = 650
    RATIO_AMOUNT = -50

    def __init__(self, human):
        super().__init__(human)
        self.flat_amount = self.FLAT_AMOUNT
        self.ratio_amount = self.RATIO_AMOUNT

    def finesse(self) -> int:
        if len(self.human.inventory) == self.human.MAXIMUM_INVENTORY_SIZE:
            return 0
        return self.flat_amount + self.ratio_amount * self.rabbit_collected()

    def rabbit_collected(self):
        return self.human.inventory.count(Food.RAW_FOOD)

    def set_config(self, config_type: str, config_value: int):
        if config_type == 'flat_amount':
            self.flat_amount = config_value
        elif config_type == 'ratio_amount':
            self.ratio_amount = config_value
        else:
            raise UnknownConfigTypeException(config_type)
