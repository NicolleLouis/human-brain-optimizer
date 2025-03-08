import random

from human_brain_optimizer.constants.food import Food
from human_brain_optimizer.models.actions.base import BaseAction


class Cook(BaseAction):
    ACTION_NAME = 'cook'
    PROBABILITY = 9/10

    @classmethod
    def run(cls, human):
        if not human.has_item(Food.RAW_FOOD):
            return

        human.remove_item(Food.RAW_FOOD)
        if random.randint(0, 99) < cls.PROBABILITY * 100:
            human.add_item(Food.COOKED_FOOD)
