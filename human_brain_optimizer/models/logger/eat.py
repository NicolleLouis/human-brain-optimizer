import json

import pandas as pd
import plotly.express as px

from human_brain_optimizer.models.logger.base import BaseLogger


class EatLogger(BaseLogger):
    BASE_FILE_DIRECTORY = 'eat'
    FOOD_LOG_TYPE = 'food'
    HUNGER_LOG_TYPE = 'hunger'

    def __init__(self):
        super().__init__()
        self.total_food = None
        self.food_dict = {}
        self.hunger_dict = {}

    def log(self, log_type: str, log_value) -> None:
        if log_type == self.FOOD_LOG_TYPE:
            self.log_food(log_value)
        if log_type == self.HUNGER_LOG_TYPE:
            self.log_hunger(log_value)

    def log_food(self, food):
        self.food_dict.setdefault(food, 0)
        self.food_dict[food] += 1

    def log_hunger(self, hunger):
        self.hunger_dict.setdefault(hunger, 0)
        self.hunger_dict[hunger] += 1

    def save(self, raw_values=False, **kwargs) -> None:
        if raw_values:
            self.save_raw()
        self.save_total_food()
        self.save_food_repartition()
        self.save_hunger_repartition()

    def save_total_food(self):
        total_food = 0
        for _food, quantity in self.food_dict.items():
            total_food += quantity
        self.total_food = total_food

    def save_hunger_repartition(self):
        df = pd.DataFrame({
            'hunger': list(map(int, self.hunger_dict.keys())),
            'value': list(self.hunger_dict.values())
        })
        df['ratio'] = df['value'] / self.total_food
        df.sort_values("hunger", inplace=True)

        fig = px.line(
            df,
            x='hunger',
            y='ratio',
            title='Meal repartition by hunger',
            labels={'hunger': 'Hunger', 'ratio': 'Percentage of meal'},
            markers=True
        )
        fig.update_layout(
            yaxis=dict(
                tickformat='.0%',
            )
        )
        self.save_graph("hunger", fig)

    def save_food_repartition(self):
        df = pd.DataFrame(list(self.food_dict.items()), columns=["Food Type", "Number"])
        fig = px.pie(
            df,
            values="Number",
            names="Food Type",
            title="Food Eaten Repartition"
        )
        self.save_graph("food_repartition", fig)

    def save_raw(self):
        json.dump(self.hunger_dict, open(self.file_path('raw_hunger.json'), 'w'))
        json.dump(self.food_dict, open(self.file_path('raw_food.json'), 'w'))

    def merge_logger(self, other_logger) -> None:
        self.merge_hunger_dict(other_logger.hunger_dict)
        self.merge_food_dict(other_logger.food_dict)

    def merge_hunger_dict(self, other_hunger_dict):
        for key, value in other_hunger_dict.items():
            if key in self.hunger_dict:
                self.hunger_dict[key] += value
            else:
                self.hunger_dict[key] = value

    def merge_food_dict(self, other_food_dict):
        for key, value in other_food_dict.items():
            if key in self.food_dict:
                self.food_dict[key] += value
            else:
                self.food_dict[key] = value
