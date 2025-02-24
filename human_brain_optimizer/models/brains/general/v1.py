from human_brain_optimizer.models.brains.general.base import Brain
from human_brain_optimizer.models.brains.specific.eat import EatBrain
from human_brain_optimizer.models.brains.specific.random import RandomSpecificBrain
from human_brain_optimizer.models.brains.specific.sleep import SleepBrain


class BrainV1(Brain):
    CONFIG = {
        'sleep': SleepBrain,
        'eat': EatBrain,
        'hunt': RandomSpecificBrain,
    }
