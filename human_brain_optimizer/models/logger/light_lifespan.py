import pandas as pd

from human_brain_optimizer.exceptions.models.logger import LifespanLoggerMessageNotRecognizedException
from human_brain_optimizer.models.logger.base import BaseLogger


class LightLifespanLogger(BaseLogger):
    BASE_FILE_DIRECTORY = 'lifespan'
    IGNORE_LOG_TYPE = ['death_cause']

    def __init__(self):
        super().__init__()
        self.lifespan_dict = {}
        self.lifespan_df = None
        self.average_lifespan = None

    def log(self, log_type: str, log_value) -> None:
        if log_type == 'lifespan':
            self.lifespan_dict.setdefault(log_value, 0)
            self.lifespan_dict[log_value] += 1
        elif log_type in self.IGNORE_LOG_TYPE:
            pass
        else:
            raise LifespanLoggerMessageNotRecognizedException('log_type unknown')

    def reset(self) -> None:
        self.__init__()

    def enrich_dataframe(self) -> None:
        df = (pd.DataFrame({
            'age': list(map(int, self.lifespan_dict.keys())),
            'death_count': list(self.lifespan_dict.values())
        })
              .sort_values(by='age')
              .reset_index(drop=True))

        df['cumulative_deaths'] = df['death_count'].cumsum()

        self.lifespan_df = df

    def compute_mathematical_analysis(self):
        self.average_lifespan = (self.lifespan_df['age'] * self.lifespan_df['death_count']).sum() / self.lifespan_df['death_count'].sum()

    def save(self) -> None:
        self.enrich_dataframe()
        self.compute_mathematical_analysis()

    def load(self) -> dict:
        raise NotImplementedError

    def merge_logger(self, other_logger) -> None:
        raise NotImplementedError
