from abc import ABC, abstractmethod


class BaseBrain(ABC):
    MAX_FINESSE = 1000

    def __init__(self, human):
        self.human = human

    @abstractmethod
    def finesse(self) -> int:
        pass

    def score(self):
        score = self.finesse()
        return min(self.MAX_FINESSE, score)

    @abstractmethod
    def set_config(self, config_type: str, config_value: int):
        pass
