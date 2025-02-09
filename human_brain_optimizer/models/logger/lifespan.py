import json

import pandas as pd
import plotly.express as px

from human_brain_optimizer.models.logger.base import BaseLogger


class LifespanLogger(BaseLogger):
    BASE_FILE_DIRECTORY = 'lifespan'

    def __init__(self):
        super().__init__()
        self.result_dict = {}
        self.df = None

    def log(self, lifespan: int) -> None:
        self.result_dict.setdefault(lifespan, 0)
        self.result_dict[lifespan] += 1

    def save_raw(self):
        json.dump(self.result_dict, open(self.file_path('raw.json'), 'w'))

    def enrich_dataframe(self) -> None:
        df = (pd.DataFrame({
            'age': list(map(int, self.result_dict.keys())),
            'death_count': list(self.result_dict.values())
        })
              .sort_values(by='age')
              .reset_index(drop=True))

        df['cumulative_deaths'] = df['death_count'].cumsum()

        total_specimens = df['death_count'].sum()
        df['alive_before'] = total_specimens - df['cumulative_deaths'].shift(fill_value=0)
        df['death_probability'] = df['death_count'] / df['alive_before']

        self.df = df

    def save_cumulative_death_chart(self):
        chart_name = "cumulative_deaths_chart"
        fig_line = px.line(
            self.df,
            x='age',
            y='cumulative_deaths',
            title='Cumulative Deaths by Age',
            labels={'age': 'Age', 'cumulative_deaths': 'Accumulated Number of Dead Specimens'},
            markers=True
        )
        fig_line.write_html(self.file_path(f"{chart_name}.html"))
        fig_line.write_image(self.file_path(f"{chart_name}.png"))

    def save_probability_death_chart(self):
        chart_name = "probability_death_chart"
        fig_bar = px.bar(
            self.df,
            x='age',
            y='death_probability',
            title='Death Probability by Age',
            labels={'age': 'Age', 'death_probability': 'Death Probability'}
        )
        fig_bar.update_yaxes(tickformat='.1%')
        fig_bar.write_html(self.file_path(f"{chart_name}.html"))
        fig_bar.write_image(self.file_path(f"{chart_name}.png"))

    def save(self) -> None:
        self.save_raw()
        self.enrich_dataframe()
        self.save_cumulative_death_chart()
        self.save_probability_death_chart()

    def load(self) -> dict:
        return json.load(open(self.file_path('raw.json')))
