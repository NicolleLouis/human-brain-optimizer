from human_brain_optimizer.models.brains.general.base import Brain
from human_brain_optimizer.models.brains.specific.cook import CookBrain
from human_brain_optimizer.models.brains.specific.eat import EatBrain
from human_brain_optimizer.models.brains.specific.hunt import HuntBrain
from human_brain_optimizer.models.brains.specific.sleep import SleepBrain
from human_brain_optimizer.models.brains.specific.train import TrainBrain


class BrainV1(Brain):
    CONFIG = {
        'cook': CookBrain,
        'eat': EatBrain,
        'hunt': HuntBrain,
        'sleep': SleepBrain,
        'train': TrainBrain,
    }
