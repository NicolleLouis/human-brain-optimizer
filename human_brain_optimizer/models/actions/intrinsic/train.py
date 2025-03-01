import random

from human_brain_optimizer.models.actions.base import BaseAction


class Train(BaseAction):
    ACTION_NAME = 'train'
    PROBABILITY = 1/2

    @classmethod
    def run(cls, human):
        if random.randint(0, 99) < cls.PROBABILITY * 100:
            human.gain_dexterity()
