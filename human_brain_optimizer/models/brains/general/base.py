from abc import ABC

from human_brain_optimizer.exceptions.models.brain import UnknownActionNameException
from human_brain_optimizer.models.actions.base import BaseAction
from human_brain_optimizer.models.data.brain_config import BrainConfig


class Brain(ABC):
    CONFIG = None

    def __init__(self, human):
        self.config = {}
        for action_name, brain_class in self.CONFIG.items():
            self.config[action_name] = brain_class(human)

    def get_brain(self, action: BaseAction = None, action_name: str = None):
        if action is not None:
            action_name = action.ACTION_NAME

        if action_name not in self.CONFIG:
            raise UnknownActionNameException(action_name)

        return self.config[action_name]

    def finesse(self, action: BaseAction) -> int:
        brain = self.get_brain(action = action)
        return brain.score()

    def set_configs(self, brain_config: [BrainConfig]):
        for config in brain_config:
            self.set_config(config)

    def set_config(self, config: BrainConfig):
        brain = self.get_brain(action_name = config.brain_name)
        brain.set_config(
            config_type=config.config_name,
            config_value=config.value
        )
