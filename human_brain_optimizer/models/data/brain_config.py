"""
Brain Config contains a single value for a brain
"""
class BrainConfig:
    def __init__(self, brain_name, config_name, value):
        self.brain_name = brain_name
        self.config_name = config_name
        self.value = value

    def __str__(self):
        return f'{self.brain_name} - {self.config_name}: {self.value}'
