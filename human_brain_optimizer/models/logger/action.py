import json

from human_brain_optimizer.models.logger.base import BaseLogger


class ActionLogger(BaseLogger):
    BASE_FILE_DIRECTORY = 'action'

    def __init__(self):
        super().__init__()
        self.action_dict = {}

    def log(self, action_name) -> None:
        self.action_dict.setdefault(action_name, 0)
        self.action_dict[action_name] += 1

    def save(self) -> None:
        json.dump(self.action_dict, open(self.file_path('raw.json'), 'w'))

    def merge_logger(self, other_logger) -> None:
        for key, value in other_logger.action_dict.items():
            if key in self.action_dict:
                self.action_dict[key] += value
            else:
                self.action_dict[key] = value
