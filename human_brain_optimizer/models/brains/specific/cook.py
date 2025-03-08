from human_brain_optimizer.constants.food import Food
from human_brain_optimizer.exceptions.models.brain import UnknownConfigTypeException
from human_brain_optimizer.models.brains.specific.base import BaseBrain


class CookBrain(BaseBrain):
    FLAT_AMOUNT = 340
    UNCOOKED_RATIO_AMOUNT = 30
    COOKED_RATIO_AMOUNT = -20


    def __init__(self, human):
        super().__init__(human)
        self.flat_amount = self.FLAT_AMOUNT
        self.uncooked_ratio_amount = self.UNCOOKED_RATIO_AMOUNT
        self.cooked_ratio_amount = self.COOKED_RATIO_AMOUNT

    def finesse(self) -> int:
        if not self.human.has_item(Food.RAW_FOOD):
            return 0
        uncooked_score = self.uncooked_ratio_amount * self.rabbit_collected()
        cooked_score = self.cooked_ratio_amount * self.cooked_rabbit_collected()
        return self.flat_amount + uncooked_score + cooked_score

    def cooked_rabbit_collected(self):
        return self.human.inventory.count(Food.COOKED_FOOD)

    def rabbit_collected(self):
        return self.human.inventory.count(Food.RAW_FOOD)

    def set_config(self, config_type: str, config_value: int):
        if config_type == 'flat_amount':
            self.flat_amount = config_value
        elif config_type == 'uncooked_ratio_amount':
            self.uncooked_ratio_amount = config_value
        elif config_type == 'cooked_ratio_amount':
            self.cooked_ratio_amount = config_value
        else:
            raise UnknownConfigTypeException(config_type)
