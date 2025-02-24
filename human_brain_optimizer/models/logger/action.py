import json

from human_brain_optimizer.models.logger.base import BaseLogger


class ActionLogger(BaseLogger):
    BASE_FILE_DIRECTORY = 'action'

    def __init__(self):
        super().__init__()
        self.total_actions = None
        self.action_dict = {}

    def log(self, action_name) -> None:
        self.action_dict.setdefault(action_name, 0)
        self.action_dict[action_name] += 1

    def save_normalized(self):
        normalized_dict = {}
        for key, value in self.action_dict.items():
            normalized_dict[key] = round(100*value/self.total_actions, 2)
        json.dump(normalized_dict, open(self.file_path('normalized.json'), 'w'))

    def compute_total_actions(self):
        total_actions = 0
        for action_number in self.action_dict.values():
            total_actions += action_number
        self.total_actions = total_actions

    def save(self) -> None:
        self.compute_total_actions()
        self.save_normalized()

    def merge_logger(self, other_logger) -> None:
        for key, value in other_logger.action_dict.items():
            if key in self.action_dict:
                self.action_dict[key] += value
            else:
                self.action_dict[key] = value
