import random

from human_brain_optimizer.models.actions.base import BaseAction


class Hunt(BaseAction):
    ACTION_NAME = 'hunt'
    PROBABILITY = 2/14
    MAX_DEXTERITY = 20

    @classmethod
    def run(cls, human):
        if random.randint(0, 99) < cls.hunt_probability(human):
            human.add_item("rabbit")

    @classmethod
    def hunt_probability(cls, human):
        return cls.PROBABILITY * 100 + min(cls.MAX_DEXTERITY, human.dexterity)
