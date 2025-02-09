from human_brain_optimizer.exceptions.models.brain import UnknownActionNameException
from human_brain_optimizer.models.actions.base import BaseAction
from human_brain_optimizer.models.brains.sleep import SleepBrain


class MainBrain:
    def __init__(self):
        self.config = {
            'sleep': SleepBrain()
        }

    def finesse(self, action: BaseAction) -> int:
        action_name = action.ACTION_NAME
        if action_name not in self.config:
            raise UnknownActionNameException(action_name)

        brain = self.config[action_name]
        return brain.finesse(action)
