import json

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from human_brain_optimizer.models.logger.base import BaseLogger


class ActionLogger(BaseLogger):
    BASE_FILE_DIRECTORY = 'action'

    def __init__(self):
        super().__init__()
        self.df = None
        self.summarized_actions = None
        self.total_actions = None
        self.action_dict = {}

    def log(self, action_name, finesse) -> None:
        self.action_dict.setdefault(action_name, [])
        self.action_dict[action_name].append(finesse)

    def compute_summarized_values(self):
        self.summarized_actions = {}
        for key, value in self.action_dict.items():
            self.summarized_actions[key] = len(value)

    def save_donut_chart(self):
        df = pd.DataFrame(list(self.summarized_actions.items()), columns=["Action", "Number"])
        fig = px.pie(
            df,
            values="Number",
            names="Action",
            title="Action Repartition"
        )
        self.save_graph("action_repartition", fig)

    def save_normalized(self):
        normalized_dict = {}
        for key, value in self.summarized_actions.items():
            normalized_dict[key] = round(100*value/self.total_actions, 2)
        json.dump(normalized_dict, open(self.file_path('normalized.json'), 'w'))

    def compute_total_actions(self):
        total_actions = 0
        for finesse_scores in self.action_dict.values():
            total_actions += len(finesse_scores)
        self.total_actions = total_actions

    def generate_dataframe(self):
        rows = []
        for action, scores in self.action_dict.items():
            for score in scores:
                rows.append({'action': action, 'score': score})
        df_actions = pd.DataFrame(rows)

        df_total = df_actions.copy()
        df_total['action'] = 'total'

        self.df = pd.concat([df_total, df_actions], ignore_index=True)

    def save_score_repartition_graph(self):
        fig = px.box(
            self.df,
            x='action',
            y='score',
            title='Score Repartition',
            points=False
        )

        means = self.df.groupby('action')['score'].mean().reset_index()
        fig.add_trace(go.Scatter(
            x=means['action'],
            y=means['score'],
            mode='markers',
            marker=dict(color='red', size=12, symbol='diamond'),
            name='Average'
        ))

        stats = self.df.groupby('action')['score'].agg(
            min_score='min',
            q1=lambda x: x.quantile(0.25),
            median_score='median',
            q3=lambda x: x.quantile(0.75),
            max_score='max',
            mean_score='mean'
        ).reset_index()
        for _, row in stats.iterrows():
            fig.add_annotation(
                x=row['action'],
                y=row['mean_score'],
                text=f"Average: {row['mean_score']:.1f}",
                showarrow=False,
                yshift=10,
                font=dict(color="red")
            )
            if row['min_score'] != row['mean_score']:
                fig.add_annotation(
                    x=row['action'],
                    y=row['min_score'],
                    text=f"Min: {row['min_score']}",
                    showarrow=False,
                    yshift=-10,
                    font=dict(color="blue")
                )
            if row['max_score'] != row['mean_score']:
                fig.add_annotation(
                    x=row['action'],
                    y=row['max_score'],
                    text=f"Max: {row['max_score']}",
                    showarrow=False,
                    yshift=10,
                    font=dict(color="blue")
                )

        fig.update_layout(xaxis_title="Action", yaxis_title="Score")

        self.save_graph("score_repartition", fig)

    def save(self) -> None:
        self.compute_total_actions()
        self.generate_dataframe()
        self.compute_summarized_values()
        self.save_normalized()
        self.save_donut_chart()
        self.save_score_repartition_graph()

    def merge_logger(self, other_logger) -> None:
        for key, value in other_logger.action_dict.items():
            if key in self.action_dict:
                self.action_dict[key].extend(value)
            else:
                self.action_dict[key] = value
