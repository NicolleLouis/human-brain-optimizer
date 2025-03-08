import json
import random

import pandas as pd
import plotly.express as px

from human_brain_optimizer.models.data.brain_config import BrainConfig
from human_brain_optimizer.models.logger.base import BaseLogger


class TrainingResultLogger(BaseLogger):
    BASE_FILE_DIRECTORY = 'training'

    def __init__(self):
        super().__init__()
        self.df = None
        self.results = {}

    def log(self, result: float, brain_config: [BrainConfig]) -> None:
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

    def save_histogram(self):
        fig = px.histogram(self.df, x='values', nbins=20)
        self.save_graph("histogram_repartition", fig)

    def save_box_plot(self):
        fig = px.box(self.df, y='values')
        self.save_graph("boxplot_repartition", fig)

    def save_all_brain_config_repartition(self):
        example_brain_configs = self.random_brain_configs()
        for config_index in range(len(example_brain_configs)):
            self.save_brain_config_repartition(config_index)

    def save_brain_config_repartition(self, brain_config_index):
        brain_config = self.random_brain_configs()[brain_config_index]
        chart_name = f"{brain_config.brain_name}-{brain_config.config_name}"
        df = pd.DataFrame(
            [
                {
                    'config': brain_configs[brain_config_index].value,
                    'value': result
                }
                for brain_configs, result in self.results.items()
            ]
        )
        fig = px.scatter(
            df,
            x='config',
            y='value',
            trendline='ols',
            title=chart_name
        )
        self.save_graph(chart_name, fig)


    def random_brain_configs(self):
        return random.choice(list(self.results.keys()))


    def enrich_dataframe(self):
        self.df = pd.DataFrame({
            'values': list(map(int, self.results.values()))
        })

    def save(self, raw_values=False) -> None:
        self.enrich_dataframe()
        if raw_values:
            self.save_raw()
        self.summary()
        self.save_histogram()
        self.save_box_plot()
        self.save_all_brain_config_repartition()

    def merge_logger(self, other_logger) -> None:
        pass
