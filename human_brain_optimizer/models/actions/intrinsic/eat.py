import random

from human_brain_optimizer.constants.death_cause import DeathCause
from human_brain_optimizer.models.actions.base import BaseAction


class Eat(BaseAction):
    ACTION_NAME = 'eat'
    FOOD_POISONING_PROBABILITY = 5

    @classmethod
    def run(cls, human):
        if 'rabbit' not in human.inventory:
            return

        cls.eat(human)
        cls.food_poisoning_check(human)

    @staticmethod
    def eat(human):
        human.remove_item('rabbit')
        human.food_level += 12
        human.sanitize()

    @classmethod
    def food_poisoning_check(cls, human):
        if random.randint(0, 99) < cls.FOOD_POISONING_PROBABILITY:
            human.death_cause = DeathCause.FOOD_POISONING.value
            human.dead = True
