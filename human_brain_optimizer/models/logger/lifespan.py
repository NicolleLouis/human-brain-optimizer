import json

from human_brain_optimizer.models.logger.base import BaseLogger

class LifespanLogger(BaseLogger):
    BASE_FILE_NAME = 'lifespan'

    def __init__(self):
        super().__init__()
        self.result_dict = {}

    def log(self, lifespan: int) -> None:
        self.result_dict.setdefault(lifespan, 0)
        self.result_dict[lifespan] += 1

    def save(self) -> None:
        json.dump(self.result_dict, open(self.file_name(), 'w'))

    def load(self) -> dict:
        return json.load(open(self.file_name()))
