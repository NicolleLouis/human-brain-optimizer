from human_brain_optimizer.exceptions.models.brain import UnknownConfigTypeException
from human_brain_optimizer.models.brains.specific.base import BaseBrain


class TrainBrain(BaseBrain):
    MAXIMUM_DEXTERITY = 20

    FLAT_AMOUNT = 605
    RATIO_AMOUNT = 0
    HUNGER_RATIO_AMOUNT = -5
    SLEEP_RATIO_AMOUNT = -5

    def __init__(self, human):
        super().__init__(human)
        self.sleep_ratio_amount = self.SLEEP_RATIO_AMOUNT
        self.hunger_ratio_amount = self.HUNGER_RATIO_AMOUNT
        self.flat_amount = self.FLAT_AMOUNT
        self.ratio_amount = self.RATIO_AMOUNT

    def finesse(self) -> int:
        if self.human.dexterity >= self.MAXIMUM_DEXTERITY:
            return 0
        score = self.flat_amount
        score += self.ratio_amount * self.human.dexterity
        score += self.sleep_ratio_amount * self.human.sleepiness()
        score += self.hunger_ratio_amount * self.human.hunger()

        return score

    def set_config(self, config_type: str, config_value: int):
        if config_type == 'flat_amount':
            self.flat_amount = config_value
        elif config_type == 'ratio_amount':
            self.ratio_amount = config_value
        elif config_type == 'hunger_ratio_amount':
            self.hunger_ratio_amount = config_value
        elif config_type == 'sleep_ratio_amount':
            self.sleep_ratio_amount = config_value
        else:
            raise UnknownConfigTypeException(config_type)
