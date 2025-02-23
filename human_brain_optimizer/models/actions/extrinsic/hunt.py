import random

from human_brain_optimizer.models.actions.base import BaseAction


class Hunt(BaseAction):
    ACTION_NAME = 'hunt'
    PROBABILITY = 2/14

    @classmethod
    def run(cls, human):
        if random.randint(0, 99) < cls.PROBABILITY * 100:
            human.add_item("rabbit")
