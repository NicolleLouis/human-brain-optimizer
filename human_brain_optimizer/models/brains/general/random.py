from human_brain_optimizer.models.brains.general.base import Brain
from human_brain_optimizer.models.brains.specific.random import RandomSpecificBrain


class RandomBrain(Brain):
    CONFIG = {
        'sleep': RandomSpecificBrain
    }
