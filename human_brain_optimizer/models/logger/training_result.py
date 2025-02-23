import json

from human_brain_optimizer.models.data.brain_config import BrainConfig
from human_brain_optimizer.models.logger.base import BaseLogger


class TrainingResultLogger(BaseLogger):
    BASE_FILE_DIRECTORY = 'training'

    def __init__(self):
        super().__init__()
        self.results = {}

    def log(self, result: float, brain_config: BrainConfig) -> None:
        self.results[brain_config] = result

    def save_raw(self):
        simple_output = {}
        for brain_config, result in self.results.items():
            condensed_name = " && ".join([str(config) for config in brain_config])
            simple_output[condensed_name] = result
        json.dump(simple_output, open(self.file_path('raw.json'), 'w'))

    def summary(self):
        values = list(self.results.values())
        average = sum(values) / len(values)
        minimum = min(values)
        maximum = max(values)

        max_config = max(self.results, key=self.results.get)

        with open(self.file_path("summary.txt"), 'w') as file:
            file.write(f"Average: {average}\n")
            file.write(f"Min: {minimum}\n")
            file.write(f"Max: {maximum}\n")
            file.write(f"Best configuration: \n")
            for config in max_config:
                file.write(f"{str(config)}\n")


    def save(self) -> None:
        self.save_raw()
        self.summary()

    def merge_logger(self, other_logger) -> None:
        pass
