import json

import pandas as pd
import plotly.express as px

from human_brain_optimizer.models.logger.base import BaseLogger


class InventoryLogger(BaseLogger):
    BASE_FILE_DIRECTORY = 'inventory'
    INVENTORY_SIZE_TYPE = 'inventory_size'
    SPECIFIC_ITEM_TYPE = 'specific_item'

    def __init__(self):
        super().__init__()
        self.total_values = 0
        self.df = None
        self.size_dict = {}
        self.specific_items = {}

    def log(self, log_type: str, log_value) -> None:
        if log_type == self.INVENTORY_SIZE_TYPE:
            self.log_size(log_value)
        if log_type == self.SPECIFIC_ITEM_TYPE:
            self.log_specific_item_size(log_value)

    def log_size(self, inventory_size):
        self.size_dict.setdefault(inventory_size, 0)
        self.size_dict[inventory_size] += 1

    # item_size = {item_1: quantity_1, item_2; quantity_2}
    def log_specific_item_size(self, item_size):
        for item, size in item_size.items():
            self.specific_items.setdefault(item, {})
            self.specific_items[item].setdefault(size, 0)
            self.specific_items[item][size] += 1

    def save(self, raw_values=False, **kwargs) -> None:
        self.compute_total_values()
        self.fill_specific_items()
        if raw_values:
            self.save_raw()
        self.save_total_linechart()
        self.save_by_item()

    def fill_specific_items(self):
        for item_repartition in self.specific_items.values():
            non_empty_turn = 0
            for turn_number in item_repartition.values():
                non_empty_turn += turn_number
            empty_turn = self.total_values - non_empty_turn
            item_repartition[0] = empty_turn

    def save_total_linechart(self):
        df = pd.DataFrame(list(self.size_dict.items()), columns=['Inventory Size', 'Raw Value'])
        df.sort_values(by='Inventory Size', inplace=True)
        df['Value'] = df['Raw Value'] / self.total_values
        fig = px.line(df, x='Inventory Size', y='Value', markers=True, title="Inventory Size")
        fig.update_layout(
            yaxis=dict(
                tickformat='.0%',
            )
        )
        self.save_graph('total_size', fig)

    def save_by_item(self):
        data = []
        for objet, points in self.specific_items.items():
            for x, y in points.items():
                data.append({"object": objet, "x": int(x), "y": y})
        df = pd.DataFrame(data)
        df['y_percentage'] = df['y'] / self.total_values
        df.sort_values("x", inplace=True)
        fig = px.line(
            df,
            x="x",
            y="y_percentage",
            color="object",
            markers=True,
            title="Item Repartition",
            labels={'x': 'Quantity', 'y_percentage': 'Average time'},
        )
        fig.update_layout(
            yaxis=dict(
                tickformat='.0%',
            )
        )
        self.save_graph("item_repartition", fig)


    def save_raw(self):
        json.dump(self.size_dict, open(self.file_path('raw_size.json'), 'w'))
        json.dump(self.specific_items, open(self.file_path('raw_specific.json'), 'w'))

    def compute_total_values(self):
        self.total_values =  0
        for value in self.size_dict.values():
            self.total_values += value

    def merge_logger(self, other_logger) -> None:
        self.merge_size_dict(other_logger.size_dict)
        self.merge_specific_items(other_logger.specific_items)

    def merge_size_dict(self, other_size_dict):
        for key, value in other_size_dict.items():
            if key in self.size_dict:
                self.size_dict[key] += value
            else:
                self.size_dict[key] = value

    def merge_specific_items(self, other_specific_items):
        for item, item_dict in other_specific_items.items():
            if item in self.specific_items:
                self.merge_specific_item(item, item_dict)
            else:
                self.specific_items[item] = item_dict

    def merge_specific_item(self, item, other_item_dict):
        for key, value in other_item_dict.items():
            if key in self.specific_items[item]:
                self.specific_items[item][key] += value
            else:
                self.specific_items[item][key] = value
