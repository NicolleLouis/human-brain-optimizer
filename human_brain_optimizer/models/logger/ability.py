import json

import pandas as pd
import plotly.express as px

from human_brain_optimizer.exceptions.models.logger import AbilityLoggerMessageNotRecognizedException
from human_brain_optimizer.models.logger.base import BaseLogger


class AbilityLogger(BaseLogger):
    BASE_FILE_DIRECTORY = 'ability'

    def __init__(self):
        super().__init__()
        self.by_age_df = None
        self.by_age = {}
        self.end_of_life = {}

    def log(self, log_type: str, log_value, age=None) -> None:
        if log_type == 'end_of_life':
            self.end_of_life.setdefault(log_value, 0)
            self.end_of_life[log_value] += 1
        elif log_type == 'by_age':
            self.by_age.setdefault(age, [])
            self.by_age[age].append(log_value)
        else:
            raise AbilityLoggerMessageNotRecognizedException('log_type unknown')

    def save_raw(self):
        json.dump(self.by_age, open(self.file_path('raw_by_age.json'), 'w'))
        json.dump(self.end_of_life, open(self.file_path('raw_end_of_life.json'), 'w'))

    def save_end_of_life_line_chart(self):
        df = (pd.DataFrame({
            'ability_score': list(map(int, self.end_of_life.keys())),
            'count': list(self.end_of_life.values())
        })
              .sort_values(by='ability_score')
              .reset_index(drop=True))

        fig_line = px.line(
            df,
            x='ability_score',
            y='count',
            title='Ability Score at End of Life',
            labels={'ability_score': 'Ability Score', 'count': 'Number of humans'},
            markers=True
        )
        self.save_graph("end_of_life", fig_line)

    def save_by_age_line_chart(self):
        fig_line = px.line(
            self.by_age_df,
            x='turn_number',
            y='average_score',
            title='Average Ability Score by Turn',
            labels={'turn_number': 'Turn', 'average_score': 'Score moyen'},
            markers=True
        )
        self.save_graph("by_age", fig_line)

    def compute_by_age_df(self):
        data = []
        for turn, scores in self.by_age.items():
            average = sum(scores) / len(scores)
            data.append({"turn_number": turn, "average_score": average})

        df = pd.DataFrame(data)
        df.sort_values("turn_number", inplace=True)

        self.by_age_df = df

    def save(self) -> None:
        self.compute_by_age_df()
        self.save_raw()
        self.save_end_of_life_line_chart()
        self.save_by_age_line_chart()

    def merge_logger(self, other_logger) -> None:
        self.merge_end_of_life(other_logger)
        self.merge_by_age(other_logger)

    def merge_end_of_life(self, other_logger):
        for key, value in other_logger.end_of_life.items():
            if key in self.end_of_life:
                self.end_of_life[key] += value
            else:
                self.end_of_life[key] = value

    def merge_by_age(self, other_logger):
        for key, value in other_logger.by_age.items():
            if key in self.by_age:
                self.by_age[key].extend(value)
            else:
                self.by_age[key] = value
