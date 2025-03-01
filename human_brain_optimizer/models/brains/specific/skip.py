from human_brain_optimizer.models.brains.specific.base import BaseBrain


class SkipSpecificBrain(BaseBrain):
    def finesse(self) -> int:
        return 0

    def set_config(self, config_type: str, config_value: int):
        pass
