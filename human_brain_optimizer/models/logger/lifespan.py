import json

import pandas as pd
import plotly.express as px

from human_brain_optimizer.constants.death_cause import DeathCause
from human_brain_optimizer.exceptions.models.logger import LifespanLoggerMessageNotRecognizedException
from human_brain_optimizer.models.logger.base import BaseLogger


class LifespanLogger(BaseLogger):
    BASE_FILE_DIRECTORY = 'lifespan'

    def __init__(self):
        super().__init__()
        self.lifespan_dict = {}
        self.lifespan_df = None
        self.death_cause = {}

    def log(self, log_type: str, log_value) -> None:
        if log_type == 'lifespan':
            self.lifespan_dict.setdefault(log_value, 0)
            self.lifespan_dict[log_value] += 1
        elif log_type == 'death_cause':
            self.add_death_cause(log_value)
        else:
            raise LifespanLoggerMessageNotRecognizedException('log_type unknown')

    def add_death_cause(self, death_cause: str) -> None:
        valid_death_cause = [death_cause.value for death_cause in DeathCause]
        if death_cause not in valid_death_cause:
            raise LifespanLoggerMessageNotRecognizedException('death_cause unknown')

        self.death_cause.setdefault(death_cause, 0)
        self.death_cause[death_cause] += 1


    def save_raw(self):
        json.dump(self.lifespan_dict, open(self.file_path('raw.json'), 'w'))

    def enrich_dataframe(self) -> None:
        df = (pd.DataFrame({
            'age': list(map(int, self.lifespan_dict.keys())),
            'death_count': list(self.lifespan_dict.values())
        })
              .sort_values(by='age')
              .reset_index(drop=True))

        df['cumulative_deaths'] = df['death_count'].cumsum()

        total_specimens = df['death_count'].sum()
        df['alive_before'] = total_specimens - df['cumulative_deaths'].shift(fill_value=0)
        df['death_probability'] = df['death_count'] / df['alive_before']

        self.lifespan_df = df

    def save_death_cause_chart(self):
        df = pd.DataFrame(list(self.death_cause.items()), columns=["Death Cause", "Number"])
        fig = px.pie(
            df,
            values="Number",
            names="Death Cause",
            title="Death Cause"
        )
        self.save_graph("death_cause", fig)

    def save_cumulative_death_chart(self):
        fig_line = px.line(
            self.lifespan_df,
            x='age',
            y='cumulative_deaths',
            title='Cumulative Deaths by Age',
            labels={'age': 'Age', 'cumulative_deaths': 'Accumulated Number of Dead Specimens'},
            markers=True
        )
        self.save_graph("cumulative_deaths_chart", fig_line)

    def save_probability_death_chart(self):
        fig_bar = px.bar(
            self.lifespan_df,
            x='age',
            y='death_probability',
            title='Death Probability by Age',
            labels={'age': 'Age', 'death_probability': 'Death Probability'}
        )
        fig_bar.update_yaxes(tickformat='.1%')
        self.save_graph("probability_death_chart", fig_bar)

    def save_mathematical_analysis(self):
        analysis = {
            'average_lifespan': (self.lifespan_df['age'] * self.lifespan_df['death_count']).sum() / self.lifespan_df['death_count'].sum()
        }

        json.dump(analysis, open(self.file_path('math.json'), 'w'))

    def save_death_cause(self):
        json.dump(self.death_cause, open(self.file_path('death_cause.json'), 'w'))

    def save(self, extensive=False) -> None:
        self.save_raw()
        self.save_death_cause()
        self.enrich_dataframe()
        self.save_cumulative_death_chart()
        self.save_mathematical_analysis()
        self.save_death_cause_chart()
        if extensive:
            self.save_probability_death_chart()

    def load(self) -> dict:
        return json.load(open(self.file_path('raw.json')))

    def merge_logger(self, other_logger) -> None:
        raise NotImplementedError
