from human_brain_optimizer.constants.food import Food
from human_brain_optimizer.exceptions.models.brain import UnknownConfigTypeException
from human_brain_optimizer.models.brains.specific.base import BaseBrain


class EatBrain(BaseBrain):
    FLAT_AMOUNT = 275
    RATIO_AMOUNT = 33
    UNCOOKED_MALUS = 150

    def __init__(self, human):
        super().__init__(human)
        self.uncooked_malus = self.UNCOOKED_MALUS
        self.flat_amount = self.FLAT_AMOUNT
        self.ratio_amount = self.RATIO_AMOUNT

    def finesse(self) -> int:
        if not self.has_food():
            return 0
        if self.human.hunger() < 12:
            return 0
        score = self.flat_amount
        score += self.ratio_amount * self.human.hunger()
        if not self.has_cooked_food():
            score -= self.uncooked_malus

        return score

    def has_food(self):
        return self.human.has_item(Food.RAW_FOOD) or self.human.has_item(Food.COOKED_FOOD)

    def has_cooked_food(self):
        return self.human.has_item(Food.COOKED_FOOD)

    def set_config(self, config_type: str, config_value: int):
        if config_type == 'flat_amount':
            self.flat_amount = config_value
        elif config_type == 'ratio_amount':
            self.ratio_amount = config_value
        elif config_type == 'uncooked_malus':
            self.uncooked_malus = config_value
        else:
            raise UnknownConfigTypeException(config_type)
