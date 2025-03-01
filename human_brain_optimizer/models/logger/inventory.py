import json

import pandas as pd
import plotly.express as px

from human_brain_optimizer.models.logger.base import BaseLogger


class InventoryLogger(BaseLogger):
    BASE_FILE_DIRECTORY = 'inventory'

    def __init__(self):
        super().__init__()
        self.total_values = 0
        self.df = None
        self.inventory_dict = {}

    def log(self, inventory_size) -> None:
        self.inventory_dict.setdefault(inventory_size, 0)
        self.inventory_dict[inventory_size] += 1

    def save_linechart(self):
        df = pd.DataFrame(list(self.inventory_dict.items()), columns=['Inventory Size', 'Raw Value'])
        df.sort_values(by='Inventory Size', inplace=True)
        df['Value'] = df['Raw Value'] / self.total_values
        fig = px.line(df, x='Inventory Size', y='Value', markers=True, title="Inventory Size")
        fig.update_layout(
            yaxis=dict(
                tickformat='.0%',
            )
        )
        self.save_graph('size_per_turn', fig)

    def save_raw(self):
        json.dump(self.inventory_dict, open(self.file_path('raw.json'), 'w'))

    def compute_total_values(self):
        self.total_values =  0
        for value in self.inventory_dict.values():
            self.total_values += value

    def save(self) -> None:
        self.compute_total_values()
        self.save_raw()
        self.save_linechart()

    def merge_logger(self, other_logger) -> None:
        for key, value in other_logger.inventory_dict.items():
            if key in self.inventory_dict:
                self.inventory_dict[key] += value
            else:
                self.inventory_dict[key] = value
