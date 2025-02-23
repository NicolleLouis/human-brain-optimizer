"""
Brain Config Range contains 3 infos: brain_name, config and range
"""
from human_brain_optimizer.models.data.brain_config import BrainConfig


class BrainConfigRange:
    def __init__(self, brain_name, config_name, value_range):
        self.brain_name = brain_name
        self.config_name = config_name
        self.value_range = value_range

    def convert_to_array(self) -> [BrainConfig]:
        brain_configs = []
        for value in self.value_range:
            brain_configs.append(
                BrainConfig(
                    brain_name=self.brain_name,
                    config_name=self.config_name,
                    value=value
                )
            )
        return brain_configs

    def size(self):
        return len(self.value_range)

    def __str__(self):
        return f'{self.brain_name} - {self.config_name}: {len(self.value_range)} options'
