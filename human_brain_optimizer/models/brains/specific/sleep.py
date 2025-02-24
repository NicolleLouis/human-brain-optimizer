from human_brain_optimizer.exceptions.models.brain import UnknownConfigTypeException
from human_brain_optimizer.models.actions.base import BaseAction
from human_brain_optimizer.models.brains.specific.base import BaseBrain


class SleepBrain(BaseBrain):
    FLAT_AMOUNT = 0
    RATIO_AMOUNT = 30
    ALREADY_ASLEEP_BONUS = 450


    def __init__(self, human):
        super().__init__(human)
        self.flat_amount = self.FLAT_AMOUNT
        self.ratio_amount = self.RATIO_AMOUNT
        self.already_asleep_bonus = self.ALREADY_ASLEEP_BONUS

    def finesse(self, action: BaseAction) -> int:
        finesse = self.flat_amount + self.ratio_amount * self.sleepiness()
        if self.was_sleeping():
            finesse += self.already_asleep_bonus
        return finesse

    def was_sleeping(self):
        return self.human.last_action == 'sleep'

    def sleepiness(self):
        return self.human.MAXIMUM_INDICATOR_LEVEL - self.human.energy_level

    def set_config(self, config_type: str, config_value: int):
        if config_type == 'flat_amount':
            self.flat_amount = config_value
        elif config_type == 'ratio_amount':
            self.ratio_amount = config_value
        elif config_type == 'already_asleep_bonus':
            self.already_asleep_bonus = config_value
        else:
            raise UnknownConfigTypeException(config_type)
