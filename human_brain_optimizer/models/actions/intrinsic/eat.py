import random

from human_brain_optimizer.constants.death_cause import DeathCause
from human_brain_optimizer.constants.food import Food
from human_brain_optimizer.models.actions.base import BaseAction


class Eat(BaseAction):
    ACTION_NAME = 'eat'
    FOOD_POISONING_PROBABILITY = 5
    FOOD_ENERGY_VALUE = 12

    @classmethod
    def run(cls, human):
        if Food.COOKED_FOOD in human.inventory:
            cls.eat(human, cooked=True)
        elif Food.RAW_FOOD in human.inventory:
            cls.eat(human, cooked=False)
            cls.food_poisoning_check(human)

    @classmethod
    def eat(cls, human, cooked=False):
        target_food = Food.COOKED_FOOD if cooked else Food.RAW_FOOD
        human.remove_item(target_food)
        human.food_level += cls.FOOD_ENERGY_VALUE
        human.sanitize()

    @classmethod
    def food_poisoning_check(cls, human):
        if random.randint(0, 99) < cls.FOOD_POISONING_PROBABILITY:
            human.death_cause = DeathCause.FOOD_POISONING.value
            human.dead = True
